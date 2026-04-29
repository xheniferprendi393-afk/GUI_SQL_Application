import tkinter as tk


class FoodApp:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("my foodpanda app...")
        self.window.geometry("400x500")

        self.layout()


        self.window.mainloop()


    def layout(self):
        tk.Label(self.window,text="Fast Food App").pack()



app = FoodApp()
