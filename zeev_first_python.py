# התוכנית הראשונה שכתבתי בפייתון.
# שואלת גיל, שואלת כמה שנים קדימה, ומחשבת.

try:
    age = int(input("your age is : "))
    years = int(input("how many years : "))
except ValueError:
    print("Please enter whole numbers only.")
else:
    print("the result is :", years * 2)
    print("your age in", years, "years :", age + years)
    print("over 18 :", age + years >= 18)
