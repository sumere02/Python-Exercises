from random import randint
import time
import sys

class computer():
    def __init__(self,brand = "None",ram = "Empty",processor = "Empty",graphic_card = "Empty",os = "FreeDos",programs = [],power = "Off",sound = 0,program = "None"):
        self.brand = brand
        self.ram = ram
        self.processor = processor
        self.graphic_card = graphic_card
        self.os = os
        self.programs = programs
        self.power = power
        self.sound = sound
        self.program = program
    def __len__(self):
        print("{} Program Installed".format(len(self.programs)))
    def __str__(self):
        print("Brand: {}\nRAM: {}\nProcessor: {}\nGraphic Card: {}\nOS: {}\nPrograms: {}\nPower: {}\nVolume: {}\nProgram Number: {}\nProgram: {}\n".format(self.brand,self.ram,self.processor,self.graphic_card,self.os,self.programs,self.power,self.sound,len(self.programs),self.program))
    def __del__(self):
        print("PC Removed")
    def switch(self,operation):
        if(self.power == "Off"):
            if(operation == "1"):
                print(self.brand,self.os,sep="\n")
                time.sleep(1)
                self.power = "On"
            else:
                print("PC is already off")
                time.sleep(1)
        else:
            if(operation == '1'):
                print("PC is already open")
                time.sleep(1)
            else:
                print("Shutting Down")
                time.sleep(1)
                self.power = "Off"
    def volume(self):
        while True:
            c = input("Sound Menu\nVolume Up > : \nVolume Down < : \nExit Q : ")
            if(c == 'Q'):
                print("Volume:",self.sound)
                break
            elif(c == '>'):
                if(self.sound < 100):
                    self.sound +=1
                else:
                    print(self.sound)
            elif c == '<':
                if(self.sound > 0):
                    self.sound -=1
                else:
                    print(self.sound)
            else:
                print("Unvalid setting")
    def program_download(self):
        print("Microsoft Store\n")
        time.sleep(1)
        while True:
            name = input("Program name(Q Exit): ")
            if(name == 'Q'):
                break
            else:
                self.programs.append(name)

    def random_program(self):
        self.program = self.programs[randint(0,len(self.programs)-1)]
        print(self.program)

print("""**********************
PC MARKET
1.Buy PC
Q.Exit
**********************""")

while True:
    print("Welcome")
    market = input("Operation: ")
    if market == '1':
        brand = input("PC Brand: ")
        ram = int(input("RAM: "))
        processor = input("Processor: ")
        graphic_card = input("Graphic Card: ")
        programs = list()
        while True:
            program = input("Install Program: ")
            programs.append(program)
            q = input("Exit (Q): ")
            if(q == 'Q'):
                break
        os = input("OS: ")
        break
    elif market == 'Q':
        print("Goodday")
        sys.exit()
    else:
        print("404 Error")
comp = computer(brand,ram,processor,graphic_card,os,programs)
    
print("""************************
PC
************************
1.Power On
2.Power Off
3.Sound Settings
4.Download Program
5.Number Of Programs
6.Random Program
7.PC Info
Q.Exit
************************""")

while True:
    o = input("Operation: ")
    if o == 'Q':
        print("Goodbye")
        break
    elif o == '1' or o == '2':
        comp.switch(o)
    elif o > '2' and o < '8':
        if comp.power == 'Off':
            print("PC is off")
        else:
            if o == '3':
                comp.volume()
            elif o == '4':
                comp.program_download()
            elif o == '5':
                comp.__len__()
            elif o == '6':
                comp.random_program()
            else:                
                comp.__str__()
    else:
        print("Unvalid Operation")
