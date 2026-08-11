age = int(input(" enter your age : "))
if age * 2 >= 100 :
          print (f"Over 100 ")
elif age * 2 >= 75 :
          print (f"Over 75 ")
elif age * 2 == 50 :
          print (f"Exactly 50 ")
elif age * 2 >= 30 :
          print (f"Between 30 and 74 ")
elif age * 2 >= 10 and age * 2 < 20 :
          print (f"Under 20 ")
else:
          print (f"Under 10 ")
