import discord
import os
import asyncio
import yt_dlp
from dotenv import load_dotenv
""""
şarkılar seçilmedi hazır değil
"""
def run_bot():
    load_dotenv()
    TOKEN = os.getenv('DİSCOR_TOKEN_PHONK')
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    # Şarkı URL'leri
    song_urls = [
        'https://youtu.be/ddkZM3Gyjjg',  # İlk video bağlantısı
        'https://youtu.be/525bD4QtGPM',  # İkinci video bağlantısı
          # Üçüncü video bağlantısı
    ]

    voice_client = None  # Global değişken tanımı
    yt_dl_options = {"format": "bestaudio/best"}
    ytdl = yt_dlp.YoutubeDL(yt_dl_options)

    ffmpeg_options = {
        'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5',
        'options': '-vn -filter:a "volume=0.25"'
    }

    @client.event
    async def on_ready():
        print(f'{client.user} is now jamming')
        await start_playing()

    async def start_playing():
        global voice_client

        # Belirtilen ses kanalına bağlan
        channel_id = 1292837383787778159  # Buraya kanal ID'sini yerleştirdin
        channel = client.get_channel(channel_id)

        if not channel:
            print("Ses kanalı bulunamadı.")
            return
        
        voice_client = await channel.connect()

        while True:
            for url in song_urls:
                loop = asyncio.get_event_loop()
                data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=False))
                song = data['url']
                player = discord.FFmpegOpusAudio(song, **ffmpeg_options)
                voice_client.play(player)
                
                while voice_client.is_playing():
                    await asyncio.sleep(1)

    client.run(TOKEN) 