import tkinter as tk
from typing import Text

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")
      
        self.fred = tk.Button(self,fg="red")  ## eu criei 
        self.fred["text"] = "Testando o fred"
        self.fred.pack(side="left")

        self.fred2 = tk.Button(self,fg="red",bg='blue',bd=5) #testando estilos
        self.fred2["text"] = "Testando o fred"
        self.fred2.pack(side="left")

    def say_hi(self):
        print("hi there, everyone!")




root = tk.Tk()
app = Application(master=root)
app.mainloop()