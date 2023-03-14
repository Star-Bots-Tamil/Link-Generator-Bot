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
from WebStreamer.bot.plugins.start_filter import *
from WebStreamer.bot.plugins.files_list import *
import os
import time
import string
import random
import asyncio
import aiofiles
import datetime

################################################################################################################################################################################################################################################
# Telegram Files List

FILES_LIST_BUTTONS = [
            [
                InlineKeyboardButton('👨🏻‍💻 Creator', url='https://t.me/Star_Movies_Karthik'),
                InlineKeyboardButton('📢 Update Channel', url='https://t.me/Star_Moviess_Tamil')
            ]
        ]

@StreamBot.on_message(files_list_filter)
async def files_list(client, message):
    mention = message.from_user.mention
    reply_markup = InlineKeyboardMarkup(ABOUT_BUTTONS)
    if Var.ALLOWED_USERS and not ((str(m.from_user.id) in Var.ALLOWED_USERS) or (m.from_user.username in Var.ALLOWED_USERS)):
        return await m.reply(
            "<b>Hello 👋🏻 {mention} ❤️,\nSorry {mention}! You're not the Subscriber of Our Premium Plans, Only Subscribers of Our Premium Plans Can Use Our [File to Link Star Bots](https://t.me/File_to_Link_Star_Bot).</b>",
            disable_web_page_preview=True, quote=True
        )
    await message.reply_text(
            text="<b>Hi 👋🏻 {} ♥️, Telegram Files List</b>".format(
                mention
            ),
            quote=True,
            parse_mode=ParseMode.HTML,
            reply_markup=reply_markup,
            disable_web_page_preview=True
        )
