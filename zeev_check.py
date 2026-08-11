def check_number(number):
    if number >= 100 and number <= 150: 
        print("Over 100")
    if number >= 50:
        print("Over 50")
    if number >= 30:
        print("Over 30")
    if number >= 10:
        print("Over 10")
    if number >= 0 :
        print("Over 0 ")
    if number < 0 :
        print("Negative number")

number = int(input(" Enter a number that you want:"))
check_number(number)
             
