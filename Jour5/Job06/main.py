def calculDistance(nMarche, hMarche):
    distanceParJourEnCm = nMarche * hMarche * 5 * 2
    distanceParSemaineeEnCm = distanceParJourEnCm * 7
    distanceParSemaineeEnM = distanceParSemaineeEnCm / 100
    print(f"Pour {nMarche} marches de {hMarche} cm, le gardien parcourt {distanceParSemaineeEnM} m par semaine.")

nMarche = int(input("Nombre de marche : "))
hMarche = int(input("Hauteur des marches (en cm) : "))
calculDistance(nMarche, hMarche)