import asyncio
from time import time
from datetime import datetime
from helpers.filters import command
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton



@Client.on_message(command("start") & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/5fb191c3cd9bf108a3bfd.png",
        caption=f"""**𝐇𝐞𝐥𝐥𝐨 𝐆𝐮𝐲𝐬! 𝐢𝐚𝐦 𝐀𝐝𝐯𝐚𝐧𝐜𝐞 𝐌𝐮𝐬𝐢𝐜 𝐑𝐨𝐛𝐨𝐭 𝐃𝐞𝐩𝐥𝐨𝐲𝐞𝐝 𝐕𝐩𝐬 - 𝐆𝐫𝐨𝐨𝐭 𝐌𝐮𝐬𝐢𝐜 𝐍𝐞𝐭𝐰𝐨𝐫𝐤. 
(𝐉𝐨𝐢𝐧 𝐎𝐮𝐫 𝐆𝐫𝐨𝐮𝐩 ❤️](https://t.me/Elsa_network)



𝐈𝐟 𝐘𝐨𝐮 𝐇𝐚𝐯𝐞 𝐀𝐧𝐲 𝐐𝐮𝐞𝐬𝐭𝐢𝐨𝐧𝐬 𝐀𝐧𝐝 𝐇𝐞𝐥𝐩 𝐓𝐡𝐞𝐧 𝐃𝐦 𝐌𝐲 𝐁𝐨𝐬𝐬 = [𝐎𝐖𝐍𝐄𝐑 🌱❤️](https://t.me/mynameisGroot)**""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🥀 Jᴏɪɴ Hᴇʀᴇ & Sᴜᴘᴘᴏʀᴛ ✨", url=f"https://t.me/Elsa_network")
                ]
                
           ]
        ),
    )
    

@Client.on_message(command(["repo"]) & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/5fb191c3cd9bf108a3bfd.png",
        caption=f"""""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "💥 ᴄᴏᴍᴍᴀɴᴅs 💞", url=f"https://telegra.ph/file/5fb191c3cd9bf108a3bfd.png")
                ]
            ]
        ),
    )
