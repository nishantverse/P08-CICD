FINE_PER_DAY = 5

def calculate_fine(days_late):
    if days_late <= 0:
        return 0

    return days_late * FINE_PER_DAY
