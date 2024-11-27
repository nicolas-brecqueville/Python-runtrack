def drew_rectangle(width, height):
    for nbLigne in range(height):
        if nbLigne == 0 or nbLigne == (height-1):
            print("|", "-"*width, "|")
        else:
            print("|", " "*width, "|")

width = int(input("Rentrez la largeur du rectangle : "))
height = int(input("Rentrez la hauteur du rectangle : "))

drew_rectangle(width, height)
