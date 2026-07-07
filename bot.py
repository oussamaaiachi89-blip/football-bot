from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

# التوكن الخاص ببوتك (تم التأكد منه)
TOKEN = "8935013119:AAG7SSGEmpJV5AoADxJcM-l8P7T5qYm8O0"

# معرف قناة المصدر (التي تسحب منها)
SOURCE_CHANNEL_ID = -1002114461923 

# معرف قناتك الخاصة (SPURTS.HD)
DESTINATION_CHANNEL_ID = -1004381263503 

async def forward_content(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # وظيفة نقل الرسائل تلقائياً
    if update.channel_post and update.channel_post.chat.id == SOURCE_CHANNEL_ID:
        await context.bot.forward_message(
            chat_id=DESTINATION_CHANNEL_ID,
            from_chat_id=SOURCE_CHANNEL_ID,
            message_id=update.channel_post.message_id
        )

if __name__ == '__main__':
    application = ApplicationBuilder().token(TOKEN).build()
    
    # ربط البوت بقناة المصدر للمراقبة
    channel_handler = MessageHandler(filters.Chat(chat_id=SOURCE_CHANNEL_ID), forward_content)
    application.add_handler(channel_handler)
    
    print("البوت يعمل الآن ويراقب القناة المصدر لنقل المحتوى إلى SPURTS.HD!")
    application.run_polling()
    
