#  import necessary libraries
import tkinter as tk       #  for making gui
import tensorflow as tf    #  used for deep learning, creating models
import numpy as np         #  for working with arrays and scientific computation
import win32gui            #  for locating a window
import keras               #  to build deep learning models
from PIL import ImageGrab  #  to deal with image related tasks

#  function that extracts the character image drawn on the canvas screen and returns it 
def get_img() :
    canvas_screen_id = canvas_screen.winfo_id()  #  returns identifier id for canvas widget
    canvas_screen_rect = win32gui.GetWindowRect(canvas_screen_id)  #  getting the canvas from its id
    drawn_image = ImageGrab.grab(canvas_screen_rect)  #  store the canvas content i.e the drawn character
    drawn_image = drawn_image.resize((28, 28))  #  resize image to 28x28 size
    drawn_image = drawn_image.convert("L")  #  convert to grayscale image
    drawn_image = np.array(drawn_image)     #  convert image to pixels array 
    drawn_image = drawn_image.reshape((1, 28, 28, 1))  #  reshape image to suit cnn model input
    drawn_image = drawn_image / 255.0  #  normalize pixel array
    return drawn_image  #  return image's pixel array to calling function

#  function to clear the canvas screen, scr_clear_but button is bind to this function
def scr_clear(event) :
    canvas_screen.delete("all")  #  clears everything drawn on the canvas

#  function to predict the character drawn on the canvas
def pred_char(event) :
    class_names = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
                   'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 
                   'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']  #  names of all classes/labels 
    model_use = tf.keras.models.load_model("cnn_model")  #  loading the cnn model, to be used for prediction
    
    drawn_char = get_img()  #  getting the image drawn on the canvas, in form of array and reshaped for the cnn model
    pred_char_prob = model_use.predict(drawn_char)  #  predicting the drawn image, returns prediction probabilities for each label   
    ind = pred_char_prob.argmax()  #  get index of the label with highest prediction probability
    
    message_box = tk.Toplevel(pred_GUI)  #  a gui to display the prediction message
    message_box.title("Prediction")  #  title of the message box
    message_box.geometry(f"260x80+{550}+{550}")  #  size of the message box, and its position on the main window
    message_info = tk.Label(message_box, text = f"Recognized Character :  {class_names[ind]}", foreground = "green", font = ('Helvetica 15 underline'))  #  print the prediction
    message_info.pack()  #  places message to display in the message box

#  function that helps to draw on canvas, canvas_screen is bind to this function
def mouse_move(event) :
    x = event.x  #  gives x coordinate of mouse pointer position
    y = event.y  #  gives y coordinate of mouse pointer
    canvas_screen.create_oval(x, y, x, y, fill = "white", outline = "white", width = 25)  #  draws ovals accordingly as the mouse pointer is moved on the canvas screen

#  function that closes the application, close_but button is bind to this
def close_app(event) :
    pred_GUI.destroy()  #  destroys the pred_GUI window

#  function to bind buttons, canvas screen to events to perform tasks when buttons are pressed
def define_events() :
    scr_clear_but.bind("<Button-1>", scr_clear)  #  means when left mouse button is pressed, perform work defined in function scr_clear() 
    pred_but.bind("<Button-1>", pred_char)
    close_but.bind("<Button-1>", close_app)
    canvas_screen.bind("<B1-Motion>", mouse_move)  #  means when left mouse button is pressed and mouse moved in canvas, do work defined in mouse_move() 

#  function to place buttons at suitable place in gui
def place_GUI() :
    l.pack()  #  pack() declares the position of widgets in relation to each other
    scr_clear_but.pack(side = "left")
    pred_but.pack(side = "left")
    close_but.pack(side = "right")
    canvas_screen.pack()
    but_frame.pack()


#  create the main window
pred_GUI = tk.Tk()  #  used to create the root window
pred_GUI.geometry("900x700")  #  dimensions of the main window
pred_GUI.title("Character Recognition Using Deep Learning")  #  set title of the window

#  creating a label to display instruction
l = tk.Label(text = "\nNote : Click left mouse button and move over the black screen to draw the desired character\n", foreground = "red", font = 23)

#  create button frame to place buttons
but_frame = tk.Frame(pred_GUI)  #  creates a frame on pred_GUI window

#  creating buttons to place in button frame
scr_clear_but = tk.Button(but_frame, text = "Clear Screen", background = "yellow", foreground = "black", font = 13)  #  button to clear screen
pred_but = tk.Button(but_frame, text = "Click for Prediction", background = "yellow", foreground = "black", font = 13)  #  button to predict character
close_but = tk.Button(but_frame, text = "Close", background = "yellow", foreground = "black", font = 13)  #  button to exit from app

#  create canvas screen to draw character on it
canvas_screen = tk.Canvas(pred_GUI, bg = "black", width = "360", height = "360")  #  canvas helps to draw in a window, bg means background

#  function called for placing buttons in gui
place_GUI()

#  function called for binding buttons, canvas to their respective events
define_events()

pred_GUI.mainloop()  #  running the tkinter event loop, listens for events like button press, etc. until window is closed