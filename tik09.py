#Steven Pikajago IT-24
#12.02.2025
import tkinter as tk

aken = tk.Tk()
aken.title("Raadionuppude näide")

def show_selection():
    print("Hind:", selected_color.get())
    print(var1.get(), var2.get(), var3.get())

selected_color = tk.IntVar(value=5)

# Loome raadionupud
radio_red = tk.Radiobutton(aken, text="Väike (5€)", variable=selected_color, value=5)
radio_green = tk.Radiobutton(aken, text="Suur (8€)", variable=selected_color, value=8)
radio_blue = tk.Radiobutton(aken, text="Pere (12€)", variable=selected_color, value=12)
radio_red.pack()
radio_green.pack()
radio_blue.pack()

var1 = tk.StringVar(value=0)
var2 = tk.StringVar(value=0)
var3 = tk.StringVar(value=0)

checkbox1 = tk.Checkbutton(aken, text="juust (+1€)", variable=var1, onvalue=1, offvalue=0)
checkbox2 = tk.Checkbutton(aken, text="Pepperoni(+1.5€)", variable=var2, onvalue=1.5, offvalue=0)
checkbox3 = tk.Checkbutton(aken, text="seen(+1€)", variable=var3, onvalue=1, offvalue=0)
checkbox1.pack()
checkbox2.pack()
checkbox3.pack()

btn_confirm = tk.Button(aken, text="Kinnita valik", command=show_selection)
btn_confirm.pack()

aken.mainloop()