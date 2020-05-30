#running module
from engine import *

recog_engine = recog_engine()
recog_engine.findImages("./known_people", False) # simulating finding images on social media
recog_engine.findImages("./unknown_people", True) # loading the images of the missing persons


for known_images in recog_engine.getKnown():
    for unknown_images in recog_engine.getUnknown():

        recog_engine.compare(known_images, unknown_images)

recog_engine.displayObjects()


recog_engine.displayErrorCount()

#Comparing the images found
while True:
    eval(input("Entry allowed: "))
