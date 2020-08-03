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


def get_waifu_image_url(waifu_id):
    link_directory = f"E:\\Waifu Database\\{waifu_id}\\images\\links"
    with open(f'{link_directory}\\{random.choice(os.listdir(link_directory))}', 'r') as link_txt:
        return link_txt.read()


def get_waifu_initials(waifu_id):
    with open(f'E:\\Waifu Database\\{waifu_id}\\info\\initials.txt') as initials:
        return initials.read()


def create_drop_embed(waifu_id, img_url):
    # random_image = random.choice(os.listdir(f"E:\\Waifu Database\\{waifu_id}\\images\\links"))
    embed = discord.Embed(title='**Character**', description=f'A waifu/husbando has appeared!\nTry guessing their name with `.claim <name>` to claim them!\n\nHints:\nThis characters initials are \'{get_waifu_initials(waifu_id)}\'\n'
                                                             f'Use `.lookup <name>` if you can\'t remember the full name.\n\n(If the image is missing, click [here]({img_url}).)')
    embed.set_image(url=img_url)
    return embed


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
    weighted_choice = WeightedChoice(((False, 97), (True, 3)))
    # weighted_choice = WeightedChoice(((False, 20), (True, 80)))
    random_waifu_id = get_random_waifu_id()
    if msg.author == bot.user:
        return
    if weighted_choice.next():
        await msg.channel.send(content=None, embed=create_drop_embed(random_waifu_id, get_waifu_image_url(random_waifu_id)))
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
