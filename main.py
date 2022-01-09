from logging import error
import discord
import os
from discord import guild
from discord.ext import commands
from discord import client
from discord import embeds
from discord.colour import Color
from discord.embeds import E
from discord.ext import commands, tasks
from discord.role import R
from discord.ext.commands import Bot, has_permissions, CheckFailure
from discord import user
import time
import random
from youtube_dl import YoutubeDL
from discord.channel import VoiceChannel
import asyncio
from TOKEN import TOKEN
import json

os.chdir("C:\\Users\\Admin\\OneDrive\\Desktop\\Programing\\Discord\\V-Moderation")

# def get_prefix(client, message):
#     with open('prefix_data.json', 'r') as f:
#         prefixes = json.load(f)
#     return prefixes[str(message.guild.id)]

client = commands.Bot(command_prefix=['>>', 'v.'])



client.remove_command('help')
client.remove_command('invite')

# @client.event
# async def on_guild_join(guild):
#     with open('prefix_data.json', 'r') as f:
#         prefixes = json.load(f)
#     prefixes[str(guild.id)] = '>>'
#     with open('prefix_data.json', 'w') as f:
#         prefixes = json.load(f)

@client.group(invoke_without_command=True)
async def help(ctx):
    em = discord.Embed(title='**V-Moderation Help**', description='Dùng command `>>help <command/category>` để biết chi tiết các lệnh', color=ctx.author.color)        
    em.add_field(name='Moderation', value='`kick ban unban\nmute unmute clear\narole rrole crole\ndrole send`')
    em.add_field(name='Action', value='`hello chui ranimg`')
    em.add_field(name='Invite', value='`invite`')
    await ctx.send(embed = em)

@help.command()
async def category(ctx):
    em = discord.Embed(title='**V-Moderation Help**', description='', color=ctx.author.color) 
    em.add_field(name='**Category**', value='Moderation\nAction\nInvite')
    await ctx.send(embed = em)

@help.command()
async def moderation(ctx):
    em = discord.Embed(title='**V-Moderation Help**', description='', color=ctx.author.color) 
    em.add_field(name='**Moderation**', value='`kick ban unban mute unmute clear arole rrole crole drole send`')
    await ctx.send(embed = em)

@help.command()
async def action(ctx):
    em = discord.Embed(title='**V-Moderation Help**', description='', color=ctx.author.color) 
    em.add_field(name='**Action**', value='`hello chui ranimg`')
    await ctx.send(embed = em)

@help.command()
async def invite(ctx):
    em = discord.Embed(title='**Invite**', description='''
    **V-Moderation**: https://discord.com/api/oauth2/authorize?client_id=900963690931695667&permissions=8&scope=bot
    **V-Economy**: https://discord.com/api/oauth2/authorize?client_id=927009128054931547&permissions=137439267840&scope=bot''', color=ctx.author.color) 
    await ctx.send(embed = em)
    
@help.command()
async def kick(ctx):
    em = discord.Embed(title='**Kick**', description='Dùng command `>>kick <member> [lí do]` để đá đít người khác khỏi server', color=ctx.author.color) 
    em.add_field(name='Yêu cầu:', value='Có quyền kick các thành viên khác', inline=False)
    await ctx.send(embed = em)

@help.command()
async def ban(ctx):
    em = discord.Embed(title='**Ban**', description='Dùng command `>>ban <@member> [thời gian] [lí do]` để quẳng người khác vô cũi :>>>', color=ctx.author.color) 
    em.add_field(name='Yêu cầu:', value='Có quyền ban các thành viên khác', inline=False)
    await ctx.send(embed = em)

@help.command()
async def unban(ctx):
    em = discord.Embed(title='**Unban**', description='Dùng command `>>unban <name#id>` để bỏ ban người khác', color=ctx.author.color) 
    em.add_field(name='Yêu cầu:', value='Có quyền unban các thành viên khác', inline=False)
    await ctx.send(embed = em)

@help.command()
async def mute(ctx):
    em = discord.Embed(title='**Mute**', description='Dùng command `>>mute <@member> [thời gian] [lí do]` để mute người khác', color=ctx.author.color) 
    em.add_field(name='Yêu cầu:', value='Có quyền mute các thành viên khác', inline=False)
    await ctx.send(embed = em)

