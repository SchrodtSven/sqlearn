import tkinter as tk
import pandas as pd
from sqlearn.gui.app import App
from sqlearn.core.query import Query


q = Query()
dta = q.exc("SELECT * FROM Py").f_all()

df = pd.DataFrame(columns=dta[0].keys(), data=dta)


if __name__ == '__main__':
    app = App()
    app.run(df).mainloop()    
