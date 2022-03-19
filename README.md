# **autoMOTUS**
### *(Bot that helps finding the correct word in the french game : MOTUS)*

---

### Bienvenu sur Auto MOTUS !
Vous pouvez revisionner cette aide en tapant :
```sh
python3 motus.py --help
```
Comment faire fonctionner le bot :  
Ecrivez le mot que vous avez tapé, en écrivant les lettres en fonction de leur résultat :
- **A** *(majuscule)* : Lettre bien placée.
- **a** *(minuscule)* : Lettre mal placée.
- **\a** *(précédée par un \\)* : Mauvaise lettre.

Vous pouvez spécifier plusieurs lignes de la grille, en les séparant par un espace.  

Si vous ne savez pas par quoi commencer, vous pouvez spécifier la lettre de début puis le nombre de lettres *(**m5** par exemple)*, le bot vous indiquera alors toutes les possibilités.

---

**Exemples :**  
```sh
python3 motus.py m5
```
`-> motus, ...`
```sh
python3 motus.py M\a\i\nS MOT\oS
```
`-> motus`

---

Nous n'avons pas tous les mots malheureusement, mais une liste de **336 531** mots.  
Si vous souhaitez ajouter de nouveaux mots, vous pouvez éditer le fichier fr-wordlist.json et faire une PR, merci !  
De plus, **l'algorithme n'est pas tout à fait complet**, il manque quelques subtilités, donc faites attention !