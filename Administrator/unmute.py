import discord
from discord import client
from discord import embeds
from discord.ext import commands
import random
import time
from discord.ext.commands import Bot, has_permissions, CheckFailure

class unmute():
    @commands.command()
    @has_permissions(kick_members=True)
    async def unmute(self, ctx, member: discord.Member):
        mutedRole = discord.utils.get(ctx.guild.roles, name="muted")

        await member.remove_roles(mutedRole)
        embed = discord.Embed(title="", description=f"Unmute {member.mention}",colour=ctx.author.color)
        await ctx.send(embed=embed)

    @unmute.error
    async def unmute_error(self, ctx, error):
        if isinstance(error, CheckFailure):
            em = discord.Embed(title='', description='Bạn không có quyền sử dụng command này', color=ctx.author.color) 
            await ctx.send(embed = em)