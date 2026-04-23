import os
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters

TOKEN = os.getenv("BOT_TOKEN")

AUTO_REPLY = "Assalomu alaykum, hozir men offline man."

async def auto_reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(AUTO_REPLY)

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT, auto_reply))

app.run_polling()
