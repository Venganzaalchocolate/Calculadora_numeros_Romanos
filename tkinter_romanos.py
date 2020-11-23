from tkinter import *
from tkinter import ttk

class mainApp():
    root=Tk()
    
    root.geometry('400x600')
    root.title('Calculadora de numeros romanos')
    root.configure(bg='yellowgreen')
    
if __name__ == "__main__":
    app=mainApp()
    app.root.mainloop()