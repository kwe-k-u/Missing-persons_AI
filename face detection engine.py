#imports
import face_recognition as face_rec
import os
import cv2
import numpy as np


#counts for error checking
count_distance = 0
count_npargmin = 0
count_compare = 0
count = 0
errors = 0
known_filenames = [] #array to hold the file names of those scanned

#This function gets the images in the location directory and returns them in an array
def crawler(location):

    image_array = []
    for dirpath, dnames, fnames in os.walk(os.getcwd() + "/" + location ):
        for face in fnames: #face is the name of the file and fnames is the array that holds the names of all the files

            known_filenames.append(face)

            try:
                image = face_rec.load_image_file(os.getcwd() +"/" + location +"/"+ face)
                image_array.append(image)

            except:
                print("Error with crawler function")
    return image_array

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
            face = face_rec.load_image_file("known_people/" + f)
            encoding = face_rec.face_encodings(face)
            holder[f.split(".")[0]] = encoding # f is the file name

    return holder




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





known = crawler("/known_people/")
size = []
print("known", len(known))

compare(encode_unknown("test.jpg"),encode_known().values())






print(" \t \t Number of errors caught")
print("face comparison", count_compare)
print("distance calculation", count_distance)
print("smallest comparison", count_npargmin)



#todo drag and drop picture to start search
#todo add report of how many images were searched































# =============================================================================
# #this function converts images to facial encodings  and returns the ecncodings for comparison
# def encode_face(image):
#     #Find the location of the faces in the image
#     img = cv2.imread(image,1)
#     face_location = face_rec.face_locations(img)
#
#
#
#     image = face_rec.face_encodings(image)
#     print("ksdhfsdfsdfsdjfsdjdsfkdfskj",image)
# # =============================================================================
# #     try:
# #         image = face_rec.face_encodings(image)
# #
# #     except:
# #         print("Error with encode_face function")
# #         print("Couldn't encode", image)
# # =============================================================================
#     return image
#
# =============================================================================
