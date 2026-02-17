import tkinter as tk
root = tk.Tk()
root.title("Calculator")
root.configure(bg = "grey")
root.resizable(False,False)
entry = tk.Entry(
    root,
    font = ("Segoe UI", 20),
    bg = "Black",
    fg = "White",
    bd = 0,
    justify = "right"

)
entry.grid(row = 0, column = 0, columnspan = 4, padx = 12, pady = 12, ipady = 15)
def press(v):
    entry.insert(tk.END,v)
def clear():
    entry.delete(0, tk.END)
def calc():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except :
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

buttons = [
    "7","8","9","/",
    "4","5","6","*",
    "1","2","3","-",
    "0",".","=","+",
    "C"
]
row_val = 1
col_val = 0
for button in buttons:
    if button == "C":
        cmd = clear
    elif button == "=":
        cmd = calc
    else:
        cmd = lambda x=button: press(x)
    b = tk.Button(
        root,
        text = button,
        font = ("Segoe UI", 18),
        fg = "Black",
        bd = 0,
        width = 5,
        height = 2,
        bg="Orange" if button in {"+","-","*","/","="} else "White",
        command = cmd
    )
    b.grid(row = row_val, column = col_val, padx = 10, pady = 10)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1
root.mainloop()

