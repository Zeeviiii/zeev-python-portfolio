def check_name ():
    """ ask for 8 name and print their length"""
    name_1 = 0
    while name_1 <8 :
        name_2 = input ("Enter a name : ")
        print (f"the name has {len(name_2)} letters")
        name_1 += 1

check_name ()
