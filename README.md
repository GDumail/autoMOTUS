# **autoMOTUS**
### *(Bot that helps finding the correct word in the french game : MOTUS)*

---

### Bienvenu sur Auto MOTUS !
Vous pouvez revisionner cette aide en tapant :
```sh
python3 motus.py --help
```
Voici comment faire fonctionner ce bot :
- **A** *(majuscule)* : Lettre bien placée.
- **a** *(minuscule)* : Lettre mal placée.
- **\a** *(précédée par un \\)* : Mauvaise lettre.

Vous pouvez spécifier plusieurs lignes de la grille.  
**Exemple :**  
```sh
python3 motus.py M\a\i\nS MOT\oS
```
`-> motus`

Nous n'avons pas tous les mots malheureusement, mais une liste de **336 531** mots.  
Si vous souhaitez ajouter de nouveaux mots, vous pouvez éditer le fichier fr-wordlist.json et faire une PR, merci !  
De plus, **l'algorithme n'est pas tout à fait complet**, il manque quelques subtilités, donc faites attention !