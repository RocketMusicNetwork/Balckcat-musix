import asyncio
from time import time
from datetime import datetime
from helpers.filters import command
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton



@Client.on_message(command("start") & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/f4e1c2ebc7a14110faf47.jpg",
        caption=f"""**ʜᴇʟʟᴏ ɪ'ᴍ ᴀᴅᴠᴀɴᴄᴇ ᴍᴜsɪᴄ ʀᴏʙᴏᴛ ᴅᴇᴘʟᴏʏᴇᴅ ᴠᴘs  ᴄᴀᴛ sᴇᴠᴇ. 
        ┏━━━━━━━━━━━━━━━━━┓

┣» ᴏᴘ ᴍᴜꜱɪᴄ ᴘʟᴀʏᴇʀ ʙᴏᴛ. 

┣» ʜɪɢʜ ǫᴜᴀʟɪᴛʏ  ᴍᴜꜱɪᴄ.

┣» ᴀᴅᴠᴀɴᴄᴇᴅ ꜰᴇᴀᴛᴜʀᴇꜱ.

┣» ꜱᴜᴘᴇʀꜰᴀꜱᴛ ꜱᴘᴇᴇᴅ.

┗━━━━━━━━━━━━━━━━━┛
[ʙʟᴀᴄᴋ ᴄᴀᴛ ❤️](https://t.me/catmusicworld)



𝐈𝐟 𝐘𝐨𝐮 𝐇𝐚𝐯𝐞 𝐀𝐧𝐲 𝐐𝐮𝐞𝐬𝐭𝐢𝐨𝐧𝐬 𝐀𝐧𝐝 𝐇𝐞𝐥𝐩 𝐓𝐡𝐞𝐧 𝐃𝐦 𝐌𝐲 𝐁𝐨𝐬𝐬 = [ʙʟᴀᴄᴋ ᴄᴀᴛ🐱❤️](https://t.me/The_cat_lover0)**""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🥀 Jᴏɪɴ Hᴇʀᴇ & Sᴜᴘᴘᴏʀᴛ ✨", url=f"https://t.me/catmusicworld")
                ]
                
           ]
        ),
    )
    

@Client.on_message(command(["repo"]) & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/f4e1c2ebc7a14110faf47.jpg",
        caption=f"""""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "💥 ᴄᴏᴍᴍᴀɴᴅs 💞", url=f"https://telegra.ph/%CA%99%CA%9F%E1%B4%80%E1%B4%84%E1%B4%8B-%E1%B4%84%E1%B4%80%E1%B4%9B-01-05")
                ]
            ]
        ),
    )
