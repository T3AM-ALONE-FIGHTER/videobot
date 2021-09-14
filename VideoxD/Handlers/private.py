from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

from .. import HELP, bot

# basic commands


@bot.on_message(filters.command("alive"))
async def startxd(client, message):
    return await message.reply("𝐘𝐄𝐀𝐇 𝐁𝐀𝐁𝐘 𝐈 𝐀𝐌 𝐀𝐋𝐈𝐕𝐄!")


@bot.on_message(filters.command(["start", "help"]) & filters.private)
async def start(client, message):
    sender_mention = message.from_user.mention
    return await message.reply(
        f"Hi! {sender_mention}, 𝐇𝐄𝐘 𝐈 𝐀𝐌 𝐇𝐎𝐓 𝐕𝐈𝐃𝐄𝐎 𝐏𝐋𝐀𝐘𝐄𝐑 𝐁𝐎𝐓",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="OWNER",
                        url="https://t.me/PANDIT_xD",
                    )
                ],
                [
                    InlineKeyboardButton(
                        text="Commands", callback_data="commands"
                    )
                ],
                [
                    InlineKeyboardButton(
                        text="ABOUT CHANNEL",
                        url="https://t.me/ABOUT_PANDIT",
                    )
                ],
            ]
        ),
    )


@bot.on_callback_query(filters.regex("commands"))
async def command_(_, cb):
    await bot.send_message(cb.message.chat.id, text=HELP)
    return await cb.message.delete()
