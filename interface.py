#running module
from engine import *

recog_engine = recog_engine() #Initialising recognition engine
recog_engine.findImages("known_people", False) # simulating finding images on social media
recog_engine.findImages("unknown_people", True) # loading the images of the missing persons


#comparing the images found
recog_engine.compare()

#Displaying the information about the images
recog_engine.displayObjects()

#Displaying Error information
recog_engine.displayErrorCount()

#Allowing terminal access to the code
while True:
    eval(input("Entry allowed: "))
