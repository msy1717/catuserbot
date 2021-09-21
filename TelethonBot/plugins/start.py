from .. import BotzHub
from telethon import events, Button

@BotzHub.on(events.NewMessage(incoming=True, pattern="/start"))
async def start(event):
    await event.reply("Hello!",
                    buttons=[
                        [Button.url("Developer", url="https://t.me/Godmrunal")],
                        [Button.inline("Main Menu",data="semx")]
                    ])

@BotzHub.on(events.callbackquery.CallbackQuery(data="semx"))
async def ex(event):
    await event.edit("**Main_Menu**",
                    buttons=[
                        [Button.inline("Logo", data="lgi")],
                        [Button.inline("ip Finder",data="op")]
                    ])
@BotzHub.on(events.callbackquery.CallbackQuery(data="lgi"))
async def ex(event):
    await event.edit("**Commands For logo**\n🔹 `/logo <text>`\n🔹`/wlogo`<text>",parse_mode=ParseMode.MARKDOWN,
            disable_web_page_preview=True,#when needed
            reply_markup=InlineKeyboardMarkup(
                [
                 [
                    InlineKeyboardButton(text="Back", callback_data="semx")
                 ]
                ]
            ),
        )
    
@BotzHub.on(events.callbackquery.CallbackQuery(data="op"))
async def ex(event):
    await event.edit("**Commands For ipfinder**\n🔹 `/ip <iphere>`",parse_mode=ParseMode.MARKDOWN,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                 [
                    InlineKeyboardButton(text="Back", callback_data="semx")
                 ]
                ]
            ),
        )
    
        
