def guess_name ():
    while True :
        name = input("Guess my name : ")
        if name.lower() == "zeev" or name == "זאב":
            print (f" You are Guess my name the : {name}")
            break
        else:
            print(" Try again....")


guess_name ()
    
