from lib.wumpus2 import WumpusWorld


def suiv(dico, string):
    l1 = []
    for i in ([-1, 1]):
        w = chr(ord(string[:1]) + i) + string[1:]
        b = string[:1] + chr(ord(string[1:]) + i)
        l1.append(w) if w in dico else l1
        l1.append(b) if b in dico else l1
    return l1


def convert(string):
    return ord(string[:1]) - ord('A'), ord(string[1:]) - ord('1')


total = 0
for p in range(100000):
    ww = WumpusWorld()
    taille_jeu = ww.get_n()
    dico_zone = {chr(i + ord('A')) + chr(j + ord('1')) for i in range(taille_jeu) for j in range(taille_jeu)}
    ma_dimension = {chr(i + ord('A')) + chr(j + ord('1')): [0.0, 0.0, "Original", "Original"] if j == 0 and i == 0 else [0.25, 1/16, "Original", "Original"] for i in range(taille_jeu) for j in range(taille_jeu)}
    wumpus_catch = False

    while len(ma_dimension) > 0:
        ma_dimension = dict(sorted(ma_dimension.items(), key=lambda x: max(x[1][0], x[1][1])))

        zone = list(ma_dimension.keys())[0]
        if ma_dimension[zone][0] == 0.0 and ma_dimension[zone][1] == 0.0:
            if ma_dimension[zone][2] == "Original" and ma_dimension[zone][3] == "Original":
                type_zone = (ww.get_percepts())[2]
            else:
                type_zone = (ww.probe(convert(zone)[0], convert(zone)[1]))[1]
        else:
            zone = list(ma_dimension.keys())[len(ma_dimension)-1]
            type_zone = (ww.cautious_probe(convert(zone)[0], convert(zone)[1]))[1]

        if 'B' in type_zone:
            for i in suiv(ma_dimension, zone):
                if ma_dimension[i][2] == "Original":
                    ma_dimension[i][0] = 1.0/len(suiv(dico_zone, i))
                    ma_dimension[i][2] = "Modifié"
                else:
                    ma_dimension[i][0] = ma_dimension[i][0] + (1.0 / len(suiv(dico_zone, i)))
        if 'S' in type_zone:
            if not wumpus_catch:
                for i in suiv(ma_dimension, zone):
                    if ma_dimension[i][3] == "Original":
                        ma_dimension[i][1] = 1.0/len(suiv(dico_zone, i))
                        ma_dimension[i][3] = "Modifié"
                    else:
                        ma_dimension[i][1] = ma_dimension[i][1] + (1.0 / len(suiv(dico_zone, i)))
        if 'W' in type_zone:
            for i in ma_dimension:
                ma_dimension[i][1] = 0.0
                ma_dimension[i][3] = "Modifié"
            wumpus_catch = True
        del ma_dimension[zone]

        for i in suiv(ma_dimension, zone):
            if ma_dimension[i][0] != 0.0:
                if ma_dimension[i][2] == "Original":
                    if ma_dimension[i][0] - 0.25 + len((suiv(ma_dimension, i))) * 1 / len(suiv(dico_zone, i)) < 1:
                        ma_dimension[i][0] = 0.0
                        ma_dimension[i][2] = "Modifié"
                else:
                    if ma_dimension[i][0] + len((suiv(ma_dimension, i))) * 1 / len(suiv(dico_zone, i)) < 1:
                        ma_dimension[i][0] = 0.0

            if ma_dimension[i][1] != 0.0:
                if ma_dimension[i][3] == "Original":
                    if ma_dimension[i][1] - (1 / 16) + len((suiv(ma_dimension, i))) * 1 / len(suiv(dico_zone, i)) < 1:
                        ma_dimension[i][1] = 0.0
                        ma_dimension[i][3] = "Modifié"
                else:
                    if ma_dimension[i][1] + len((suiv(ma_dimension, i))) * 1 / len(suiv(dico_zone, i)) < 1:
                        ma_dimension[i][1] = 0.0

    #print(ww.get_cost())
    #print(ww.get_knowledge())
    total = ww.get_cost() + total
    print(total/(p+1))

