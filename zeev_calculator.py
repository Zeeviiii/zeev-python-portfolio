def calculator():
    while True:
        number_1 = int(input(" Enter a first number :"))
        operand = input("Operation(+, - , *, /, **, //, %, or 0 to exit : ")
        if operand == "0":
            print("Goodbye!!")
            break
        number_2 = int(input(" Enter a Second number :"))
        if operand == "+":
            result = number_1 + number_2
        elif  operand == "-":
            result = number_1 - number_2
        elif  operand == "*":
            result = number_1 * number_2
        elif  operand == "/":    
            result = number_1 / number_2
        elif  operand == "**":    
            result = number_1 ** number_2 
        elif  operand == "//":    
            result = number_1 // number_2 
        elif  operand == "%":    
            result = number_1 % number_2
        else:
            print("Invalid operation")
            continue 
        print(f"The result is:{result}")
    
calculator()      
              
