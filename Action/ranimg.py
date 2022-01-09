import discord
from discord.ext import commands
from discord.ext.commands.core import command
import random

class random_image():
    @commands.command()
    async def ranimg(self, ctx):
        em = discord.Embed(title="Random Image", color=ctx.author.color)
        a = random.randint(200, 600)
        b = random.randint(200, 600)
        em.set_image(url=f'https://picsum.photos/{a}/{b}')
        await ctx.send(embed=em)