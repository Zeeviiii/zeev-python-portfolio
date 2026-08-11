def average():
    num_1 = 0
    while num_1 <= 5:
        num = int(input("Enter a number : "))
        if num >=50:
            num = num *2
            print(f" you result : {num}")
        elif num < 50 and num > 10:
            num = num //2
            print(f" you result : {num}")
        else:
            num = num + 2
            print(f" you result : {num}")
        num_1+= 1


average()
            
