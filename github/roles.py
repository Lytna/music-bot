import discord
from discord.ext import commands

# Bot'un prefix'ini ve gerekli ayarları yapın
intents = discord.Intents.default()
intents.message_content = True
intents.reactions = True
intents.guilds = True
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

# Bot hazır olduğunda konsola bir mesaj yazdır
@bot.event
async def on_ready():
    print(f'Bot olarak giriş yapıldı: {bot.user}')

# Belirli bir kanala mesaj atma komutu
@bot.command()
async def mesaj_at(ctx):
    # Mesajı göndermek istediğiniz kanalın ID'sini burada belirtin
    kanal_id = 1292828666128240712  # Değiştirin
    kanal = bot.get_channel(kanal_id)
    
    if kanal:
        embed = discord.Embed(
            title="Dinlemek istediğin türleri seç 📝",
            description="⛔ Türkçe rap  \n \n 🎶 Türkçe pop  \n \n 💀 Phonk \n \n 🎉 Yabancı pop",
            color=discord.Color.blue()  # İstediğiniz renkte değiştirin
        )
        
        mesaj = await kanal.send(embed=embed)  # Embed ile mesaj gönder
        await mesaj.add_reaction('⛔')  # Tepki ekle
        await mesaj.add_reaction('🎶')  # Tepki ekle
        await mesaj.add_reaction('💀')  # Tepki ekle 
        await mesaj.add_reaction('🎉')  # Tepki ekle 
# Tepkilere tıklanıldığında rol verme
@bot.event
async def on_reaction_add(reaction, user):
    if user.bot:
        return  # Botların tepkilerine yanıt verme

    # Tepki kontrolü
    if reaction.emoji == '⛔':
        role = discord.utils.get(reaction.message.guild.roles, name='⛔RAP⛔')  # Rol adını değiştirin
    elif reaction.emoji == '🎶':
        role = discord.utils.get(reaction.message.guild.roles, name='🎶T-POP🎶')  # Rol adını değiştirin
    elif reaction.emoji == '🎉':
        role = discord.utils.get(reaction.message.guild.roles, name='🎉POP🎉')  # Rol adını değiştirin
    elif reaction.emoji == '💀':
        role = discord.utils.get(reaction.message.guild.roles, name='💀PHONK💀')  # Rol adını değiştirin
    else:
        return  # Tanımlı tepki değil

    if role:
        member = reaction.message.guild.get_member(user.id)
        await member.add_roles(role)
        await user.send(f'{role.name} rolü verildi!')

# Botu çalıştırmak için token'ı buraya girin
bot.run("MTI5MjgyOTE1MTAyNzUzMTgxOA.GFR102.txJ2XDSNz5Bo1MZoosRN_zWZDxqGkIQj917MD0")
