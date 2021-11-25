from module1 import*
user=loe_failist_listinsse("users.txt")
password=loe_failist_listisse("password.txt")

While True:
    print("Näita kõike-0,Reg-1,Avt-2,välja-3")
    v=int(input())
    if v==0:
        koik_kasutajad(users.password)
    elif v==1:
        print("Registreerimine")
        while 1:
            log=input("Kasutajatunnus")
            if log not in users:
                print("Tunnus soobib")
            else:
                print("See nimi joba on olemas")