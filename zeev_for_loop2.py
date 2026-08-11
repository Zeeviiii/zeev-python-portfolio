def number ():
    user_num = int(input("Enter a number : "))
    for x in range(user_num):
        if x % 2 == 0 :
            print(f"{x} is even")
        else:
            print(f"{x} is odd")
            

number ()
