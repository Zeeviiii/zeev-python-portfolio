#Checks the temperature of the refrigerator.
fridges = {"pharmacy_a":4.2, "lab_b":9.5, "er_storage":3.8}
for name, temp in fridges.items():
    if  temp < 8:
      print(name, temp,"-- ok")
    else:
      print(name, temp,"ALERT: too warm ")
