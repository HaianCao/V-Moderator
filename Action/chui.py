import discord
from discord.ext import commands
import random


class chui():
    @commands.command()
    async def chui(self, ctx, member : discord.Member):
        randomChosen = random.randint(0, 10)
        a = [
            f'{member.mention} gà con :hatching_chick:',
            f'{member.mention} non xanh :smiley:',
            f'{member.mention} đồ ngốk :yum:',
            f'{member.mention} sao so đc vs a an đzai :smirk:',
            f'{member.mention} tuổi gì :)))',
            f'{member.mention} là gà công nghiệp :rooster:',
            f'{member.mention} quêeeeeeee',
            f'Baka {member.mention} :flushed:',
            f'{member.mention} :333333',
            f'Iu a {member.mention} nhất :333',
            f'Vc  đ gì t phải chửi {member.mention} hộ m :stuck_out_tongue_closed_eyes:'
        ]
        await ctx.send(a[randomChosen])
