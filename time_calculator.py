def get_days_later(days):
    """ Helper function to format days later"""
    if days == 1:
        return "(next day)"
    elif days > 1 and days < 2:
        return "(next day)"
    elif days >= 2:
        return f"({days} days later)"
    return ""


def add_time(start, duration, day = False):
    week_days =  [
        'monday', 'tuesday',
        'wednesday', 'thursday',
        'friday', 'saturday',
        'sunday'
    ]

    days_later = 0
    duration_tuple = duration.partition(":")
    duration_hours = int(duration_tuple[0])
    duration_minutes = int(duration_tuple[2])

    start_tuple = start.partition(":")
    start_hours = int(start_tuple[0])
    start_minutes_tuple = start_tuple[2].partition(" ")
    start_minutes = int(start_minutes_tuple[0])
    period = start_minutes_tuple[2].lower()

    end_minutes = start_minutes + duration_minutes
    end_hours = start_hours + duration_hours
    if end_minutes >= 60:
        end_hours += int(end_minutes / 60)
        end_minutes = int(end_minutes % 60)

    if period == "pm" and end_hours > 12:
        if end_hours % 24 >= 1:
            days_later += 1

    if end_hours >= 12:
        hours_left = end_hours / 24
        days_later += int(hours_left)

    tth = end_hours

    while True:
        if tth < 12:
            break
        if tth >= 12:
            if period == "am":
                period = "pm"
            elif period == "pm":
                period = "am"
            tth -= 12
    remaining_hours = int(end_hours % 12) or start_hours + 1

    remaining_mins = int(end_minutes % 60)


    results = f'{remaining_hours}:{remaining_mins:02} {period.upper()}'
    if day: # add day of the week
        day = day.strip().lower()
        selected_day = int((week_days.index(day) + days_later) % 7)
        current_day = week_days[selected_day]
        results += f', {current_day.title()} {get_days_later(days_later)}'

    else: # add days later
        results = " ".join((results, get_days_later(days_later)))

    return results.strip()

print(add_time("11:06 PM", "2:02"))
