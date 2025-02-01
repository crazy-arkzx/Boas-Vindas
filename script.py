# SISTEMA DE BOAS VINDAS PARA SEU SERVIDOR
# FEITO POR: Crazy_ArKzX
# GitHub: https://github.com/crazy-arkzx

import discord
from discord.ext import commands
from discord.ui import View, Button

TOKEN = "SEU_TOKEN"
GUILD_ID = 12345678910  # ID do seu servidor
WELCOME_CHANNEL_ID = 12345678910  # ID do canal de boas-vindas
ROLE_ID = 12345678910  # ID do cargo que será atribuido apos a entrada do membro
# OBS: O CARGO DO BOT PRECISA ESTAR A CIMA DO CARGO QUE SERA ATRIBUIDO AUTOMATICAMENTE!

intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Sistema de Boas Vindas Carregado com Sucesso!")

@bot.event
async def on_member_join(member):
    guild = bot.get_guild(GUILD_ID)
    if not guild:
        return

    channel = guild.get_channel(WELCOME_CHANNEL_ID)
    if not channel:
        return

    view = View()
    button1 = Button(label="Botao 1", url="https://seulinkaqui.com")
    button2 = Button(label="Botao 2", url="https://seulinkaqui.com")
    view.add_item(button1)
    view.add_item(button2)

    embed = discord.Embed(
        title="Bem-Vindo(a) ao Servidor!",
        description=f"Ola {member.mention}, seja bem-vindo(a) ao nosso servidor!\n\n"
                    "Leia as regras e aproveite sua estadia!",
        color=discord.Color.red()
    )
    embed.set_thumbnail(url=member.avatar.url if member.avatar else member.default_avatar.url)
    embed.set_image(url="LINK_DA_IMAGEM")  # Imagem da embed
    embed.add_field(name="Field 1:", value="Description 1", inline=False)
    embed.add_field(name="Field 2:", value="Description 2", inline=False)
    embed.add_field(name="Field 3:", value="Description 3", inline=False)
    embed.set_footer(text="Estamos felizes em ter voce aqui!")

    await channel.send(embed=embed, view=view)

    role = guild.get_role(ROLE_ID)
    if role:
        await member.add_roles(role)

    # Envi uma mensagem no PV do Membro
    try:
        await member.send(f"Ola {member.name}, seja bem-vindo(a) ao servidor! Esperamos que se divirta!")
    except discord.Forbidden:
        print(f"Nao consegui enviar mensagem para {member.name}")

bot.run(TOKEN)