from tkinter import *
from tkinter import ttk

class mainApp(Tk):
    size='400x600'
    
    def __init__(self):
        Tk.__init__(self)
        
        self.geometry(self.size)
        self.title('Calculadora de numeros romanos')
        self.configure(bg='yellowgreen')
    
    def start(self):
        self.mainloop()
    
if __name__ == "__main__":
    app=mainApp()
    app.start()

ttk.Button
ttk.Radiobutton
ttk.Entry