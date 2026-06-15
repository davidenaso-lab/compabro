import os
from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes

STAFF_CHAT_ID = -5598663431

async def forward(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=STAFF_CHAT_ID,
        text=update.message.text
    )

app = Application.builder().token(os.environ["BOT_TOKEN"]).build()
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, forward))
app.run_polling()
