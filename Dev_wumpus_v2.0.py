from lib.wumpus2 import WumpusWorld
from lib.gopherpysat import Gophersat
gophersat_exec = "C:/Users/orion/TestNotCloud/PRJ/lib/cmd/gophersat-1.1.6.exe"


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


def init_jeu_sat(taille):
    etat_0 = ['S', 'B', 'G', 'R']
    etat = ['W', 'S', 'P', 'B', 'G', 'R']
    ma_dimension = {}
    for i in range(taille):
        for j in range(taille):
            name = chr(i + ord('A')) + chr(j + ord('1'))
            if j != 0 and i != 0:
                ma_dimension[name] = {name + "_" + e for e in etat_0}
            else:
                ma_dimension[name] = {name + "_" + e for e in etat}
    return ma_dimension


def init_jeu_prob(taille):
    ma_dimension = {}
    for i in range(taille):
        for j in range(taille):
            name = chr(i + ord('A')) + chr(j + ord('1'))
            if j != 0 and i != 0:
                ma_dimension[name] = [-1.0, -1.0]
            else:
                ma_dimension[name] = [0.0, 0.0]
    return ma_dimension


def closes_puits(zone_):
    closes_p = []
    for i in zone_:
        close_p = [i + "_P"]
        for j in suiv(zone_, i):
            close_p.append('-' + j + "_B")
        closes_p.append(close_p)
        del close_p
    return closes_p


def closes_wumpus(zone_):
    closes_w = []
    for i in zone_:
        close_w = [i + "_W"]
        for j in suiv(zone_, i):
            close_w.append('-' + j + "_S")
        closes_w.append(close_w)
        del close_w
    return closes_w


def solve(closes):
    gs = Gophersat(gophersat_exec, dico_zone)
    for i in closes:
        gs.push_pretty_clause(i)
    return gs.get_pretty_model()


ww = WumpusWorld()
taille_jeu = ww.get_n()

dimension_sat = init_jeu_sat(taille_jeu)
dimension_prob = init_jeu_prob(taille_jeu)

closes_puits = closes_puits(dimension_sat)
closes_wumpus = closes_wumpus(dimension_sat)

voc = ["A", "B", "C"]

gs = Gophersat(gophersat_exec, voc)
gs.push_pretty_clause(["B", "A"])
gs.push_pretty_clause(["-B"])
print(gs.dimacs())
print(gs.solve())
print(gs.get_pretty_model())
print(gs.get_model())


wumpus_catch = False


