import pyautogui as mod
import time
from win32api import GetSystemMetrics
import sys

def checkscreen():
 

    if GetSystemMetrics(0) !=1920 and GetSystemMetrics(1)!=1080:

        print("ERROR: This program only works with screens that are 1080x1920.")
        k=input("press anything to exit") 
        sys.exit()

    if mod.pixelMatchesColor(1225, 856,(254, 254, 254)):

        return True;
    else:
        print("ERROR: This program only works if Club penguin rewritten is snapped to the right side of the screen and scrolled fully up and to the left in Chrome.")
        k=input("press anything to exit") 
        sys.exit()


def mine(x, y):
    if checkscreen():
        mod.click(x, y)
        time.sleep(1.5)
        mod.typewrite('d')
        time.sleep(10.3)

    else:
        print("Goodbye")
        
def work():
    mod.typewrite('j')
    mine(1233, 700)
    '''
    mine(1393, 685)
    mine(1580, 700)
    mine(1566, 788)
    '''
    mine(1412, 775)
    mine(1241, 767)
    
       
def main():
    while checkscreen():
        print("Press [Ctrl + w] or close this window  to stop the script")
        work()


        
main()



'''
time to finish mine: 10 secs

snowball 
x = 1225
y = 856
color = (254,254,254)

lights
x = 1535
y = 345


penguin size top to bottom
60 pixels
'''