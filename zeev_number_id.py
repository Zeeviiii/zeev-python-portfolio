def number_id (number_1 ,number_2 , number_3):
    """ A function that checks which number is the largest among 3 numbers """
    if  number_1 > number_2 and number_1 > number_3 : #checking the first number it is biggest 
        print ("Number one is the biggest !")
    elif number_2 > number_1 and number_2 > number_3 :#checking the second number it is biggest
        print ("Number two is the biggest !")
    elif number_3 > number_1 and number_3 > number_2 :#checking the third number it is biggest
        print ("Number three is the biggest !")
    else:
        print ("All are equal to each other!")

number_1 = int(input("Enter a Number one: "))
number_2 = int(input("Enter a Number two: "))
number_3 = int(input("Enter a Number three: "))
number_id (number_1 ,number_2 , number_3 )               
