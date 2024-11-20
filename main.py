import discord
from discord.ext import commands
from config.config import intents, token 
from commands.commandsModerator import kick, ban, unban



# Tipo de push de comando
bot = commands.Bot(command_prefix="!", intents=intents)

# Eventos do Pinguinn Bot
@bot.event
# Verficando se o bot está online
async def on_ready():
    print("Penguinn está pronto ✅")
    await bot.change_presence(status=discord.Status.idle, activity=discord.Game('HOCKEY 🏒 '))
    await bot.tree.sync()
    
    # Id da mensagem
    embed_message_id = 1308861576425766964

    # Id do chat de regras
    rules_chat_id = 1308189320074498148
    channel = bot.get_channel(rules_chat_id)

    # Bsucando canal de regras
    if not channel:
        print("Canal de regras não encontrado!")
        return
    print(f"Canal de regras encontrado! ")

    if embed_message_id:
        try:
            existing_message = await channel.fetch_message(embed_message_id)
            if existing_message:
                print("O embed já foi enviado!")
                return
        except discord.NotFound:
            print("Mensagem antiga não encontrada. Um novo embed será enviado.")

    #Regras do Servidor
    embed_rules = discord.Embed(
        title="📜 Regras da Comunidade",
        description="Leia as regras para manter um ambiente saudável e divertido no servidor.",
        color=discord.Color.purple(),
    )
    
    embed_rules.set_image(url="https://i.imgur.com/Fd7ss2X.gif")

    embed_rules.add_field(
        name="1. Termos de Segurança",
        value="Respeite as Diretrizes da Comunidade e os Termos de Serviço.",
        inline=False,
    )
    embed_rules.add_field(
        name="2. Termos proibidos",
        value="É proibido o uso de termos relacionados a assuntos indevidos, como pedofilia, toxicidade e preconceito.",
        inline=False,
    )
    embed_rules.add_field(
        name="3. Atenção ao chat",
        value="Respeite o canal em que você está. Não envie imagens ou vídeos em canais de conversa por exemplo, respeite o espaço.",
        inline=False,
    )
    embed_rules.add_field(
        name="4. Conteúdos +18",
        value="É proibido conteúdo relacionado a pornografia ou imagens com teor erótico. Isso resultará em remoção do servidor.",
        inline=False,
    )
    embed_rules.set_footer(text="Respeite as regras e divirta-se no servidor! 😊")

# Boas-Vindas ao Servidor
@bot.event
async def on_member_join(member: discord.Member):
    # Definindo Id dos canais
    channel = bot.get_channel(1307529809911480320)
    channel_rules_id = 1308189320074498148
    channel_question_id = 1308193696486789122

    channel_rules = bot.get_channel(channel_rules_id)
    channel_question = bot.get_channel(channel_question_id)

    name_tag = f"{member.name}"

    # Configurando o Embed
    embed_welcome = discord.Embed(
        title=f'Bem-vindo(a) | {name_tag}!',
        description="Explore, o iglu do Iced Club. 🐧\n\n"
        f"Antes de se aventurar leia as {channel_rules.mention}. 🥶\n\n"
        f"Se estiver com dúvidas acesse {channel_question.mention}. 😉\n\n\n ",
        color=discord.Color.purple()
    )
    embed_welcome.set_thumbnail(url=member.avatar.url)
    embed_welcome.set_footer(text=f"{member.guild.name} | Iced Club", icon_url=member.guild.icon.url)

    await channel.send(embed=embed_welcome)



#Commandos do servidor

# Comando de kick, ban e unban
bot.add_command(kick)
bot.add_command(ban)
bot.add_command(unban)




# Bot Token
bot.run(token)