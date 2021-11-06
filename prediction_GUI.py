#  import necessary libraries
import tkinter as tk       #  for making gui
import tensorflow as tf    #  used for deep learning, creating models
import numpy as np         #  for working with arrays and scientific computation
import win32gui            #  for locating a window
import keras               #  to build deep learning models
from PIL import ImageGrab  #  to deal with image related tasks

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

pred_GUI.mainloop()  #  running the tkinter event loop, listens for events like button press, etc. until window is closed 