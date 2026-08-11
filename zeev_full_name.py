def full_name():
    first = input("first name: ").strip()
    last = input("last name: ").strip()
    full = first + " " + last
    print(f"hello, {full}!")
    print(f"Your name has {len(full)} characters")


full_name()    
