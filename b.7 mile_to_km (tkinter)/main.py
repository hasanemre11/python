import tkinter

window = tkinter.Tk()
window.title("title")
window.minsize(300, 100)
window.config(padx=20, pady=20)

miles = tkinter.Label(text="Miles", font=("Arial", 10))
miles.grid(row=0, column=2)

is_eq = tkinter.Label(text="is equal to", font=("Arial", 10))
is_eq.grid(row=1, column=0)

result = tkinter.Label(text="0", font=("Arial", 10))
result.grid(row=1, column=1)

km = tkinter.Label(text="Km", font=("Arial", 10))
km.grid(row=1, column=2)

entry = tkinter.Entry()
entry.grid(row=0, column=1)


def calculating():
    number = float(entry.get())
    result.config(text=f"{number * 1.6}")


calculate = tkinter.Button(text="Calculate", command=calculating)
calculate.grid(row=2, column=1)

window.mainloop()
