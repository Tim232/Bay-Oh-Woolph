from discord.ext import commands
from utils import *
import discord
import asyncio
from cogs.updateroster import UpdateRoster

from config import Config

import logging
logger = logging.getLogger('bayohwoolph.cogs.basicpromotions')

BASICPROMOTIONS = Config.config['BASICPROMOTIONS']

ROLE_CADET = BASICPROMOTIONS['ROLE_CADET']
ROLE_OFFICER = BASICPROMOTIONS['ROLE_OFFICER']
ROLE_PS4 = BASICPROMOTIONS['ROLE_PS4']

CADETS_MESS = BASICPROMOTIONS['CADETS_MESS']
PS4_ROOM = BASICPROMOTIONS['PS4_ROOM']
OFFICERS_CLUB = BASICPROMOTIONS['OFFICERS_CLUB']
BOT_NOISE = BASICPROMOTIONS['bot_noise']

ROLE_MEMBER = BASICPROMOTIONS['ROLE_MEMBER']

NEWPCCADETMSG = """**Welcome to Dark Echo, {0}!**

**<:echoBlue:230423421983522816> Here are the basic steps to get started with Dark Echo: <:echoBlue:230423421983522816>**

1. Sign up for a forum account at <http://darkecho.org/forums/ucp.php?mode=register>
2. If you use Inara, join us at http://inara.cz/wing/300
3. In the game, under "Friends and Private Groups", request membership in the "Dark Echo" private group and send "Dark Echo" a friend request.
4. Send in-game friend requests to the Echoes you see currently active on Discord and/or via in the in-game private group.
5. Check <#161529165223428096> for current priorities and <#173601634096644106> for all sorts of useful stuff.
6. Move your primary base of operations (any additional ships, etc) to Snodgrass Orbital in Disci.
7. Once your forum account is activated, look for "Getting Started" instructions there.
8. Set your ship id to [ECHO] or put [ECHO] in your ship name, whichever you prefer.

Note: You cannot get to Disci in a starter sidewinder.  You need 9.5LY jump range.  Upgrade Sidewinder or Eagle from "E" to "D"; or use a Hauler. If you're still having trouble, talk to us and somebody can help.

Make sure you get that forum account set up, since that's what we use to track how long you've been a Cadet.

Please set an avatar image in Discord, as it greatly helps with telling people apart when using the in-game overlay.

If you stay active with us for a couple of weeks and haven't heard about a promotion to Officer, please remind the <@&146724062301913088>.
"""

NEWPS4CADETMSG = """**Welcome to Dark Echo, {0}!**

**<:echoBlue:230423421983522816> Here are the basic steps to get started with Dark Echo: <:echoBlue:230423421983522816>**

1. Sign up for a forum account at <http://darkecho.org/forums/ucp.php?mode=register>
2. If you use Inara, join us at http://inara.cz/wing/300
3. Send a PSN friend request to "Elite-DarkEcho".
3. Once PSN friend request is accepted: In the game, under "Friends and Private Groups",Send a friend request and request membership in the "Elite-DarkEcho" private group.
4. Once your forum account is set up, visit <http://darkecho.org/forums/memberlist.php?g=14&mode=group> and send everybody on that list a friend request.
5. Check <#161529165223428096> for current priorities and <#173601634096644106> for all sorts of useful stuff.
6. Move your primary base of operations (any additional ships, etc) to Snodgrass Orbital in Disci.
7. Once your forum account is activated, look for "Getting Started" instructions there.
8. Set your ship id to [ECHO] or put [ECHO] in your ship name, whichever you prefer.

Note: You cannot get to Disci in a starter sidewinder.  You need 9.5LY jump range.  Upgrade Sidewinder or Eagle from "E" to "D"; or use a Hauler. If you're still having trouble, talk to us and somebody can help.

Make sure you get that forum account set up, since that's what we use to track how long you've been a Cadet.

If you stay active with us for a couple of weeks and haven't heard about a promotion to Officer, please remind the Leadership.
"""

