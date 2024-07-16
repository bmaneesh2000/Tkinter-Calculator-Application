import tkinter as tk

root = tk.Tk()
root.title("Calculator")
root.geometry("640x500")
root.configure(bg='#708090')
root.resizable(False, False)

expression = ""
input_text = tk.StringVar()

def button_click(item):
    global expression
    expression += str(item)
    input_text.set(expression)

def clear():
    global expression
    expression = ""
    input_text.set("")

def calculate():
    global expression
    try:
        result = str(eval(expression))
        input_text.set(result)
        expression = result
    except:
        input_text.set("Error")
        expression = ""

input_frame = tk.Frame(root, height=50, bd=0, highlightbackground="black", highlightcolor="black", highlightthickness=2)
input_frame.pack(side=tk.TOP)

input_field = tk.Entry(input_frame, textvariable=input_text, font=('arial', 18, 'bold'), bd=0, insertwidth=4, width=50, justify=tk.RIGHT)
input_field.grid(row=0, column=0)
input_field.pack(ipady=10)

button_frame = tk.Frame(root)
button_frame.pack()

tk.Button(button_frame, text="C", font=('arial', 18, 'bold'), fg="black", width=10, height=3, bd=0, bg="#ff6666", cursor="hand2", command=clear).grid(row=1, column=0, padx=1, pady=1)
tk.Button(button_frame, text="/", font=('arial', 18, 'bold'), fg="black", width=10, height=3, bd=0, bg="#ff9966", cursor="hand2", command=lambda: button_click("/")).grid(row=1, column=1, padx=1, pady=1)
tk.Button(button_frame, text="*", font=('arial', 18, 'bold'), fg="black", width=10, height=3, bd=0, bg="#ffcc66", cursor="hand2", command=lambda: button_click("*")).grid(row=1, column=2, padx=1, pady=1)
tk.Button(button_frame, text="-", font=('arial', 18, 'bold'), fg="black", width=10, height=3, bd=0, bg="#ffff66", cursor="hand2", command=lambda: button_click("-")).grid(row=1, column=3, padx=1, pady=1)

tk.Button(button_frame, text="7", font=('arial', 18, 'bold'), fg="black", width=10, height=3, bd=0, bg="#99ff66", cursor="hand2", command=lambda: button_click("7")).grid(row=2, column=0, padx=1, pady=1)
tk.Button(button_frame, text="8", font=('arial', 18, 'bold'), fg="black", width=10, height=3, bd=0, bg="#66ff66", cursor="hand2", command=lambda: button_click("8")).grid(row=2, column=1, padx=1, pady=1)
tk.Button(button_frame, text="9", font=('arial', 18, 'bold'), fg="black", width=10, height=3, bd=0, bg="#66ff99", cursor="hand2", command=lambda: button_click("9")).grid(row=2, column=2, padx=1, pady=1)
tk.Button(button_frame, text="+", font=('arial', 18, 'bold'), fg="black", width=10, height=3, bd=0, bg="#66ffff", cursor="hand2", command=lambda: button_click("+")).grid(row=2, column=3, padx=1, pady=1)

tk.Button(button_frame, text="4", font=('arial', 18, 'bold'), fg="black", width=10, height=3, bd=0, bg="#66ccff", cursor="hand2", command=lambda: button_click("4")).grid(row=3, column=0, padx=1, pady=1)
tk.Button(button_frame, text="5", font=('arial', 18, 'bold'), fg="black", width=10, height=3, bd=0, bg="#6699ff", cursor="hand2", command=lambda: button_click("5")).grid(row=3, column=1, padx=1, pady=1)
tk.Button(button_frame, text="6", font=('arial', 18, 'bold'), fg="black", width=10, height=3, bd=0, bg="#6666ff", cursor="hand2", command=lambda: button_click("6")).grid(row=3, column=2, padx=1, pady=1)
tk.Button(button_frame, text="=", font=('arial', 18, 'bold'), fg="black", width=10, height=3, bd=0, bg="#9966ff", cursor="hand2", command=calculate).grid(row=3, column=3, padx=1, pady=1)

tk.Button(button_frame, text="1", font=('arial', 18, 'bold'), fg="black", width=10, height=3, bd=0, bg="#cc66ff", cursor="hand2", command=lambda: button_click("1")).grid(row=4, column=0, padx=1, pady=1)
tk.Button(button_frame, text="2", font=('arial', 18, 'bold'), fg="black", width=10, height=3, bd=0, bg="#ff66ff", cursor="hand2", command=lambda: button_click("2")).grid(row=4, column=1, padx=1, pady=1)
tk.Button(button_frame, text="3", font=('arial', 18, 'bold'), fg="black", width=10, height=3, bd=0, bg="#ff66cc", cursor="hand2", command=lambda: button_click("3")).grid(row=4, column=2, padx=1, pady=1)
tk.Button(button_frame, text="0", font=('arial', 18, 'bold'), fg="black", width=10, height=3, bd=0, bg="#ff6699", cursor="hand2", command=lambda: button_click("0")).grid(row=4, column=3, padx=1, pady=1)

root.mainloop()
