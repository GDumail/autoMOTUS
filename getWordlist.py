import json

words = []

with open("frgut.txt", "r") as file:
  for line in file:
    stripped_line = line.strip()
    words.append(stripped_line.lower()
        .replace('é', 'e')
        .replace('è', 'e')
        .replace('ù', 'u')
        .replace('ê', 'e')
        .replace('ô', 'o')
        .replace('û', 'u')
        .replace('à', 'a')
        .replace('ï', 'i')
        .replace('ö', 'o')
        .replace('ë', 'e')
        .replace('â', 'a')
    )

wordlist = {}
for i in range(1, 26):
    wordlist[str(i)] = []
for word in words:
    wordlist[str(len(word))].append(word)

with open('fr-wordlist.json'.format(1), 'w', encoding='utf-8') as file:
    json.dump(wordlist, file, ensure_ascii=False)