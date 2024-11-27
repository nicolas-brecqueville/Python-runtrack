def drew_triangle(height):
    print(" "*(height+1), "/\\")
    for i in range(height):
        print(" "*(height-i), "/", " "*(i*2), "\\")
    print("", "/", "_"*(height*2), "\\")

height = int(input("Rentrez la hauteur de votre triangle : "))
drew_triangle(height)

        