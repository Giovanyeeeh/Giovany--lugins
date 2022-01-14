import asyncio

@kannax.on_cmd(r"(?:Kek|:/)$",
               about={'header': "Check yourself, hint: :/"}, name='Kek',
               trigger='', allow_via_bot=False)
async def kek_(message: Message):
    """hue"""
    kek = [":p", ":D"]
    for i in range(1, 9):
        await message.try_to_edit(":" + kek[i % 2])
