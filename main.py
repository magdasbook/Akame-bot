import os
import discord
from discord.ext import commands
import random # dodatkowy import, żeby nie pisać discord.ext.commands

# commands.Bot - Client z dodatkowymi funkcjami
bot = commands.Bot(intents=discord.Intents.all(), # zmienna bot i klasa commands.Bot zamiast discord.Client
                   command_prefix=['a.']) # https://discordpy.readthedocs.io/en/latest/ext/commands/api.html#discord.ext.commands.Bot.command_prefix

@bot.event
async def on_ready():
    print('Hello world!')

@bot.event # 3 rodzaje - event(, command, listen)
async def on_member_join(member):
    await member.send('Witaj na serwerze **{}**!'.format(member.display_name))

messages = 0
@bot.listen('on_message') # https://discordpy.readthedocs.io/en/latest/ext/commands/api.html#discord.ext.commands.Bot.listen
async def message_send(message):
    global messages # używa globalnej zmiennej o tej nazwie
    messages += 1 # zwiększa ją o 1
    
@bot.command(name='liczba') # https://discordpy.readthedocs.io/en/latest/ext/commands/api.html#discord.ext.commands.Command
async def mess_num(ctx): # pierwszym argumentem jest zawsze commands.Context, tu zmienna ctx
    #channel = bot.get_guild(766777229304397854).get_channel(768806625242120193) # wybiera kanał o konkre
    await ctx.send('Liczba wiadomości to: {}'.format(messages)) # https://discordpy.readthedocs.io/en/latest/ext/commands/api.html#discord.ext.commands.Context
@bot.command()
async def hey(ctx):
  await ctx.send('Hej!')


@bot.command()
async def pa(ctx):
  await ctx.send('do zobaczenia!')

@bot.command(name='pos')
async def pos(ctx, *, question):
  respondes = ['czuje się dobrze', 'czuje się wyśmienicie', 'zabiłabym kogoś', 'źle', 'koronawirus', 'może być', 'źle, bo zgubiłam teigu']
  await ctx.send(f'Question: {question}\nAnswer: {random.choice(respondes)}')

@bot.command()
async def clear(ctx, amount=5):
  await ctx.channel.purge(limit=amount)
  
@bot.command()
async def ban(ctx, member : discord.Member):
  await member.ban()

@bot.command()
async def unban(ctx, *, member : discord.User):
  banned_users = await ctx.guild.bans()


  for ban_entry in banned_users:
    user = ban_entry.user
    if user == member:
      await ctx.guild.unban(user)
      await ctx.send(f'Unbanned {user.mention}')
      return

token = os.environ.get('TOKEN')
print(token)
bot.run(token)