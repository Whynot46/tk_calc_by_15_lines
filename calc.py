import tkinter as tk
window = tk.Tk()
c,r = 0,1
calc_entry = tk.Entry(window, width = 33)
calc_entry.grid(row=0, column=0)
def calc(key):
    if str(key) == '=':calc_entry.insert(tk.END,'=' + str(eval(calc_entry.get())))
    elif key == 'c':calc_entry.delete(0,tk.END)
    elif key != '=' or key != 'c': calc_entry.insert(tk.END,key)
for i in ["7", "4", "1", "/", "8", "5", "2","0", "9", "6", "3", "*", "c", "-", "+", ".",'(',')','**','=']:
    buttons = tk.Button(text=i,width = 10, command=lambda x=i: calc(x)).grid(column=r, row=c)
    c += 1
    if c > 3:
        c, r = 0, r+1
window.mainloop()