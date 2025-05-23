import sqlite3

conn = sqlite3.connect('animebot.db', check_same_thread=False)
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY,
    username TEXT
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS watchlist (
    user_id INTEGER,
    anime_id INTEGER,
    PRIMARY KEY (user_id, anime_id)
)
''')

conn.commit()

def add_user(user_id, username):
    cursor.execute('INSERT OR IGNORE INTO users (user_id, username) VALUES (?, ?)', (user_id, username))
    conn.commit()

def add_to_watchlist(user_id, anime_id):
    cursor.execute('INSERT OR IGNORE INTO watchlist (user_id, anime_id) VALUES (?, ?)', (user_id, anime_id))
    conn.commit()

def get_watchlist(user_id):
    cursor.execute('SELECT anime_id FROM watchlist WHERE user_id = ?', (user_id,))
    return [row[0] for row in cursor.fetchall()]