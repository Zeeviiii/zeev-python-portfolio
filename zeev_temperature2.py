def temperature():
    name = "CPU-1"
    temp = 67.5
    name_1 = "CPU-2"
    temp_1 = 8.20
    name_2 = "CPU-3"
    temp_2 = 102.75
    print("{:>5}: {:.2f}".format(name,temp))
    print("{:>5}: {:.2f}".format(name_1,temp_1))
    print("{:>5}: {:.2f}".format(name_2,temp_2))


temperature()
