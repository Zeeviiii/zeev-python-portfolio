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
