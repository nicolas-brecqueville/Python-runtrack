def testPass(eleve):
    for i in range(len(eleve)):
        if eleve[i][1] >= 40:
            print(f"L'élève {eleve[i][0] + 1} passe le test")
        else:
            print(f"L'élève {eleve[i][0] + 1} ne passe pas le test..")

def arrondirNote(list):
    eleve = []
    for i in range(len(list)):
        if list[i] % 5 >= 3:
            result = list[i] - (5 - list[i] % 5)
            eleve.append([i, result])
        else:
            eleve.append([i, list[i]])
    print(eleve)
    return eleve

list = [int(input("Rentrez la note du 1er élève : ")),
        int(input("Rentrez la note du 2e élève : ")),
        int(input("Rentrez la note du 3e élève : ")),
        int(input("Rentrez la note du 4e élève : ")),
        int(input("Rentrez la note du 5e élève : ")),
        int(input("Rentrez la note du 6e élève : "))]



testPass(arrondirNote(list))

