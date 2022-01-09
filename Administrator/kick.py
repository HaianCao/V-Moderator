import discord
from discord import client
from discord import embeds
from discord.ext import commands
import random
import time
from discord.ext.commands import Bot, has_permissions, CheckFailure

class kick():
    @commands.command()
    @has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member=None, reason=None):
        await member.kick(reason=reason)
        em = discord.Embed(title='', description=f'''Kick {member.mention}
        **Lí do**: {reason}''', color=ctx.author.color) 
        await ctx.send(embed = em)

    @kick.error
    async def kick_error(self, ctx, error):
        if isinstance(error, CheckFailure):
            em = discord.Embed(title='', description='Bạn không có quyền sử dụng command này', color=ctx.author.color) 
            await ctx.send(embed = em)