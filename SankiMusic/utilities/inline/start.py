def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="★ ʜᴇʟᴘ ☆",
                callback_data="settings_back_helper"
            )
        ],
        [
            InlineKeyboardButton(
                text="✭ ᴜᴘᴅᴀᴛᴇs ✭",
                url=config.SUPPORT_CHANNEL
            ),
            InlineKeyboardButton(
                text="✭ sᴜᴘᴘᴏʀᴛ ✭",
                url=config.SUPPORT_GROUP
            )
        ]
    ]
    return buttons
