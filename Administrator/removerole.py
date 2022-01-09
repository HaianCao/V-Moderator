import discord
from discord import client
from discord import embeds
from discord.ext import commands
import random
import time
from discord.ext.commands import Bot, has_permissions, CheckFailure

class rrole():
    @commands.command()
    @has_permissions(manage_roles=True)
    async def rrole(self, ctx, member: discord.Member, role: discord.Role):
        await member.remove_roles(role)
        em = discord.Embed(title='', description=f'Đã bỏ role {role.mention} khỏi {member.mention}', color=ctx.author.color) 
        await ctx.send(embed = em)
    
    @rrole.error
    async def rrole_error(self, ctx, error):
        if isinstance(error, CheckFailure):
            em = discord.Embed(title='', description='Bạn không có quyền sử dụng command này', color=ctx.author.color) 
            await ctx.send(embed = em)