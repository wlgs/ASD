def babiarz(G, T, W):
    # pokoje w kolejnosci malejacej

    # na zmiane kolor wlosow


    pass


G1 = [[(1, 1), (2, 5), (3, 11), (4, 3)],
      [(0, 1), (3, 3), (5, 1), (6, 1)],
      [(0, 5), (3, 3), (5, 42)],
      [(2, 3), (1, 1), (0, 11)],
      [(0, 3)],
      [(2, 42), (1, 1)],
      [(1, 1)]]
T1 = ["Łysy", "Brun", "Brun", "Blond", "Blond", "Blond", "Blond"]
W1 = 47
odp1 = [0, 3, 2]

G2 = [[(11, 21), (8, 15), (1, 1), (2, 5), (3, 11), (4, 3)],
      [(0, 1), (3, 3), (5, 1), (6, 1)],
      [(0, 5), (3, 3), (5, 42)],
      [(2, 3), (1, 1), (0, 11)],
      [(0, 3)],
      [(2, 42), (1, 1)],
      [(1, 1)],
      [(4, 1), (8, 10), (5, 5)],
      [(0, 15), (7, 10)],
      [],
      [],
      [(0, 21), (7, 37)]]
T2 = ["Łysy", "Brun", "Blond", "Brun", "Blond", "Blond", "Brun", "Blond", "Blond", "Brun", "Brun", "Blond"]
W2 = 63
odp2 = [0, 11, 7, 5]

print(babiarz(G1, T1, W1) == odp1)
print(babiarz(G2, T2, W2) == odp2)
