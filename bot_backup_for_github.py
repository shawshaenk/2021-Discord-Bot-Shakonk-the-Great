import discord
import random
import sys
import os
import asyncio
import praw
import time
from discord.ext import commands
import urllib.parse, urllib.request, re
from PIL import Image
from io import BytesIO
import json
from datetime import datetime, timezone
from discord.ext.commands.cooldowns import BucketType

intents = discord.Intents(messages=True, guilds=True, members=True)

snipe_message_content = []
snipe_message_author = []
snipe_message_id = []
snipe_message_channel = []
snipe_message_by=[]
snipe_message_time=[]
t = time.localtime()
current_time = time.strftime("%I:%M", t)
time_var_2=""
created=""

edit_message_id=[]
edit_message_author=[]
edit_message_id=[]
edit_message_channel=[]
edit_message_content=[]
msg=""

client=commands.Bot(command_prefix="/", case_insensitive=True, intents=intents)
token="[YOUR TOKEN HERE]"

def is_it_me(ctx):
 return ctx.author.id==[YOUR AUTHOR ID HERE]



client.remove_command('help')

@client.command()
async def help(ctx, arg=None):
 string1=""
 if arg==None:
     commands=["**Version: 8.0**",
               "**Bot prefix: /**",
               "",
               "**Useful Commands:**",
               "help: Displays this message",
               "snipe: Shows the last deleted messages",
               "edsnipe: Snipes the last edited message",
               "clear: Clears a certain amount of message",
               "ping: Tests your network delay",
               "timer: Sets a timer for a specified amount of minutes",
               "",
               "**Fun Commands:**",
               "reddit: Sends a random image from a subreddit of your choice",
               "help economy: Shows another help command",
               "yt: Searches something of your choice and randomly sends a video based on the search's results",
               "kakashi: Puts your pfp or someone else's pfp on a Naruto scene",
               "describe: Describes something of your choice",
               "wizard: Tells you the future by randomly generating an 8ball reply",
               "fortune: Randomly returns the name of someone in the server",
               "appa: Sends pictures of Appa"]
     for i in commands:
         string1+=f"{i}\n"
     embed = discord.Embed(title="Shakonk The Great", description=f"{string1}", color=0x3498db)
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/711581020671180820/779792802120466482/Shakonk_The_Great.png")
     embed.set_footer(text="(More commands coming soon!)", icon_url="https://cdn.discordapp.com/attachments/711581020671180820/779792802120466482/Shakonk_The_Great.png")
     await ctx.send(embed=embed)
     return
 elif arg=="economy":
     commands=["profile: Shows you your profile",
               "beg: You can get free money transferred to your wallet",
               "negotiate: You can get free money transferred to your bank",
               "stocks: Invest some money and see your wealth grow",
               "steal: Steals money from another user and puts it in your wallet",
               "give: Gives money to another person and puts it in their wallet",
               "businesses: Checks how your businesses are doing and puts their money in your bank",
               "withdraw: Takes money from your bank and puts it in your wallet",
               "deposit: Takes money from your wallet and puts it in your bank",
               "invest: Invests money in stocks from your wallet",
               "withdrawstocks: Withdraws the money you made from stocks"]
     for i in commands:
         string1+=f"{i}\n"
     embed = discord.Embed(title="Shakonk The Great: Economy Edition", description=f"{string1}", color=0x3498db)
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/780474442446405644/781242284096094228/unknown.png")
     embed.set_footer(text="(More commands coming soon!)", icon_url="https://cdn.discordapp.com/attachments/711581020671180820/779792802120466482/Shakonk_The_Great.png")
     await ctx.send(embed=embed)
     return

@client.event
async def on_ready():
 await client.change_presence(status=discord.Status.online, activity=discord.Game("/help"))
 print("Bot is ready")

rreddit = praw.Reddit(
    client_id="[REDDIT_CLIENT_ID]",
    client_secret="[REDDIT_CLIENT_SECRET]",
    username="[REDDIT_USERNAME]",
    password="[REDDIT_PASSWORD]",
    user_agent="[REDDIT_USER_AGENT]"
)

@client.command(pass_context=True)
async def appa(ctx):
   subreddit = rreddit.subreddit(f"appa")
   all_subs = []

   top = subreddit.top(limit=50)

   for submission in top:
       all_subs.append(submission)

   random_sub = random.choice(all_subs)

   name = random_sub.title
   url = random_sub.url

   em = discord.Embed(title=name, colour=0x3498db)

   em.set_image(url=url)

   await ctx.send(embed=em)



