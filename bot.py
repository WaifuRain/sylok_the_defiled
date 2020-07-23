import discord
import os
from discord.ext import commands
from IDs.id_list import id_list
# from id_list import id_list
from Deprecated_Files.get_image import get_image
# from get_image import get_image
from random import choice
from MAL_Parser import Character
# from get_attributes import Character
import random
from stats import WeightedChoice


bot = commands.Bot(command_prefix='.', case_insensitive=True, owner_id=465283213217103882)
token = os.environ.get('SYLOK_KEY')
bot.version = '0.1.2'  # major changes, minor changes, small changes
waifu_database_root = 'E:\\Waifu Database'


def is_registered(author_id):
    with open('C:\\Users\\bridg\\PycharmProjects\\sylok_the_defiled\\IDs\\registered_users.txt', 'r') as f:
        if str(author_id) in f.read():
            return True
        else:
            return False


def create_waifu_id_list():
    return next(os.walk(waifu_database_root))[1]


def get_random_waifu_id():
    return random.choice(create_waifu_id_list())


@bot.event  # error handler
async def on_command_error(ctx, error):
    ignored = (commands.CommandNotFound, commands.UserInputError)
    if isinstance(error, ignored):
        return
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.send(f'You are on cooldown. Seconds remaining: {round(error.retry_after, 2)}s')
    elif isinstance(error, commands.CheckFailure):
        await ctx.send('You lack permission to use this command.')
    raise error


@bot.event
async def on_message(msg):
    weighted_choice = WeightedChoice(((False, 88), (True, 2)))
    if msg.author == bot.user:
        return
    if weighted_choice.next():
        await msg.channel.send('This would have been a waifu if it was implemented lmao')
    else:
        await msg.channel.send('Unlucky. No waifu this time.')


@commands.cooldown(1, 4, commands.BucketType.user)
@bot.command()
async def roll(ctx, arg=None):
    if arg is not None:
        await ctx.send('Invalid usage of .groll')
        return
    if not is_registered(ctx.author.id):
        await ctx.send(f'You are not registered! Register using {bot.command_prefix}register .')
        return
    waifu = Character(choice(id_list()))
    embed = discord.Embed(title='Waifu Gacha', description=f'Roll Result:\n**{waifu.name}** [α]')
    try:
        embed.set_image(url=f'{choice(waifu.images)}')
    except IndexError:
        print(f'There was an Exception! id: {waifu.character_id}')
        embed.set_image(url=f'{get_image(waifu.character_id)}')
    embed.add_field(name='Character Stats', value='**Agility:** n/a\n**Defense:** n/a\n**Endurance:** n/a\n**Strength:** n/a\n**Total CSI:** n/a')
    embed.add_field(name='Roll Type', value='Standard', inline=False)
    embed.set_footer(text=f"{str(ctx.author)[:str(ctx.author).find('#')]}'s Gacha Roll")
    await ctx.send(content=None, embed=embed)


@bot.command()
@commands.is_owner()
async def test(ctx):
    print(ctx.author)  # Waifu Hearts#7777
    print(ctx.message)  # message object
    print(ctx.message.author.id)  # 465283213217103882
    print(ctx)  # context object


@bot.command()
async def register(ctx):
    if is_registered(ctx.message.author.id):
        await ctx.send('You are already registered!')
    else:
        with open('ID', 'a') as f:
            f.write(f'{ctx.message.author.id}\n')


@bot.command()
@commands.is_owner()
async def disconnect(ctx):
    await bot.logout()

bot.run(token)
