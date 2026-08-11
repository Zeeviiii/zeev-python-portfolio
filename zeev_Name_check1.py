def Name_check():
    name = input("Enter a name : ")
    biggest_letter = name[0]

    for letter in name:
        if ord(letter)> ord(biggest_letter):
         biggest_letter = letter
    print(f"The biggest letter is: {biggest_letter}")

Name_check()    
    
