from telegram.ext import Updater, CommandHandler
import config
import handlers

def main():
    updater = Updater(token=config.BOT_TOKEN)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", handlers.start))
    dp.add_handler(CommandHandler("latest", handlers.latest))
    dp.add_handler(CommandHandler("addwatch", handlers.add_watch))
    dp.add_handler(CommandHandler("watchlist", handlers.watchlist))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()