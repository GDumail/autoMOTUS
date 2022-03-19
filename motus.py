import sys
import json

def init(wordlist):
    allPossibilities = []
    if len(sys.argv[1]) == 2 and sys.argv[1][1].isdigit():
        for word in wordlist[sys.argv[1][1]]:
            if word.startswith(sys.argv[1][0]):
                allPossibilities.append(word)
        print(allPossibilities)
        exit()

if len(sys.argv) < 2 or sys.argv[1] == "--help":
    print("Bienvenu sur Auto MOTUS !")
    print("Vous pouvez revisionner cette aide en tapant : 'python3 motus.py --help'")
    print("Comment faire fonctionner le bot :")
    print("Ecrivez le mot que vous avez tapé, en écrivant les lettres en fonction de leur résultat :")
    print("- A (majuscule) : Lettre bien placée.")
    print("- a (minuscule) : Lettre mal placée.")
    print("- \\a (précédée par un \\) : Mauvaise lettre.")
    print()
    print("Vous pouvez spécifier plusieurs lignes de la grille, en les séparant par un espace.")
    print()
    print("Si vous ne savez pas par quoi commencer, vous pouvez spécifier la lettre de début puis le nombre de lettres (m5 par exemple), le bot vous indiquera alors toutes les possibilités.")
    print()
    print("Exemples :")
    print("    python3 motus.py m5")
    print("    -> motus, ...")
    print("    python3 motus.py M\\a\\i\\nS MOT\\oS")
    print("    -> motus")
    print()
    print("Nous n'avons pas tous les mots malheureusement, mais une liste de 336531 mots.")
    print("Si vous souhaitez ajouter de nouveaux mots, vous pouvez éditer le fichier fr-wordlist.json et faire une PR, merci !")
    print("De plus, l'algorithme n'est pas tout à fait complet, il manque quelques subtilités, donc faites attention !")
    exit()

with open('fr-wordlist.json') as file:
    wordlist = json.load(file)
    init(wordlist)
    length = 0
    for c in sys.argv[1]:
        if c != '\\':
            length += 1
    allPossibilities = []
    for j in range(1, len(sys.argv)):
        clues = sys.argv[j]
        known = {}
        unsure = []
        avoid = []
        knownArray = []
        avoidDict = {} # TODO
        index = 0
        for i in range(0, len(clues)):
            if clues[i] == '\\':
                continue
            if i > 0 and clues[i - 1] == '\\':
                if clues[i] not in avoid:
                    avoid.append(clues[i])
                avoidDict[index] = clues[i] # TODO
            else:
                if clues[i].isupper():
                    known[index] = clues[i].lower()
                    if clues[i].lower() not in knownArray:
                        knownArray.append(clues[i].lower())
                else:
                    unsure.append(clues[i])
                    avoidDict[index] = clues[i] # TODO
            index += 1
        possibilities = []
        for word in wordlist[str(length)]:
            found = True
            for knownLetter in known:
                if word[knownLetter] != known[knownLetter]:
                    found = False
            for avoidLetter in avoidDict: # TODO
                if word[avoidLetter] == avoidDict[avoidLetter]: # TODO
                    found = False # TODO
            for avoidLetter in avoid:
                if avoidLetter in word and avoidLetter not in unsure and avoidLetter not in knownArray:
                    found = False
            for unsureLetter in unsure:
                if unsureLetter not in word:
                    found = False
            if found == True:
                possibilities.append(word)
        if len(allPossibilities) == 0:
            allPossibilities = possibilities
        else:
            allPossibilities = list(set(allPossibilities) & set(possibilities))

    print(allPossibilities)