def compare_speeds(v1_kmh, v2_ms):
    # Функція для порівняння двох швидкостей.
    # Перетворення км/год в м/с
    v1_ms = v1_kmh / 3.6
    # Перетворення м/с в км/год
    v2_kmh = v2_ms * 3.6

    result = {
        "v1_ms": v1_ms,
        "v2_kmh": v2_kmh
    }

    if v1_ms > v2_ms:
        result["comparison"] = "Швидкість v1 більша, ніж v2."
    elif v1_ms < v2_ms:
        result["comparison"] = "Швидкість v1 менша, ніж v2."
    else:
        result["comparison"] = "Швидкості однакові."
    
    return result

def translate_text(text, lang_code):
    # Функція для перекладу тексту.
    translations = {
        "uk": { "language": "Українська", "speed_v1": "Швидкість v1", "speed_v2": "Швидкість v2", "greater": "більша", "less": "менша", "equal": "однакові"},
        "en": {"language": "English", "speed_v1": "Speed v1", "speed_v2": "Speed v2", "greater": "greater", "less": "less", "equal": "equal"}
    }
    if lang_code not in translations:
        lang_code = "uk"  # Українську за замовченням

    return translations[lang_code].get(text, text)