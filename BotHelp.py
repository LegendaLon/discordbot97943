import discord
from discord.ext import commands

from main import module

import config

class Help(commands.Cog):
	def __init__(self, client):
		self.client = client

	@commands.command(aliases = ["сервер", "серв", "server", "Server"]) # Информация о сервере рабоает также с командами...
	async def Сервер(self, ctx):
	    guild = ctx.guild
	    embed = discord.Embed(title=f"Сервер: **{guild.name}**", description="**Енот Бот** был сделан специально для этого сервера.", color=config.orange) # Создает строку
	    embed.add_field(name=":wave: **Привет дорогой друг.** :wave:", value=f"Если ты тут значит тебя приняли,\n чтобы узнать айпи напиши - {config.PREFIX_COMMAND}ip", inline=True) # Создает строку
	    embed.add_field(name="Людей на сервере", value=f"{guild.member_count}", inline=False)
	    embed.add_field(name="**Немного о сервере:**", value="Нету приватов, нету доната, свобода действий, не ограниченая территория.", inline=False) # Создает строку
	    embed.add_field(name="**Узнать все команды:**", value=f"{config.PREFIX_COMMAND}Помощь.", inline=False) # Создает строку
	    embed.add_field(name="**Пожертвования:**", value=f"Если у вас появилось желание помочь серверу\n просто напишите - {config.PREFIX_COMMAND}donate", inline=False) # Создает строку
	    embed.set_footer(text=f"Все права на бота пренадлежат: {config.BOT_AUTHOR}") # Подвал сообщения
	    await ctx.send(embed=embed) # Отправляет сообщение а потому удалит после 300 секунд

	@commands.command(aliases=["помощь", "Help", "help"]) # Команда Помощь работает также с...
	async def Помощь(self, ctx): # Создает команду
	    embed = discord.Embed(title="Все команды **Енот Бот**", description="", color=config.orange) # Создает красивый вывод с заголовком title и цветом green 
	    embed.add_field(name=f'**{config.PREFIX_COMMAND}Сервер**', value="Информация о сервере.", inline=False) # Создает строку
	    embed.add_field(name=f'**{config.PREFIX_COMMAND}cat**', value="Отправляет гифку кота =D.", inline=False) # Создает строку
	    embed.add_field(name=f'**{config.PREFIX_COMMAND}ver**', value="Узнать версию бота.", inline=False) # Создает строку
	    embed.add_field(name=f'**{config.PREFIX_COMMAND}шар**', value="Отвечает на заданый вопрос.", inline=False) # Создает строку
	    embed.set_footer(text=f"Все права на бота пренадлежат: {config.BOT_AUTHOR}") # Подвал сообщения
	    await ctx.send(embed=embed) # 

	@commands.command(aliases = ["версия", "Версия", "Ver"]) # 
	async def ver(self, ctx): # Создает команду
	    embed = discord.Embed(title="**Версия бота**", color=config.orange) # 
	    embed.add_field(name="**Последняя версия**", value=f"Версия - {config.version}", inline=True) # 
	    embed.set_footer(text=f"Все права на бота пренадлежат: {config.BOT_AUTHOR}") # Подвал сообщения
	    await ctx.send(embed=embed) # 

	@commands.command(aliases=["донат", "Донат", "Donate"])
	async def donate(ctx):
		pass
	    # embed = discord.Embed(title="**Реквизиты**", description="Места куда можно скинуть денюжку.", color=config.orange)
	    # embed.add_field(name="**Реквизиты**", value=f"QIWI - {donate_qiwi}\nWebMoney - {donate_webmoney}", inline=True) # 
	    # embed.set_footer(text=f"Все права на бота пренадлежат: {config.BOT_AUTHOR}") # Подвал сообщения
	    # await ctx.author.send(embed=embed)

class Info(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases = ["Module", "Модули", "модули"])
    async def module(self, ctx):
    	author = ctx.message.author
    	await ctx.send(f'{author}, все модули которые бот использует: ``{module}``')


def setup(client):
	client.add_cog(Help(client))
	client.add_cog(Info(client))