@client.command(pass_context=True)
async def reddit(ctx, arg="memes"):
   try:
       subreddit = rreddit.subreddit(f"{arg}")

       if subreddit.over18:
           raise Exception()

       all_subs = []

       top = subreddit.top(limit=50)

       for submission in top:
           if submission.over_18:
               top.remove(submission)
           else:
               all_subs.append(submission)

       random_sub = random.choice(all_subs)

       name = random_sub.title
       url = random_sub.url

       em = discord.Embed(title=name, colour=0x3498db)

       em.set_image(url=url)

       await ctx.send(embed=em)
   except:
       await ctx.send("Sorry, you either tried to visit a restricted subreddit or I couldn't find the subreddit. Please try again.")

@client.command()
async def ping(ctx):
   await ctx.send(f"Pong! Your latency is: {round(client.latency*1000)}ms")

@client.command()
@commands.check(is_it_me)
async def run(ctx):
  await ctx.send("Successfully created script. Will now run in background.")
  os.execv(sys.executable, ['python'] + sys.argv)

@client.command()
@commands.check(is_it_me)
async def say(ctx, *, arg):
 if len(await ctx.channel.purge(limit=200, check=lambda x: ('/say' in x.content.strip().lower()))) > 0:
     await ctx.send(arg)

@client.command()
@commands.check(is_it_me)
async def cleartext(ctx, *, arg):
  if len(await ctx.channel.purge(limit=200, check=lambda x: (f'{arg}' in x.content.strip().lower()))) > 0:
      pass

@client.group()
async def timer(ctx, arg, arg2, arg3):
  arg2=float(arg2)
  if arg3=="minutes" or arg3=="minute":
      await ctx.send(f'"{arg}" timer for {int(arg2)} minute(s) has begun.')
      arg2 = arg2 * 60
      await asyncio.sleep(arg2)
      await ctx.send(f'{ctx.author.mention} "{arg}" timer has ended.')
  elif arg3=="hours" or arg3=="hour":
      await ctx.send(f'"{arg}" timer for {int(arg2)} hour(s) has begun.')
      arg2 = arg2 * 3600
      await asyncio.sleep(arg2)
      await ctx.send(f'{ctx.author.mention} "{arg}" timer has ended.')
  elif arg3=="seconds" or arg3=="second":
      await ctx.send(f'"{arg}" timer for {int(arg2)} second(s) has begun.')
      await asyncio.sleep(arg2)
      await ctx.send(f'{ctx.author.mention} "{arg}" timer has ended.')

