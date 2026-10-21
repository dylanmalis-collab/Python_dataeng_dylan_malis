import collections
def somme_cumulee(liste):
    resultat =[]
    total = 0
    for i in liste:
        total += i
        resultat.append(total)
    return resultat
def compter_occurrences(liste):
    return collections.Counter(liste)
def inverser_dict(dictionnaire):
    return {v:k for k, v in dictionnaire.items()}
def filtrer_pairs(liste):
    resultat = []
    for i in liste:
        if i % 2 == 0:
            resultat.append(i)
    return resultat
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32
def trouver_doublons(liste):
    resultat = set()
    vus = set()
    for i in liste:
        if i in liste and vus not in resultat:
            resultat.add(i)
        else:
            vus.add(i)
    return list(resultat)
def calculer_moyenne_ponderee(valeurs, poids):
    somme_ponderee = 0
    somme_poids = 0
    for v, p in zip(valeurs, poids):
        somme_ponderee += v * p
        somme_poids += p
    return somme_ponderee / somme_poids

 