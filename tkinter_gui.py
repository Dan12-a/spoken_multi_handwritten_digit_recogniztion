from tkinter import *
from tkinter import messagebox, filedialog, colorchooser
import tkinter.font as tkFont
from PIL import Image, ImageDraw, ImageTk
import PIL
import pickle
import numpy as np
import cv2
import pyttsx3

# Load the pre-trained model
loaded_model = open("trained_model.p", "rb")
model = pickle.load(loaded_model)

lastx, lasty = None, None
image1 = None
loaded_image = None  # Initialize loaded_image globally
draw_color = '#000000'  # Default drawing color
draw_history = []  # List to store drawing history for undo/redo functionality
draw_history_index = -1  # Index to track current position in draw history
selected_language = 'en'  # Default language is English

# Function to clear the drawing widget
def clear_widget():
    global draw_board, image1, draw, text, lastx, lasty, loaded_image, draw_history, draw_history_index
    # Clear the image, text widget, and canvas
    image1 = PIL.Image.new("RGB", (600, 200), (255, 255, 255))
    text.delete(1.0, END)
    draw = ImageDraw.Draw(image1)
    draw_board.delete('all')
    # Reactivate drawing event
    draw_board.bind('<Button-1>', activate_event)
    # Reset lastx and lasty
    lastx, lasty = None, None
    loaded_image = None  # Reset loaded_image
    # Clear draw history
    draw_history = []
    draw_history_index = -1

# Function to draw lines when mouse button is pressed and moved
def draw_lines(event):
    global lastx, lasty, draw_history
    x, y = event.x, event.y
    draw_board.create_line((lastx, lasty, x, y), width=8, fill=draw_color, capstyle=ROUND, smooth=TRUE, splinesteps=12)
    draw.line([lastx, lasty, x, y], fill=draw_color, width=10)
    lastx, lasty = x, y
    # Append to draw history
    draw_history.append(image1.copy())

# Function to activate drawing event
def activate_event(event):
    global lastx, lasty
    lastx, lasty = event.x, event.y
    draw_board.bind('<B1-Motion>', draw_lines)

# Function to predict and speak the handwritten digit
def predict_and_speak():
    global lastx, lasty, image1, loaded_image
    if (lastx is None and lasty is None or image1 is None) and loaded_image is None:
        # If no drawing has been made and no image has been loaded, display an error message
        messagebox.showerror("Error", "Please draw something or load an image to predict.")
        return
    try:
        if lastx is not None and lasty is not None:
            # If drawing has been done, proceed with the prediction
            text_num = []
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
            text.insert("end", final_text)
            
            print("Size of the image window:", image.shape[1], "x", image.shape[0])
            
            # Display the image
            cv2.imshow('image',image)
            
            engine = pyttsx3.init()

            # Iterate through predicted numbers and convert them to speech
            for digit in text_num:
                engine.say(f"The predicted number is {digit}.")
                engine.runAndWait()

            # Destroy pyttsx3 engine instance
            engine.stop()
            cv2.waitKey(0)

            # Reset lastx and lasty after making predictions
            lastx, lasty = None, None

        elif loaded_image is not None:
            # If no drawing, try to predict directly from the loaded image
            text_num = []
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
            text.insert("end", final_text)
            cv2.imshow('image', image)
            engine = pyttsx3.init()

            # Iterate through predicted numbers and convert them to speech
            for digit in text_num:
                engine.say(f"The predicted number is {digit}.")
                engine.runAndWait()

            # Destroy pyttsx3 engine instance
            engine.stop()
            cv2.waitKey(0)

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred while predicting: {str(e)}")
        # Clear canvas and text widget in case of error
        clear_widget()

# Function to save the image
def save_image():
    global image1
    try:
        filename = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png"), ("All Files", "*.*")])
        if filename:
            image1.save(filename)
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred while saving the image: {str(e)}")

# Function to load an image
def load_image():
    global image1, loaded_image
    try:
        filename = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
        if filename:
            # Open the selected image file
            loaded_image = Image.open(filename)
            # Resize the image to fit the canvas
            loaded_image = loaded_image.resize((600, 200))
            # Display the image on the canvas
            draw_board.create_image(0, 0, anchor=NW, image=ImageTk.PhotoImage(loaded_image))
            # Update the PIL image object
            image1 = loaded_image.copy()
            # Clear the text widget
            text.delete(1.0, END)
            # Call predict_and_speak function to predict from the loaded image
            predict_and_speak()
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred while loading the image: {str(e)}")

# Function to select drawing color
def choose_color():
    global draw_color
    color = colorchooser.askcolor(title="Choose Drawing Color", initialcolor=draw_color)
    if color:
        draw_color = color[1]

win=Tk()
win.geometry("700x600")  # Set the window size
win.title("Multiple Handwritten Digit Recognition")
win.config(background="#00ADA9")  # Light gray background

# Define font style
fontStyle = tkFont.Font(family="Arial", size=15, slant="italic")

# Label for instructions
write_label = Label(win, text="Draw your number:", bg="#FFC0CB", font=fontStyle, fg="white")
write_label.place(relx=0.03, rely=0.03)

# Create canvas for drawing
draw_board = Canvas(win, width=500, height=250, bg='white')  # Decrease height further
draw_board.place(relx=0.03, rely=0.1, relwidth=0.94, relheight=0.3)  # Adjust the placement and relative size
draw_board.bind('<Button-1>', activate_event)

# Create PIL image and draw object for drawing on canvas
image1 = PIL.Image.new("RGB", (600, 200), (255, 255, 255))
draw = ImageDraw.Draw(image1)

# Button to predict and speak the digit
button = Button(text="PREDICT and SPEAK", command=predict_and_speak, bg="#FFC0CB", font=tkFont.Font(family="Arial", size=15, slant="italic"), relief=RAISED)
button.place(relx=0.5, rely=0.45, anchor=CENTER)  # Adjusted position

# Label to display predicted number
predict_label = Label(win, text="Predicted Number:", bg="#FFB06B", font=tkFont.Font(family="Arial", size=15, slant="italic"))
predict_label.place(relx=0.4, rely=0.55)  # Adjusted position

# Text widget to display predicted number
text = Text(win, height=2, width=18, font=tkFont.Font(family="Arial", size=13), relief=RAISED)
text.place(relx=0.4, rely=0.62)  # Adjusted position

# Button to clear canvas and text widget
del_btn = Button(win, text="CLEAR ALL", command=clear_widget, width=10, font=tkFont.Font(family="Arial", size=15, slant="italic"), relief=RAISED)
del_btn.place(relx=0.03, rely=0.73)  # Adjusted position

# Button to load an image
load_btn = Button(win, text="LOAD IMAGE", command=load_image, width=12, font=tkFont.Font(family="Arial", size=15, slant="italic"), relief=RAISED)
load_btn.place(relx=0.4, rely=0.73)  # Adjusted position

# Button to save the drawn digit as an image file
save_btn = Button(win, text="SAVE IMAGE", command=save_image, width=12, font=tkFont.Font(family="Arial", size=15, slant="italic"), relief=RAISED)
save_btn.place(relx=0.75, rely=0.73)  # Adjusted position

# Button to select drawing color
color_btn = Button(win, text="SELECT COLOR", command=choose_color, width=14, font=tkFont.Font(family="Arial", size=15, slant="italic"), relief=RAISED)
color_btn.place(relx=0.03, rely=0.82)  # Adjusted position

# Run the tkinter event loop
win.mainloop()
