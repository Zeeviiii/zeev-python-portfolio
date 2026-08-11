def multiplication_table ():
    user_num = int(input("Enter table size: "))
    for i in range(1, user_num +1):
        for j in range(1, user_num +1):
            print(f"{i} x {j} = {i * j}")
        print("---")

multiplication_table ()
    
