import pyjokes # Imported Pyjokes Module
import pyautogui as gui # Imported PyAutoGui
import time # Imported Time


# jokes = pyjokes.get_jokes(language="en", category="chuck") #get the jokes from Pyjoke API
# for joke in jokes: #creating a for loop to print all jokes in the given list
#     print(joke)

joke = pyjokes.get_joke(language="en", category="all")

gui.hotkey("win", "r") # Pressing Windows + R 
time.sleep(1) # Delay of 1 sec or 1000 miliseconds

gui.typewrite("notepad") #Typing Notepad in the Run Dilogue Box
time.sleep(1) # Delay of 1 sec or 1000 miliseconds


gui.hotkey("enter") # Pressing Enter
time.sleep(1) # Delay of 1 sec or 1000 miliseconds

gui.typewrite(joke) # Typing the joke in the Notepad Window

