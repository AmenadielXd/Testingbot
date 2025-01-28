"""
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ParseMode, Update


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
            InlineKeyboardButton(text="ᴀʙᴏᴜᴛ", user_id=config.OWNER_ID),
            InlineKeyboardButton(text="sᴜᴘᴘᴏʀᴛ ᴄʜᴀᴛ", url=config.SUPPORT_GROUP),
        ],
    ]
    return buttons"""