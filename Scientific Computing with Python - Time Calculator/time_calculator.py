def add_time(start, duration, day=False):
    # Auxiliary Variables
    am_pm_flip = {"AM": "PM", "PM": "AM"}
    days_array = [
        "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday",
        "Sunday"
    ]
    days_index = {
        "monday": 0,
        "tuesday": 1,
        "wednesday": 2,
        "thursday": 3,
        "friday": 4,
        "saturday": 5,
        "sunday": 6
    }

    start_hour = int(start.split(":")[0])
    start_minute = int(start.split(":")[1].split(" ")[0])

    duration_hour = int(duration.split(":")[0])
    duration_minute = int(duration.split(":")[1])
    
    am_pm = start.split(":")[1].split(" ")[1]
    
    duration_days = int(duration_hour / 24)
    
    result_minute = start_minute + duration_minute

    if result_minute >= 60:
        start_hour += 1
        result_minute = result_minute % 60
    am_pm_flips = int((start_hour + duration_hour) / 12)
    result_hour = (start_hour + duration_hour) % 12


    result_minute = result_minute if result_minute > 9 else "0" + str(
        result_minute)
    result_hour = result_hour = 12 if result_hour == 0 else result_hour

    if (am_pm == "PM" and start_hour + (duration_hour % 12) >= 12):
        duration_days += 1

    result_am_pm = am_pm_flip[am_pm] if am_pm_flips % 2 == 1 else am_pm

    new_time = str(result_hour) + ":" + str(result_minute) + " " + result_am_pm

    if (day):
        day = day.lower()
        index = int((days_index[day]) + duration_days) % 7
        result_day = days_array[index]
        new_time += ", " + result_day

    if (duration_days == 1):
        return new_time + " " + "(next day)"
    elif (duration_days > 1):
        return new_time + " (" + str(duration_days) + " days later)"

    return new_time
