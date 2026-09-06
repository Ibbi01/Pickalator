def mark_checker():
    mark = int(input("Enter your mark: "))
    if mark>100 or mark<0:
        print("Your marks are invalid you moron")
    elif mark>=50:
        print("You have passed")
    else:
        print("You are a failure")
mark_checker()