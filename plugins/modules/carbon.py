from pyrogram import filters
from aiohttp import ClientSession
from pyrogram import Client as bot
from plugins.function import make_carbon
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
aiohttpsession = ClientSession()

C = "Successfully Created Your Carbon"
F = InlineKeyboardMarkup(
[[
     InlineKeyboardButton("JOIN ", url="https://t.me/BACKUPFILMBOX")
]]
)




@bot.on_message(filters.command("carbon"))
async def carbon_func(_, message):
    if not message.reply_to_message:
        return await message.reply_text(
            "Reply To A Text Message To Make Carbon /n/nMADE BY ❤️ @TN_LINKZZ"
        )
    if not message.reply_to_message.text:
        return await message.reply_text(
            "Reply To A Text Message To Make Carbon /n/nMADE BY ❤️ @TN_LINKZZ"
        )
    user_id = message.from_user.id
    m = await message.reply_text("Processing...")
    carbon = await make_carbon(message.reply_to_message.text)
    await m.edit("Uploading..")
    await message.reply_photo(
        photo=carbon,
        caption=C,
        reply_markup=F)
    await m.delete()
    carbon.close()
