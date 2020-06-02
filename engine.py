#imports
import face_recognition as face_rec
import os
import cv2
import numpy as np
from imageClass import *

#counts for error checking
class recog_engine:

    def __init__(self):
        self.distance_error = 0
        self.npargmin_error = 0
        self.compare_error = 0
        self.crawler_error = 0
        self.total_errors = 0
        self.known_images = []
        self.unknown_images = []





    #This section deals with the images


    # This function finds the images to be analysed.
    def findImages(self,location,missing): #location is the file directory

        #Missing is a boolean for if the image being found is of missing people or tethered people
        try:
            if missing:
                #Prompt to let us know the system is working
                print("WORKING")
                print("Finding images of missing persons")

                for dirpath, dnames, fnames in os.walk(os.getcwd() + "/" + location ):
                    for face in fnames: #face is the name of the file and fnames is the array that holds the names of all the files

                        self.unknown_images.append(ImageData(face,location)) #Add image to list of missing people


            else:
                #Prompt to let us know the system is working
                print("WORKING")
                print("Simulating finding images on social media")


                # route for "known" images
                for dirpath, dnames, fnames in os.walk(os.getcwd() + "/" + location ):
                    for face in fnames: #face is the name of the file and fnames is the array that holds the names of all the files
                        self.known_images.append(ImageData(face,location)) #add image to the list of not mising people

        except:
            print(face)
            self.updateError("crawler")




    #temp
    def displayObjects(self):
        print("\t \t Printing out the known image details")
        for i in self.known_images:
            i.displayData()
            print()
            print()

        print("\t \t Printing out the unknown image details")
        for i in self.unknown_images:
            i.displayData()
            print()
            print()


    #Compare the images
    def compare(self):
        #unknown and known are of the type ImageClass
        try:

            for known in self.known_images:

                #Getting the encoding of the image of not missing person
                kEncoding = known.getEncoding()

                for unknown in self.unknown_images:
                    dis = False
                    uEncoding = unknown.getEncoding() #getting the encoding of the image of the missing person

                    distance = face_rec.face_distance(uEncoding[0], kEncoding)[0] #Getting the difference value for the two image encoding
                    if unknown.matchDistance == None or unknown.matchDistance > distance:

                        print(distance)
                        dis = True

                    if face_rec.compare_faces(kEncoding, uEncoding[0])[0] and dis:
                        unknown.setMatch(known) #if a match is found, tag the image of the missing person
        except:
            self.updateError("compare")





    #This section deals with error handling



    #updates the count for the error type
    def updateError(self,subError):

        if subError == "distance":
            self.distance_error +=1 #updating count for errors from measuring distance [compare]

        elif subError == "npargmin":
            self.npargmin_error +=1

        elif subError == "crawler":
            self.crawler_error +=1 #updating count for errors from loading imagess [findImages]

        else:
            self.compare_error +=1 #update count for comparison error [compare?]

        self.total_errors +=1 #update total error count



    #Displays the error counts
    def displayErrorCount(self):
        #todo format
        print("\t \t Error Report".center(20))
        print("Errors with distance calculation \t",self.distance_error)
        print("Errors with comparison", self.compare_error)
        print("Errors with npargmin", self.npargmin_error)
        print("Errors with image search", self.crawler_error)
        print("Total Error count \t \t", self.total_errors)



    def getUnknown(self):
        #return the list of images of missing persons
        return self.unknown_images

    def getKnown(self):
        #return the list of images of not missing persons
        return self.known_images












#todo drag and drop picture to start search
#todo add report of how many images were searched