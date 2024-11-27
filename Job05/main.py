def chiffrer(msg):
    for i in msg:
        transform = ord(i)
        if 65 <= transform <= 90 or 97 <= transform <= 122:
            print(chr(ord(i) + 3))
        else:
            print(i)

msg = input("Rentrez votre msg : ")
chiffrer(msg)