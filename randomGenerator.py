__author__ = 'Ryan Lindberg'

import random
import mapGenerator as MG
class randomGenerator:


    alphabet = {0:0, 1:1, 2:2, 3:3, 4:4, 5:5, 6:6, 7:7, 8:8, 9:9, 10:'a', 11:'b', 12:'c',
                13:'d', 14:'e', 15:'f', 16:'g', 17:'h', 18:'i', 19:'j', 20:'k', 21:'l',
                22:'m', 23:'n', 24:'o', 25:'p', 26:'q', 27:'r', 28:'s', 29:'t', 30:'u',
                31:'v', 32:'w', 33:'x', 34:'y', 35:'z'}

    #Three separate seeds so peoples worlds seem the same if they put a random seed in
    #The seed they will see with be 24 characters, but in actuality will be three eight
    #digit seeds
    def __init__(self,seed = None):

        if seed == None or not(len(seed) == 24):
            seed = ""
            for i in range(0,24):
                temp = random.randint(0,36)
                seed = seed + str(self.alphabet[temp])
        self.RNGgen = random.Random()
        self.RNGgen.seed(seed[0:8])
        self.RNGreroll = random.Random()
        self.RNGreroll.seed(seed[8:16])
        self.RNGworld = random.Random()
        self.RNGworld.seed(seed[16:24])
        print(seed)

    def random_int(self):
        for i in range(1,10):
            print(self.RNGgen.randint(1,10))

    def roll_dice(self, numdice, dicetype):
        if numdice < 1:
            return 0
        else:
            die = []
            for i in range(0,numdice):
                die.append(self.RNGgen.randint(1,dicetype))
        return die, sum(die)

    def new_item(self, lvl, area, gen):
        return None

    # new_weapon and new_armour are probably going to end up in a new file.
    def new_weapon(self, lvl, area, gen):
        return None

    def new_armor(self, lvl, area, gen):
        return None

    def new_map(self, h=36, w=36, i=3):
        map = MG.Map(self.RNGworld, h, w, i)
        return map

    def new_monster(self, lvl, area, gen):
        return None

    def new_stage(self, lvl, area, gen):
        return none