def List_number(number , name ):
    if len(name.lower()) == number:
      result = "Exactiy the same number"
    else:
      result = "Exactiy not the same number"
    return result

name = input("Enter a name :")
number = int(input(" Enter a number:"))
print(List_number(number , name))
                
