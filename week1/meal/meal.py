def main():
    time = input("What time is it? ")
    print(meal(time))

def meal(time):
    hour, minute = time.split(":")
    hour = int(hour)
    if 7 <= hour <=8:
        return "Breakfast Time"
    elif 12 <= hour <= 13:
        return "Lunch Time"
    elif 18 <= hour <= 19:
        return "Dinner Time"
    else:
        return "Not the time for a meal"

main()