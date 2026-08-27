# Checks the employee number and if the initials of a business appear, there is approval.
# בודק את מספר עובד ועם מופיע ש אותיות ראשונות של בית עסק יש אישור 
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
