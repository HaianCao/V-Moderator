import discord
from discord.ext import commands
from discord.role import R
from Action.chui import chui
from Action.hello import hello
from Action.ranimg import random_image


class contact(commands.Cog, hello, chui, random_image):
    def __init__(self, client):
        self.client = client
        self.hello = hello
        self.chui = chui
        self.ranimg = random_image



def setup(client):
    client.add_cog(contact(client))