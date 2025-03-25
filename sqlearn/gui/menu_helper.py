import tkinter as tk
from tkinter import Menu


class Mnu:
    def __init__(self, context):
        self.context = context
    
   
    def main_mnu(self, mnu_content):
        menubar = Menu(self.context)
        self.context.config(menu=menubar)
        
        curr_menu = Menu(menubar)
        menubar.add_cascade(label='File', menu=curr_menu)
        curr_menu.add_command(label="Open", command=self.context.destroy)
        curr_menu.add_command(label="Save", command=self.context.destroy)
        curr_menu.add_command(label="Save as", command=self.context.destroy)
        curr_menu.add_separator()
        curr_menu.add_command(label="Exit", command=self.context.destroy)
        
        curr_menu = Menu(menubar)
        menubar.add_cascade(label='Objects', menu=curr_menu)
        
        for label in mnu_content:
            curr_menu.add_command(label=label, command=mnu_content[label])    
        
        
        
        return menubar