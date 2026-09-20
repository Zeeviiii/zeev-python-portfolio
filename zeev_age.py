# Checks age, multiplies by 2, and reports which band the result falls in
# בודק את הגיל, מכפיל ב-2, ואומר לאיזה טווח התוצאה נופלת
 
try:
    age = int(input(" enter your age : "))
except ValueError:
    print("That is not a number.")
else:
    result = age * 2
 
    # הטווחים יורדים ברצף ובלי חורים: כל תוצאה נופלת לענף אחד בדיוק
    if result >= 100:
        print("100 or more")
    elif result >= 75:
        print("Between 75 and 99")
    elif result >= 50:
        print("Between 50 and 74")
    elif result >= 30:
        print("Between 30 and 49")
    elif result >= 20:
        print("Between 20 and 29")
    elif result >= 10:
        print("Between 10 and 19")
    else:
        print("Under 10")
