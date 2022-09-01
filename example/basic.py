from chord import Client

client = Client()

@client.on()
async def ready():
    print("Logged in as f{client.user.tag}!")

@client.on()
async def interactionCreate(interaction):

    if (interaction.commandName == 'ping'):
        await interaction.reply('Pong!')

client.run("")