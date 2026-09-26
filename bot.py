from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler

async def start(update: Update, context: ContextTypes. DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="I am a bot to host Telegram videos and stream them.")

if __name__ == '__main__':
    application = ApplicationBuilder().token('6399560910:AAEKMMneewfdfdNa6-mIjij4-WxOXE7k4Uo').build()
    
    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)
    
    application.run_polling()
  
