import tkinter

window = tkinter.Tk()
window.minsize(250, 150)
window.title("Mile to Km Converter")
window.config(padx=25, pady=25)


def miles_to_km():
    miles = float(entry.get())
    km = round(miles * 1.609, 3)
    km_result.config(text=km)


is_equal_to = tkinter.Label(text="is equal to")
is_equal_to.grid(column=0, row=1)

entry = tkinter.Entry(width=10)
entry.grid(column=1, row=0)

km_result = tkinter.Label(text="0")
km_result.grid(column=1, row=1)

button = tkinter.Button(text="Calculate", command=miles_to_km)
button.grid(column=1, row=2)

label1 = tkinter.Label(text="Miles")
label1.grid(column=2, row=0)

label2 = tkinter.Label(text="Km")
label2.grid(column=2, row=1)

window.mainloop()
