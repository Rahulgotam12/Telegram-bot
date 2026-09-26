from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters
import yt_dlp
import os

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="I am a video downloader bot. Send me a link!")

async def process_video(update: Update, context: ContextTypes.DEFAULT_TYPE):
    url = update.message.text
    chat_id = update.effective_chat.id
    
    await context.bot.send_message(chat_id=chat_id, text="Processing...")
    
    ydl_opts = {
        'format': 'best',
        'outtmpl': 'downloads/%(id)s.%(ext)s',
        'noplaylist': True,
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            filename = ydl.prepare_filename(info)

        # Download option
        await context.bot.send_video(chat_id=chat_id, video=open(filename, 'rb'), caption="Here is your video!")
        os.remove(filename)  # Delete the file after sending
    except Exception as e:
        await context.bot.send_message(chat_id=chat_id, text=f"Error: {str(e)}")

if __name__ == '__main__':
    application = ApplicationBuilder().token('6399560910:AAEKMMneewfdfdNa6-mIjij4-WxOXE7k4Uo').build()
    
    start_handler = CommandHandler('start', start)
    message_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), process_video)
    
    application.add_handler(start_handler)
    application.add_handler(message_handler)
    
    application.run_polling()
    
