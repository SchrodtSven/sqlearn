import tkinter as tk
from sqlearn.gui.file import File

class Mnu:
    def __init__(self, context):
        self.context = context
        self.file = File()
    
   
    def main_mnu(self, mnu_content):
        menubar = tk.Menu(self.context)
        self.context.config(menu=menubar)
        
        curr_menu = tk.Menu(menubar)
        menubar.add_cascade(label='File', menu=curr_menu)
        curr_menu.add_command(label="New", command=self.file.new)
        curr_menu.add_command(label="Open", command=self.file.open)
        curr_menu.add_command(label="Save", command=self.file.save)
        curr_menu.add_command(label="Save as", command=self.file.save_as)
        curr_menu.add_separator()
        curr_menu.add_command(label="Exit", command=self.context.destroy)
        
        curr_menu = tk.Menu(menubar)
        menubar.add_cascade(label='Objects', menu=curr_menu)
        
        for label in mnu_content:
            curr_menu.add_command(label=label, command=mnu_content[label])    
        
        
        
        return menubar