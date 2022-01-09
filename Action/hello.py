import discord
from discord.ext import commands
from discord.ext.commands.core import command
import random

class hello():
    @commands.command()
    async def hello(self, ctx):
        randomChoose = random.randint(0, 10)
        a = [
            'Lô cc',
            'Hê nhô :3',
            'Trào cậu :woozy_face:',
            'Cút :expressionless:',
            'M nghĩ m là ai :smirk:',
            'Sin nhỗi mk ko gei :face_vomiting:',
            'O,,w,,O',
            '500k bao phòng :woozy_face:',
            'Dạ e chào a ạ :kissing:',
            'Tuổi :smirk:',
            'Loli iz da bét :3333'
        ]
        await ctx.send(a[randomChoose])