def birth_kits ():
    """ תוכנית להתאמת מחלקות לקומות בבית החולים שערי צדק """
    hospital = 0
    while hospital < 10:
        department = input("הכנס שם מחלקה :")
        floor = int(input(" הכנס מספר קומה :"))
        if department == "יולדת" and floor == 9 :
                    print(" הקומה נכונה ")
        elif department == "חדר ניתוח" and floor == 2 :
                    print(" הקומה נכונה ")       
        elif department == "מרפאה חוץ" and floor == 4 :
                    print(" הקומה נכונה ")  
        elif department == "מחלקת ילדים" and floor == 7 :
                    print(" הקומה נכונה ")
        elif department == "פנימית" and floor == 8 :
                    print(" הקומה נכונה ")   
        elif department == "אורטופדיה" and floor == 5 :
                    print(" הקומה נכונה ") 
        elif department == "אף אוזן וגרון" or department == "הנדסה רפואית" and floor == 3 :
                    print(" הקומה נכונה ") 
        elif department == "מחלקת לב" and floor == 10 :
                    print(" הקומה נכונה ") 
        elif department == "אספקה סטרלית" or department == "מטבח" and floor == 1 :
                    print(" הקומה נכונה ")
        elif department == "כירוגיה כללית" and floor == 6 :
                    print(" הקומה נכונה ")
        elif department == " חנויות " or department == "יציאה" and floor == 4:
                    print(" הקומה נכונה ")
        else:
                    print ("הקומה שגויה!!")

        hospital += 1            

birth_kits ()
