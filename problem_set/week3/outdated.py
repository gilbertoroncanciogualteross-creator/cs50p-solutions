# Implement a program that prompts the user for a date, anno Domini, in month-day-year order
# formatted like 9/8/1636 or September 8, 1636. Then output that same date in YYYY-MM-DD
# If the user's input is not a valid date in either format, prompt the user again.

months = ["January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"]

while True:
    try:
        date = input("Date: ")

        if "/" in date:
            date = date.split("/")
            month = int(date[0])
            day = int(date[1])
            year = int(date[2])

        else:
            date = date.replace(",", "")
            date = date.split()
            month = months.index(date[0]) + 1
            day = int(date[1])
            year = int(date[2])

        if 1 <= month <= 12 and 1 <= day <= 31:
            print(f"{year}-{month:02}-{day:02}")
            break

    except (ValueError, IndexError):
        pass
