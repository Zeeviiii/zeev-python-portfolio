def check_name (name):
    if len(name)< 4:
     print ("Short")
    elif len(name) >= 4 and len (name)<=7:
     print ("medium")
    else:
     print ("Long")

name = input("Enter a name:")
check_name(name)            
