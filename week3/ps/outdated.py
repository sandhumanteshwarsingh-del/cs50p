def main():
    months = {
        "January": 1,
        "February": 2,
        "March": 3,
        "April": 4,
        "May": 5,
        "June": 6,
        "July": 7,
        "August": 8,
        "September": 9,
        "October": 10,
        "November": 11,
        "December": 12
    }
    while True:
        try:
            date = input("Date: ")
            for a in date:
                if a == " ":
                    month, day, year = date.split()
                    day = day.replace(",", "")
                    for key in months:
                        if key == month:
                            month = months[key]
                    
            for a in date:
                if a == "/":
                    month, day, year = date.split("/")
            month = int(month)
            day = int(day)
            year = int(year)
        except ValueError:
            pass

        else:
            if month > 12 or day > 31:
                continue
            else:
                break

    padded_year = f"{year:04d}"
    padded_month = f"{month:02d}"
    padded_day = f"{day:02d}"
    print(f"{padded_year}-{padded_month}-{padded_day}")

main()