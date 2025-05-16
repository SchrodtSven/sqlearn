import numpy as np
import pandas as pd
import sqlite3


conn = sqlite3.connect("tmp/Chinook.db")
df = pd.read_sql_query("SELECT * FROM tracks", con=conn)

print(df.keys())
exit(234)




cond = [df["Milliseconds"] < 400000, df["Milliseconds"] > 600000]

choice = ["short", "long"]

df["trackLength_descr"] = np.select(
    condlist=cond, choicelist=choice, default="In the middle of nowhere"
)




def classify_length(milliseconds):
    return "long" if milliseconds > 200000 else "short"


df['track_classified'] = df["Milliseconds"].apply(classify_length)

print(df['trackLength_descr'].unique())

