from telegram import Update
from telegram.ext import CallbackContext
from anime_api import get_latest_anime
from database import add_user, add_to_watchlist, get_watchlist

def start(update: Update, context: CallbackContext):
    user = update.effective_user
    add_user(user.id, user.username or "")
    update.message.reply_text(f"Salom, {user.first_name}! Anime botga xush kelibsiz.")

def latest(update: Update, context: CallbackContext):
    animes = get_latest_anime()
    if not animes:
        update.message.reply_text("Hozircha yangi animelar mavjud emas.")
        return
    msg = "Yangi chiqqan anime ro'yxati:\n"
    for anime in animes[:5]:
        msg += f"- {anime['title']} ({anime['type']})\n"
    update.message.reply_text(msg)

def add_watch(update: Update, context: CallbackContext):
    user = update.effective_user
    if len(context.args) != 1:
        update.message.reply_text("Iltimos, qo‘shmoqchi bo‘lgan anime ID sini kiriting.")
        return
    anime_id = context.args[0]
    add_to_watchlist(user.id, anime_id)
    update.message.reply_text(f"Anime (ID: {anime_id}) kuzatuv ro‘yxatingizga qo‘shildi.")

def watchlist(update: Update, context: CallbackContext):
    user = update.effective_user
    anime_ids = get_watchlist(user.id)
    if not anime_ids:
        update.message.reply_text("Sizning kuzatuv ro‘yxatingiz bo‘sh.")
        return
    msg = "Siz kuzatayotgan animelar:\n" + "\n".join(str(aid) for aid in anime_ids)
    update.message.reply_text(msg)