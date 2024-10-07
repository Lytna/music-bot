import discord
import os
import asyncio
import yt_dlp
from dotenv import load_dotenv
""""
şarkılar seçilmedi hazır
"""
def run_bot():
    load_dotenv()
    TOKEN = os.getenv('discord_token')
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    # Şarkı URL'leri
    song_urls = [
        'https://youtu.be/5J-w9AHKHsc',  # İlk video bağlantısı
        'https://youtu.be/_8VlmpKCYCM',  # İkinci video bağlantısı
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
        channel_id = 1292816261247668345  # Buraya kanal ID'sini yerleştirdin
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

    client.run('MTI5MjU4NDQwOTc5ODU0MTMxMg.GDZb8M.BaIUjerMKFZ0FZ9vY8jrlyr9XJ9KDKKpvDPJFE')
