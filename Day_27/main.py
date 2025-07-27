import tkinter

window = tkinter.Tk()
window.title("Mile to Km Converter")
# window.minsize(width=500, height=300)
window.config(padx=20, pady= 20)

def convert():
    """This function collects the miles value, converts it to kilometer and displays the converted value"""
    miles = float(miles_input.get())
    km = miles * 1.609
    km_value.config(text=f"{km}")

#create label to show what it is equal to
equal_label = tkinter.Label(text="Is equal to")
equal_label.grid(column=0, row=1)

#create entry to input values for conversion
miles_input = tkinter.Entry(width=7)
miles_input.grid(column=1, row=0)

km_value = tkinter.Label(text="0")
km_value.grid(column=1, row=1)

#create button to calculate the conversion
button = tkinter.Button(text="Calculate", command=convert)
button.grid(column=1, row=2)

#label to show miles
miles_label = tkinter.Label(text="Miles")
miles_label.grid(column=2, row=0)

#label to show kilometer
km_label = tkinter.Label(text="Km")
km_label.grid(column=2, row=1)






window.mainloop()