#  modules that the script uses
print('make sure you got this python version https://www.python.org/downloads/release/python-3913/')
import os 
os.system("pip install bloxflipsearch")
import bloxflipsearch
from tabnanny import check
import discord
from discord.ext import commands
import time
import math
from discord_webhook import DiscordWebhook, DiscordEmbed
from bloxflippredictor import *



# Setup/Configs
TOKEN=""
bombs=4    #  This is for maths it will show the % when one bomb is used you can make the % with this higher or lower

#  Discord bot definition
intents = discord.Intents.all()
client = commands.Bot(command_prefix='.', help_command=None, intents=intents)
client.remove_command("help")




# Stuff used for predicter
ids = []


#  Event when the bot is online
@client.event
async def on_ready():
  print('Bot is online')




# Check if the round id is used
def checkid(roundid):
  if roundid in ids:
    return False
  ids.append(roundid)    #  This is not forever it will delete after the file is stopped
  
 


  

#  Tower predictor
@client.command(name="towers")
async def rege(ctx, e):
    a = len(e)
    if a == 36:
      await ctx.send(f'Getting round id {e}')
      if checkid(e) == False:
        return 
      await anu(ctx, e)
    else:
      time.sleep(2)
      await ctx.send('invalid round id')
async def anu(ctx, e):
  o = bloxflippredictor.towers
  an = o.towerspredictor()
  embed=discord.Embed(title="xolos prediction", description=f"predicting: {e}")
  embed.add_field(name="towers", value=an, inline=False)
  await ctx.send(ctx.author.mention, embed=embed)



  
#  Mines predictor
@client.command(name="mines")
async def reg(ctx, e):
    a = len(e)
    if a == 36:    #  Checks if the message is 36 characters long
      await ctx.send(f'Getting round id {e}')
      if checkid(e) == False:
        return
      await mines(ctx, e)    #  Starts the mine predictor
    else:
      time.sleep(2)
      await ctx.send('invalid round id')



# Mines predictor code
async def mines(ctx, e):
    def check(msg):
      return msg.author == ctx.author and msg.channel == ctx.channel
    tiles = list(range(1,26))
    time.sleep(2)
    await ctx.send(f'{ctx.author.mention} How many tiles do you want open? ')
    msg = await client.wait_for("message", check=check)
    msgo = int(msg.content)
    totalsquaresleft = 25
    formel = ((totalsquaresleft - bombs) / (totalsquaresleft))
    totalsquareslefts = 24
    formel2 = ((totalsquareslefts - bombs) / (totalsquareslefts))
    output=minespredictor(msgo, bombs)
    end = formel2 * 100
    multiplier = calculate_multiplier(msgo, bombs)
    embed=discord.Embed(title="xolos prediction", description=f" predicting: {e}")
    embed.add_field(name="mines", value=output, inline=False)
    embed.add_field(name="chances", value=f"Your win chance is {int(end)}%", inline=False)
    embed.add_field(name="winnings", value="Multiplier: {0:.2f}".format(multiplier), inline=False)
    await ctx.send(ctx.author.mention, embed=embed)

#  Maths for mines
def nCr(n,r):
  f = math.factorial
  return f(n) // f(r) // f(n-r)

def calculate_multiplier(bombs, msgo):
  house_edge = 0.01
  return (0.96 - house_edge) * nCr(25, msgo) / nCr(25 - bombs, msgo)




#  Crash could get banned from the api



@client.command(name='crash')
async def crash(ctx):
                chan = False
                varName = crashpredictor()
                if type(varName) == dict:
                  pass
                else:
                 await ctx.send(varName)
                 return
                chance = varName['crashchance']
                prediction = varName['crashprediction']
                if float(chance) > 2:
                    color = 0x81fe8f
                else:
                    color = 0xfe8181
                if float(chance) >= 80:
                 
                 desc = f"""
        **Crashpoint:**
        *{prediction:.2f}x*
        **High chance:**
        ```{chance:.2f}%```"""
                else:
                 desc = f"""
        **Crashpoint:**
        *{prediction:.2f}x*
        **normal chance:**
        ```{chance:.2f}%```"""
                if float(chance) <= 10:
                 desc = f"""
        **Crashpoint:**
        *{prediction:.2f}x*
        **Low chance:**
        ```{chance:.2f}%```"""

                  

                em=discord.Embed(description=desc,color=color)
                await ctx.reply(embed=em)
   

   
  
  
# Roulette predictor
@client.command(name="roulette")
async def roulette(ctx):
  output = roulettepredictor()
  embed=discord.Embed(title="xolos prediction", description=f" predicting: roulette")
  embed.add_field(name="roulette", value=output, inline=False)
  await ctx.reply(embed=embed)

  
#  Runs the token
try:
  client.run(TOKEN)
except:
    os.system('Token invalid or rate limit')