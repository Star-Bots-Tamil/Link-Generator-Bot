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
