total_marks=int(input("enter total marks "))
if total_marks >=90 and total_marks <=100:
    print("Grade A")
elif total_marks >=80 and total_marks <=89:
    print("Grade B")
elif total_marks >=70 and total_marks <=79:
    print("Grade C")
elif total_marks >=60 and total_marks <=69:
    print("Grade D")
elif total_marks <60 and total_marks >=0:
    print("Grade F")
else:
    print("Invalid mark")