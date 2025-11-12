Keylogger Program using pynput
Overview
This project is a simple Python program that demonstrates how to capture and log keyboard input using the pynput library. It listens for key presses and records them into a text file named key_log.txt. The program is intended for educational purposes to show how event listeners and file handling work in Python.

Features
Records every key pressed on the keyboard.
Differentiates between printable characters and special keys.
Stores logs in a persistent text file (key_log.txt).

Runs continuously until manually stopped.
How It Works
The program imports the keyboard module from pynput.
A log file (key_log.txt) is defined as the destination for all keystrokes.
The on_press function handles key press events:
If the key has a char attribute (letters, numbers, symbols), it writes the character directly.
If the key does not have a char attribute (special keys like Enter, Shift, Ctrl), it writes the key name enclosed in square brackets.
A keyboard.Listener object is created to monitor key presses and call on_press whenever a key is pressed.
The listener runs indefinitely with listener.join(), keeping the program active until stopped.

Requirements
Python 3.x
pynput library
You can install pynput using:
bash
pip install pynput
Usage
Save the script to a file, for example keylogger.py.
Run the script:
bash
python keylogger.py
All keystrokes will be logged into key_log.txt in the same directory.
