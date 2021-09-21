from .. import BotzHub
from telethon import events, Button

@BotzHub.on(events.NewMessage(incoming=True, pattern="/help"))
async def start(event):
    await event.reply("**Hello! commands are below**")
    BotzHub.run_until_disconnected()

                    
