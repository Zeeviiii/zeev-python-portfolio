def user_name(first_name , last_name):
    if len(first_name) == 0 and len(last_name) == 0:
          result = "No letters"
    elif len(first_name) >= 4 and len(last_name) >= 4:
          result = "Both name are long"
    elif len(first_name) >= 4:
          result = "Long first name"
    elif len(last_name) >= 4:
          result = "Long last name"
    else:
          result = "Short name"
    return result

first_name = input("enter your first name :")
last_name = input ("enter your last name :")
print(user_name(first_name , last_name))
