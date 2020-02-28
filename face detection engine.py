#imports
import face_recognition as face_rec
import face_recognition
import os
count = 0
errors = 0
#this function converts images to facial encodings for comparison
def encode_face(image):
    print(image)
    try:
        image = face_rec.face_encodings(image)
    except:
        print("Error")
    return image



# This function compares the faces to see if its the same person
def compare(untethered, tethered):
    #untethered is the picture of the missing person
    #tethered is the image of the one we know(online)
    known_image = face_rec.load_image_file(tethered)
    unknown_image = face_rec.load_image_file(untethered)

    known_encoding = face_rec.face_encodings(known_image)[0]
    unknown_encoding = face_rec.face_encodings(unknown_image)[0]

    results = face_rec.compare_faces([known_encoding], unknown_encoding)
    print(results)


#This function gets multiple faces of those known
def crawler(location):

    for dirpath, dnames, fnames in os.walk(os.getcwd() + "/" + location ):
        for face in fnames:
            print(face)
            try:
                image = face_rec.load_image_file(os.getcwd() +"/" + location +"/"+ face)
                return image
            except:
                print("Error")


#running the code
# =============================================================================
# location = "/" + input("Enter a folder name to look in")
# =============================================================================
array = []
unknown = crawler("/Missing")
print("here")
box_unknown = []
box_known = []
array = crawler("/known_people/")
for known in array:
    try:
        count +=1
        if unknown[0] not in box_unknown:
            box_unknown.append(unknown[0])
        if known[0] not in box_known:
            box_known.append(known[0])
        compare(encode_face(unknown[0]),encode_face(known[0]))
    except:
        errors +=1



print("Report after AI checks")
print("The loop run", count, "times")
print("Number of errors caught:",errors)
print(box_known)
print(box_unknown)
