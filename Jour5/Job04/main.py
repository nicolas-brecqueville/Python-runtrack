def drew_tapis(n):
    print("+" + "-"*(n+1) + "+")
    for i in range(n+1):
        print("|" + "#"*(n-i) + " " + "#"*i + "|")
    print("+" + "-"*(n+1) + "+")

n = int(input("Rentrez la hauteur du tapis : "))
drew_tapis(n) 