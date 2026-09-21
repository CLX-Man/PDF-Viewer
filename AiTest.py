import fitz  # PyMuPDF
import tkinter as tk
from PIL import Image, ImageTk

# 1. PDF laden
file_name = "Test.pdf"
doc = fitz.open(file_name)
page = doc.load_page(0)  # Erste Seite laden


# 2. Seite in ein Bild (Pix Map) rendern
pix = page.get_pixmap()
img_data = pix.tobytes("ppm")

# 3. UI mit Tkinter erstellen
root = tk.Tk()
root.title(file_name)

# Bild für Tkinter konvertieren und anzeigen
img = ImageTk.PhotoImage(data=img_data)
label = tk.Label(root, image=img)
label.pack()

root.mainloop()