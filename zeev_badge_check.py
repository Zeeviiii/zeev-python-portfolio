def id_name ():
    badge = input("Please enter a your badge: ") 
    print(badge[3:5])
    worker_id = badge[5:]
    print(worker_id)
    if badge[:3]== "SHR":
        print("Access granted - Shaarei Tzedek")
    else:
        print("Access denied")

id_name ()
