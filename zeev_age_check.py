def id_names():
    """ a Function to check age suitable for work """
    number = 0
    while number <= 10:# loop for 10 times 
        id_num = int(input("Enter your age :"))
        if id_num < 18:# too young 
              print ("you are NOT the right age to work ")
        elif id_num >= 18 and id_num <= 67:#working age 
              print ("you are of the right age to work ")
        else: #68 and above 
              print ("you are at retirement age ")

        number += 1
             

id_names()    
