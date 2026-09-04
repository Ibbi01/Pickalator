def smallest_num_out_of_3(num1,num2,num3):
    if num1<num2 and num1<num3:
        print(num1,"is smallest number")
    elif num2<num1 and num2<num3:
        print(num2,"is smallest number")
    else:
        print(num3,"is smallest number")
smallest_num_out_of_3(10,8,20)
