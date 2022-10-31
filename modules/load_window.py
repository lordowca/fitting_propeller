import tkinter as tk
import os
from propeller_bv_legend import PropellerBVLegend
from propeller_dnv_legend import PropellerDNVLegend
from propeller_lr_legend import PropellerLRLegend


class OpenWindow(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master

    def open_new_window(self, file_name):
        self.master.withdraw()
        os.system(file_name)
        self.master.deiconify()

    def load_top_window(self, file_name):
        if file_name == 'propeller_bv_legend.py':
            top = tk.Toplevel()
            PropellerBVLegend(master=top)
        if file_name == 'propeller_dnv_legend.py':
            top = tk.Toplevel()
            PropellerDNVLegend(master=top)
        if file_name == 'propeller_lr_legend.py':
            top = tk.Toplevel()
            PropellerLRLegend(master=top)
