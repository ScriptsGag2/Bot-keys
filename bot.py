import discord
from discord import app_commands
import time
import secrets

class BotDeKeys(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.default())
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self):
        await self.tree.sync()

client = BotDeKeys()

@client.tree.command(name="key", description="Genera una key temporal de 24 horas")
async def key(interaction: discord.Interaction):
    # 24 horas en segundos (86400). Puedes cambiarlo si quieres que dure más o menos.
    tiempo_expiracion = int(time.time()) + 86400 
    token_azar = secrets.token_hex(12)
    
    # Formato que lee tu script de Roblox
    key_temporal = f"RBX-{tiempo_expiracion}-{token_azar}"
    
    embed = discord.Embed(
        title="🔑 Tu Key Temporal",
        description=f"Copia y pega esta key en Roblox (válida por 24 horas):\n\n`{key_temporal}`",
        color=discord.Color.green()
    )
    await interaction.response.send_message(embed=embed, ephemeral=True)

# Tu token de Discord real
client.run("MTU2OTA0MzY0Mzg1Mzk3MTQ3Nw.GIr5UU.Ovgiv8P1T4qc1JtOsuHX-mm3jAvw9Y7633X3sQ")
