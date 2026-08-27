#disk_check.py
#checks disk usage and decides if cleanup is needed
#בדיקת נפח דיסק קשיח

def check_disk(used_percent):
    if used_percent >= 90:
        return "CRITICAL - cleanup now"
    elif used_percent >= 75:
        return "WARNING - getting full"
    else:
        return "OK"

for i in range(5):
    server_name = input("Server name : ")
    used_percent = int(input("Disk used :"))

    status = check_disk(used_percent)
    print("Server:",server_name)
    print("Disk used:",used_percent)
    print("Status:",status)                    
    print()

    
