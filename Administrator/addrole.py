import discord
from discord.ext import commands
import random
import time
from discord.ext.commands import Bot, has_permissions, CheckFailure
import asyncio

class arole():
    @commands.command(pass_context=True)
    @has_permissions(manage_roles=True)
    async def arole(self, ctx, member: discord.Member, role: discord.Role, time=None):
        if time==None:
            await member.add_roles(role)
            em = discord.Embed(title='', description=f'Thêm role {role} cho {member.mention}', color=ctx.author.color) 
            await ctx.send(embed = em)
        else:    
            def convert_str_to_number(x):
                total_stars = 0
                num_map = {"s":1, "S":1, "m":60, "M":60, "h":3600, "H":3600, "d":86400, "D":86400}
                if x.isdigit():
                    total_stars = int(x)
                else:
                    if len(x) > 1:
                        total_stars = float(x[:-1]) * num_map.get(x[-1].upper(), 1)
                return int(total_stars)
            temprole = convert_str_to_number(time)
            await member.add_roles(role)
            em = discord.Embed(title='', description=f'Thêm role {role} cho {member.mention} trong thời gian {temprole} giây', color=ctx.author.color) 
            await ctx.send(embed = em)
            await asyncio.sleep(temprole)
            await member.remove_roles(role)

    @arole.error
    async def add_role_error(self, ctx, error):
        if isinstance(error, CheckFailure):
            em = discord.Embed(title='', description='Bạn không có quyền sử dụng command này', color=ctx.author.color) 
            await ctx.send(embed = em)