def pairs_triangle():
    user_num = int(input("Enter a size number : "))
    for left in range(user_num):
        for right in range(left , user_num):
            print("[" + str (left) + "|" + str(right) + "]", end=" ")
        print()

pairs_triangle()
        
            
        
    
