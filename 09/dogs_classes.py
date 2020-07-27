class Dogs:
    def __init__(self, name, ears):
        self.name = name
        self.ears = ears
        if ears != 2: #uz pri pocatecnim argumentu chci vyselektovat jenom psy
            raise ValueError ("It can´t be a dog, dog has 2 ears!")
        else:
            print("{} is a dog!".format(name))
    def woof (self):
        print ("Woof!")
    

class Cockerspaniel(Dogs):
    def hunt (self, prey):
        print ("{} hunts {}!".format(self.name, prey))

class Terriers(Dogs):
     def bullterrier(self):
         nose = input ("Is the {}´s nose long or short?".format(self.name))
         if nose == "long":
           print ("It´s a bully!")
           return True
         else:
             print ("It has to be another breed!")
     def foxterrier(self):
         fur = input ("Is the {}´s fur tough?".format(self.name))
         if fur == "yes":
             return True
         else:
             print ("Try another feature!")
     def number_of_bullteriers(self):
         number = 0
         if self.bullterrier() == True: #i v teto fci se mi spousti vysledek z fce bullterier a to uplne nechcu
             number += 1
             print ("Number of bullterriers:", number)
         else:
            print ("No bully here!")
         return number

class Mixed(Terriers, Cockerspaniel):
    def meeting (self): 
        if self.number_of_bullteriers > 1: 
            print (self.hunt("ducks.")," ","Bullies are just watching")
        elif self.number_of_bullteriers == 1:
            print (self.hunt("birds.")," ", "Bully is sad and alone!")
        else:
            return self.hunt("pigeons")
            print ("There are just cockers.")

     
ben = Terriers("Ben", 2)
azor = Mixed("Azor", 2)
ben.woof()
ben.number_of_bullteriers()
azor.meeting()

