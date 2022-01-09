import discord
from discord.ext import commands
import random
import time
from discord.ext.commands import Bot, has_permissions, CheckFailure
import asyncio

class ban():
    @commands.command(pass_context=True)
    @has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, time=None, *, reason=None):
        if time==None:
            await member.ban(reason=reason)
            em = discord.Embed(title='', description=f'''Ban {member.mention} vĩnh viễn
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
            tempban = convert_str_to_number(time)
            await member.ban(reason=reason)
            em = discord.Embed(title='', description=f'Ban {member.mention} trong thời gian {tempban} giây', color=ctx.author.color) 
            await ctx.send(embed = em)
            await asyncio.sleep(tempban)
            await member.unban(reason='Tự động unban bởi @Society\'s Vices (Beta)#7577')

        time.sleep(1.0)
        chosen = random.randint(0, 10)
        a = [
            'Bờ an ban :3',
            'Vô cũi :3',
            'Ăn ban lè :3',
            'Ai muốn là tù nhân của e nào :3',
            'Ban cho nhớ :))',
            'Chết lè con trai :D',
            'Phía sau song sắt là phòng giam :3',
            'Luật hoa quả ko chừa 1 ai :D',
            'Hasagi',
            'Trao cho a chiếc còng tay...',
            'Quẳng vào ngục cho chừa này :3'
        ]
        await ctx.send(a[chosen])

    @ban.error
    async def ban_error(self, ctx, error):
        if isinstance(error, CheckFailure):
            em = discord.Embed(title='', description='Bạn không có quyền sử dụng command này', color=ctx.author.color) 
            await ctx.send(embed = em)