from pyrogram import filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
import random 
from VenomX import app as bot
from datetime import datetime

WEL_GIFS = [
    "https://telegra.ph/file/bd77135692ad077d34d64.mp4",
    "https://telegra.ph/file/d035da20a017e98bff27c.mp4"
]

def create_close_button():
    return InlineKeyboardMarkup(
        [[InlineKeyboardButton("✨✧༏ ᴍů༏ꜱꜱ✧ʏᴏᴜ ✨", callback_data="close")]]
    )

@bot.on_message(filters.new_chat_members)
async def welcome(_, m: Message):
    random_wel_gif = random.choice(WEL_GIFS)
    join_date = datetime.utcfromtimestamp(m.date.timestamp()).strftime('%Y-%m-%d')
    
    await m.reply_animation(
        random_wel_gif,
        caption=f"💌ᴛʜɪs ɪs👻 {m.from_user.mention}\🌲𝐖ᴇʟᴄᴏᴍᴇ 𝐈ɴ 𝐀 𝐍ᴇᴡ 𝐆ʀᴏᴜᴘ💐 {m.chat.title}!\n• ♥️𝑱𝒐𝒊𝒏➪⏱: {join_date}\n┏━━━━━━━━━━━━━━━━━━━━┓\n• 💨ꜰᴏʟʟᴏᴡ ᴏᴜʀ ʀᴜʟᴇꜱ ᴘʟᴇᴀꜱᴇ❣️\n\n╚»🔮『🔇ᴅᴏɴ'ᴛ ᴜᴘʟᴏᴀᴅ 18+ ᴍᴀᴛᴇʀɪᴀʟ☠️\n╚»🍒 🍷ꜱᴘᴀᴍᴍɪɴɢ & ꜰɪɪɢʜᴛ ɴᴏᴛ ᴀʟʟᴏᴡᴇᴅ☃️\n╚»♦️ʙᴏᴛ ᴏᴡɴᴇʀ 💨 @L2R_KING0 🎀\n╚»🧸ɢɪʀʟꜱ ᴅᴍ ɴᴏᴛ ᴀʟʟᴏᴡᴇᴅ𔘓🪽\n╚» 🥃ᴏᴛʜᴇʀᴇ ᴡɪsᴇ ʏᴏᴜ ᴡɪʟʟ ɴᴇ ʙᴀɴᴇᴅ🖇️♕︎\n╚»『 💒ᴇɴᴊᴏʏ ᴏᴜʀ ɢʀᴏᴜᴘ❁͜͡ ➛【🇮🇳】\n┗━━━━━━━━━━━━━━━━━━━━",
    )

@bot.on_message(filters.left_chat_member)
async def member_has_left(_, m: Message):
    left_gif = "https://telegra.ph/file/d53f47bcb7c6f9101bd93.mp4"
    await m.reply_animation(
        left_gif,
        caption=f"Sᴀᴅ Tᴏ Sᴇᴇ Yᴏᴜ Lᴇᴀᴠɪɴɢ {m.from_user.mention}\nTᴀᴋᴇ Cᴀʀᴇ!\n",
        reply_markup=create_close_button()
    )
