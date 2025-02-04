#Steven Pikajago IT-24
#04.02.2025
import tkinter as tk
from PIL import Image, ImageTk

def loe_fail(failinimi):
    with open(failinimi, 'r', encoding='utf-8') as file:
        return file.read()
def kuva_pilt(aken, failinimi, laius, korgus):
    pilt = Image.open(failinimi)
    pilt = pilt.crop((0, 0,laius,korgus)) 
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
    
    kuva_pilt(aken, "chun.jpg", 200, 200)
    aken.mainloop()
    tekst = tk.Text(aken, wrap=tk.WORD)
    scrollbar = tk.Scrollbar(aken, command=tekst.yview)
    tekst.config(yscrollcommand=scrollbar.set)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    tekst.pack(expand=True, fill=tk.BOTH)

    failisisu = loe_fail("text.txt")
    tekst.insert(tk.INSERT, failisisu)
if __name__ == "__main__":
    main()