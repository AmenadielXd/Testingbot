def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="ᴀᴅᴅ ᴍᴇ ᴛᴏ ᴄʜᴀᴛ",
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
        [InlineKeyboardButton(text="ɢᴜɪᴅᴇ", callback_data="settings_back_helper")],
        [
            InlineKeyboardButton(text="ᴀʙᴏᴜᴛ", url=f"https://t.me/{SUPPORT_CHAT}"),
            InlineKeyboardButton(text="sᴜᴘᴘᴏʀᴛ ᴄʜᴀᴛ", url=f"https://t.me/{SUPPORT_CHAT}"),
        ],
    ]
    return buttons
