from typing import Union
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import config
from InsaneMusic import app


def start_pannel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_5"],
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text=_["S_B_8"],
                callback_data="settings_back_helper",
            ),
            InlineKeyboardButton(text=_["S_B_2"], callback_data="settings_helper"),
        ],
    ]
    return buttons


def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_3"],
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
        [InlineKeyboardButton(text=_["S_B_4"], callback_data="settings_back_helper")],
        [
            InlineKeyboardButton(text=_["S_B_3"], callback_data="lood"),
            InlineKeyboardButton(text=_["S_B_9"], callback_data="gib_source"),
            
        ],
        [
            InlineKeyboardButton(text=_["S_B_7"], user_id=config.OWNER_ID),
        ],
        [
            InlineKeyboardButton("ᴅᴏɴᴀᴛᴇ", callback_data="donate"),
        ],
    ]
    return buttons
