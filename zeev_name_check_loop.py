def check_name ():
    """ ask for 8 name and print their length"""
    name_1 = 0
    while name_1 <8 :
        name_2 = input ("Enter a name : ")
        if   len(name_2)== 0 :#empty input 
            print(f"You didn't enter a name !!")
        elif len(name_2)< 4:#less than 4 characters
            print(f"{name_2} is Short name")
        elif len(name_2)<= 7:#above 4 and less 7 characters
            print(f"{name_2} is Medium name")
        else:#above 8 characters
            print (f"{name_2} is Long name")
        name_1 += 1

check_name ()