@client.command()
async def wizard(ctx):
 responses=["It is certain.",
              "It is decidedly so.",
              "Without a doubt.",
              "Yes – definitely.",
              "You may rely on it.",
              "As I see it, yes.",
              "Most likely.",
              "Outlook good.",
              "Yes.",
              "Signs point to yes.",
              "Don't count on it.",
              "My reply is no.",
              "My sources say no.",
              "Outlook not so good.",
              "Very doubtful.",
]
 choice=random.choice(responses)
 numbers=[10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
 num_choice=random.choice(numbers)
 squares=[]
 str1=""

 for i in range(num_choice//10):
     squares.append("⬜")

 while True:
     if len(squares)==10:
         break
     else:
         squares.append("🔳")

 for i in squares:
     str1+=(f"{i} ")

 embed = discord.Embed(title=f"{choice}", description=f"**Accuracy: {num_choice}%**\n{str1}",color=0x3498db)
 await ctx.send(embed=embed)
 return

@client.command()
@commands.check(is_it_me)
async def clear(ctx, amount=0):
 await ctx.channel.purge(limit=amount)

@client.command()
@commands.check(is_it_me)
async def annoy(ctx, amount=0):
 num=1
 while num<=amount:
     await ctx.send(f"I'm Annoying hahahahahhahahah ({num}/{amount})")
     num+=1
 await ctx.send("Limit reached. Will now exit annoy_now.")

@client.command()
async def describe(ctx):
 personalities=["https://cdn.discordapp.com/attachments/711581020671180820/744366678678306986/image0.png",
                "https://cdn.discordapp.com/attachments/711581020671180820/744366568825159790/image0.png",
                "https://cdn.discordapp.com/attachments/711581020671180820/744366344119517266/image0.png",
                "https://cdn.discordapp.com/attachments/711581020671180820/744366338490892318/image0.png",
                "https://cdn.discordapp.com/attachments/711581020671180820/744366337681260544/image0.png",
                "https://cdn.discordapp.com/attachments/711581020671180820/744366338524315768/image0.png",
                "https://cdn.discordapp.com/attachments/711581020671180820/744366315602706442/image0.png",
                "https://cdn.discordapp.com/attachments/711581020671180820/744376501667102800/image0.png",
                "https://cdn.discordapp.com/attachments/711581020671180820/744376511892815933/image0.png",
                "https://cdn.discordapp.com/attachments/711581020671180820/744376516380590221/image0.png",
                "https://cdn.discordapp.com/attachments/711581020671180820/744376521585721361/image0.png",
                "https://cdn.discordapp.com/attachments/711581020671180820/744376525951860796/image0.png",
                "https://cdn.discordapp.com/attachments/711581020671180820/744376529252909127/image0.png",
                "https://cdn.discordapp.com/attachments/711581020671180820/744607471133261844/image0.png",
                "https://cdn.discordapp.com/attachments/711581020671180820/744607478204858388/image0.png",
                "https://cdn.discordapp.com/attachments/711581020671180820/744607481334071336/image0.png",
                "https://cdn.discordapp.com/attachments/711581020671180820/744607479890968666/image0.png",
                "https://cdn.discordapp.com/attachments/711581020671180820/744607487604293672/image0.png",
                "https://cdn.discordapp.com/attachments/711581020671180820/744607494227361873/image0.png",
                "https://cdn.discordapp.com/attachments/711581020671180820/744607494177030154/image0.png",
                "https://cdn.discordapp.com/attachments/711581020671180820/744607618064056400/image0.png"]
 await ctx.send(f"{random.choice(personalities)} ")

@client.command()
@commands.check(is_it_me)
async def shutdown(ctx):
 await ctx.send("Successfully ended task. Will now go offline.")
 raise SystemExit

@client.command()
async def bulk(message):
   global snipe_message_content
   global snipe_message_author
   global snipe_message_id
   global snipe_message_channel
   global snipe_message_by
   global snipe_message_time
   global t
   global current_time
   global time_var_2
   global created
   async for entry in message.guild.audit_logs(action=discord.AuditLogAction.message_delete, limit=1):
       delete_by = "{0.target}".format(entry)
       delete_by_list = delete_by.split("#")
       delete_by_list.pop(-1)
       delete_by = ""
       for i in delete_by_list:
           delete_by += i
       sendtime=message.created_at
       if sendtime>=entry.created_at:
           if delete_by==message.author.name:
               delete_by_2 = "{0.user}".format(entry)
               delete_by_2_list = delete_by_2.split("#")
               delete_by_2_list.pop(-1)
               delete_by_2 = ""
               for i in delete_by_2_list:
                   delete_by_2 += i
               snipe_message_by.append(f"{delete_by_2}")
           else:
               snipe_message_by.append(f"{message.author.name}")
       else:
           snipe_message_by.append(f"{message.author.name}")

@client.event
async def on_message_delete(message):
   global snipe_message_content
   global snipe_message_author
   global snipe_message_id
   global snipe_message_channel
   global snipe_message_by
   global snipe_message_time
   global t
   global current_time
   global time_var_2
   global created
   snipe_message_channel.append(message.channel.id)
   snipe_message_content.append(message.content)
   snipe_message_author.append(message.author.name)
   snipe_message_id.append(message.id)
   t = time.localtime()
   time_var = time.strftime("%I:%M %p", t)
   snipe_message_time.append(time_var)
   async for entry in message.guild.audit_logs(action=discord.AuditLogAction.message_delete, limit=1):
       delete_by = "{0.target}".format(entry)
       delete_by_list = delete_by.split("#")
       delete_by_list.pop(-1)
       delete_by = ""
       for i in delete_by_list:
           delete_by += i
       sendtime=message.created_at
       if sendtime<=entry.created_at:
           if delete_by==message.author.name:
               delete_by_2 = "{0.user}".format(entry)
               delete_by_2_list = delete_by_2.split("#")
               delete_by_2_list.pop(-1)
               delete_by_2 = ""
               for i in delete_by_2_list:
                   delete_by_2 += i
               snipe_message_by.append(f"{delete_by_2}")
           else:
               com=client.get_command(name='bulk')
               await com.callback(message)
       else:
           com = client.get_command(name='bulk')
           await com.callback(message)


@client.command()
async def snipe(message, arg=1):
   try:
       global snipe_message_channel
       arg=int(arg)
       arg=-arg
       if snipe_message_content==[]:
           await message.channel.send("There's nothing to snipe!")
       if snipe_message_channel[arg]!=message.channel:
           count=arg
           list1=[]
           for h in snipe_message_channel:
               list1.append(f"{h}")
           index=[i for i, n in enumerate(list1) if n == f'{message.channel.id}'][count]
           embed = discord.Embed(description=f"{snipe_message_content[index]}\n\n**Deleted By**: {snipe_message_by[index]}", colour=0x3498db)
           embed.set_footer(text=f"Asked by {message.author.name}#{message.author.discriminator}", icon_url=message.author.avatar_url)
           embed.set_author(name=f"@{snipe_message_author[index]} - {snipe_message_time[index]}")
           await message.channel.send(embed=embed)

       if snipe_message_channel[arg]==message.channel:
           count=arg
           list1=[]
           for h in snipe_message_channel:
               list1.append(f"{h}")
           index=[i for i, n in enumerate(list1) if n == f'{message.channel.id}'][count]
           embed = discord.Embed(description=f"{snipe_message_content[index]}\n\n**Deleted By**: {snipe_message_by[index]}", colour=0x3498db)
           embed.set_footer(text=f"Asked by {message.author.name}#{message.author.discriminator}", icon_url=message.author.avatar_url)
           embed.set_author(name= f"@{snipe_message_author[index]} - {snipe_message_time[index]}")
           await message.channel.send(embed=embed)
           return
   except IndexError:
       await message.channel.send("There's nothing to snipe!")


@client.command()
async def chsnipe(message, channel_2: discord.TextChannel=None, arg=1):
   try:
       if channel_2 == None:
           chan=message.channel
           channel_2 = message.channel.id
       else:
           chan=channel_2
           channel_2=channel_2.id
       global snipe_message_channel
       arg=int(arg)
       arg=-arg
       if snipe_message_content==[]:
           await message.channel.send("There's nothing to snipe!")
       if snipe_message_channel[arg]!=channel_2:
           count=arg
           list1=[]
           for h in snipe_message_channel:
               list1.append(f"{h}")
           index=[i for i, n in enumerate(list1) if n == f'{channel_2}'][count]
           embed = discord.Embed(description=f"{snipe_message_content[index]}\n\n**Deleted By**: {snipe_message_by[index]}", colour=0x3498db)
           embed.set_footer(text=f"Sniped In: {chan}", icon_url=message.author.avatar_url)
           embed.set_author(name=f"@{snipe_message_author[index]} - {snipe_message_time[index]}")
           await message.channel.send(embed=embed)

       if snipe_message_channel[arg]==channel_2:
           count=arg
           list1=[]
           for h in snipe_message_channel:
               list1.append(f"{h}")
           index=[i for i, n in enumerate(list1) if n == f'{channel_2}'][count]
           embed = discord.Embed(description=f"{snipe_message_content[index]}\n\n**Deleted By**: {snipe_message_by[index]}", colour=0x3498db)
           embed.set_footer(text=f"Sniped In: {chan}", icon_url=message.author.avatar_url)
           embed.set_author(name= f"@{snipe_message_author[index]} - {snipe_message_time[index]}")
           await message.channel.send(embed=embed)
           return
   except IndexError:
       await message.channel.send("There's nothing to snipe!")

# @client.command()
# async def psnipe(message, user1: discord.Member=None, arg=1):
#     # try:
#         global snipe_message_channel
#         global snipe_message_content
#         user1 = str(user1)
#         user1_list = user1.split("#")
#         user1_list.pop(-1)
#         user1 = ""
#         for i in user1_list:
#             user1 += i
#         arg=int(arg)
#         arg=-arg
#         if snipe_message_content==[]:
#             await message.channel.send("There's nothing to snipe!")
#         if snipe_message_channel[arg]!=message.channel:
#             count=arg
#             list1=[]
#             for h in snipe_message_channel:
#                 list1.append(f"{h}")
#             list2=[]
#             for g in snipe_message_content:
#                 list2.append(f"{g}")
#             list3=[]
#             for i in list2:
#                 if i==user1:
#                     list3.append(f"{list2.index(i)}")
#             while True:
#                 index=[i for i, n in enumerate(list1) if n == f'{message.channel.id}'][count]
#                 if list3[index]==user1:
#                     break
#                 else:
#                     pass
#             embed = discord.Embed(description=f"{snipe_message_content[index]}\n\n**Deleted By**: {snipe_message_by[index]}", colour=0x3498db)
#             embed.set_footer(text=f"Person Sniped: {user1}", icon_url=message.user.avatar_url)
#             embed.set_author(name=f"@{snipe_message_author[index]} - {snipe_message_time[index]}")
#             await message.channel.send(embed=embed)
#
#         if snipe_message_channel[arg]==message.channel:
#             count=arg
#             list1=[]
#             for h in snipe_message_channel:
#                 list1.append(f"{h}")
#             list2=[]
#             for g in snipe_message_content:
#                 list2.append(f"{g}")
#             list3=[]
#             for i in list2:
#                 user1 = str(user1)
#                 user1_list = user1.split("#")
#                 user1_list.pop(-1)
#                 user1 = ""
#                 for i in user1_list:
#                     user1 += i
#                 if i==user1:
#                     list3.append(f"{i}")
#             index=[i for i, n in enumerate(list3) if n == f'{message.channel.id}'][count]
#             embed = discord.Embed(description=f"{snipe_message_content[index]}\n\n**Deleted By**: {snipe_message_by[index]}", colour=0x3498db)
#             embed.set_footer(text=f"Person Sniped: {user1}", icon_url=message.user.avatar_url)
#             embed.set_author(name=f"@{snipe_message_author[index]} - {snipe_message_time[index]}")
#             await message.channel.send(embed=embed)
   # except IndexError:
   #     await message.channel.send("There's nothing to snipe!")

@client.command()
async def test(message, user1: discord.Member=None):
   user1=str(user1)
   user1_list = user1.split("#")
   user1_list.pop(-1)
   user1 = ""
   for i in user1_list:
       user1 += i
   await message.channel.send(f"{user1}")
   await message.channel.send(f"{message.author.name}")

@client.event
async def on_message_edit(ctx, arg):
   if ctx.author==client.user:
       raise Exception()

   global edit_message_id
   global edit_message_author
   global edit_message_content
   global edit_message_channel

   edit_message_id.append(ctx.id)
   edit_message_author.append(ctx.author.name)
   edit_message_content.append(ctx.content)
   edit_message_channel.append(ctx.channel.id)

@client.command()
async def edsnipe(message, arg=1):
   try:
       global edit_message_channel
       arg=int(arg)
       arg=-arg
       if edit_message_content==[]:
           await message.channel.send("There's nothing to snipe!")
       if edit_message_channel[arg]!=message.channel:
           count=arg
           list1=[]
           for h in edit_message_channel:
               list1.append(f"{h}")
           index=[i for i, n in enumerate(list1) if n == f'{message.channel.id}'][count]
           msg = await message.fetch_message(int(edit_message_id[index]))
           embed = discord.Embed(description=f"**Message Before:**\n{edit_message_content[index]}\n\n**Message Now:**\n{msg.content}", color=0x3498db)
           embed.set_footer(text=f"Asked by {message.author.name}#{message.author.discriminator}", icon_url=message.author.avatar_url)
           embed.set_author(name=f"@{edit_message_author[index]}")
           await message.send(embed=embed)
           return

       if edit_message_channel[arg] == message.channel:
           count=arg
           list1=[]
           for h in edit_message_channel:
               list1.append(f"{h}")
           index=[i for i, n in enumerate(list1) if n == f'{message.channel.id}'][count]
           msg = await message.fetch_message(int(edit_message_id[index]))
           embed = discord.Embed(description=f"**Message Before:**\n{edit_message_content[index]}\n\n**Message Now:**\n{msg.content}", color=0x3498db)
           embed.set_footer(text=f"Asked by {message.author.name}#{message.author.discriminator}", icon_url=message.author.avatar_url)
           embed.set_author(name=f"@{edit_message_author[index]}")
           await message.send(embed=embed)
           return
   except IndexError:
       await message.channel.send("There's nothing to snipe!")

@client.command()
async def yt(ctx, *, search):
   num = random.randint(0, 20)
   num = int(num)
   query_string = urllib.parse.urlencode({'search_query': search})
   htm_content = urllib.request.urlopen(
       'http://www.youtube.com/results?' + query_string)
   search_results = re.findall(r'/watch\?v=(.{11})',
                               htm_content.read().decode())
   await ctx.send('http://www.youtube.com/watch?v=' + search_results[num])

@client.command()
async def fortune(ctx):
   member=random.choice(ctx.guild.members)
   numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
   num_choice = random.choice(numbers)
   squares = []
   str1 = ""

   for i in range(num_choice // 10):
       squares.append("⬜")

   while True:
       if len(squares) == 10:
           break
       else:
           squares.append("🔳")

   for i in squares:
       str1 += (f"{i} ")

   embed = discord.Embed(title=f"{member}", description=f"**Accuracy: {num_choice}%**\n{str1}", color=0x3498db)
   await ctx.send(embed=embed)
   return


@client.command()
async def kakashi(ctx, user: discord.Member=None):
   if user==None:
       user=ctx.author

   kakashi=Image.open("1000 Years of Death.jpg")

   asset=user.avatar_url_as(size=128)
   data=BytesIO(await asset.read())
   pfp=Image.open(data)
   pfp=pfp.resize((80, 80))
   kakashi.paste(pfp, (60, 62))
   kakashi.save("profile.jpg")

   await ctx.send(file=discord.File("profile.jpg"))

@client.command()
@commands.cooldown(1, 7, commands.BucketType.user)
async def profile(ctx):
   await open_account(ctx.author)
   with open("Economy.json", "r") as f:
       users=json.load(f)
   wallet_amt=users[str(ctx.author.id)]["wallet"]
   bank_amt=users[str(ctx.author.id)]["bank"]
   stocks_amt=users[str(ctx.author.id)]["stocks"]
   embed=discord.Embed(title=f"{ctx.author.name}'s Inventory:", color=0x3498db)
   embed.add_field(name="Wallet: ", value=f"{wallet_amt}")
   embed.add_field(name="Bank: ", value=f"{bank_amt}")
   embed.add_field(name="Stocks: ", value=f"{stocks_amt}")
   embed.set_thumbnail(url=f"{ctx.author.avatar_url}")
   await ctx.send(embed=embed)

@profile.error
async def profile_error(ctx, error):
   if isinstance(error, commands.CommandOnCooldown):
       msg = 'This command is on cooldown, by default it is 7 seconds. Please try again in {:.2f}s'.format(error.retry_after)
       await ctx.send(msg)
   else:
       raise error

async def open_account(user):
   with open("Economy.json", "r") as f:
       users=json.load(f)
   if str(user.id) in users:
       return False
   else:
       users[str(user.id)]={"wallet": 100, "bank": 100, "stocks": 100}
   with open("Economy.json", "w") as f:
       json.dump(users, f)
   return True

@client.command()
@commands.cooldown(1, 7, commands.BucketType.user)
async def beg(ctx):
   with open("Economy.json", "r") as f:
       users=json.load(f)
   num=random.randint(1, 100)
   choices=[num, "No one wants to donate any money...", "Uh-oh, it looks like you got stolen from instead!"]
   choice=random.choice(choices)
   if choice=="No one wants to donate any money...":
       await ctx.send(f"{choice}")
   elif choice=="Uh-oh, it looks like you got stolen from instead!":
       users[str(ctx.author.id)]["wallet"]-=num
       await ctx.send(f"Uh-oh, it looks like you got stolen from instead! You lost {num} coins!")
   else:
       users[str(ctx.author.id)]["wallet"]+=num
       await ctx.send(f"Someone has donated {num} coins to {ctx.author.name}!!!")
   with open("Economy.json", "w") as f:
       json.dump(users, f)

@beg.error
async def beg_error(ctx, error):
   if isinstance(error, commands.CommandOnCooldown):
       msg = 'This command is on cooldown, by default it is 7 seconds. Please try again in {:.2f}s'.format(error.retry_after)
       await ctx.send(msg)
   else:
       raise error

@client.command()
@commands.cooldown(1, 7, commands.BucketType.user)
async def negotiate(ctx):
   with open("Economy.json", "r") as f:
       users=json.load(f)
   num=random.randint(1, 1000)
   choices=[num, "No company wants to negotiate...", "Uh-oh, it looks like you got scammed!"]
   choice=random.choice(choices)
   if choice=="No company wants to negotiate...":
       await ctx.send("No company wants to negotiate...")
   elif choice=="Uh-oh, it looks like you got scammed!":
       users[str(ctx.author.id)]["bank"]-=num
       await ctx.send(f"Uh-oh, it looks like you got scammed! You lost {num} dollars.")
   else:
       users[str(ctx.author.id)]["bank"]+=num
       await ctx.send(f"A company wants to negotiate! You gained {num} dollars!")
   with open("Economy.json", "w") as f:
       json.dump(users, f)

@negotiate.error
async def negotiate_error(ctx, error):
   if isinstance(error, commands.CommandOnCooldown):
       msg = 'This command is on cooldown, by default it is 7 seconds. Please try again in {:.2f}s'.format(error.retry_after)
       await ctx.send(msg)
   else:
       raise error

@client.command()
@commands.cooldown(1, 7, commands.BucketType.user)
async def stocks(ctx):
   with open("Economy.json", "r") as f:
       users=json.load(f)
   logos=["https://cdn.discordapp.com/attachments/780474442446405644/780959372028936222/unknown.png",
          "https://cdn.discordapp.com/attachments/780474442446405644/780959993938706442/unknown.png",
          "https://cdn.discordapp.com/attachments/780474442446405644/780960183668965396/unknown.png",
          "https://cdn.discordapp.com/attachments/780474442446405644/780960377227837470/unknown.png",
          "https://cdn.discordapp.com/attachments/780474442446405644/780960594316230716/unknown.png"]
   stocks_amt=users[str(ctx.author.id)]["stocks"]
   if stocks_amt==0:
       stocks_amt+=1
   elif stocks_amt<0:
       num=random.randint(stocks_amt, -stocks_amt)
   elif stocks_amt>0:
       num = random.randint(-stocks_amt, stocks_amt)
   users[str(ctx.author.id)]["stocks"] += num
   with open("Economy.json", "w") as f:
       json.dump(users, f)
   if num<0:
       emoji=":arrow_down: "
   elif num>0:
       emoji=":arrow_up: "
   else:
       emoji=":arrow_right: "
   stocks_amt=users[str(ctx.author.id)]["stocks"]
   embed=discord.Embed(title=f"{ctx.author.name}'s Stocks: ", description=f"**{stocks_amt} {emoji}**", color=0x3498db)
   embed.set_thumbnail(url=f"{random.choice(logos)}")

   await ctx.send(embed=embed)

@stocks.error
async def stocks_error(ctx, error):
   if isinstance(error, commands.CommandOnCooldown):
       msg = 'This command is on cooldown, by default it is 7 seconds. Please try again in {:.2f}s'.format(error.retry_after)
       await ctx.send(msg)
   else:
       raise error

@client.command()
@commands.cooldown(1, 7, commands.BucketType.user)
async def steal(ctx, user: discord.Member=None):
   with open("Economy.json", "r") as f:
       users=json.load(f)
   num=random.randint(1, 100)
   possibilities=["You stole from someone!", "You got caught..."]
   if user==None:
       await ctx.send("Please give a user you want to steal from.")
   else:
       choice=random.choice(possibilities)
       if choice=="You stole from someone!":
           if users[str(user.id)]["wallet"] < 0:
               await ctx.send("This person doesn't have any money.")
               raise Exception()
           else:
               users[str(ctx.author.id)]["wallet"] += num
               users[str(user.id)]["wallet"] -= num
               await ctx.send(f"{ctx.author.name} successfully stole {num} dollars from {user}!")
       elif choice=="You got caught...":
           if users[str(ctx.author.id)]["wallet"] < 0:
               users[str(ctx.author.id)]["wallet"] -= num
               await ctx.send(f"{user.name} has put {ctx.author.name} into debt.")
               raise Exception()
           else:
               users[str(user.id)]["wallet"] += num
               users[str(ctx.author.id)]["wallet"] -= num
               await ctx.send(f"Uh-oh, you got caught...{user} stole {num} dollars from {ctx.author.name}.")
   with open("Economy.json", "w") as f:
       json.dump(users, f)

@steal.error
async def steal_error(ctx, error):
   if isinstance(error, commands.CommandOnCooldown):
       msg = 'This command is on cooldown, by default it is 7 seconds. Please try again in {:.2f}s'.format(error.retry_after)
       await ctx.send(msg)
   else:
       raise error

@client.command()
@commands.cooldown(1, 7, commands.BucketType.user)
async def businesses(ctx):
   with open("Economy.json", "r") as f:
       users=json.load(f)
   embed=discord.Embed(title=f"{ctx.author.name}'s Businesses: ", color=0x3498db)
   embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/780474442446405644/781013261793493022/unknown.png")
   tech=random.randint(-100, 100)
   oil=random.randint(-100, 100)
   insurance=random.randint(-100, 100)
   car=random.randint(-100, 100)
   if tech>0:
       emoji=":arrow_up: "
   elif tech<0:
       emoji=":arrow_down: "
   else:
       emoji = ":arrow_right: "
   embed.add_field(name="Tech Company: ", value=f"{tech} {emoji}")
   if oil>0:
       emoji=":arrow_up: "
   elif oil<0:
       emoji=":arrow_down: "
   else:
       emoji = ":arrow_right: "
   embed.add_field(name="Oil Company: ", value=f"{oil} {emoji}")
   if insurance>0:
       emoji=":arrow_up: "
   elif insurance<0:
       emoji=":arrow_down: "
   else:
       emoji = ":arrow_right: "
   embed.add_field(name="Insurance Company: ", value=f"{insurance} {emoji}")
   if car>0:
       emoji=":arrow_up: "
   elif car<0:
       emoji=":arrow_down: "
   else:
       emoji = ":arrow_right: "
   embed.add_field(name="Automobile Company: ", value=f"{car} {emoji}")
   await ctx.send(embed=embed)
   users[str(ctx.author.id)]["bank"] += tech
   users[str(ctx.author.id)]["bank"] += oil
   users[str(ctx.author.id)]["bank"] += insurance
   users[str(ctx.author.id)]["bank"] += car
   with open("Economy.json", "w") as f:
       json.dump(users, f)

@businesses.error
async def businesses_error(ctx, error):
   if isinstance(error, commands.CommandOnCooldown):
       msg = 'This command is on cooldown, by default it is 7 seconds. Please try again in {:.2f}s'.format(error.retry_after)
       await ctx.send(msg)
   else:
       raise error

@client.command()
@commands.cooldown(1, 7, commands.BucketType.user)
async def withdraw(ctx, arg="all"):
   with open("Economy.json", "r") as f:
       users=json.load(f)
   bank_amt=users[str(ctx.author.id)]["bank"]
   if arg=="all":
       users[str(ctx.author.id)]["bank"]-=bank_amt
       users[str(ctx.author.id)]["wallet"]+=bank_amt
       await ctx.send(f"{bank_amt} dollars have been transferred to your wallet.")
   else:
       if users[str(ctx.author.id)]["bank"]<0:
           await ctx.send("You cannot withdraw any money from your bank.")
           raise Exception()
       users[str(ctx.author.id)]["bank"]-=int(arg)
       users[str(ctx.author.id)]["wallet"]+=int(arg)
       await ctx.send(f"{arg} dollars have been transferred to your wallet.")
   with open("Economy.json", "w") as f:
       json.dump(users, f)

@withdraw.error
async def withdraw_error(ctx, error):
   if isinstance(error, commands.CommandOnCooldown):
       msg = 'This command is on cooldown, by default it is 7 seconds. Please try again in {:.2f}s'.format(error.retry_after)
       await ctx.send(msg)
   else:
       raise error

@client.command()
@commands.cooldown(1, 7, commands.BucketType.user)
async def invest(ctx, arg="all"):
   with open("Economy.json", "r") as f:
       users=json.load(f)
   wallet_amt=users[str(ctx.author.id)]["wallet"]
   if users[str(ctx.author.id)]["wallet"]<0:
       await ctx.send("You do not have enough money to invest in stocks.")
       raise Exception()
   if arg=="all":
       users[str(ctx.author.id)]["wallet"]-=wallet_amt
       users[str(ctx.author.id)]["stocks"]+=wallet_amt
       await ctx.send(f"You have successfully invested {wallet_amt} dollars.")
   else:
       arg=int(arg)
       users[str(ctx.author.id)]["stocks"]+=arg
       users[str(ctx.author.id)]["wallet"]-=arg
       await ctx.send(f"You have successfully invested {arg} dollars in stocks.")
   with open("Economy.json", "w") as f:
       json.dump(users, f)

@invest.error
async def invest_error(ctx, error):
   if isinstance(error, commands.CommandOnCooldown):
       msg = 'This command is on cooldown, by default it is 7 seconds. Please try again in {:.2f}s'.format(error.retry_after)
       await ctx.send(msg)
   else:
       raise error

@client.command()
@commands.cooldown(1, 7, commands.BucketType.user)
async def deposit(ctx, arg="all"):
   with open("Economy.json", "r") as f:
       users=json.load(f)
   wallet_amt=users[str(ctx.author.id)]["wallet"]
   if arg=="all":
       users[str(ctx.author.id)]["wallet"]-=wallet_amt
       users[str(ctx.author.id)]["bank"]+=wallet_amt
       await ctx.send(f"{wallet_amt} dollars have been transferred to your bank.")
   else:
       if users[str(ctx.author.id)]["wallet"]<0:
           await ctx.send("You cannot deposit any money to your bank.")
           raise Exception()
       users[str(ctx.author.id)]["bank"]+=int(arg)
       users[str(ctx.author.id)]["wallet"]-=int(arg)
       await ctx.send(f"{arg} dollars have been transferred to your bank.")
   with open("Economy.json", "w") as f:
       json.dump(users, f)

@deposit.error
async def deposit_error(ctx, error):
   if isinstance(error, commands.CommandOnCooldown):
       msg = 'This command is on cooldown, by default it is 7 seconds. Please try again in {:.2f}s'.format(error.retry_after)
       await ctx.send(msg)
   else:
       raise error

@client.command()
@commands.cooldown(1, 7, commands.BucketType.user)
async def withdrawstocks(ctx, arg="all"):
   with open("Economy.json", "r") as f:
       users=json.load(f)
   stocks_amt=users[str(ctx.author.id)]["stocks"]
   if users[str(ctx.author.id)]["bank"]<0:
       await ctx.send("You cannot withdraw any money from your bank.")
       raise Exception()
   if arg=="all":
       users[str(ctx.author.id)]["stocks"]-=stocks_amt
       users[str(ctx.author.id)]["bank"]+=stocks_amt
       await ctx.send(f"{stocks_amt} dollars have been transferred to your bank.")
   else:
       arg=int(arg)
       users[str(ctx.author.id)]["stocks"]-=arg
       users[str(ctx.author.id)]["bank"]+=arg
       await ctx.send(f"{arg} dollars have been transferred to your bank.")
   with open("Economy.json", "w") as f:
       json.dump(users, f)

@withdrawstocks.error
async def withdrawstocks_error(ctx, error):
   if isinstance(error, commands.CommandOnCooldown):
       msg = 'This command is on cooldown, by default it is 7 seconds. Please try again in {:.2f}s'.format(error.retry_after)
       await ctx.send(msg)
   else:
       raise error

@client.command()
async def give(ctx, user: discord.Member=None, arg=None):
   with open("Economy.json", "r") as f:
       users=json.load(f)
   if user==None and arg==None:
       await ctx.send("You need to provide the amount of money you want to give and you have to provide what user you want to give that money to.")
       raise Exception()
   if user==None:
       await ctx.send("You need to provide the amount of money you want to give and you have to provide what user you want to give that money to.")
       raise Exception()
   if arg==None:
       await ctx.send("You need to provide the amount of money you want to give and you have to provide what user you want to give that money to.")
       raise Exception()
   arg=int(arg)
   users[str(user.id)]["wallet"]+=arg
   users[str(ctx.author.id)]["wallet"]-=arg
   await ctx.send(f"{arg} dollars have been transferred to {user}.")
   with open("Economy.json", "w") as f:
       json.dump(users, f)

client.run(token)







