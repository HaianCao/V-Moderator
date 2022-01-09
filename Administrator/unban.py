import discord
from discord import client
from discord import embeds
from discord.ext import commands
import random
import time
from discord.ext.commands import Bot, has_permissions, CheckFailure

class unban():
    @commands.command()
    @has_permissions(ban_members=True)
    async def unban(self, ctx, *,member: str):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')
        for ban_entry in banned_users:
            user = ban_entry.user
            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                em = discord.Embed(title='', description=f'Unban @{member}', color=ctx.author.color) 
                await ctx.send(embed = em)
                return

    @unban.error
    async def unban_error(self, ctx, error):
        if isinstance(error, CheckFailure):
            em = discord.Embed(title='', description='Bạn không có quyền sử dụng command này', color=ctx.author.color) 
            await ctx.send(embed = em)