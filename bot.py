import openai 
import config
from discord.ext import commands


openai.api_key = config.API
bot = commands.Bot(command_prefix= config.Prefix)


@bot.event
async def on_ready():
    print(f'✅ El bot {bot.user.name} está funcionando correctamente.')

@bot.command()
async def ia(ctx, *, message):
    respuesta = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role":"user", "content": message}])
    await ctx.send(respuesta.choices[0].message.content)

bot.run(config.TOKEN)


# Todos los derechos reservados a https://www.luc4s.dev