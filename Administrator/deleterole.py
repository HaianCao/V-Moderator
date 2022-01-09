import discord
from discord import client
from discord import embeds
from discord.ext import commands
import random
import time
from discord.ext.commands import Bot, has_permissions, CheckFailure

class drole():
    @commands.command()
    @has_permissions(manage_roles=True)
    async def drole(self, ctx, *, role:discord.Role):
        await role.delete()
        em = discord.Embed(title='', description=f'Đã xóa role @{role}', color=ctx.author.color) 
        await ctx.send(embed = em)

    @drole.error
    async def drole_error(self, ctx, error):
        if isinstance(error, CheckFailure):
            em = discord.Embed(title='', description='Bạn không có quyền sử dụng command này', color=ctx.author.color) 
            await ctx.send(embed = em)