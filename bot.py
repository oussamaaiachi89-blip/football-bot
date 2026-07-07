import os
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler

TOKEN = "8935013119:AAG7SSGEmpJV5AoADxJcMDHuJL3mQrvpQeo"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="أهلاً! البوت يعمل الآن ويراقب الأهداف.")

if __name__ == '__main__':
    application = ApplicationBuilder().token(TOKEN).build()
    
    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)
    
    print("البوت يعمل الآن...")
    application.run_polling()
