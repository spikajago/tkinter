#Steven Pikajago IT-24
#04.02.2025
import tkinter as tk
from PIL import Image, ImageTk

def kuva_pilt(aken, failinimi, laius, korgus):
    pilt = Image.open(failinimi)
    pilt = pilt.crop((0, 0,laius us)) 
    foto = ImageTk.PhotoImage(pilt)
    label = tk.Label(aken, image=foto)
    label.image = foto
    label.pack()

def main():


    aken = tk.Tk()
    aken.title("Minu esimene Tkinteri aken")
    aken.geometry("400x300")
    aken.resizable(True, False)
    label = tk.Label(aken, text="Cuk Murris",font=("Arial",16,"bold"),fg="blue").pack()
    button = tk.Button(aken, text="Sulge", command=aken.destroy).pack()
    kuva_pilt(aken, "", 200, 200)
    aken.mainloop()

if __name__ == "__main__":
    main()