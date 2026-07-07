from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

TOKEN = "8935013119:AAG7SSGEmpJV5AoADxJcMDHuJL3mQrvpQeo"
DESTINATION_CHANNEL_ID = -1004381263503

SOURCE_CHANNELS = [-1002114461923, -1002402557947]

async def forward_content(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.channel_post and update.channel_post.chat.id in SOURCE_CHANNELS:
        await context.bot.forward_message(
            chat_id=DESTINATION_CHANNEL_ID,
            from_chat_id=update.channel_post.chat.id,
            message_id=update.channel_post.message_id
        )

if __name__ == '__main__':
    application = ApplicationBuilder().token(TOKEN).build()
    
    channel_handler = MessageHandler(filters.Chat(chat_id=tuple(SOURCE_CHANNELS)), forward_content)
    application.add_handler(channel_handler)
    
    application.run_polling()
    
