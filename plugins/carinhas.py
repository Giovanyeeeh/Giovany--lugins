import asyncio
import os
import random
import re
import requests
import wget
import datetime
import math
from cowpy import cow
from random import randint, choice

from kannax import Message, kannax


@kannax.on_cmd("carinhas", about={"header": "carinhas"})
async def snake_(message: Message):
    """carinhas fodas"""
    out = f"""
( ͡❛ ͜ʖ ͡❛)⠀⠀           
"""

    out2 = f"""
(. ͡❛ ͜ʖ ͡❛.)
"""
    out3 = f"""
【 ͡❛ ͜ʖ ͡❛】
"""

    out4 = f"""
¯\_( ͡❛ ͜ʖ ͡❛)_/¯⠀
"""
    
    out5 = f"""
¯\_( ͡ಠ ͜ʖ ͡ಠ)_/¯
     """
        
    out6 = f"""
¯\_( ͡ಥ ͜ʖ ͡ಥ)_/¯⠀
     """
    
    out7 = f"""
 ( ͡ಥ ͜ʖ ͡ಥ)
    """
    
    out8 = f"""
    ¯\_(ツ)_/¯
    ""
    
    out9 = f"""
    ಠ_ಠ
    """
    
    await message.edit(out)
    await asyncio.sleep(1)
    await message.edit(out2)
    await asyncio.sleep(1)
    await message.edit(out3)
    await asyncio.sleep(1)
    await message.edit(out4)
    await asyncio.sleep(1)
    await message.edit(out5)
    await asyncio.sleep(1)
    await message.edit(out6)
    await asyncio.sleep(1)
    await message.edit(out7)
    await asyncio.sleep(1)
    await message.edit(out8)
    await asyncio.sleep(1)
    await message.edit(out9)
    await asyncio.sleep(1)
