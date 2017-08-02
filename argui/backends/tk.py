import tkinter as tk

class ArgumentDialogTk(tk.Frame):
    def __init__(self, parser):
        self.parser = parser
        super().__init__(self, master=None)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=root.destroy)
        self.quit.pack(side="bottom")

    def say_hi(self):
        print("hi there, everyone!")

def show_dialog_tk(parser):
    root = tk.Tk()
    dialog = ArgumentDialogTK(parser, master=root)
    dialog.mainloop()
