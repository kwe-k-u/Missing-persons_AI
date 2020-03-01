#imports
import face_recognition as face_rec
import os


count = 0
errors = 0

#This function gets the images in the location directory and returns them in an array
def crawler(location):
    facecount=0 #remove
    image_array = []
    for dirpath, dnames, fnames in os.walk(os.getcwd() + "/" + location ):
        for face in fnames: #face is the name of the file and fnames is the array that holds the names of all the files
            facecount += 1 #remove
            print(face)# remove
            print("face count is", facecount) #remove
            try:
                image = face_rec.load_image_file(os.getcwd() +"/" + location +"/"+ face)
                image_array.append(image)
                key = image.keys()
                print(key)

            except:
                print("Error with crawler function")
    return image_array



#this function converts images to facial encodings  and returns the ecncodings for comparison
def encode_face(image):
    image = face_rec.face_encodings(image)
    print("ksdhfsdfsdfsdjfsdjdsfkdfskj",image)
# =============================================================================
#     try:
#         image = face_rec.face_encodings(image)
#
#     except:
#         print("Error with encode_face function")
#         print("Couldn't encode", image)
# =============================================================================
    return image



# This function compares the faces to see if its the same person
def compare(untethered, tethered):
    #untethered is the array of the picture of the missing person
    #tethered is an array of the images of the people who aren't missing but might know the missing person(online)

    results = []
    distances = [] #Array to hold the distances for each set
    print("the length of untethered is",len(untethered))
    print("the length of tethered is",len(tethered))
    for tethered_image in tethered:
        for untethered_image in untethered:
# =============================================================================
#             known_image = face_rec.load_image_file(tethered_image)
#             unknown_image = face_rec.load_image_file(untethered_image)
# =============================================================================

            known_encoding = face_rec.face_encodings(tethered_image)
            unknown_encoding = face_rec.face_encodings(untethered_image)

            results.append(face_rec.compare_faces([known_encoding], unknown_encoding))
            distance = face_recognition.face_distance(tethered_image, untethered_image)
            print("distance", type(distance), distance)

# =============================================================================
#              face_distances = face_recognition.face_distance(faces_encoded, face_encoding)
#         best_match_index = np.argmin(face_distances)
#         if matches[best_match_index]:
#             name = known_face_names[best_match_index]
#
#         face_names.append(name)
#
# =============================================================================


    print("results",results)
    print("Result printing starts now")
    print(results)



#This function groups the encoding
#running the code
# =============================================================================
# location = "/" + input("Enter a folder name to look in")
# =============================================================================

unknown = crawler("/Missing")
known = crawler("/known_people/")
size = []
for known_image in known:
    print("known image", known_image)
    for unknown_image in unknown:
        size.append(unknown_image[0][1])
        print("unknown image", unknown_image)
        compare(encode_face(unknown_image),encode_face(known_image))
# =============================================================================
#     try:
#         count +=1
#         if unknown[0] not in box_unknown:
#             box_unknown.append(unknown[0])
#         if known[0] not in box_known:
#             box_known.append(known[0])
#         compare(encode_face(unknown[0]),encode_face(known[0]))
#     except:
#         errors +=1
# =============================================================================



print("Report after AI checks")
print("The loop run", count, "times")
print("Number of errors caught:",errors)
print(unknown)
print(known)


#todo drag and drop picture to start search
#todo add report of how many images were searched
