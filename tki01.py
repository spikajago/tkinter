#Steven Pikajago IT-24
#04.02.2025
import tkinter as tk
def main():
    aken = tk.Tk()
    aken.title("Minu esimene Tkinteri aken")
    aken.geometry("400x300")
   
    label = tk.Label(aken, text="Tere, maailm!").pack()
    button = tk.Button(aken, text="Sulge", command=aken.destroy).pack()
   
    aken.mainloop()

if __name__ == "__main__":
    main()