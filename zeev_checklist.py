# Check the temperature of an autoclave (sterilization machine) with this one to see if it's ready to use or not!
# בודק טפרטורה של אוטוקלב (מכונה לעיקור) עם זה מוכן לשימוש או לא !
def checklist ():
    machine = 1
    while machine <= 4:
        temp = int(input(f"enter temperature for machine {machine}:"))
        if temp >= 130:
            print (f"Machine {machine} is ready!")
        else:
             print (f"Machine {machine} NOT ready ,only {temp}c!")

        machine += 1

checklist ()
