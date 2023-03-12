# (c) Star Bots Tamil

from pyrogram import filters
from pyrogram.types import Message
from pyrogram import Client
from pyrogram import StopPropagation, filters
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram import Client, filters, enums
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, CallbackQuery
from WebStreamer.vars import Var 
from WebStreamer.bot import StreamBot
from pyrogram.enums.parse_mode import ParseMode
from pyrogram.errors import MessageNotModified, UserIsBlocked, InputUserDeactivated, FloodWait
import os
import time
import string
import random
import asyncio
import aiofiles
import datetime
from WebStreamer.handlers.broadcast import broadcast
from WebStreamer.handlers.database import Database
from WebStreamer.handlers.check_user import handle_user_status
from pyrogram.types import Message
LOG_CHANNEL = Var.LOG_CHANNEL
AUTH_USERS = Var.AUTH_USERS
DB_URL = Var.DB_URL
DB_NAME = Var.DB_NAME

db = Database(DB_URL, DB_NAME)


################################################################################################################################################################################################################################################
# Start Command

MAIN_MENU_BUTTONS = [
            [
                InlineKeyboardButton('👨🏻‍💻 Creator', url='https://t.me/Star_Movies_Karthik')
            ],
            [
                InlineKeyboardButton('😁 Help', callback_data="TUTORIAL_CALLBACK"),
                InlineKeyboardButton('👥 Support', callback_data="GROUP_CALLBACK"),
                InlineKeyboardButton('😎 About', callback_data="HELP_CALLBACK")
            ],
            [
                InlineKeyboardButton('📢 Update Channel', url='https://t.me/Star_Moviess_Tamil')
            ]
        ]

@StreamBot.on_message(filters.private)
async def _(bot, cmd):
    await handle_user_status(bot, cmd)

    chat_id = cmd.from_user.id
    if not await db.is_user_exist(chat_id):
        data = await client.get_me()
        BOT_USERNAME = data.username
        await db.add_user(chat_id)
        if LOG_CHANNEL:
            await client.send_message(
                LOG_CHANNEL,
                f"**#New_User :- \n\nNew User [{message.from_user.first_name}](tg://user?id={message.from_user.id})\n ID :- {message.from_user.id} Started @{BOT_USERNAME} !!**",
            )
        else:
            logging.info(f"New User :- Name :- {message.from_user.first_name} ID :- {message.from_user.id}")

@StreamBot.on_message(filters.command("start") & filters.private)
async def start(_, m: Message):
    reply_markup = InlineKeyboardMarkup(MAIN_MENU_BUTTONS)
    mention = m.from_user.mention(style="md")
    await m.reply_text(
            text="<b>Hi 👋🏻 {} ♥️,\nI'm an Star Bots Official [File to Link Star Bots](https://t.me/File_to_Link_Star_Bot).\nMaintenance By :- [Karthik](https://t.me/TG_Karthik)\nI'm Generate Permanent Link From Telegram File 📂 / Video 🎥. I Can Generate Direct Download Link For any File / Video to Get  📥 Download Link,  🖥 Watch Link and 🔗 Shortened Link. Send me Any File / Video to See My Magic ✨.\n\n❗Note :- 🔞 Don't Forward  Porn Files to me, You will Get 🚨 Permanent BAN\n\nMore than [8 Types of Telegram Files](https://t.me/File_to_Link_Star_Bot?start=Lists_of_Files) are Supported</b>".format(
                mention
            ),
            quote=True,
            parse_mode=ParseMode.HTML,
            reply_markup=reply_markup,
            disable_web_page_preview=True
        )
    raise StopPropagation


################################################################################################################################################################################################################################################
# Help Command

HELP_BUTTONS = [
            [
                InlineKeyboardButton('👨🏻‍💻 Creator', url='https://t.me/Star_Movies_Karthik'),
                InlineKeyboardButton('📢 Update Channel', url='https://t.me/Star_Moviess_Tamil')
            ]
        ]

@StreamBot.on_message(filters.command("help") & filters.private & filters.incoming)
async def help(client, message):
    reply_markup = InlineKeyboardMarkup(HELP_BUTTONS)
    mention = message.from_user.mention
    await message.reply_text(
            text="<b>Hi 👋🏻 {} ♥️,  Send me a File 📂 to get an Instant Stream link.</b>".format(
                mention
            ),
            quote=True,
            parse_mode=ParseMode.HTML,
            reply_markup=reply_markup,
            disable_web_page_preview=True
        )

################################################################################################################################################################################################################################################
# About Command

ABOUT_BUTTONS = [
            [
                InlineKeyboardButton('👨🏻‍💻 Creator', url='https://t.me/Star_Movies_Karthik'),
                InlineKeyboardButton('📢 Update Channel', url='https://t.me/Star_Moviess_Tamil')
            ]
        ]

