def format_anime_info(anime):
    return f"{anime['title']} ({anime['type']}) - {anime.get('episodes', '?')} epizod"