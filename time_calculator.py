def add_time(start, duration, start_day=False):
  days = [
      "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday",
      "Sunday"
  ]
  # Get the start time and duration time
  start_time_meridiem = start.split()
  start_time = start_time_meridiem[0].split(":")
  meridiem = start_time_meridiem[1]
  duration = duration.split(":")
  if meridiem == "PM": start_time[0] = int(start_time[0]) + 12
  # Calculate the end time
  end_hour = int(start_time[0]) + int(duration[0])
  end_min = int(start_time[1]) + int(duration[1])

  if end_min > 60:
    end_hour += (end_min // 60)
    end_min %= 60
  next_days = end_hour // 24
  if next_days > 0:
    end_hour %= 24
    if end_hour == 0:
      end_hour = 12
      end_meridiem = "AM"
    elif end_hour > 12:
      end_hour -= 12
      end_meridiem = "PM"
    elif end_hour >= 12:
      end_meridiem = "PM"
    else:
      end_meridiem = "AM"
    if next_days == 1:
      new_time = f"{end_hour}:{end_min:02d} {end_meridiem} (next day)"
    else:
      new_time = f"{end_hour}:{end_min:02d} {end_meridiem} ({next_days} days later)"
  else:
    if end_hour > 12:
      end_hour -= 12
      end_meridiem = "PM"
    elif end_hour >= 12:
      end_meridiem = "PM"
    else:
      end_meridiem = "AM"
    new_time = f"{end_hour}:{end_min:02d} {end_meridiem}"
  if start_day is not False:
    for i in range(len(days)):
      if start_day.lower() == days[i].lower():
        keyword = new_time.find("M")
        new_time = new_time[:keyword + 1] + ", " + days[
            (i + next_days) % 7] + new_time[keyword + 1:]
  return new_time
