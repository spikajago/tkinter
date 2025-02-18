#Steven Pikajago IT-24
#12.02.2025
import tkinter as tk
from tkinter import messagebox
mport ttkbootstrap as ttk
from ttkbootstrap.constants import *

# aken = tk.Tk()
aken = ttk.Window(themename="darkly")
aken.title("Raadionuppude näide")
aken.geometry("300x400")

def show_selection():
    # print("Hind:", selected_color.get())
    # print(var1.get(), float(var2.get()), var3.get())
    # print(selected_option.get())
    if selected_option.get()=="kuller":
        trans=3
    else:
        trans=0
    summa=selected_color.get()+ var1.get()+ float(var2.get())+ var3.get()+ trans
    messagebox.showinfo("Sinu pitsa summa", str(summa)+"€")

selected_color = tk.IntVar(value=5)

tk.Label(aken, text="Kasutaja ja ID", font="Arial 16").pack()
tk.Entry(aken).pack()

tk.Label(aken, text="Vali suurus", font="Arial 16").pack()

radio_red = tk.Radiobutton(aken, text="Väike (5€)", variable=selected_color, value=5)
radio_green = tk.Radiobutton(aken, text="Suur (8€)", variable=selected_color, value=8)
radio_blue = tk.Radiobutton(aken, text="Pere (12€)", variable=selected_color, value=12)
radio_red.pack()
radio_green.pack()
radio_blue.pack()

var1 = tk.IntVar(value=0)
var2 = tk.StringVar(value=0)
var3 = tk.IntVar(value=0)

tk.Label(aken, text="Vali lisandid", font="Arial 16").pack()

checkbox1 = tk.Checkbutton(aken, text="juust (+1€)", variable=var1, onvalue=1, offvalue=0)
checkbox2 = tk.Checkbutton(aken, text="Pepperoni(+1.5€)", variable=var2, onvalue="1.5", offvalue=0)
checkbox3 = tk.Checkbutton(aken, text="seen(+1€)", variable=var3, onvalue=1, offvalue=0)
checkbox1.pack()
checkbox2.pack()
checkbox3.pack()

tk.Label(aken, text="Vali kättetoimetamine", font="Arial 16").pack()

#dropdown
valikud = ["kuller", "kohapeal"]
selected_option = tk.StringVar()
selected_option.set("Vali üksus")

dropdown = tk.OptionMenu(aken, selected_option, *valikud)
dropdown.pack()


btn_confirm = tk.Button(aken, text="Kinnita valik", command=show_selection)
btn_confirm.pack()

aken.mainloop()