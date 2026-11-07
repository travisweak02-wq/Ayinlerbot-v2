
import os
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes
)

TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 Welcome to AYINLERBOT V2!\n\n"
        "Your new AI-inspired Telegram experience starts here.\n\n"
        "Use /help to see my commands."
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "⚡ AYINLERBOT V2 COMMANDS\n\n"
        "/start - Start the bot\n"
        "/help - Show commands"
    )

def main():
    if not TOKEN:
        raise RuntimeError("BOT_TOKEN is missing!")

    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))

    print("AYINLERBOT V2 is online!")
    app.run_polling()

if __name__ == "__main__":
    main()
