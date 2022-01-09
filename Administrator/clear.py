import discord
from discord.ext import commands
import random
import time
from discord.ext.commands import Bot, has_permissions, CheckFailure

class clear():
    @commands.command(pass_context=True)
    @has_permissions(manage_messages=True)
    async def clear(self, ctx, amount = 2):
        await ctx.channel.purge(limit = amount)


    @clear.error
    async def clear_error(self, ctx, error):
        if isinstance(error, CheckFailure):
            em = discord.Embed(title='', description='Bạn không có quyền sử dụng command này', color=ctx.author.color) 
            await ctx.send(embed = em)