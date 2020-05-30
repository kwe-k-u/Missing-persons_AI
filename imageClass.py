#This class holds image data
#imports
import face_recognition as face_rec

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

    def __init__(self, name, location):
        self.name = name.split(".")[0] #This holds the account name(or file name) for the image
        self.location = location # This holds the url for the image (or file location)
        self.matchedStatus = False; #This holds a boolean for if a match was found for the image
# =============================================================================
#         self.imageEncoding = setEncoding(name, location) # This holds the image encoding
# =============================================================================
        self.matchImage = None
        self.matchDistance = None
        self.setEncoding(name. location)




    def getEncoding(self):
        return self.imageEncoding

    def getImage(self):
        return self.image

    def displayData(self):
        print("Image name:", self.name)
        print("Image location", self.location)
        print("Match status", self.matchedStatus)
        print("Match Image", self.matchImage)

    def setMatch(self, matchData): #sets match status to  true if a match is found
        self.matchedStatus = True
        self.matchImage = matchData


    def setEncoding(name, location):
        image = face_rec.load_image_file(os.getcwd() +"/" + location +"/"+ name)
        location = face_rec.face_locations(image)
        return face_rec.face_encodings(image, location)



# =============================================================================
#
# #This function encodes the image of the missing person
# def encode_unknown(image): # make it such that image == the file names
#
#     img = cv2.imread(image,1)
#     print("img",type(img))
#     face_locations = face_rec.face_locations(img) #finding the locations of the faces in the image
#     face_encodings =face_rec.face_encodings(img, face_locations)
#
#     return face_encodings
#
# #This function encodes the images of the
# def encode_known():
#     holder = {} #dictionary to hold the name(key) and encoding of the image
#
#
#     for dirpath, dnames, fnames in os.walk("./known_people"):
#         for f in fnames:
#             face = face_rec.load_image_file("known_people/" + f)
#             encoding = face_rec.face_encodings(face)
#             holder[f.split(".")[0]] = encoding # f is the file name
#
#     return holder
#
# =============================================================================
