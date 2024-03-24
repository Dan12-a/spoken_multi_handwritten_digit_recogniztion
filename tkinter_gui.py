from tkinter import *
import tkinter.font as tkFont
from PIL import Image, ImageDraw
import PIL
import pickle
import numpy as np
import cv2
import pyttsx3

# Load the pre-trained model
loaded_model = open("trained_model.p", "rb")
model = pickle.load(loaded_model)

lastx, lasty = None, None

# Function to clear the drawing widget
def clear_widget():
    global draw_board, image1, draw, text
    # Clear the image, text widget, and canvas
    image1 = PIL.Image.new("RGB", (600, 200), (255, 255, 255))
    text.delete(1.0, END)
    draw = ImageDraw.Draw(image1)
    draw_board.delete('all')

# Function to draw lines when mouse button is pressed and moved
def draw_lines(event):
    global lastx, lasty
    x, y = event.x, event.y
    draw_board.create_line((lastx, lasty, x, y), width=8, fill='black', capstyle=ROUND, smooth=TRUE, splinesteps=12)
    draw.line([lastx, lasty, x, y], fill="black", width=10)
    lastx, lasty = x, y

# Function to activate drawing event
def activate_event(event):
    global lastx, lasty
    draw_board.bind('<B1-Motion>', draw_lines)
    lastx, lasty = event.x, event.y

# Function to predict and speak the handwritten digit
def save():
    text_num = []
    global image_number
    filename = 'image_out.png'
    image1.save(filename)
    image = cv2.imread(filename)
    gray = cv2.cvtColor(image.copy(), cv2.COLOR_BGR2GRAY)
    ret, th = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

    contours = cv2.findContours(th, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]

    for cnt in contours:
        x, y, w, h = cv2.boundingRect(cnt)
        cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 1)
        digit = th[y:y + h, x:x + w]
        resized_digit = cv2.resize(digit, (18, 18))
        padded_digit = np.pad(resized_digit, ((5, 5), (5, 5)), "constant", constant_values=0)
        print(padded_digit.shape)
        digit = padded_digit.reshape(1, 28, 28, 1)
        digit = digit / 255.0

        pred = model.predict([digit])[0]
        final_pred = np.argmax(pred)
        text_num.append([x, final_pred])


        data = str(final_pred) + ' ' + str(int(max(pred) * 100)) + '%'

        font = cv2.FONT_HERSHEY_SIMPLEX
        fontScale = 0.5
        color = (0, 0, 0)
        thickness = 1
        cv2.putText(image, data, (x, y - 5), font, fontScale, color, thickness)

    text_num = sorted(text_num, key=lambda t: t[0])
    text_num = [i[1] for i in text_num]
    final_text = "".join(map(str, text_num))
    text.insert(END, final_text)
    cv2.imshow('image', image)
    engine = pyttsx3.init()

    # Iterate through predicted numbers and convert them to speech
    for digit in text_num:
        engine.say(f"The predicted number is {digit}.")
        engine.runAndWait()

    # Destroy pyttsx3 engine instance
    engine.stop()
    cv2.waitKey(0)

# Create the tkinter window
win = Tk()
win.geometry("650x500")  # Set the window size
win.title("Multiple Handwritten Digit Recognition")
win.config(background="#3aa9ae")

# Define font style
fontStyle = tkFont.Font(family="Lucida Grande", size=15)

# Label for instructions
write_label = Label(win, text="Write your number:", bg="#FF3040", font=fontStyle)
write_label.place(relx=0.03, rely=0.03)

# Create canvas for drawing
draw_board = Canvas(win, width=800, height=300, bg='white')  # Increase width and height
draw_board.place(relx=0.03, rely=0.1, relwidth=0.94, relheight=0.45)  # Adjust the placement and relative size
draw_board.bind('<Button-1>', activate_event)

# Create PIL image and draw object for drawing on canvas
image1 = PIL.Image.new("RGB", (600, 200), (255, 255, 255))
draw = ImageDraw.Draw(image1)

# Button to predict and speak the digit
button = Button(text="PREDICT and SPEAK", command=save, bg="#FFC0CB", font=tkFont.Font(family="Lucida Grande", size=15))
button.place(relx=0.5, rely=0.63, anchor=CENTER)

# Label to display predicted number
predict_label = Label(win, text="PREDICTED NUMBER:", bg="#FFC0CB", font=tkFont.Font(family="Lucida Grande", size=15))
predict_label.place(relx=0.03, rely=0.7)

# Text widget to display predicted number
text = Text(win, height=2, width=10, font=tkFont.Font(family="Lucida Grande", size=13))
text.place(relx=0.03, rely=0.77)

# Button to clear canvas and text widget
del_btn = Button(win, text="CLEAR ALL", command=clear_widget, bg="#FFC0CB", width=10, font=tkFont.Font(family="Lucida Grande", size=15))
del_btn.place(relx=0.03, rely=0.88)

# Run the tkinter event loop
win.mainloop()
