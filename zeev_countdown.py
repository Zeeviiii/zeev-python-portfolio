def countdown(n):
    if n == 0:
        print("Liftoff!")
    else:
        print(n)
        countdown(n-1)

start = int(input("Enter countdown number: "))
countdown(start)
