import tkinter as tk
from tkinter import filedialog
import cv2
from PIL import Image, ImageDraw
mn=tk.Tk()
mn.title('Face marker')
mn.geometry('500x300')
def mark():
    try:
        filee=filedialog.askopenfilename(title="Chose image to recognize from")
        if filee:
            image_path = filee
            image = cv2.imread(image_path)
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
            faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
            image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            pil_image = Image.fromarray(image_rgb)
            draw = ImageDraw.Draw(pil_image)
            for (x, y, w, h) in faces:
                draw.rectangle(((x, y), (x+w, y+h)), outline="red", width=3)
            key = filedialog.asksaveasfilename(title="Save Image image as",defaultextension=".png",filetypes=[("PNG files", "*.png"), ("JPEG files", "*.jpg"),("BMP files", "*.bmp"),("GIF files", "*.gif"),("TIFF files", "*.tiff"), ("All files", "*.*")])
            if key:
                pil_image.show()
                pil_image.save(key)
            else:
                return
        else:
            return
    except ValueError:
        return
b=tk.Button(mn,text="Proceed",command=lambda:mark(),cursor="hand2")
b.place(x=200,y=75)
mn.mainloop()