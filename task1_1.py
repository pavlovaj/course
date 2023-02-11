def season(month):
    if month in (1, 2, 12):
        return "зима"
    if month in (3, 4, 5):
        return "весна"
    if month in (6, 7, 8):
        return "лето"
    elif month in (9, 10, 11):
        return "осень"