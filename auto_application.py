import os
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw() # Prevents an empty tkinter window from opening

print("Pick a directory to store job files:")

file_path = filedialog.askdirectory()

print("You have selected: ", file_path)
os.chdir(file_path)

if not os.path.exists(os.getcwd() + "\job applications"):
    os.mkdir('job applications')

if not os.path.exists(os.getcwd() + "\resumes"):
    os.mkdir('resumes')
