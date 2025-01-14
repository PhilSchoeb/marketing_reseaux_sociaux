import math
import sys

# Set up pour l'ouverture du fichier à lire (à compléter)
#name = sys.argv[1]
name = "instance.txt"
file = open(name, 'r')
f = file.readlines()

# Initialisation
listeInfluenceurs = []
listePersonnesRestantes = []
k = 0 # k représente l'index de la ligne d'influenceur lue

# Lecture du document
for line in f:
    # Si c'est la première ligne
    if line[0] != 'i':
        nbInfluenceur = ''
        nbPersonne = ''
        i = 0
        while line[i] != ' ':
            nbInfluenceur += line[i]
            i += 1
        while line[i+1] != '\n' and line[i+1] != ' ':
            nbPersonne += line[i+1]
            i += 1
    # Si la ligne n'est pas la première
    else:
        listePersonnesRestantes.append([])
        influenceur = ''
        j = 0
        while line[j] != ' ':
            influenceur += line[j]
            j += 1
        listeInfluenceurs.append(influenceur)
        personne = ''
        j += 3
        while line[j] != '\n' and j+1 < len(line):
            if line[j] != ' ':
                personne += line[j]
                j += 1
            else:
                listePersonnesRestantes[k].append(personne)
                personne = '' # On reset le string pour la prochaine personne après
                j += 1
        if line[j] != '\n': # Seulement pour la dernière ligne
            personne += line[j]
        listePersonnesRestantes[k].append(personne)
        k += 1

# Formation d'une liste complète qui contient les influenceurs et leur audience
listeComplete = []
for i in range (len(listeInfluenceurs)):
    element = []
    element.append(listeInfluenceurs[i])
    element.append(listePersonnesRestantes[i])
    listeComplete.append(element)

# Fonction pour trier la liste complète en ordre décroissant d'audience avec le tri fusion
def triFusionLongueur(tab):
    # Cas de base
    if len(tab) == 1:
        return tab
    # Cas récursif
    tab1 = tab[0:math.floor(len(tab)/2)]
    tab2 = tab[math.floor(len(tab)/2):len(tab)]
    tabTri1 = triFusionLongueur(tab1)
    tabTri2 = triFusionLongueur(tab2)
    tabTri = []
    i = 0
    j = 0
    while i < len(tabTri1) or j < len(tabTri2):
        # Si tabTri1 a été vidé
        if i == len(tabTri1):
            tabTri.append(tabTri2[j])
            j += 1
        # Si tabTri2 a été vidé
        elif j == len(tabTri2):
            tabTri.append(tabTri1[i])
            i += 1
        # Comparaison de l'élément de tabTri1 à celui de tabTri2
        elif len(tabTri1[i][1]) > len(tabTri2[j][1]):
            tabTri.append(tabTri1[i])
            i += 1
        else:
            tabTri.append(tabTri2[j])
            j += 1
    return tabTri

# Fonction pour enlever un groupe de personnes (tabPersonnes) dans la liste complète (tabToUpdate)
def update(tabToUpdate, tabPersonnes):
    for element in tabToUpdate:
        i = 0
        while i < len(element[1]):
            personneCheck = element[1][i]
            for personneEnlever in tabPersonnes:
                if personneCheck == personneEnlever:
                    element[1].remove(personneCheck)
            if i < len(element[1]):
                if element[1][i] == personneCheck:
                    i += 1
    return tabToUpdate


# Algorithme vorace
listeTri = triFusionLongueur(listeComplete)
listeReponse = [] # Liste d'influenceurs sélectionnés

while len(listeTri[0][1]) > 0 and len(listeTri) > 0:
    influenceurPris = listeTri.pop(0) # Prendre l'influenceur avec la plus grande audience
    listeReponse.append(influenceurPris[0])
    listePersonnesPrises = influenceurPris[1]
    listeTri = update(listeTri, listePersonnesPrises) # Enlever les personnes atteintes de la liste complète
    listeTri = triFusionLongueur(listeTri) # Trier la liste après les modifications

# Création du texte contenu dans le document écrit
text = ""
for influen in listeReponse:
    text += influen + " "

# Set up pour l'écriture du document qui contient le résultat
nomFile = "resultat" + name
with open(nomFile, 'w') as file2:
    file2.write(text)