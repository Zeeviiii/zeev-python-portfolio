def guess_number():
    while True:
        id_num = int(input("Enter a number "))
        if id_num == 0:
            print("Goodbye!")
            break
        for x in range(id_num + 1):
            if x == id_num :
              print(f"{x} Correct guess")
              break 

guess_number()
