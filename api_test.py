import face_recognition

image = face_recognition.load_image_file("sample_imgs/A.jpg")
face_locations = face_recognition.face_locations(image)
print(type(face_locations))
print(face_locations)
