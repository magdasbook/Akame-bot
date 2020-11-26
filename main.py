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
@bot.command(name='jw')
async def jw(ctx, *, question):
  respondes = [ 'https://i.pinimg.com/736x/52/cf/cd/52cfcd6e34946308864c34e9aa7286cd.jpg', 'https://media.tenor.com/images/fc414e7575823b656edd53d28a933020/tenor.png', 'https://cdn.myanimelist.net/s/common/uploaded_files/1448464899-18993ec2b1c4adbe9dd1c278f4d3d22f.png', 'https://images4.alphacoders.com/950/950614.png', 'https://i.redd.it/prg8bawekz911.jpg' ]
  await ctx.send(f'Question: {question}\nAnswer: {random.choice(respondes)}')

@bot.command(name='k')
async def k(ctx, *, question):
  respondes = ['https://media.tenor.com/images/593140d25dcd8e2f6afb7b5a5981c919/tenor.gif', 'https://steamuserimages-a.akamaihd.net/ugc/911283084454613080/2F314F856BFAB573A80D32E95729ED67297B32CC/', 'https://thumbs.gfycat.com/AnimatedTepidAfricanfisheagle-small.gif', 'https://i.imgur.com/G9EVXbZ.gif']
  await ctx.send(f'Question: {question}\nAnswer: {random.choice(respondes)}')

@bot.command(name='h')
async def h(ctx, *, question):
  respondes = ['https://i.pinimg.com/originals/3f/71/a1/3f71a113af26224cbfb30bdd9894042a.gif', 'spadaj https://i.pinimg.com/originals/55/e3/f9/55e3f9fb450842d64b96730f703525d6.gif']
  await ctx.send(f'Question: {question}\nAnswer: {random.choice(respondes)}')

@bot.command(name='kc')
async def kc(ctx, *, question):
  respondes = ['Kocham cię', 'Nie kocham cię', 'hmmmmmmm musze się zastanowić', 'bardziej kocham PISULE', 'Kocham cię najbardziej na świecie']
  await ctx.send(f'Question: {question}\nAnswer: {random.choice(respondes)}')

@bot.command()
async def uwu(ctx):
  await ctx.send('https://media1.tenor.com/images/f53c0741b7cb2ea45e9bfa41c0957900/tenor.gif?itemid=14953637')


@bot.command(name='d')
async def d(ctx, *, question):
  respondes = ['Dziękuję!', 'Spadaj, ja nie dziękuję ', 'Skoro muszę... Dzięki!', 'Dziękuje bardzo!!!', 'Nigdy w życiu']
  await ctx.send(f'Question: {question}\nAnswer: {random.choice(respondes)}')

@bot.command(name='kcs')
async def kcs(ctx, *, question):
  respondes = ['Magdziunia!', 'Moim stwórcą jest Magdalena Surma - znana aktualnie jako serowy cheetos', 'Wspaniała osoba- Madzia', 'Moją mame jest Magdziunia']
  await ctx.send(f'Question: {question}\nAnswer: {random.choice(respondes)}')

@bot.command(name='sr')
async def sr(ctx, *, question):
  respondes = ['przepraszam', 'sory', 'ja nie przepraszam', 'Nie mam za co przepraszać!', 'dobrze mamo, przepraszam', ' strasznie przepraszam...  https://i.pinimg.com/originals/3f/71/a1/3f71a113af26224cbfb30bdd9894042a.gif']
  await ctx.send(f'Question: {question}\nAnswer: {random.choice(respondes)}')

@bot.command()
async def komendy(ctx):
  await ctx.send(' prefiks "a." po prefiksie piszesz w zależności od komendy, którą chcesz wywołać. Komendy: "hey"- bot się wita, "pa" - bot się żegna, "liczba" - liczba wysłanych wiadomości, """pos" + po spacji pytanie o samopoczucie"- pyta o samopoczucie bota, "ban + wzmianka członka" - wiadoma funkcja, "unban + wzmianka" - wiadome, "clear"- usuwa ostatnie 5 wiadomości, "jw + po spacji pytanie o wygląd akame", "k + pytanie o zabijanie po spacji" -  wyświetla giphy z zabijaniem w odp, "h + pytanie o przytualenie lub hug po prostu po spacji" - przytula lub nie, "kc + pytanie o to czy cie kocha", "uwu"- wysyła gipha uwu, "d + po spacji podziękuj lub coś z dziękowaniem", "kcs + pytanie kto cię stworzył po spacji" - pytanie o stwórce, "sr + przeproś" - przeprasza')
  

token = os.environ.get('TOKEN')
print(token)
bot.run(token)