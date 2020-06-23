import discord
import os
from discord.ext import commands
import get_image
from id_list import id_list
from get_image import get_image
from random import choice
from get_attributes import Character


bot = commands.Bot(command_prefix='.')
# client = discord.Client()

token = os.environ.get('SYLOK_KEY')


def is_registered(author_id):
    with open('registered_users.txt', 'r') as f:
        if str(author_id) in f.read():
            return True
        else:
            return False


@commands.cooldown(1, 4, commands.BucketType.user)
@bot.command()
async def groll(ctx, arg=None):
    if arg is not None:
        await ctx.send('Invalid usage of .groll')
        raise discord.DiscordException
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
        with open('registered_users.txt', 'a') as f:
            f.write(f'{ctx.message.author.id}\n')

bot.run(token)
# client.run(token)
