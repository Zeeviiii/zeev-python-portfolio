def list_toole():
    list_name = []
    while True:
        name = input(" הכניס שם :")
        if name == "stop" or name == "די":
            break
        list_name.append(name)
    print(list_name)

list_toole()
