import tkinter as tk
from sqlearn.gui.menu_helper import Mnu
from pandastable import Table

class App:
    
    
    def __init__(self):
        self.root = tk.Tk()
        self.root.state("zoomed")
        self.root.title("Example GUI App with TK")

    
    def run(self, df):
        mnu_ct = {"Customers": self.save_me, "Cities": self.save_me, "Countries": self.save_me}

        mnu_help = Mnu(self.root)
        mnu_help.main_mnu(mnu_ct)
        frame = tk.Frame(self.root, bg="#c0c0c0")
        frame.place(relheight=0.9, relwidth=1)

        my_table = Table(frame, dataframe=df)
        my_table.grid(row=1, column=2)
        my_table.show()

        lbl = tk.ttk.Button(self.root, text="Save", command=self.save_me)
        lbl.grid(row=1, column=2)

        return self.root
        
    def save_me(self):
            """ Mock method
            """
            print("Implement persisting functionality")