@help.command()
async def unmute(ctx):
    em = discord.Embed(title='**Unmute**', description='Dùng command `>>unmute <@member>` để unmute người khác', color=ctx.author.color) 
    em.add_field(name='Yêu cầu:', value='Có quyền unmute các thành viên khác', inline=False)
    await ctx.send(embed = em)

@help.command()
async def clear(ctx):
    em = discord.Embed(title='**Clear**', description='Dùng command `>>clear <số lượng>` để xóa tin nhắn', color=ctx.author.color) 
    em.add_field(name='Yêu cầu:', value='Có quyền quản lí tin nhắn', inline=False)
    await ctx.send(embed = em)

@help.command()
async def arole(ctx):
    em = discord.Embed(title='**Add Role**', description='Dùng command `>>arole <@member> <@role> [thời gian]` để thêm role cho người khác', color=ctx.author.color) 
    em.add_field(name='Yêu cầu:', value='Có quyền quản lí role', inline=False)
    await ctx.send(embed = em)

@help.command()
async def rrole(ctx):
    em = discord.Embed(title='**Remove Role**', description='Dùng command `>>rrole <@member> <@role>` để loại bỏ role khỏi người khác', color=ctx.author.color) 
    em.add_field(name='Yêu cầu:', value='Có quyền quản lí role', inline=False)
    await ctx.send(embed = em)

@help.command()
async def crole(ctx):
    em = discord.Embed(title='**Create Role**', description='Dùng command `>>crole <màu> <tên role>` để tạo 1 role mới', color=ctx.author.color) 
    em.add_field(name='Yêu cầu:', value='Có quyền quản lí role', inline=False)
    em.add_field(name='Lưu ý:', value='Màu sắc được thiết lập bằng hex color', inline=False)
    await ctx.send(embed = em)

@help.command()
async def drole(ctx):
    em = discord.Embed(title='**Delete Role**', description='Dùng command `>>drole <@role>` xóa role khỏi server', color=ctx.author.color) 
    em.add_field(name='Yêu cầu:', value='Có quyền quản lí role', inline=False)
    await ctx.send(embed = em)

@help.command()
async def send(ctx):
    em = discord.Embed(title='**Send**', description='Dùng command `>>send <#channel> <message>` để gián tiếp gửi tin nhắn đến 1 channel khác', color=ctx.author.color) 
    em.add_field(name='Yêu cầu:', value='Moderator', inline=False)
    await ctx.send(embed = em)

@help.command()
async def hello(ctx):
    em = discord.Embed(title='**Hello**', description='Dùng command `>>hello` để chào bot', color=ctx.author.color) 
    await ctx.send(embed = em)

@help.command()
async def chui(ctx):
    em = discord.Embed(title='**Chửi**', description='Dùng command `>>chui <@member>` để bot chửi người đó hộ bạn', color=ctx.author.color) 
    await ctx.send(embed = em)

@help.command()
async def ranimg(ctx):
    em = discord.Embed(title='**Random Image**', description='Dùng command `>>ranimg` để xem ảnh ngẫu nhiên', color=ctx.author.color) 
    await ctx.send(embed = em)


@client.command()
async def invite(ctx):
    em = discord.Embed(title='**Invite**', description='''
    **V-Moderation**: https://discord.com/api/oauth2/authorize?client_id=900963690931695667&permissions=8&scope=bot
    **V-Economy**: https://discord.com/api/oauth2/authorize?client_id=927009128054931547&permissions=137439267840&scope=bot''', color=ctx.author.color) 
    await ctx.send(embed = em)


# @client.command()
# @commands.has_permissions(administrator=True)
# async def prefix(ctx, prefix):
#     with open('prefix_data.json', 'r') as f:
#         prefixes = json.load(f)
#     prefixes[str(guild.id)] = prefix
#     with open('prefix_data.json', 'w') as f:
#         json.dump(prefixes, f)



@client.event
async def on_ready():
    print('Connected to bot: {}'.format(client.user.name))
    print('Bot ID: {}'.format(client.user.id))

async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')
async def load(ctx, extension):
    client.unload_extension(f'cogs.{extension}')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run(TOKEN)
