import discord
from discord.ext import commands
import random
import time
from Administrator.ban import ban
from Administrator.clear import clear
from Administrator.kick import kick
from Administrator.mute import mute
from Administrator.unban import unban
from Administrator.unmute import unmute
from Administrator.mute import mute
from Administrator.addrole import arole
from Administrator.removerole import rrole
from Administrator.createrole import crole
from Administrator.deleterole import drole
from Administrator.sendmes import sendmes





class administrator(commands.Cog, ban, kick, unban, clear, unmute, mute, arole, rrole, crole, drole, sendmes):
    def __init__(self, client):
        self.client = client
        self.kick = kick
        self.ban = ban
        self.unban = unban
        self.clear = clear
        self.mute = mute
        self.unmute = unmute
        self.arole = arole
        self.rrole = rrole
        self.crole = crole
        self.drole = drole
        self.drole = drole
        self.send = sendmes



def setup(client):
    client.add_cog(administrator(client))