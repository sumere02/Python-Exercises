import random
import time

class controller():
    def __init__(self,brand = "None",state = "off",sound = 0,channel = [],channel_number = 0):
        self.brand = brand
        self.state = state
        self.sound = sound
        self.channel = list()
        self.channel = channel
        self.channel_number = channel_number
    def __del__(self):
        print("TV Erased")
    def __len__(self):
        print("{} Channel".format(self.channel_number))
    def __str__(self):
        return "Brand: {}\nState: {}\nSound: {}\nChannel: {}\nChannel Number: {}\n".format(self.brand,self.state,self.sound,self.channel,self.channel_number)
    def power(self,operation):
        if(operation == 1):
            if(self.state == 'off'):
                print(self.brand)
                time.sleep(1)
                self.state='on'
            else:
                print("TV is already working")
        else:
            if(self.state == 'on'):
                print("Shutting Down")
                time.sleep(1)
                self.state='off'
            else:
                print(self.brand)
    def sound_tv(self):
        print("Sound: {}".format(self.sound))
        print("Increase sound: >\nDecrease Sound: <\nExit: Q")
        while True:
            c = input("Sound Operation: ")
            if(c == 'Q'):
                print("Sound: {}".format(self.sound))
                break
            elif(c == '<'):
                if(self.sound > 0):
                    self.sound -=1
                else:
                    print("Sound: {}".format(self.sound))
            elif(c == '>'):
                if(self.sound < 100):
                    self.sound +=1
                else:
                    print("Sound: {}".format(self.sound))
            else:
                print("Unvalid sound operation")

    def channel_add(self):
        channel_name = input("Name of channel: ")
        self.channel.append(channel_name)
        self.channel_number +=1
    def rand_channel(self):
        if(self.channel_number > 0):
            number = random.randint(0,self.channel_number-1)
            print("Channel: {}".format(self.channel[number]))
        else:
            print("0 Channel Exists")
print("""************************
Controller Program
************************
1 - Power On
2 - Power Off
3 - Sound Settings
4 - Add Channel
5 - Number Of Channels
6 - Random Channel
7 - TV Info
8 - Exit
************************""")

brand = input("Brand: ")
controller_lg = controller(brand)

while True:
    operation = int(input("Operation: "))
    if operation == 8:
        break
    else:
        if(operation == 1 or operation == 2):
                controller_lg.power(operation)
        elif(controller_lg.state == 'on'):
            if(operation == 3):
                controller_lg.sound_tv()
            elif(operation == 4):
                controller_lg.channel_add()
            elif(operation == 5):
                controller_lg.__len__()
            elif(operation == 6):
                controller_lg.rand_channel()
            elif(operation == 7):
                controller_lg.__str__()
            else:
                print("Unvalid Operation")
        else:
            print("TV is off")
