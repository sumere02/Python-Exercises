class animals():
    def __init__(self,nutrition,breathing,excretion,reproductive):
        self.nutrition = nutrition
        self.breathing = breathing
        self.excretion = excretion
        self.reproductive = reproductive
    def __del__(self):
        print("Animal deleted from database")
    def __str__(self):
        print("Nutrition: {}\nBreathing: {}\nExcretion: {}\nReproductive: {}\n".format(self.nutrition,self.breathing,self.excretion,self.reproductive))
class dogs(animals):
    def __init__(self, nutrition, breathing, excretion, reproductive,name,weight,height,type):
        super().__init__(nutrition, breathing, excretion, reproductive)
        self.name = name
        self.weight = weight
        self.height = height
        self.type = type
    def __del__(self):
        print("Dog deleted from database")
    def __str__(self):
        super().__str__()
        print("Name: {}\Weight: {}\nHeight: {}\nType: {}\n".format(self.name,self.weight,self.height,self.type))
class birds(animals):
    def __init__(self,nutrition,breathing,excretion,reproductive,name,weight,height,type):
        super().__init__(nutrition,breathing,excretion,reproductive)
        self.name = name
        self.weight = weight
        self.height = height
        self.type = type
    def __del__(self):
        super().__del__()
    def __str__(self):
        super().__str__()
        print("Name: {}\Weight: {}\nHeight: {}\nType: {}\n".format(self.name,self.weight,self.height,self.type))
class horses(animals):
    def __init__(self, nutrition, breathing, excretion, reproductive,name,weight,height,type):
        super().__init__(nutrition, breathing, excretion, reproductive)
        self.name = name
        self.weight= weight
        self.height = height
        self.type = type
    def __del__(self):
        super().__del__()
    def __str__(self):
        super().__str__()
        print("Name: {}\Weight: {}\nHeight: {}\nType: {}\n".format(self.name,self.weight,self.height,self.type)) 
        
horse = horses("grass","Oxygen","Urea","Double","Poyraz","86","1.80","White")
dog = dogs("Meat","Oxygen","Urea","Double","Firfir","35","55","Golden")
bird = birds("Worm","Oxygen","Urea","Solo","Kelek","10","14","Parrot")
horse.__str__()
dog.__str__()
bird.__str__()
