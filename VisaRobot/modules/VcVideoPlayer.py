from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from config import SOURCE_CODE, ASSISTANT_NAME, SUPPORT_GROUP, UPDATES_CHANNEL, BOT_USERNAME
from plugins.tr import *
from pyrogram.errors import MessageNotModified

@Client.on_message(filters.command("start"))
async def start(client, message):
   buttons = [
            [
                InlineKeyboardButton("ʜᴇւᴩ ＆ ϲοϻϻѧɴᴅ𝒔ꜱ", callback_data="help"),
            ],
            [
                InlineKeyboardButton("ϲʜѧɴɴᴇւ", url=f"https://t.me/VisaBots"),
            ],
            [
                InlineKeyboardButton("ѧʙου𝞽", callback_data="about"),
                InlineKeyboardButton("ᴅᴇ𝘃𝒔ꜱ", callback_data="devs"),
            ],
            [
               InlineKeyboardButton("𝒔υϻϻοɴ ϻᴇ", url=f"https://t.me/MissVisaRobot?startgroup=true"),
            ]
            ]
   reply_markup = InlineKeyboardMarkup(buttons)
   if message.chat.type == 'private':
       await message.reply_text(
          START_TEXT,
          reply_markup=reply_markup
       )
   else:
      await message.reply(f"**@VisaAssistant is Alive! ✨**")

@Client.on_callback_query()
async def cb_handler(client: Client, query: CallbackQuery):
    if query.data=="help":
        buttons = [
            [
                InlineKeyboardButton("ʙѧϲ𝞳"", callback_data="start"),
                InlineKeyboardButton ("𝒔υᴩᴩοʀ𝞽", url=f"https://t.me/Visa_Support"),
            ]
            ]
        reply_markup = InlineKeyboardMarkup(buttons)
        try:
            await query.edit_message_text(
                HELP_TEXT,
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass

    elif query.data=="about":
        buttons = [
            [
                InlineKeyboardButton("ʙѧϲ𝞳", callback_data="start"),
                InlineKeyboardButton ("𝒔υᴩᴩοʀ𝞽", url=f"https://t.me/Visa_Support"),
            ]
            ]
        reply_markup = InlineKeyboardMarkup(buttons)
        try:
            await query.edit_message_text(
                ABOUT_TEXT,
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass

    elif query.data=="devs":
        buttons = [
            [
                InlineKeyboardButton("𝘃ɪ𝒔ѧꜱ", url="https://t.me/VisaBots"),
                InlineKeyboardButton("ϲѧււϻᴇ𝘃ᴩ", url="https://t.me/call_me_vp"),
            ],
            [
                InlineKeyboardButton("ϻѧɴᴊᴇᴇ𝞽", url="https://t.me/Murat_30_God"),
                InlineKeyboardButton("ѧϻѧɴ", url="https://t.me/Aman_57"),
            ],
            [
                InlineKeyboardButton("ѧւοɴᴇ ւο𝘃ᴇʀʙο𝞬", url="https://t.me/Alone_loverboy"),
            ],
            [
                InlineKeyboardButton("Bᴀᴄᴋ", callback_data="start"),
            ]
            ]
        reply_markup = InlineKeyboardMarkup(buttons)
        try:
            await query.edit_message_text(
                DEVS_TEXT,
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass

    elif query.data=="start":
        buttons = [
            [
                InlineKeyboardButton("ʜᴇւᴩ ＆ ϲοϻϻѧɴᴅ𝒔ꜱ", callback_data="help"),
            ],
            [
                InlineKeyboardButton("𝒔ουʀϲᴇ", url="https://t.me/call_me_vp"),
                InlineKeyboardButton("ϲʜѧɴɴᴇւ", url=f"https://t.me/VisaBots"),
            ],
            [
                InlineKeyboardButton("ѧʙου𝞽", callback_data="about"),
                InlineKeyboardButton("ᴅᴇ𝘃𝒔ꜱ", callback_data="devs"),
            ],
            [
               InlineKeyboardButton("𝒔υϻϻοɴ ϻᴇ", url=f"https://t.me/MissVisaRobot?startgroup=true"),
            ]
            ]
        reply_markup = InlineKeyboardMarkup(buttons)
        try:
            await query.edit_message_text(
                START_TEXT,
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass
