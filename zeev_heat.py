def temperature(machine,heat):
    if machine <=4 and machine >=1 and heat <= 135 and heat >= 90 :
       result = "Machine ready!"
    elif machine >= 1 and machine <=4:
       result = "Check temperature!"
    elif heat >= 90 and heat <= 135 :
       result = "Check Machinte number!"
    else :
       result = "DANGER - Stop everything !!!"
    return result   
     
machine = int(input(" enter number machine : "))
heat = int(input(" enter heat number :"))
print (temperature(machine, heat )) 
