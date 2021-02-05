#Script to prevent getting kicked from Blackboard Collaborate Ultra due to inactivity
import pyautogui, sys
import time

#Prevents script from crashing when cursor reaches one of the edges of screen 
pyautogui.FAILSAFE = False

#Default coordinates for mic button on BCU; As observed on 14" 1080p Lenovo display
xdef = 923
ydef = 982

#Simple counter to perform a button click within BCU intermittently
movecounter = 0

print("Press Ctrl+C to interrupt the program")

try:
    while True:
        xrand, yrand = pyautogui.position() #Get the current position of cursor on screen
        
        pyautogui.moveTo(xrand+5, yrand+5) #Move the cursor back & forth to keep screen awake
        time.sleep(0.2)
        pyautogui.moveTo(xrand, yrand)
        
        pyautogui.press("shift") #Perform a keystroke to prevent the computer from going into sleep
        time.sleep(0.2)
        
        movecounter += 1
        
        if(movecounter>=500): #Double click the mic button on BCU to simulate user activity. Stops BCU from kicking user due to inactivity
            pyautogui.click(button='left', clicks=2, interval=1.5, x=xdef, y=ydef)
            movecounter = 0
        
except KeyboardInterrupt:
    print("Interrupted by user")

        