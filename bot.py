from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

TOKEN = "8935013119:AAG7SSGEmpJV5AoADxJcM-18P7T5qYm800"
SOURCE_CHANNEL_ID = -1002114461923
DESTINATION_CHANNEL_ID = -1004381263503

async def forward_content(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.channel_post and update.channel_post.chat.id == SOURCE_CHANNEL_ID:
        await context.bot.forward_message(
            chat_id=DESTINATION_CHANNEL_ID,
            from_chat_id=SOURCE_CHANNEL_ID,
            message_id=update.channel_post.message_id
        )

if __name__ == '__main__':
    application = ApplicationBuilder().token(TOKEN).build()
    channel_handler = MessageHandler(filters.Chat(chat_id=SOURCE_CHANNEL_ID), forward_content)
    application.add_handler(channel_handler)
    application.run_polling()
    
