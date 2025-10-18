import cv2
from PIL import Image, ImageDraw
image_path = "group.png"
image = cv2.imread(image_path)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
pil_image = Image.fromarray(image_rgb)
draw = ImageDraw.Draw(pil_image)
for (x, y, w, h) in faces:
    draw.rectangle(((x, y), (x+w, y+h)), outline="red", width=3)
pil_image.show()
pil_image.save("output.png")





# import face_recognition
# from PIL import Image, ImageDraw
# image = face_recognition.load_image_file("group.jpg")
# face_locations = face_recognition.face_locations(image)
# pil_image = Image.fromarray(image)
# draw = ImageDraw.Draw(pil_image)
# for top, right, bottom, left in face_locations:
#     draw.rectangle(((left, top), (right, bottom)), outline="red", width=3)

# pil_image.show()
# pil_image.save("output.png")



