def temperature(temp):
    if temp > 130 :
        print ("Ready to use ")
    elif temp == 130 :
        print ("Wait for the temperature to rise above 130")
    else:
        print ("Not ready at all")

temp = int(input("Enter your temperature number :"))
temperature(temp)
