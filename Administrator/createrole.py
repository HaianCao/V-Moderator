import discord
from discord import client
from discord import embeds
from discord import guild
from discord.ext import commands
import random
import time
from discord.ext.commands import Bot, has_permissions, CheckFailure

class crole():
    @commands.command()
    @has_permissions(manage_roles=True)
    async def crole(self, ctx, color=None, *, role_name):
        if color==None:
            await ctx.guild.create_role(name=role_name, colour=discord.Colour(0xfcba03))
            role=discord.utils.get(ctx.guild.roles, name=role_name)
            em = discord.Embed(title='', description=f'Đã tạo role {role.mention}', color=ctx.author.color) 
            await ctx.send(embed = em)
        else:    
            await ctx.guild.create_role(name=role_name, colour=discord.Colour(int(f"0x{color}", 16)))
            role=discord.utils.get(ctx.guild.roles, name=role_name)
            em = discord.Embed(title='', description=f'Đã tạo role {role.mention}', color=ctx.author.color) 
            await ctx.send(embed = em)


    @crole.error
    async def unmute_error(self, ctx, error):
        if isinstance(error, CheckFailure):
            em = discord.Embed(title='', description='Bạn không có quyền sử dụng command này', color=ctx.author.color) 
            await ctx.send(embed = em)