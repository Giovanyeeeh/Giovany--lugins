# Copyright (C) 2020 by UsergeTeam@Github, < https://github.com/UsergeTeam >.
#
# Editado por fnixdev

import asyncio
from datetime import datetime

from kannax import Message, kannax


@kannax.on_cmd(
    "pong",
    about={
        "header": "check how long it takes to ping your userbot",
        "flags": {"-a": "average ping"},
    },
    group=-1,
)
async def pingme(message: Message):
    start = datetime.now()
    if "-a" in message.flags:
        await message.edit("`!....`")
        await asyncio.sleep(0.3)
        await message.edit("`..!..`")
        await asyncio.sleep(0.3)
        await message.edit("`....!`")
        end = datetime.now()
        t_m_s = (end - start).microseconds / 1000
        m_s = round((t_m_s - 0.6) / 3, 3)
        await message.edit(f"🏓 Vendo os negocio aq! \n`{m_s} ᴍs`")
    else:
        await message.edit("`🏓 ta na ai`")
        end = datetime.now()
        m_s = (end - start).microseconds / 1000
        await message.edit(f"ᴘɪɴɢ - `{m_s} ᴍs`\nᴜᴘᴛɪᴍᴇ - `{kannax.uptime}`")
