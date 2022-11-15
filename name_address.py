import tkinter
import tkinter.messagebox


class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.title('Info')

        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        self.name_value = tkinter.StringVar()
        self.street_value = tkinter.StringVar()
        self.city_value = tkinter.StringVar()

        self.name_label = tkinter.Label(self.top_frame, textvariable=self.name_value, width=30)
        self.street_label = tkinter.Label(self.top_frame, textvariable=self.street_value, width=30)
        self.city_label = tkinter.Label(self.top_frame, textvariable=self.city_value, width=30)

        self.name_label.pack()
        self.street_label.pack()
        self.city_label.pack()

        self.show_info_button = tkinter.Button(self.bottom_frame, text="Show Info", command=self.show_button)
        self.quit_button = tkinter.Button(self.bottom_frame, text="Quit", command=self.main_window.destroy)
        self.show_info_button.pack(side='left')
        self.quit_button.pack(side='right')

        self.top_frame.pack()
        self.bottom_frame.pack()
        tkinter.mainloop()

    def show_button(self):
        self.name_value.set("Sherlock Holmes")
        self.street_value.set('221B Baker Street')
        self.city_value.set('London, U.K.')


if __name__ == '__main__':
    MyGUI()
