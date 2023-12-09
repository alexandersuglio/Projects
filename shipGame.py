import random

class game():

    def __init__(self):

        self.shipNames = [
            "HMS Victory", "HMS Royal Sovereign", "HMS Britannia", "HMS Bellerophon", "HMS Agamemnon",
            "HMS Elephant", "HMS Minotaur", "HMS Vanguard", "HMS Temeraire", "HMS Ajax", "HMS Dreadnought",
            "HMS Orion", "HMS Mars", "HMS Trafalgar", "HMS Nile", "HMS Foudroyant", "HMS Defiance", "HMS Thunderer",
            "HMS Conqueror", "HMS Monarch", "HMS Colossus", "HMS Revenge", "HMS Renown", "HMS Swiftsure",
            "HMS Caledonia", "HMS Leviathan", "HMS Victory", "HMS Ajax", "HMS St. Vincent"
        ]

        self.firstNames = [
            "Albert", "Arthur", "Charles", "Daniel", "Edward", "Frederick", "George", "Henry", "James", "John",
            "Joseph", "Nathaniel", "Oliver", "Reginald", "Robert", "Samuel", "Thomas", "Walter", "William", "Archibald",
            "Benjamin", "Caleb", "Clement", "David", "Edmund", "Elias", "Ezekiel", "Francis", "Gilbert", "Harold",
            "Hiram", "Horace", "Hugh", "Isaac", "Jonathan", "Julian", "Lawrence", "Leslie", "Lucas", "Michael", "Martin",
            "Francis", "Maxwell", "Merrill", "Morris", "Nathaniel", "Oscar", "Patrick", "Philip", "Ralph", "Reuben"
        ]

        self.lastNames = [
            "Chandler", "Cunningham", "Barker", "Tate", "Floyd", "Burton", "Ball", "Conway", "Harmon", "Meadows",
            "Maddox", "Giles", "Jacobs", "Strickland", "Kent", "Boone", "Glover", "David", "Smith", "Burgess",
            "Doyle", "Quinn", "Lyons", "Lucas", "Nicholson", "Mason", "Norton", "Curtis", "Ballard", "Welch", "Owen",
            "Ross", "Tate", "Lewis", "Little", "Abbott", "Cain", "Fox", "Morton", "Barrett", "Brewer", "Hammond",
            "Hopkins", "Forbes", "Johnson", "Cross", "Owen", "Harmon", "Horton", "Franklin"
        ]

        # ["Navigator"], ["Quartermaster"]
        self.crew = [["Captain"], ["Lieutenant"], ["Seaman"], ["Seaman"], ["Seaman"], ["Marine"], ["Marine"], ["Surgeon"]]

        self.newCrew = ["Seaman", "Marine"]

        self.ship = []

    def start(self):
        print(" Ahoy! Your ship is the", self.ship[0])
        print()
        print(" Crewed by:")

    def buildCrew(self):

        for i in range(len(self.crew)):
            first_name = random.choice(self.firstNames)
            last_name = random.choice(self.lastNames)
            self.crew[i].append([first_name, last_name])

        self.ship = [random.choice(self.shipNames)] + self.crew

        return self.ship

    def allHands(self):

        #print(" Ahoy! Your ship is the", self.ship[0])
        #print()
        #print(" Crewed by:")

        print()

        crew = self.ship[1:]
        crew.sort()

        for guy in crew:
            print("", guy[0],": ", guy[1][0], guy[1][1])

        print()

        #for i in self.ship:
        #   print(i, end='\n')

    def loseCrewMember(self):

        if len(self.ship) == 1:
            print("The whole crew is deceased! Your adventure is over!")
            return

        else:

            ceil = len(self.ship)
            # print("ceil now", ceil)

            pick = random.randrange(1, ceil)
            #print(pick)

            print("You've lost", self.ship[pick][0], self.ship[pick][1][0], self.ship[pick][1][1],"!")
            self.ship.pop(pick)

            ceil -= 1

            #if self.ship[pick][0] == "Captain":
            self.battleFieldPromotion()

    def gainCrewMember(self):

        pick = random.randrange(0, 2)
        newCrew = self.newCrew[pick]

        first_name = random.choice(self.firstNames)
        last_name = random.choice(self.lastNames)

        newAddition = [newCrew, [first_name, last_name]]
        print("Reinforcements arrived!", newAddition[0], newAddition[1][0], newAddition[1][1],"at your service!")
        self.ship.append(newAddition)

    def battleFieldPromotion(self):
        crew = self.ship[1:]
        crew.sort()

        if crew[0][0] != 'Captain':
           print("You don't have a captain!", crew[0][0], crew[0][1][0], crew[0][1][1],"has been promoted to Captain!")
           crew[0][0] = 'Captain'

        #if 'Captain' not in crew and 'Lieutenant' in crew:
        #    print("you don't have a capt but you have an lt")

        # for i in crew:
            # if 'Captain' not in crew:

                # print("no capt")
                # print("You don't have a captain!", crew[0][0], crew[0][1][0], crew[0][1][1], "has been promoted to Captain!")

        #print(crew[0][0] == 'Captain')
        #print(crew[1][0] == "Lieutenant")

    def event1(self):
        # options = ["losecrew", "gaincrew"]

        pick = random.randrange(0, 2)
        # print("pick", pick)

        if pick == 0:
            self.loseCrewMember()
        if pick == 1:
            self.gainCrewMember()

print()

game1 = game()
game1.buildCrew()
game1.start()

game1.allHands()

# print("--------------------------------------------")
# game1.loseCrewMember()
print("--------------------------------------------")
# game1.gainCrewMember()
# print("--------------------------------------------")

print()

game1.event1()

# game1.allHands()


'''
ruby = game1.ship[1:]

for i in ruby:
    print(i, end='\n')
    print('Seaman' in i)
    if 'Chef' not in i and "Captain" in i:
        print("works!")
'''
