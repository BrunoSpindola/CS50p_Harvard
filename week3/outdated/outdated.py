months_list = [
                "January",
                "February",
                "March",
                "April",
                "May",
                "June",
                "July",
                "August",
                "September",
                "October",
                "November",
                "December"
            ]

while True:
    try:
        date = input("Date: ")
        if "/" in date:
            month, day, year = date.split("/")
            month = int(month)
            day = int(day)
            year = int(year)
        elif "," in date:
            month_name, day, year = date.replace(",", "").split()
            month = months_list.index(month_name.capitalize()) + 1
            day = int(day)
            year = int(year)
        else:
            continue
        
        if 1 <= month <= 12 and 1 <= day <= 31:
            print(f"{year}-{month:02}-{day:02}")
            break
        else:
            continue

    except (ValueError, IndexError):
        pass
