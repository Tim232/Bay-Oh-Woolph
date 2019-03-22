from discord.ext import commands
import discord
from bayohwoolph import bot

from config import Config

import logging
logger = logging.getLogger('bayohwoolph.cogs.mgmanager')

MULTIGAMETAGS = Config.config['MULTIGAMETAGS']


ROLE_APEX = MULTIGAMETAGS['ROLE_APEX']
ROLE_WOW = MULTIGAMETAGS['ROLE_WOW']
ROLE_TCTD2 = MULTIGAMETAGS['ROLE_TCTD2']
ROLE_FORTNITE = MULTIGAMETAGS['ROLE_FORTNITE']
ROLE_ROE = MULTIGAMETAGS['ROLE_ROE']
ROLE_SOT = MULTIGAMETAGS['ROLE_SOT']
ROLE_MINECRAFT = MULTIGAMETAGS['ROLE_MINECRAFT']


Games = [
    'apexlegends',
    'worldofwarships',
    'minecraft',
    'seaofthieves',
    'ringofelysium',
    'fortnite',
    'thedivision2'

]

apexlegends = ROLE_APEX
worldofwarships = ROLE_WOW
minecraft = ROLE_MINECRAFT
seaofthieves = ROLE_SOT
ringofelysium = ROLE_ROE
fortnite = ROLE_FORTNITE
thedivision2 = ROLE_TCTD2




tags_added = """"Congrats your are the proud owner of a new game tag"""




class Test:

    def __init__(self,bot):
        self.bot = bot

    @commands.command()
    async def Add(self,ctx):
        """Adds game tags"""

        message = ctx.message.content
        member = ctx.message.author
        messagex = message.lower()
        messagey = messagex.replace(' ', '')
        messagey[3:]


        if messagey == any(Games):
            await ctx.send('Test Complete' +messagey)
        else:
            await ctx.send('Error')










def setup(bot):
    bot.add_cog(Test(bot))