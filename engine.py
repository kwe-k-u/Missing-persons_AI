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
# =============================================================================
#         try:
# =============================================================================
        if missing:
            #Prompt to let us know the system is working
            print("WORKING")
            print("Finding images of missing persons")

            for dirpath, dnames, fnames in os.walk(os.getcwd() + "/" + location ):
                for face in fnames: #face is the name of the file and fnames is the array that holds the names of all the files

# =============================================================================
#                         image = face_rec.load_image_file(os.getcwd() +"/" + location +"/"+ face)
# =============================================================================
                    self.unknown_images.append(ImageData(face,location))


        else:
            #Prompt to let us know the system is working
            print("WORKING")
            print("Simulating finding images on social media")


            # route for "known" images
            for dirpath, dnames, fnames in os.walk(os.getcwd() + "/" + location ):
                for face in fnames: #face is the name of the file and fnames is the array that holds the names of all the files

                        self.known_images.append(ImageData(face,location))
# =============================================================================
#         except:
#             print(face)
#             self.updateError("crawler")
# =============================================================================




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

    #Comaprison
    def compare(self,known,unknown):
        #unknown and known are of the type ImageClass



        #we might not use the distance
# =============================================================================
#         try:
#             dis = False
#             distance = face_rec.face_distance(known.getEncoding(), unknown.getEncoding())
#             print(distance)
#             if unknown.matchDistance == None or unknown.matchDistance > distance:
#                 dis = True
#                 unknown.matchDistance = distance
#         except:
#             self.updateError("distance")
# =============================================================================

        dis = False
# =============================================================================
#         print("unknown")
#         print(unknown.getEncoding())
#         print()
#         print()
#         print()
#         print("known")
#         print(known.getEncoding())
#         print()
#         print()
#         print()
# =============================================================================
# =============================================================================
#         kEncode = known.getEncoding()
#         uEncode = unknown.getEncoding()
#         print("encode")
#         print(kEncode)
#         print("decode")
#         print(uEncode)
#         for k in kEncode:
#             for u in uEncode:
#                 print("l")
#                 distance = face_rec.face_distance(known.getEncoding(), unknown.getEncoding())
# =============================================================================
# =============================================================================
#         print(distance)
# =============================================================================

# =============================================================================
#             unknown.matchDistance = distance
# =============================================================================


        #Loops through the columns of matrix to do the comaprisons
# =============================================================================
#         print()
#         for eknown in unknown_encoding:
#             if face_rec.compare_faces(known_encoding,eknown) and dis:
#                 unknown.setMatch(known)
# =============================================================================

        for known in self.known_images:
            dis = False
            kEncoding = known.getEncoding()
            print("Known encode")
            print(kEncoding)
            print()
            print()
            print()
# =============================================================================
#             for unknown in self.unknown_images:
#                 uEncoding = unknown.getEncoding()
#
#                 print("unknown encoding")
#                 print(uEncoding)
#                 print()
#                 print()
#                 distance = face_rec.face_distance(uEncoding, kEncoding)
#                 if unknown.matchDistance == None or unknown.matchDistance > distance:
#                     dis = True
#
#                 if face_rec.compare_faces(kEncoding,uEncoding) and dis:
#                     unknown.setMatch(known)
# =============================================================================
            for unknown in self.unknown_images:
                uEncoding = unknown.getEncoding()

                print("unknown encoding")
                print(uEncoding)
                print()
                print()
                distance = face_rec.face_distance(uEncoding[0], kEncoding)
                if unknown.matchDistance == None or unknown.matchDistance > distance:
                    dis = True

                if face_rec.compare_faces(kEncoding,uEncoding[0]) and dis:
                    unknown.setMatch(known)



# =============================================================================
#         try:
#             hope = face_rec.compare_faces(known.getImage(),unknown.getImage())
#             if hope:
#                 unknown.setMatch(known)
#         except:
#             self.updateError("compare")
# =============================================================================





    #This section deals with error handling


    def __updateTotalError(self):
        self.total_errors +=1

    #updates the count for the error type
    def updateError(self,subError):

        if subError == "distance":
            self.distance_error +=1

        elif subError == "npargmin":
            self.npargmin_error +=1

        elif subError == "crawler":
            self.crawler_error +=1

        else:
            self.compare_error +=1

        self.__updateTotalError()



    #Displays the error counts
    def displayErrorCount(self):
        print("\t \t Error Report".center(20))
        print("Errors with distance calculation \t",self.distance_error)
        print("Errors with comparison", self.compare_error)
        print("Errors with npargmin", self.npargmin_error)
        print("Errors with image search", self.crawler_error)
        print("Total Error count \t \t", self.total_errors)



    def getUnknown(self):
        return self.unknown_images

    def getKnown(self):
        return self.known_images







#=========================================================================================
#running the engine
#This function encodes the image of the missing person


def encode_unknown(image): # make it such that image == the file names

    img = cv2.imread(image,1)
    print("img",type(img))
    face_locations = face_rec.face_locations(img) #finding the locations of the faces in the image
    face_encodings =face_rec.face_encodings(img, face_locations)

    return face_encodings

#This function encodes the images of the
def encode_known():
    holder = {} #dictionary to hold the name(key) and encoding of the image


    for dirpath, dnames, fnames in os.walk("./known_people"):
        for f in fnames:
            image_class_array.append(imageClass.ImageData(f))
            face = face_rec.load_image_file("known_people/" + f)
            encoding = face_rec.face_encodings(face)
            holder[f.split(".")[0]] = encoding # f is the file name

    return holder



#
# This function compares the faces to see if its the same person

def compare(untethered, tethered):
    #untethered is the array of the picture of the missing person
    #tethered is an array of the images of the people who aren't missing but might know the missing person(online)

    results = [] #array to hold the results of comparisons
    distance_array = [] #Array to hold the distances for each set
    print("the length of untethered is",len(untethered))
    print("the length of tethered is",len(tethered))
    count_distance = 0
    count_npargmin = 0
    count_compare =0





    for tethered_image in tethered:
        for untethered_image in untethered:


            # face distances
            try:
                distance = face_rec.face_distance(tethered_image, untethered_image)
            except:
                count_distance +=1

            distance_array.append(distance)

            try:
                best_index = np.argmin(distance_array)
                print(best_index)
            except:
                count_npargmin +=1


            # compare_faces
            try:
                matches = face_rec.compare_faces(tethered_image, untethered_image)
            except:
                count_compare += 1
            print("matches",matches, type(matches))
            results.append(matches)




    #display results
    try:
        if results[best_index]:
            print("The closest match is", known_filenames[best_index])






        print("results",results)
        print("Result printing starts now")
        print("distances", distance_array)
    except:
        print("Error with process")




# =============================================================================
#
# known = crawler("/known_people/")
# size = []
# print("known", len(known))
#
# compare(encode_unknown("test.jpg"),encode_known().values())
#
# =============================================================================






#todo drag and drop picture to start search
#todo add report of how many images were searched






























