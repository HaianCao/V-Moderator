import discord
from discord import client
from discord import embeds
from discord.ext import commands
import random
import time
from discord.ext.commands import Bot, has_permissions, CheckFailure
import asyncio
from discord.utils import get

class mute():
    @commands.command()
    @has_permissions(kick_members=True)
    async def mute(self, ctx, member: discord.Member=None, time=None, *, reason=None):
        if get(ctx.guild.roles, name="muted"):
            muted_role=discord.utils.get(ctx.guild.roles, name="muted")
            if time==None:
                await member.add_roles(muted_role, reason=reason)
                em = discord.Embed(title='', description=f'''Mute {member.mention} vĩnh viễn
                **Lí do**: {reason}''', color=ctx.author.color) 
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
                tempmute = convert_str_to_number(time)
                await member.add_roles(muted_role, reason=reason)
                em = discord.Embed(title='', description=f'''Mute {member.mention} trong thời gian {tempmute} giây
                **Lí do**: {reason}''', color=ctx.author.color) 
                await ctx.send(embed = em)
                await asyncio.sleep(tempmute)
                await member.remove_roles(muted_role, reason='Tự động unmute bởi @Society\'s Vices (Beta)#7577')
        else: 
            await ctx.guild.create_role(name="muted", colour=discord.Colour(0xc22a1f))
            em = discord.Embed(title='', description='Do không tìm thấy role muted trong server nên mình đã tạo 1 role muted cho bạn rồi nka UwU. Hãy chỉnh lại role muted cho phù hợp với mục đích của bạn nka :smiling_face_with_3_hearts:', color=ctx.author.color) 
            await ctx.send(embed = em)

        time.sleep(1.0)
        chosen = random.randint(0, 10)
        a = [
            'Im',
            'Xuỵt',
            'Xùy xùy ￣へ￣',
            'Shut your mouth up',
            'Im nào -.-',
            'Im không t cho m ra đảo h',
            'Shhhhh',
            '(* ￣︿￣)',
            '(¬_¬")',
            '(ㆆ_ㆆ)'
        ]
        await ctx.send(a[chosen])
    @mute.error
    async def mute_error(self, ctx, error):
        if isinstance(error, CheckFailure):
            em = discord.Embed(title='', description='Bạn không có quyền sử dụng command này', color=ctx.author.color) 
            await ctx.send(embed = em)