def minutes_to_seconds():
    minutes_to_seconds = int(input("Enter a number of minutes : "))
    if minutes_to_seconds <= 0:
        print("that is not possible you monkey")
    else:
        print(60 * minutes_to_seconds)

minutes_to_seconds()