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


@kannax.on_cmd("teste", about={"header": "teste"})
async def snake_(message: Message):
    """testeee teste"""
    out = f"""
⣿⡇⠘⡇⢀⣶⣶⠄⠈⣾⡟⢂⣿⣿⣿⣿⣿⣿⡿⢉⢾⢃⣿⣿⡟⣸⢸⣿⣿⣸ ⣿⢸⣦⢧⢸⣿⣿⢱⠄⠄⣇⣼⣿⣿⣿⣿⣿⢟⣼⣿⡯⠸⣿⢳⢱⡏⣼⣿⢇⣿ ⡏⣾⢽⣼⢸⣿⣿⡘⣆⢀⠛⣿⣿⣿⣿⡿⣫⣾⣿⣿⢇⣿⠂⢌⡾⡇⣿⡿⢸⣿ ⢧⣿⠄⢹⢸⣿⣿⣷⣭⢸⡄⣿⣿⣿⢋⣵⣿⣿⡿⠟⡨⡡⠄⣾⣿⡆⣭⡇⣿⣿ ⣼⡏⡀⠄⢀⢿⣿⣿⡟⣾⡇⣿⡿⣡⢁⣿⣿⣫⡶⢃⡵⣡⣿⣮⡻⡇⣿⢸⣮⢿ ⣿⡇⣧⢠⠸⡎⡍⡭⢾⡏⣧⢋⢾⠏⣼⣿⣿⠿⣵⣾⣕⠿⣿⣿⣷⢡⠏⣾⣿⣿ ⣿⠁⣿⠈⠄⠄⢃⢹⡀⠸⢸⢿⠸⢰⢻⢿⣟⢁⣀⠄⠄⠉⠒⢝⢿⠸⣴⣿⣿⣿ ⡍⠇⣿⣷⢰⢰⢸⠄⡃⡆⠈⠈⡀⡌⠠⠸⠃⣿⣏⡳⢷⢄⡀⠄⠄⠰⣿⣿⣿⣿ ⡇⠄⠸⣿⢸⣿⣶⡄⣇⠃⡇⡄⡇⠁⠃⠄⠈⢊⠻⠿⣿⣿⣿⣦⠄⠘⣿⣿⣿⣿ ⡇⠄⠄⢻⣸⣿⣿⠏⡙⢸⣇⣡⢰⢀⠄⠄⠄⠈⡁⢱⢈⢿⣿⡿⡄⣰⣶⣿⣿⣿ ⡇⠄⠄⠄⢻⣿⡿⢰⡇⠆⠲⠶⣝⠾⠸⢴⢠⠄⠇⢸⢸⠄⡶⡜⣽⣿⣿⣿⣿⢏ ⠁⠄⠄⠄⠄⢿⡇⠧⢣⣸⣦⣄⣀⠁⠓⢸⣄⠸⢀⠄⡀⡀⡪⣽⣿⣿⢿⣿⢟⣬ ⠄⠄⠄⠄⠄⠈⢧⠯⢸⣿⣿⣿⡿⠰⣷⠄⣿⣇⡿⠄⡀⠦⣰⣿⡿⣱⣿⡏⢾⣫ ⠄⠄⠄⠄⠄⠄⠈⣌⢌⢿⣿⣿⠇⠼⢃⢠⢇⣻⣧⣿⡡⣸⣿⠿⢁⡟⢁⣳⣿⣿ ⠄⠄⠄⠄⠄⠄⠄⠄⠳⢝⣒⣒⠰⣘⣴⡧⠿⣿⣛⡯⣱⡿⣫⢎⣪⣎⣿⣧⢻⠿
"""

    out2 = f"""
⣿⣿⣿⣿⣿⠟⠋⠁⣀⣤⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣿⣿ ⣿⣿⣿⣿⠋⠁⠀⠀⠺⠿⢿⣿⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠻⣿ ⣿⣿⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣤⣤⣤⣤⠀⠀⠀⠀⠀⣤⣦⣄⠀⠀ ⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣶⣿⠏⣿⣿⣿⣿⣿⣁⠀⠀⠀⠛⠙⠛⠋⠀⠀ ⡿⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⣰⣿⣿⣿⣿⡄⠘⣿⣿⣿⣿⣷⠄⠀⠀⠀⠀⠀⠀⠀⠀ ⡇⠀⠀⠀⠀⠀⠀⠀⠸⠇⣼⣿⣿⣿⣿⣿⣷⣄⠘⢿⣿⣿⣿⣅⠀⠀⠀⠀⠀⠀⠀⠀ ⠁⠀⠀⠀⣴⣿⠀⣐⣣⣸⣿⣿⣿⣿⣿⠟⠛⠛⠀⠌⠻⣿⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀ ⠀⠀⠀⣶⣮⣽⣰⣿⡿⢿⣿⣿⣿⣿⣿⡀⢿⣤⠄⢠⣄⢹⣿⣿⣿⡆⠀⠀⠀⠀⠀⠀ ⠀⠀⠀⣿⣿⣿⣿⣿⡘⣿⣿⣿⣿⣿⣿⠿⣶⣶⣾⣿⣿⡆⢻⣿⣿⠃⢠⠖⠛⣛⣷⠀ ⠀⠀⢸⣿⣿⣿⣿⣿⣿⣾⣿⣿⣿⣿⣿⣿⣮⣝⡻⠿⠿⢃⣄⣭⡟⢀⡎⣰⡶⣪⣿⠀ ⠀⠀⠘⣿⣿⣿⠟⣛⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣿⣿⣿⡿⢁⣾⣿⢿⣿⣿⠏⠀ ⠀⠀⠀⣻⣿⡟⠘⠿⠿⠎⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣵⣿⣿⠧⣷⠟⠁⠀⠀ ⡇⠀⠀⢹⣿⡧⠀⡀⠀⣀⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠋⢰⣿⠀⠀⠀⠀ ⡇⠀⠀⠀⢻⢰⣿⣶⣿⡿⠿⢂⣿⣿⣿⣿⣿⣿⣿⢿⣻⣿⣿⣿⡏⠀⠀⠁⠀⠀⠀⠀ ⣷⠀⠀⠀⠀⠈⠿⠟⣁⣴⣾⣿⣿⠿⠿⣛⣋⣥⣶⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀ ⣿⡀
"""
    out3 = f"""
⠄⠄⠄⢰⣧⣼⣯⠄⣸⣠⣶⣶⣦⣾⠄⠄⠄⠄⡀⠄⢀⣿⣿⠄⠄⠄⢸⡇⠄⠄
 ⠄⠄⠄⣾⣿⠿⠿⠶⠿⢿⣿⣿⣿⣿⣦⣤⣄⢀⡅⢠⣾⣛⡉⠄⠄⠄⠸⢀⣿⠄
⠄⠄⢀⡋⣡⣴⣶⣶⡀⠄⠄⠙⢿⣿⣿⣿⣿⣿⣴⣿⣿⣿⢃⣤⣄⣀⣥⣿⣿⠄
⠄⠄⢸⣇⠻⣿⣿⣿⣧⣀⢀⣠⡌⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⠿⣿⣿⣿⠄
⠄⢀⢸⣿⣷⣤⣤⣤⣬⣙⣛⢿⣿⣿⣿⣿⣿⣿⡿⣿⣿⡍⠄⠄⢀⣤⣄⠉⠋⣰
⠄⣼⣖⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⣿⣿⣿⣿⢇⣿⣿⡷⠶⠶⢿⣿⣿⠇⢀⣤
⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣽⣿⣿⣿⡇⣿⣿⣿⣿⣿⣿⣷⣶⣥⣴⣿⡗
⢀⠈⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠄
⢸⣿⣦⣌⣛⣻⣿⣿⣧⠙⠛⠛⡭⠅⠒⠦⠭⣭⡻⣿⣿⣿⣿⣿⣿⣿⣿⡿⠃⠄
⠘⣿⣿⣿⣿⣿⣿⣿⣿⡆⠄⠄⠄⠄⠄⠄⠄⠄⠹⠈⢋⣽⣿⣿⣿⣿⣵⣾⠃⠄
⠄⠘⣿⣿⣿⣿⣿⣿⣿⣿⠄⣴⣿⣶⣄⠄⣴⣶⠄⢀⣾⣿⣿⣿⣿⣿⣿⠃⠄⠄
⠄⠄⠈⠻⣿⣿⣿⣿⣿⣿⡄⢻⣿⣿⣿⠄⣿⣿⡀⣾⣿⣿⣿⣿⣛⠛⠁⠄⠄⠄
⠄⠄⠄⠄⠈⠛⢿⣿⣿⣿⠁⠞⢿⣿⣿⡄⢿⣿⡇⣸⣿⣿⠿⠛⠁⠄⠄⠄⠄⠄
⠄⠄⠄⠄⠄⠄⠄⠉⠻⣿⣿⣾⣦⡙⠻⣷⣾⣿⠃⠿⠋⠁⠄⠄⠄⠄⠄⢀⣠⣴
⣿⣿⣿⣶⣶⣮⣥⣒⠲⢮⣝⡿⣿⣿⡆⣿⡿⠃⠄⠄⠄⠄⠄⠄⠄⣠⣴⣿⣿⣿
"""

    out4 = f"""
⢯⣿⡿⢠⣿⣿⣿⣿⣿⠷⢾⣿⣿⣿⣴⣿⣿⢹⣿⣯⣿⣿⡟⣿⡏⣿⣧⠻⣿⣿ ⣾⣿⣟⣼⣿⣿⣿⠟⠁⠀⢸⣿⣿⣿⣿⣿⣿⣴⣿⣟⣿⡿⠀⢻⣏⣿⣿⣷⣙⢿ ⣿⣿⣝⣿⣿⣿⣯⣖⠀⡀⢸⣿⣿⣿⣿⣿⣿⢿⣿⣿⣿⠃⠀⢸⣟⣿⣿⣿⣿⣎ ⣿⣼⣿⣿⠏⢩⣿⣿⣿⣮⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⠧⣀⡀⢨⣿⣿⣿⣿⣿⣿ ⣾⣿⡟⠃⠀⣿⣻⣿⡙⣻⣿⡿⣿⣿⣿⣿⣿⣿⣿⡏⣀⠀⠈⠉⣿⣿⣿⣿⣿⣿ ⣿⣿⣧⣷⣤⢘⣧⣿⣿⡿⠋⣇⢹⡍⣿⣿⣿⣿⣿⠀⣰⣶⣶⣾⣿⣿⣿⣿⣿⣿ ⣿⣿⣧⠀⠀⠐⠻⠿⠿⠃⡀⠸⠀⢿⣿⣿⡏⢸⡏⠐⠛⢉⣿⣿⣿⣿⣿⣿⣿⣿ ⣿⣿⠧⠀⠀⠀⠀⠀⠀⠀⠀⠠⣀⠬⢿⣿⠃⠈⠆⠀⠀⢸⡿⢿⣷⣨⣿⣿⣿⢹ ⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠰⠋⠀⠀⠻⠆⠀⠀⠀⠀⠈⢷⣾⣿⣿⣿⠿⣿⣿ ⣿⣿⠀⠀⠀⠀⠀⠀⢀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠰⢶⣌⣉⢉⡁⣠⣾⣿ ⣿⣿⣧⡀⢱⠀⠀⠀⣿⣿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠂⠀⠀⢈⣵⣿⣿⣿ ⣿⣿⣿⣷⡀⠀⠀⠀⣿⣿⣿⢻⣿⣿⣾⣥⣬⣂⠀⠀⠀⠀⠀⠀⣠⣾⣿⣿⡿⢟ ⣿⣿⣿⣿⣿⣄⠀⠀⠻⠙⠙⡿⠋⡉⡙⠛⣿⠟⠀⠀⠀⡠⠴⣻⣿⣿⡿⣫⣴⣿ ⣿⣿⣿⣿⣿⣿⣷⣄⣠⡇⣘⣀⣉⡩⢄⠐⠁⠀⠀⠀⠠⢠⣴⣿⢛⣥⣾⣿⣿⣿ ⣿⣿⣿⣿⣿⣿⣿⣿⣦⣀⣀⣀⣀⣀⣀⣠⣤⡤⠤⣶⢺⣿⣥⣔⣿⡾⣿⣿⣿⣿
"""
    
   out5 = f"""
 ⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿ ⣿⣿⣿⣿⣿⣿⣿⣿⡇⢀⢀⠍⠙⢿⡟⢿⣿⣿⣿⣿⣿⣿⣿⣿ ⠹⣿⣿⣿⣿⣿⣿⣿⠁⠈⢀⡤⢲⣾⣗⠲⣿⣿⣿⣿⣿⣿⣟⠻ ⡀⢙⣿⣿⣿⣿⣿⣿⢀⠰⠁⢰⣾⣿⣿⡇⢀⣿⣿⣿⣿⣿⣿⡄ ⣇⢀⢀⠙⠷⣍⠛⠛⢀⢀⢀⢀⠙⠋⠉⢀⢀⢸⣿⣿⣿⣿⣿⣷ ⡙⠆⢀⣀⠤⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢸⣿⣿⣿⣿⣿⣿ ⣷⣖⠋⠁⢀⢀⢀⢀⢀⢀⣀⣀⣄⢀⢀⢀⢀⢸⠏⣿⣿⣿⢿⣿ ⣿⣷⡀⢀⢀⢀⢀⢀⡒⠉⠉⢀⢀⢀⢀⢀⢀⢈⣴⣿⣿⡿⢀⡿ ⣿⣿⣷⣄⢀⢀⢀⢀⠐⠄⢀⢀⢀⠈⢀⣀⣴⣿⣿⣿⡿⠁⢀⣡ ⠻⣿⣿⣿⣿⣆⠢⣤⣄⢀⢀⣀⠠⢴⣾⣿⣿⡿⢋⠟⢡⣿⣿⣿ ⢀⠘⠿⣿⣿⣿⣦⣹⣿⣀⣀⣀⣀⠘⠛⠋⠁⡀⣄⣴⣿⣿⣿⣿ ⢀⢀⢀⠈⠛⣽⣿⣿⣿⣿⣿⣿⠁⢀⢀⢀⣡⣾⣿⣿⣿⡟⣹⣿ ⢀⢀⢀⢀⢰⣿⣿⣿⣿⣿⣿⣿⣦⣤⣶⣿⡿⢛⢿⡇⠟⠰⣿⣿ ⢀⢀⢀⢀⣿⣿⣿⡿⢉⣭⢭⠏⣿⡿⢸⡏⣼⣿⢴⡇⢸⣿⣶⣿ ⢀⢀⢀⢰⣿⣿⣿⢃⣶⣶⡏⠸⠟⣱⣿⣧⣛⣣⢾⣿⣿⣿⣿⣿ ⢀⢀⢀⣾⣿⣿⣿⣾⣿⣿⠟⢻⡿⡉⣷⣬⡛⣵⣿⣿⣿⣿⣿⣿ ⢀⢀⣸⣿⣿⣿⣿⣿⣿⡿⢰⠘⣰⣇⣿⣿⣰⣿⣿⣿⣿⣿⣿⣿ ⢀⢀⠘⢿⣿⣿⣿⣿⣿⡷⢺⣿⠟⣩⣭⣽⣇⠲⠶⣿⣿⣿⣿⣿ ⢀⠐⢀⣾⣿⣿⣿⣿⠟⢐⡈⣿⣷⣶⠎⣹⡟⠟⣛⣸⣿⣿⣿⣿ ⠠⢀⣼⣿⣿⣿⣿⣯⣼⣿⣷⣿⣷⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿
     """
        
   out6 = f"""
 ⢀⡠⡽⠛⠉⠀⠀⠣⡀⠈⠉⠒⢄⠀⠈⠙⢟⠷⣤⣀⢀⡉⢦⡀⠘⣿ ⠀⢀⢄⡴⠉⠊⠀⠀⠀⢀⡴⠋⠙⠳⣄⡀⠀⠀⠢⠀⠀⠢⡘⠻⣽⢿⣷⣝⢦⣿ ⠀⢄⣞⠀⠀⠀⡌⠀⢠⠊⠀⠀⠀⠀⠙⢷⢄⠀⠀⠠⡀⠀⢣⡤⣿⣿⣿⡻⣿⣿ ⠀⣜⠎⠀⠀⡘⠀⢠⠛⢄⠀⢀⠀⠀⠀⠀⢳⣥⣬⣤⣪⡢⣪⣿⣿⣟⣟⢿⡄⠙ ⢰⡟⡠⠀⣠⡃⣶⠃⠀⢈⢆⠀⠁⢀⡀⠀⠀⢻⣿⣿⣿⣿⣟⣿⣿⣿⣿⣿⣿⡀ ⣾⡧⡇⡪⡾⣾⣇⡠⠔⠉⠘⠀⠀⠀⠉⠓⠦⠤⣿⣿⣷⣿⣿⣿⣿⣿⣯⡻⢿⣷ ⣿⣨⣧⣮⣯⣾⡁⠀⠀⠠⠀⠨⢄⠀⠀⠐⠀⠠⢈⣿⣿⣿⣿⣿⣿⣟⣿⣿⣾⣿ ⣿⣿⣿⣿⣿⣧⣶⣶⣶⣦⡐⠀⢑⣧⠀⠈⠟⠋⠙⢟⣿⣿⣿⣿⠿⢿⡈⢿⣿⡿ ⣿⣿⣿⣿⡿⠁⠬⠷⢾⡟⠠⢌⢾⣸⣿⢦⡣⣐⣞⣟⢻⣿⣿⣿⡃⡃⣯⡪⢹⡼ ⣿⣿⣿⣿⣿⣝⣻⡻⠮⣌⣛⠮⠸⣿⠿⣷⣝⢾⣿⣿⣳⣿⣿⣿⣅⣸⡿⢫⡪⠖ ⣿⣿⣿⣿⡰⠹⠿⣌⠓⠬⠌⠀⠀⠀⠁⠉⠳⢽⠳⢙⢲⠙⣿⣿⣿⡟⡷⠁⠀⠀ ⡇⣿⣿⣿⣷⠀⣷⠄⠑⠀⢀⣀⣤⣀⣀⣤⣀⠀⠣⠀⣾⠀⣽⣿⣿⡝⠀⠀⠀⠀ ⠋⢹⡇⠛⣿⣧⡀⠀⠀⠀⣿⣿⣟⣿⣿⠟⠿⠇⠀⠀⢀⡜⠻⠿⣿⠀⠀⠀⠀⠀ ⠀⠀⠰⠀⡿⣿⣷⣄⡀⠀⠈⡿⠛⠁⠀⢀⠜⠀⠀⣠⠾⡧⠀⠀⢽⠀⠀⠀⠀⠀ ⠀⠈⢠⡤⣸⣼⣆⡇⢱⣦⣄⡘⢢⣤⡶⠷⠶⠶⢾⠿⠥⣧⣦⣄⡞⠀⠀
     """
    
    out7 = f"""
 ⣇⣠⣟⣿⣿⣿⣆⣤⣶⣿⣿⣿⢷⡜⠛⠛⠓⠢⢈⠉⠛⠻⢟⡿⣿⣯⣿⣿⣿⣿ ⣿⣿⣿⣿⣿⣿⣿⣿⡿⠛⠁⠀⢸⠁⠀⠀⠐⠠⣀⡁⠀⠀⢄⠉⠛⢝⣿⣿⣾⣯ ⣿⣿⣿⠿⣿⣿⠟⢁⠀⠀⠀⠀⠀⢠⣀⡀⠀⠀⠀⠘⢤⡀⠀⠑⢄⠀⠉⠻⣿⣿ ⠁⡰⢣⣾⡟⠁⠀⢸⠀⠀⠀⠀⠀⠀⣿⠛⠛⠶⠦⢄⡈⠙⢆⠀⠈⢳⡀⠀⠈⣩ ⣴⡁⣾⡟⠿⠀⠀⢈⡆⠀⢨⠀⠀⠀⡟⠲⡤⠲⠒⠁⠈⠑⠪⣢⠀⡀⢷⠐⣫⡾ ⠋⣹⣿⣿⣦⡞⡀⢸⣇⢀⢈⡆⠀⢰⠁⠐⠀⠀⠀⣠⣴⡶⢶⣎⢣⡷⡸⡇⢺⣶ ⠀⠛⢹⡛⠿⠖⡇⢸⢻⡮⠀⢧⠀⡆⠀⠀⠀⠀⢾⡿⢿⣿⣄⠇⠠⠁⢹⡇⠀⠸ ⢶⡀⢠⣥⡀⠀⡇⣸⠋⠙⢄⠘⢶⡇⠀⠀⠀⠀⠈⢧⣾⡼⠣⠄⠔⠓⠄⠹⣶⣠ ⠈⠳⣾⣼⣧⠀⢸⣸⠀⠀⢀⡙⠶⠗⠲⠀⣀⠤⠤⠀⠀⠂⠋⠉⠙⠀⠀⠠⣿⣿ ⣦⡀⠿⣿⣿⣇⢸⠹⣦⣾⣿⢿⣿⡂⢐⠧⣰⠌⠷⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿ ⢷⣍⢂⠀⠈⢾⣿⣴⣿⠻⣗⠾⡼⢃⣠⠌⠉⠁⠀⠀⠀⣀⠀⠀⠀⠀⠀⠀⠀⣿ ⣿⡎⢳⣦⠀⢀⠙⢧⡙⢒⠚⣫⣰⣖⡋⠀⠀⠀⠀⣰⣽⣿⣿⣦⣄⠀⠀⠀⠀⣿ ⢳⠛⢾⣿⡶⣄⠑⠦⣭⠾⠶⡎⠁⠉⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣷⡄⠀⣼⣿ ⣟⣴⣿⣟⣧⡜⢷⣤⣜⢦⡐⠃⠀⠀⠀⢀⡀⠀⠀⣿⣿⣿⣿⣿⣿⣿⢷⣰⡿⣿ ⣿⣯⣿⣿⣯⡼⣿⣷⣽⣯⣿⣅⠀⠀⠀⠀⠀⠀⠀⠸⣧⣿⣿⣿⣿⡫⠞⠉⢀⣴ ⣿⣿⡻⣾⣹⣿⣿⣿⣽⣷⡈⠙⣷⠦⣤⣀⡀⠀⠀⠀⠘⢿⡭⠚⢉⣠⣴⣾⣫⠇ ⡿⠏⠻⣤⣿⠟⣼⣿⣿⠿⠷⣴⡿⣾⣿⣿⣿⣿⣿⣿⣻⡥⠤⠾⣏⣵⡿⠛⠉⠀
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