@StreamBot.on_message(filters.command("about") & filters.private & filters.incoming)
async def about(client, message):
    mention = message.from_user.mention
    reply_markup = InlineKeyboardMarkup(ABOUT_BUTTONS)
    await message.reply_text(
            text="<b>Hi 👋🏻 {} ♥️,  Send me a File 📂 to get an Instant Stream link.</b>".format(
                mention
            ),
            quote=True,
            parse_mode=ParseMode.HTML,
            reply_markup=reply_markup,
            disable_web_page_preview=True
        )

################################################################################################################################################################################################################################################
# CallBackQuery For Star Message

@StreamBot.on_callback_query()
async def callback_query(client: Client, query: CallbackQuery):
    if query.data=="HELP_CALLBACK":
        HELP_BUTTON = [
            [
                InlineKeyboardButton("👈🏻 Back", callback_data="START_CALLBACK")
            ]
            ]
        reply_markup = InlineKeyboardMarkup(HELP_BUTTON)
        mention = query.from_user.mention
        try:
            await query.edit_message_text(
                text="<b>Hi 👋🏻 {} ♥️,  Send me a File 📂 to get an Instant Stream link.</b>".format(
                    mention
            ),
            parse_mode=ParseMode.HTML,
            reply_markup=reply_markup,
            disable_web_page_preview=True
        )
        except MessageNotModified:
            pass

    elif query.data=="GROUP_CALLBACK":
        GROUP_BUTTONS = [
            [
                InlineKeyboardButton("Star Movies Feedback", url="https://t.me/Star_Movies_Feedback_Bot")
            ],
            [
                InlineKeyboardButton("👈🏻 Back", callback_data="START_CALLBACK"),
            ]
            ]
        reply_markup = InlineKeyboardMarkup(GROUP_BUTTONS)
        mention = query.from_user.mention
        try:
            await query.edit_message_text(
                text="<b>Hi 👋🏻 {} ♥️,  Send me a File 📂 to get an Instant Stream link.</b>".format(
                    mention
            ),
            parse_mode=ParseMode.HTML,
            reply_markup=reply_markup,
            disable_web_page_preview=True
        )
        except MessageNotModified:
            pass    

    elif query.data=="TUTORIAL_CALLBACK":
        TUTORIAL_BUTTONS = [
            [
                InlineKeyboardButton("👨🏻‍✈️ Admin", url="https://t.me/Star_Movies_Karthik")
            ],
            [
                InlineKeyboardButton("👈🏻 Back", callback_data="START_CALLBACK"),
            ]
            ]
        reply_markup = InlineKeyboardMarkup(TUTORIAL_BUTTONS)
        mention = query.from_user.mention
        try:
            await query.edit_message_text(
                text="<b>Hi 👋🏻 {} ♥️,  Send me a File 📂 to get an Instant Stream link.</b>".format(
                    mention
            ),
            parse_mode=ParseMode.HTML,
            reply_markup=reply_markup,
            disable_web_page_preview=True
        )
        except MessageNotModified:
            pass      
          
    elif query.data=="START_CALLBACK":
        START_BUTTONS = [
            [
                InlineKeyboardButton('👨🏻‍💻 Creator', url='https://t.me/TG_Karthik')
            ],
            [
                InlineKeyboardButton('😁 Help', callback_data="TUTORIAL_CALLBACK"),
                InlineKeyboardButton('👥 Support', callback_data="GROUP_CALLBACK"),
                InlineKeyboardButton('😎 About', callback_data="HELP_CALLBACK")
            ],
            [
                InlineKeyboardButton('📢 Update Channel', url='https://t.me/Star_Bots_Tamil')
            ]
        ]

        reply_markup = InlineKeyboardMarkup(START_BUTTONS)
        mention = query.from_user.mention
        try:
            await query.edit_message_text(
                text="<b>Hi 👋🏻 {} ♥️,  Send me a File 📂 to get an Instant Stream link.</b>".format(
                    mention
            ),
            parse_mode=ParseMode.HTML,
            reply_markup=reply_markup,
            disable_web_page_preview=True
        )
        except MessageNotModified:
            pass    
        return

################################################################################################################################################################################################################################################

REPLY_ERROR = """<b>Use This Command as a Reply to any Telegram Message Without any Spaces.</b>"""

################################################################################################################################################################################################################################################
# Broadcast Message 

@StreamBot.on_message(filters.private & filters.command("broadcast"))
async def broadcast_handler_open(_, m):
    if m.from_user.id not in AUTH_USERS:
        await m.delete()
        return
    if m.reply_to_message is None:
        await m.reply(REPLY_ERROR, quote=True)
    else:
        await broadcast(m, db)

################################################################################################################################################################################################################################################
# Total Users in Database 📂

@StreamBot.on_message(filters.private & filters.command("stats"))
async def sts(c, m):
    if m.from_user.id not in AUTH_USERS:
        await m.delete()
        return
    await m.reply_text(
        text=f"**Total Users in Database 📂 :- {await db.total_users_count()}**",
        quote=True
    )
