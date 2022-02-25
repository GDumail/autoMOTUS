import requests
import json

words = []
start = 1
for i in range(0, 5):
    url = "https://en.wiktionary.org/wiki/Wiktionary:French_frequency_lists/{}-{}".format(start, start + 1999)
    read = None
    response = requests.get(url=url)
    if response.ok:
        while True:
            try:
                if read == None:
                    read = response.text[response.text.index('<span class="Latn" lang="fr"><a href="') + 38:len(response.text)]
                else:
                    read = read[read.index('<span class="Latn" lang="fr"><a href="') + 38:len(read)]
                word = read[read.index('>') + 1:read.index('<')]
                if "'" in word:
                    continue
                words.append(word.lower()
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
                )
            except Exception as e:
                break
        start += 2000
    else:
        break
wordlist = {}
for i in range(1, 27):
    wordlist[str(i)] = []
for word in words:
    wordlist[str(len(word))].append(word)

with open('fr-wordlist.json'.format(1), 'w', encoding='utf-8') as file:
    json.dump(wordlist, file, ensure_ascii=False)