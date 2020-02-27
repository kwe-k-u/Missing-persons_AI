import face_recognition as fr
import os
import cv2
import face_recognition
import numpy as np
from time import sleep

            # This code searches for faces and encodes them
def get_encoded_faces():
    """
    This gets the faces of those known
    REPLACE WITH API CODE FOR PICTURES ONLY
    looks through the faces folder and encodes all
    the faces

    :return: dict of (name, image encoded)
    """
    encoded = {}

    for dirpath, dnames, fnames in os.walk("./faces"): #change this to work with the twiiter api
        for f in fnames:
            if f.endswith(".jpg") or f.endswith(".png") or f.endswith(".jpeg"): # might not need this part
                face = fr.load_image_file("faces/" + f)
                encoding = fr.face_encodings(face)[0]
                encoded[f.split(".")[0]] = encoding

    return encoded



def unknown_image_encoded(img):
    """
    encode the pictures of the missing people we are trying to reconnect with family

    This will pick all the pictures in the file
    """

    for dirpath, dnames, fnames in os.walk(".people"):
        for f in fnames:
            if f.endswith(".jpg") or f.endswith(",png"):

                face = fr.load_image_file("faces/" + img)
                encoding = fr.face_encodings(face)[0]

    return encoding


# this function compares the images of people missing
def compare(lost):
    """
    will find all of the faces in a given image and label
    them if it knows what they are

    :param im: str of file path
    :return: list of face names
    """

    faces = get_encoded_faces() # pictures from api should go here
    faces_encoded = list(faces.values()) # picks the image
    known_face_names = list(faces.keys()) # names the image picked above

    img = cv2.imread(lost, 1) #not sure: probably encodes the face of the one we are looking for
    #img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)
    #img = img[:,:,::-1]

    face_locations = face_recognition.face_locations(img) #finds the faces in the image
    unknown_face_encodings = face_recognition.face_encodings(img, face_locations)

    face_names = []
    for face_encoding in unknown_face_encodings:
        # See if the face is a match for the known face(s)
        matches = face_recognition.compare_faces(faces_encoded, face_encoding)
        name = "Unknown"

        # use the known face with the smallest distance to the new face
        face_distances = face_recognition.face_distance(faces_encoded, face_encoding)
        best_match_index = np.argmin(face_distances)
        if matches[best_match_index]:
            name = known_face_names[best_match_index]

        face_names.append(name)

        #This just draws labels around the image. NOT NEEDED FOR US
# =============================================================================
#
#         for (top, right, bottom, left), name in zip(face_locations, face_names):
#             # Draw a box around the face
#             cv2.rectangle(img, (left-20, top-20), (right+20, bottom+20), (255, 0, 0), 2)
#
#             # Draw a label with a name below the face
#             cv2.rectangle(img, (left-20, bottom -15), (right+20, bottom+20), (255, 0, 0), cv2.FILLED)
#             font = cv2.FONT_HERSHEY_DUPLEX
#             cv2.putText(img, name, (left -20, bottom + 15), font, 1.0, (255, 255, 255), 2)
#
# =============================================================================

# change this to the code that records the success or failure of the search. Maybe puts them in a folder
    # Display the resulting image
    while True:

        cv2.imshow('Video', img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            return face_names


#replace this with something that changes test to an array
print(compare("test.jpg"))