![Screenshot 2024-05-04 145935](https://github.com/Dan12-a/spoken_multi_handwritten_digit_recogniztion/assets/119096073/d6a006a9-5ba0-4913-a21c-aed14e4b36c7)
## Multiple Handwritten Digit Recognition with speak
This project demonstrates Multiple handwritten digit recognition using a convolutional neural network (CNN) trained on the MNIST dataset. The user can draw a digit on the canvas provided by the tkinter GUI, and the model predicts the handwritten digit, displaying it on the GUI and speaking the prediction aloud using text-to-speech functionality.

## Requirements
Python 3.x
Libraries:
tensorflow
keras
numpy
matplotlib
PIL
cv2
pyttsx3

## Usage
1. Ensure all dependencies are installed.
2.  You can Install the required libraries using pip:  
   pip install tensorflow keras numpy matplotlib pillow opencv-python pyttsx3
3. Run the Python 
4. A tkinter window will open with a canvas where you can draw a single digit.
5. After drawing the digit, click the "PREDICT and SPEAK" button.
6. The predicted digit will be displayed in the tkinter window and spoken aloud.
7. To clear the canvas and predicted digit, click the "CLEAR ALL" button.

## How it Works
- The script loads a pre-trained CNN model (`trained_model.p`) using pickle.
- Users draw a single digit on a canvas using the tkinter GUI.
- When the "PREDICT and SPEAK" button is clicked, the drawn digit is processed:
  - The drawn image is saved to a file (`image_out.png`).
  - OpenCV is used to preprocess the image (convert to grayscale, apply thresholding, find contours, etc.).
  - Each detected digit in the image is resized, padded, and fed into the CNN model for prediction.
  - The predicted digits are displayed on the tkinter window and spoken aloud using pyttsx3.
- Users can clear the canvas and predicted digit by clicking the "CLEAR ALL" button.

## File Descriptions
model_train.py,tkinter_gui.py:Python script containing the main functionality for handwritten digit recognition.
trained_model.p: Pre-trained CNN model saved using pickle.
README.md: This file, containing instructions and information about the project.

## Additionally, here's how you can **create** and **run** a Jupyter Notebook:
1. Open Jupyter Notebook by running jupyter notebook command in your terminal or command prompt.
2. Click on "New" -> click on "Folder".
3. After Creating "Folder" Click on that "Folder" . 
4. Click on "Upload" -> upload the (`trained_model.p`).
5. Click on "New" -> "Python 3" to create a new Python 3 notebook.
6. You can then start copy and paste to run code sucessfully.
7. Save your notebook with a meaningful name.
8. TO RUN JUST CLICK **RUN** ON JUPYTER NOTEBOOK**

## Additional Notes:
- The CNN model architecture and training code are adapted from the MNIST dataset example in Keras.
- Speech synthesis is achieved using the pyttsx3 library.
- The tkinter GUI framework is used for creating the drawing interface.

## ACCURACY=99%


![Screenshot 2024-05-04 150452](https://github.com/Dan12-a/spoken_multi_handwritten_digit_recogniztion/assets/119096073/9307d3a5-dbfc-45b1-8267-070ad19fdf88)
![Screenshot 2024-05-04 151422](https://github.com/Dan12-a/spoken_multi_handwritten_digit_recogniztion/assets/119096073/99fc30e7-f7db-4c49-bfae-2dc337d9be9a)
![Screenshot 2024-05-04 145935](https://github.com/Dan12-a/spoken_multi_handwritten_digit_recogniztion/assets/119096073/3397cc48-cb09-4284-b426-3bca83aa47c2)
![Screenshot 2024-05-04 150810](https://github.com/Dan12-a/spoken_multi_handwritten_digit_recogniztion/assets/119096073/52a6039e-668e-45c1-af80-44f958765bc3)
![Screenshot 2024-04-18 105530](https://github.com/Dan12-a/spoken_multi_handwritten_digit_recogniztion/assets/119096073/941fb2a8-92fd-47b8-bb6f-ea6ec598cdaa)
![Screenshot 2024-04-18 105151](https://github.com/Dan12-a/spoken_multi_handwritten_digit_recogniztion/assets/119096073/03847bfd-17ae-419b-a8c8-46ae0420076d)
![Screenshot 2024-04-18 105118](https://github.com/Dan12-a/spoken_multi_handwritten_digit_recogniztion/assets/119096073/010e3d8d-16e1-41d8-9ea8-846697e2386c)
