__author__ = 'Ryan Lindberg'


class Map:
    weighted_land = [('w', 53), ('d', 25), ('f', 25), ('j', 25), ('p', 34), ('m', 28), ('t', 25)]
    land_pop = [val for val, cnt in weighted_land for i in range(cnt)]


    def __init__(self, gen, W = 36, H = 36, I = 3):
        self.map = [[gen.choice(self.land_pop) for j in range(H)] for i in range(W)]
        for temp in range(I):
            randi = list(range(W))
            gen.shuffle(randi)
            randj = list(range(H))
            gen.shuffle(randj)
            for i in randi:
                for j in randj:
                    count = {}
                    for k in [0, -1, 1]:
                        for l in [0, -1, 1]:
                            key = self.map[i+k if i+k < len(self.map) else 0][j+l if j+l < len(self.map[i]) else 0]
                            if key in count:
                                count[key] = count[key] + 1
                            else:
                                count[key] = 1
                    maxkey = max(count.keys(), key=(lambda key: count[key]))
                    try:
                        maxkeys = [key for key, val in count if val == count[maxkey]]
                        if not(self.map[i][j] in maxkeys):
                            self.map[i][j] = gen.choice(maxkeys)
                    except:
                        self.map[i][j] = maxkey

    def __str__(self):
        retStr = ""
        for i in self.map:
            for j in i:
                retStr = retStr + str(j) + " "
            retStr = retStr + "\n"
        return retStr