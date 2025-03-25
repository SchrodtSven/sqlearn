import tkinter as tk
from pandastable import Table
import pandas as pd
from sqlearn.core.query import Query
from sqlearn.gui.menu_helper import Mnu

q = Query()
dta = q.exc("SELECT * FROM Customer").f_all()

df = pd.DataFrame(columns=dta[0].keys(), data=dta)


# print(df.head())
def save_me():
    print("Implement persisting functionality")


root = tk.Tk()
root.state("zoomed")

mnu_ct = {"Customers": save_me, "Cities": save_me, "Countries": save_me}

mnu_help = Mnu(root)
mnu_help.main_mnu(mnu_ct)
frame = tk.Frame(root, bg="#c0c0c0")
frame.place(relheight=0.9, relwidth=1)

my_table = Table(frame, dataframe=df)
my_table.grid(row=1, column=2)
my_table.show()

lbl = tk.ttk.Button(root, text="Save", command=save_me)
lbl.grid(row=1, column=2)

root.mainloop()
