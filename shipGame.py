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

        self.crew = [["Captain"], ["Lieutenant"], ["Seaman"], ["Seaman"], ["Seaman"], ["Marine"], ["Marine"], ["Surgeon"]]

        self.newCrew = [["Seaman"], ["Marine"]]

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


            print("you lost", self.ship[pick][0], self.ship[pick][1][0], self.ship[pick][1][1],"!")
            self.ship.pop(pick)

            ceil -= 1


    def gainCrewMember(self):

        pick = random.randrange(0, 2)

        newCrew = self.newCrew[pick]

        first_name = random.choice(self.firstNames)
        last_name = random.choice(self.lastNames)
        # self.crew.append([first_name, last_name])

        #self.ship = [random.choice(self.shipNames)] + self.crew
        newAddition = [newCrew, [first_name, last_name]]
        print("got new ", newAddition)

        self.ship.append(newAddition)






print()


game1 = game()
game1.buildCrew()
game1.start()

game1.allHands()

game1.loseCrewMember()
game1.loseCrewMember()
game1.loseCrewMember()
game1.loseCrewMember()
game1.loseCrewMember()
game1.loseCrewMember()
game1.loseCrewMember()
game1.loseCrewMember()
game1.loseCrewMember()

#print(len(game1.ship))
#game1.loseCrewMember()
# print("****")

print("\nall you have left is: ")
game1.allHands()

# print(len(game1.ship))


print()

# game1.allHands()


# ruby = game1.ship
# for i in ruby:
#     print(i, end="\n")
game1.gainCrewMember()
