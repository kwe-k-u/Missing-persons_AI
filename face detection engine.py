#imports
import face_recognition as face_rec
import os

#this function converts images to facial encodings for comparison
def encode_face(image):
    image = image.face_encodings(image)[0]

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

    for dirpath, dnames, fnames in os.walk(os.getcwd()):
        for face in fnames:
            print(os.getcwd())
            image = face_rec.load_image_file(os.getcwd() +"/" + location)
            return image


#running the code
# =============================================================================
# location = "/" + input("Enter a folder name to look in")
# =============================================================================
array = []
unknown = crawler("/Missing")
array = crawler("/known_people/")
for known in array:
    compare(encode_face(unknown),encode_face(known))
