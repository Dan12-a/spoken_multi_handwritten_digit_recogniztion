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


![Screenshot 2024-03-24 153418](https://github.com/Dan12-a/spoken_multi_handwritten_digit_recogniztion/assets/119096073/907251d1-d0b8-44c5-9357-7dc6ae1e6584)
![Screenshot 2024-03-24 153459](https://github.com/Dan12-a/spoken_multi_handwritten_digit_recogniztion/assets/119096073/a8dc1777-bac2-49fa-80c5-6762571ef252)
![Screenshot 2024-03-24 153516](https://github.com/Dan12-a/spoken_multi_handwritten_digit_recogniztion/assets/119096073/aa7d3934-aa08-4a04-aae2-f507c8c4d94d)
![Screenshot 2024-03-24 153545](https://github.com/Dan12-a/spoken_multi_handwritten_digit_recogniztion/assets/119096073/191ba356-864c-4bb5-8eb6-84f67afb10c2)
![Screenshot 2024-03-24 153623](https://github.com/Dan12-a/spoken_multi_handwritten_digit_recogniztion/assets/119096073/fb3085fb-09fe-4280-b7f8-67f33380218e)
![Screenshot 2024-03-24 155248](https://github.com/Dan12-a/spoken_multi_handwritten_digit_recogniztion/assets/119096073/ce53225e-c882-499e-a01e-425b62afb13f)

