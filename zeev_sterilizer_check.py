def sterilizer_check():
    user_num = int(input("Enter a Machine number :"))
    bad_count = 0
    ok_count = 0
    for i in range(1, user_num + 1):
        temp = int(input("Enter a Temperature :"))
        if 134 >= temp and temp >=121 :
            ok_count +=1
        else:
            bad_count +=1 
    print(f"ok: {ok_count}")
    print(f"not ok : {bad_count}")
                   
sterilizer_check()
