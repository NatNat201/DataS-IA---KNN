##KNN

from math import *

def lire_fichier():
    liste=[]

    fichier = open(r'C:\Users\natal\OneDrive\Bureau\DataS & IA\KNN\preTest.csv')

    for line in fichier :
        #print(line)
        ligne=line.rstrip('\n').split(";")
        liste.append(ligne)

    fichier.close()
    return liste

# l=lire_fichier()
# print(l)


def coordonnees():
    fichier=lire_fichier()
    coordonnees=[]

    #on récupère les coordonnées
    for ligne in range (len(fichier)):
        ajout=[]
        for i in range (0,4):
            ajout.append(float(fichier[ligne][i]))
        ajout.append(fichier[ligne][4])
        coordonnees.append(ajout)

    return coordonnees


#donnees=coordonnees()
#print(donnees[0])

def distance_euclidienne(ligne1,ligne2):
    distance= float(0)
    if ligne1==ligne2:
        return float(100000)

    else:
        for i in range (0,4):
            distance = distance + float((ligne1[i]-ligne2[i])**2)
        distance=sqrt(distance)
        #print("distance",distance)
        return distance



def plus_proches_voisins(donnees,ligne,k):
    distances_ligne = []

    # on compare le point de la ligne à tous les autres en calculant leur distance euclidienne
    for row in range (len(donnees)):
        #print(donnees[row])
        dist=distance_euclidienne(donnees[row],ligne)
        #print(dist)
        distances_ligne.append([dist,row])

    #on trie les distances
    #print("avant tri",distances_ligne)
    distances_ligne=sorted(distances_ligne, key=lambda distances_ligne : distances_ligne[0])
    #print("après tri",distances_ligne)

    #on retient les k premières distances (les plus courtes)
    retenus=[]
    for i in range (k):
        retenus.append(distances_ligne[i])
        #print("retenu",retenus)

    retour=[]
    for i in range (k):
        retour.append(donnees[retenus[i][1]])

    return retour



def prediction_classification(dataset,ligne,k):
    voisins = plus_proches_voisins(dataset, ligne, k)
    #print("voisins",voisins)
    #print(voisins)

    #on récupère le nombre de fois que chaque classes
    values = [row[-1] for row in voisins]
    #print("valeurs",values)

    #on récupère celle qui apparaît le plus souvent
    prediction = max(set(values), key=values.count)
    return prediction



def test():
    count=0

    coor=coordonnees()
    res=[]

    #pour chaque ligne, on regarde la valeur que prévoit le programme
    for row in range (len(coor)):
        prediction=prediction_classification(coor,coor[row],3)
        #print(prediction)
        res.append(prediction)

    #on compare la prédiction à la vraie valeur
    for i in range (len(coor)):
        #print(coor[i][-1]," et ",res[i])
        if coor[i][-1]==res[i]:
            count += 1

    total = count/len(coor)*100
    print(total)
    return total

#le test retourne 85.8333333% de bonnes prédictions





def lire_fichier_final():
    liste=[]

    fichier = open(r'C:\Users\natal\OneDrive\Bureau\DataS & IA\KNN\finalTest.csv')

    for line in fichier :
        #print(line)
        ligne=line.rstrip('\n').split(";")
        liste.append(ligne)

    fichier.close()
    return liste

#print(lire_fichier_final())


def coordonnees_final():
    fichier=lire_fichier_final()
    coordonnees=[]

    #on récupère les coordonnées
    for ligne in range (len(fichier)):
        ajout=[]
        for i in range (0,4):
            ajout.append(float(fichier[ligne][i]))
        coordonnees.append(ajout)

    return coordonnees





def final():
    coor=coordonnees()
    res=[]

    dataset_final=coordonnees_final()
    for i in range (len(dataset_final)):
        prediction=prediction_classification(coor,dataset_final[i],3)
        res.append(prediction)

    fichier = open("C:\\Users\\natal\\OneDrive\\Bureau\\DataS & IA\\KNN\\res3.txt",'a')

    for i in range (len(res)):
        fichier.write(res[i])
        fichier.write("\n")

    fichier.close()

final()

