# Instalando Biblioteca
# pip install requests discord


# IMPORTANDO BIBLIOTECAS PARA O DISCORD
from discord_webhook import DiscordWebhook, DiscordEmbed


 
# INICIANDO MONTAGEM DA MENSAGEM PARA ENVIAR PARA O DISCORD
# Link do webhook
webhook = DiscordWebhook(
    url='https://discord.com/api/webhooks/#')


embed = DiscordEmbed(title='Nome da Notificação',
                     color='03b2f8')

embed.add_embed_field(name="Informação 1",
                      value=f"detalhes da informação 1", inline=False)

embed.add_embed_field(name="Informação 2",
                      value=f"detalhes da informação 2", inline=False)


webhook.add_embed(embed)
response = webhook.execute(embed)
