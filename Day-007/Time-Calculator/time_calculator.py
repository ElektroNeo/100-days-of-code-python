def add_time(start, duration, startDay = ''):

    # Get time
    clock = start.split()
    ending = clock[1]
    time = clock[0].split(':')
    hour = int(time[0])
    minute = int(time[1])
    day = 0

    # Day of Week
    dayOfWeek = {
        'Monday': 0,
        'Tuesday': 1,
        'Wednesday': 2,
        'Thursday': 3,
        'Friday': 4,
        'Saturday': 5,
        'Sunday': 6
    }

    # List of days
    dayList = list(dayOfWeek.keys())

    # Add time
    addTime = duration.split(':')
    addHour = int(addTime[0])
    addMinute = int(addTime[1])

    # Convert to 24 hour mode
    if ending == 'PM':
        hour += 12

    hour += addHour
    minute += addMinute

    if minute > 59:
        minute -= 60
        hour += 1

    # Calculate day
    if hour > 24:
        day = int(hour / 24)
        hour = hour % 24
    
    # Convert to 12 hour mode
    if hour >= 12:
        hour -= 12
        ending = ' PM'
    else:
        ending = ' AM'

    if hour == 0:
        hour = '12'
    else:
        hour = str(hour)

    # Convert minute to 2 digit mode
    minute = "{:02d}".format(minute)
    
    # If start day is not exist
    if startDay == '':
        # Check for passing day
        if day == 1:
            day = 'next day'
            return hour + ':' + minute + ending + ' (' + day + ')'
        elif day > 1:
            day = str(day) + ' days later'
            return hour + ':' + minute + ending + ' (' + day + ')'
        
        return hour + ':' + minute + ending
    # If start day exist
    else:
        # Capitalize start day
        startDay = startDay.capitalize()
        startDay = dayOfWeek[startDay]
        startDay += day
        
        # Get day after addet time
        startDay = dayList[startDay%7]

        # Check for passing day
        if day == 1:
            day = 'next day'
            return hour + ':' + minute + ending + ', ' + startDay + ' (' + day + ')'
        elif day > 1:
            day = str(day) + ' days later'
            return hour + ':' + minute + ending + ', ' + startDay + ' (' + day + ')'
        
        return hour + ':' + minute + ending + ', ' + startDay 