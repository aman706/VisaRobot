from telethon import events, Button, custom
import re, os
from VisaRobot.events import register
from VisaRobot import telethn as tbot
from VisaRobot import telethn as tgbot
PHOTO = "https://telegra.ph/file/1c79c1aa3faba829c8807.jpg"
@register(pattern=("/alive"))
async def awake(event):
  VisaRobot = event.sender.first_name
  VisaRobot = "**♡ I,m Visa Robot** \n\n"
  VisaRobot += "**♡ I'm Working Properly**\n\n"
  VisaRobot += "**♡ visa : 2.0 LATEST**\n\n"
  VisaRobot += "**♡ My Master :** [Callmevp](t.me/CALL_ME_VP)\n\n"
  VisaRobot += "**♡ Telethon Version : 1.23.0**\n\n"
  BUTTON = [[Button.url("𝙎𝙐𝙋𝙋𝙊𝙍𝙏", "https://t.me/Visa_Support"), Button.url("𝙐𝙋𝘿𝘼𝙏𝙀", "https://t.me/Visa_Update")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=PIKACHU,  buttons=BUTTON)


__mod_name__ = "Alive⚜️"
