import tkinter
import tkinter.messagebox


class MPG:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.title('Miles Per Gallon Calculator')

        self.input_frame = tkinter.Frame()
        self.button_frame = tkinter.Frame()

        self.prompt1_label = tkinter.Label(self.input_frame, text="Enter how many gallons your car holds: ", width=50)
        self.gallon_entry = tkinter.Entry(self.input_frame)
        self.prompt2_label = tkinter.Label(self.input_frame, text="How many miles have you traveled: ")
        self.miles_entry = tkinter.Entry(self.input_frame)
        self.prompt1_label.pack()
        self.gallon_entry.pack()
        self.prompt2_label.pack()
        self.miles_entry.pack()

        self.convert_button = tkinter.Button(self.button_frame, text="Convert", command=self.convert)
        self.quit_button = tkinter.Button(self.button_frame, text='Quit', command=self.main_window.destroy)
        self.convert_button.pack(side='left')
        self.quit_button.pack(side='right')

        self.input_frame.pack()
        self.button_frame.pack()
        tkinter.mainloop()

    def convert(self):
        miles = float(self.miles_entry.get())  # Convert miles and gallons to floats
        gallons = float(self.gallon_entry.get())
        mpg = miles / gallons
        tkinter.messagebox.showinfo('Results', f"Converted to miles per gallons: {mpg:.2f}")


if __name__ == '__main__':
    MPG()
