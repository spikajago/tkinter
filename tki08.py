#Steven Pikajago IT-24
#12.02.2025
import tkinter as tk
from tkinter import filedialog
from pathlib import Path

selected_files=[]

def open_directory():
    directory = filedialog.askdirectory()
    if directory:
        dir_label.config(text=f"Valitud kaust: {directory}")
        kausta_sisu=os.listdir(directory)
        for fail in kausta_sisu:
            file_name, file_extension=os.path
    else:
        dir_label.config(text="Kausta ei valitud.")


aken = tk.Tk()
aken.title("Peamine aken")

open_button = tk.Button(aken, text="Ava kaust", command=open_directory)
open_button.pack(pady=10)

dir_label = tk.Label(aken, text="")
dir_label.pack(pady=10)