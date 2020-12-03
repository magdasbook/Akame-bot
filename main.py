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
  respondes = ['https://media.tenor.com/images/593140d25dcd8e2f6afb7b5a5981c919/tenor.gif', 'i hyc o podłoge https://thumbs.gfycat.com/GiddyLawfulBergerpicard-size_restricted.gif', 'https://i.gifer.com/M2qo.gif' , 'https://thumbs.gfycat.com/AnimatedTepidAfricanfisheagle-small.gif', 'https://i.imgur.com/G9EVXbZ.gif']
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
  


@bot.command()
async def glupigadzet(ctx):
  await ctx.send(' ja kiedy głupi gadżet  https://i.pinimg.com/originals/2c/94/5a/2c945adbbc31699861f411f86ce8058f.gif')

@bot.command(name='f')
async def f(ctx, *, question):
  respondes = ['to jest Mine https://i.pinimg.com/originals/3a/53/da/3a53da6de9d7d4dd5bbd7b7c80cb917a.gif', 'to jest Tatsumi https://i.pinimg.com/originals/4a/d2/b3/4ad2b35ff4b0d5095a883fd028a08171.gif', 'To jest Chelsea https://i.pinimg.com/originals/fd/a4/dc/fda4dc5acf391298eed08e978eb07e21.gif', 'To jest Leone https://media1.tenor.com/images/32a6cba654620ebf91d685cd1d33110a/tenor.gif?itemid=16396218', 'To jest Sheele https://i.pinimg.com/originals/cd/b1/6c/cdb16ceecac03648689cf32561196508.gif', 'to jest Lubbock https://media1.tenor.com/images/29284ee2b2c916d636e499b4c102bfd6/tenor.gif?itemid=5001375', 'To jest Najenda - szefowa https://64.media.tumblr.com/a989692482ad43142f8ad26ec4ce7851/tumblr_nyjheww7qO1ulh7tvo2_500.gifv', 'To jest Bulat https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT5p8WsYib9wtVs988ulng1mFbBKP1etF3Iow&usqp=CAU']
  await ctx.send(f'Question: {question}\nAnswer: {random.choice(respondes)}')

@bot.command(name='pb')
async def pb(ctx, *, question):
  respondes = ['nie ma sprawy  https://media.tenor.com/images/854a8d51d6892afde1cd0631f0afd981/tenor.gif', 'prosze bardzo https://media.tenor.com/images/854a8d51d6892afde1cd0631f0afd981/tenor.gif', 'Co mam powiedzieć prócz DROBNOSTKA https://i.pinimg.com/originals/c2/ac/9d/c2ac9d3973ddf50ae22332a9f89aae8a.gif', 'masz za co https://giffiles.alphacoders.com/148/148507.gif']
  await ctx.send(f'Question: {question}\nAnswer: {random.choice(respondes)}')

@bot.command(name='tn')
async def pb(ctx, *, question):
  respondes = ['tak', 'nie', 'można jak najbardziej', 'nigdy w życiu', 'ultra rel', 'rel', 'nie rel']
  await ctx.send(f'Question: {question}\nAnswer: {random.choice(respondes)}')

@bot.command(name='xd')
async def xd(ctx, *, question):
  respondes = ['xd', 'XD', 'Xd', 'xD', 'xddddddd', 'XDDDDDDDD', 'xddd https://i.imgflip.com/1amn5g.gif', 'XDDDDDDD https://forum.psnprofiles.com/applications/core/interface/imageproxy/imageproxy.php?img=https://66.media.tumblr.com/cf1ddeda9fed34676a62cab8acd7c88e/tumblr_nyhn4tq2EH1twyezqo1_r1_500.gif&key=5da2d02d5c0281a447ff6200143514a2c7f3e61aef9c2b0253841d3548728e85' ]
  await ctx.send(f'Question: {question}\nAnswer: {random.choice(respondes)}')

@bot.command(name='wm')
async def wm(ctx, *, question):
  respondes = ['ale jak to mamo?', 'lepiej sie wstydź siebie', 'hahahahahahah beka z cb', 'mamoooo nie wstydź sie mnie', 'ale mamooooooo']
  await ctx.send(f'Question: {question}\nAnswer: {random.choice(respondes)}')

@bot.command(name='wdm')
async def wdm(ctx, *, question):
  respondes = ['obecuje poprawe', 'poprawe sie mamoo, kc', 'spadaj stara', 'zostaw mnie', 'bede lepszym dzieckiem']
  await ctx.send(f'Question: {question}\nAnswer: {random.choice(respondes)}')

@bot.command(name='ko')
async def ko(ctx, *, question):
  respondes = ['nie wyzywaj mnie', 'chyba ty', 'dobra sory już nie bede', 'spadaj', 'nie jesteś moją matką', 'moge robić co chce']
  await ctx.send(f'Question: {question}\nAnswer: {random.choice(respondes)}')

token = os.environ.get('TOKEN')
print(token)
bot.run(token)