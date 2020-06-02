#This class holds image data
#imports
import face_recognition as face_rec
import os
import cv2
# =============================================================================
# import numpy as np
# =============================================================================
#list of data in class
'''
    name- This holds the account name (or file name in locally store images) for the image
    location - This holds the url (or file location) of the image
    matchedStatus - This holds a boolean for if a match has been found for the image
    encoding - This holds the encoding for the image
    face_locations = The location of the faces in the image

'''

class ImageData:

    def __init__(self, paramName, location):
        self.known = False
        #to known if its the image of a missing person
        if location == "./known_people":
            self.known = True
        self.name = paramName.split(".")[0] #This holds the account name(or file name) for the image
        self.location = os.getcwd() + "/" + location # This holds the url for the image (or file location)
        self.matchedStatus = False; #This holds a boolean for if a match was found for the image
        self.matchImage = None
        self.matchDistance = None
        self.imageEncoding = self.setEncoding(paramName) # This holds the image encoding





    def getEncoding(self):
        return self.imageEncoding

    def getImage(self):
        return self.image

    def getMatchImage(self):
        return self.matchImage

    def getName(self):
        return self.name

    def getLocation(self):
        return self.location

    def getDistance(self):
        return self.distance

    def displayData(self):
        print("Image name:", self.name)
        print("Image location", self.location)
        print("Match status", self.matchedStatus)
        if self.matchedStatus:
            print("Match Image", self.matchImage.getName())


    def setMatch(self, matchData): #sets match status to  true if a match is found
        self.matchedStatus = True
        self.matchImage = matchData


    def setEncoding(self, fname):
        if self.known:
            image = face_rec.load_image_file(self.location + "/" + fname)
            return face_rec.face_encodings(image)
        image = face_rec.load_image_file(self.location +"/"+ fname)
        img = cv2.imread(self.location + "/" + fname,1)
        location = face_rec.face_locations(image)
        return face_rec.face_encodings(img, location)