NEWOFFICERMSG = """**<:echoBlue:230423421983522816> Welcome to Dark Echo's Officer's Club, {0}!**

Dark Echo <@&146724062301913088> believe that you are an asset to this organization, and has promoted you to a full member (Officer).

Optional but traditional and highly recommended: Please bring some sort of rare beverage to Snodgrass Orbital in Disci and share a screenshot of that run on the forums and/or in <#173953415280328704>.

A <@&235466370316238848> will update your forum permissions. Once your forum permissions are set up, make sure to:
* Read the latest Standing Orders: <http://www.darkecho.org/forums/viewforum.php?f=6>
* "Subscribe" to DE Urgent: <http://www.darkecho.org/forums/viewforum.php?f=7>
* and also "Ops": <http://www.darkecho.org/forums/viewforum.php?f=9>

If you use Inara, join us at <http://inara.cz/wing/300>

Have you checked out all the useful stuff in <#173601634096644106>?

(Reminder to <@&146724062301913088>: Go do a "!addroster Nickname" in #allies, and update forum groups)

"""

class Basicpromotions:
    """Leadership/Recruiter commands for promoting to basic membership roles."""
    
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_any_role('Leadership','Recruiter')
    @asyncio.coroutine
    def newpccadet(self,
        member1  : discord.Member = None, 
        member2  : discord.Member = None, 
        member3  : discord.Member = None, 
        member4  : discord.Member = None, 
        member5  : discord.Member = None, 
        member6  : discord.Member = None, 
        member7  : discord.Member = None, 
        member8  : discord.Member = None, 
        member9  : discord.Member = None, 
        member10 : discord.Member = None, 
        member11 : discord.Member = None, 
        member12 : discord.Member = None, 
        member13 : discord.Member = None, 
        member14 : discord.Member = None, 
        member15 : discord.Member = None, 
        member16 : discord.Member = None, 
        member17 : discord.Member = None, 
        member18 : discord.Member = None, 
        member19 : discord.Member = None, 
        member20 : discord.Member = None ):
        """Get new PC platform Cadet started."""

        yield from self.bot.type()

        # pull all the arguments into an array
        argmembers = [member1, member2, member3, member4, member5, member6, member7, member8, member9, member10, member11, member12, member13, member14, member15, member16, member17, member18, member19, member20 ]

        # and then filter out the None/empty items, so that we have only an array of things actually mentioned
        filter(None,argmembers)
        members = [i for i in argmembers if i is not None]

        memrole = discord.Object(id=ROLE_MEMBER)
        cadetrole = discord.Object(id=ROLE_CADET)

        for member in members:
            try:
                yield from self.bot.add_roles(member,cadetrole,memrole)
            except Exception as e:
                yield from self.bot.say('Unable to set Officer role.')

        mentiontext = memberlist_to_mentionlist(members)

        cadetsmess = self.bot.get_channel(CADETS_MESS)

        yield from self.bot.send_message(cadetsmess,NEWPCCADETMSG.format(mentiontext))
        yield from self.bot.say('Go check out <#{}>, '.format(CADETS_MESS) + mentiontext + '.')

    @commands.command()
    @commands.has_any_role('Leadership','Recruiter')
    @asyncio.coroutine
    def newps4cadet(self,
        member1  : discord.Member = None, 
        member2  : discord.Member = None, 
        member3  : discord.Member = None, 
        member4  : discord.Member = None, 
        member5  : discord.Member = None, 
        member6  : discord.Member = None, 
        member7  : discord.Member = None, 
        member8  : discord.Member = None, 
        member9  : discord.Member = None, 
        member10 : discord.Member = None, 
        member11 : discord.Member = None, 
        member12 : discord.Member = None, 
        member13 : discord.Member = None, 
        member14 : discord.Member = None, 
        member15 : discord.Member = None, 
        member16 : discord.Member = None, 
        member17 : discord.Member = None, 
        member18 : discord.Member = None, 
        member19 : discord.Member = None, 
        member20 : discord.Member = None ):
        """Get new Playstation4 platform Cadet started."""

        yield from self.bot.type()

        # pull all the arguments into an array
        argmembers = [member1, member2, member3, member4, member5, member6, member7, member8, member9, member10, member11, member12, member13, member14, member15, member16, member17, member18, member19, member20 ]

        # and then filter out the None/empty items, so that we have only an array of things actually mentioned
        filter(None,argmembers)
        members = [i for i in argmembers if i is not None]

        memrole = discord.Object(id=ROLE_MEMBER)
        cadetrole = discord.Object(id=ROLE_CADET)
        ps4role = discord.Object(id=ROLE_PS4)

        for member in members:
            try:
                yield from self.bot.add_roles(member,cadetrole,memrole,ps4role)
            except Exception as e:
                yield from self.bot.say('Unable to set Officer role.')

        mentiontext = memberlist_to_mentionlist(members)

        cadetsmess = self.bot.get_channel(CADETS_MESS)
        ps4room    = self.bot.get_channel(PS4_ROOM)

        yield from self.bot.send_message(cadetsmess,NEWPS4CADETMSG.format(mentiontext))
        yield from self.bot.send_message(ps4room,'<@&269222564826447872> Please send an in-game friend request to ' + mentiontext)
        yield from self.bot.say('Go check out <#{}>, '.format(CADETS_MESS) + mentiontext + '.')
        

    @commands.command()
    @commands.has_role('Leadership')
    @asyncio.coroutine
    def newofficer(self,
        member1  : discord.Member = None, 
        member2  : discord.Member = None, 
        member3  : discord.Member = None, 
        member4  : discord.Member = None, 
        member5  : discord.Member = None, 
        member6  : discord.Member = None, 
        member7  : discord.Member = None, 
        member8  : discord.Member = None, 
        member9  : discord.Member = None, 
        member10 : discord.Member = None, 
        member11 : discord.Member = None, 
        member12 : discord.Member = None, 
        member13 : discord.Member = None, 
        member14 : discord.Member = None, 
        member15 : discord.Member = None, 
        member16 : discord.Member = None, 
        member17 : discord.Member = None, 
        member18 : discord.Member = None, 
        member19 : discord.Member = None, 
        member20 : discord.Member = None ):
        """Give intro message to new officer and assign them Officer role."""

        yield from self.bot.type()

        # pull all the arguments into an array
        argmembers = [member1, member2, member3, member4, member5, member6, member7, member8, member9, member10, member11, member12, member13, member14, member15, member16, member17, member18, member19, member20 ]

        # and then filter out the None/empty items, so that we have only an array of things actually mentioned
        filter(None,argmembers)
        members = [i for i in argmembers if i is not None]

        officerrole = discord.Object(id=ROLE_OFFICER)
        cadetrole = discord.Object(id=ROLE_CADET)
        officersclub = self.bot.get_channel(OFFICERS_CLUB)
        botnoise = self.bot.get_channel(BOT_NOISE)
        
        for member in members:
            try:
                yield from self.bot.add_roles(member,officerrole)
            except Exception as e:
                yield from self.bot.say('Unable to set Officer role.')

            cleannick = member_to_clean_nick(member)
            yield from self.bot.send_message(botnoise, '!addroster ' + cleannick)

        mentiontext = memberlist_to_mentionlist(members)

        # sleep for a second to make sure the role has gone through before sending messages that need it
        yield from asyncio.sleep(1)

        yield from self.bot.send_message(officersclub,NEWOFFICERMSG.format(mentiontext))

        yield from self.bot.send_message(botnoise,"!whois -r -d -role 'Officer' -nick")

        for member in members:
            yield from self.bot.remove_roles(member,cadetrole)


def setup(bot):
    bot.add_cog(Basicpromotions(bot))
