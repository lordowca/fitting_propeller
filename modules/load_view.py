import tkinter as tk
from twopoint import TwoPointDiagrams
from fourpoint import FourPointDiagrams
from propeller_bv import PropellerBV
from propeller_dnv import PropellerDNV
from propeller_lr import PropellerLR
from database.db import Database

db = Database('database/ships.db')


class OpenView(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master

    def open_view_window(self, record):

        self.id = record['values'][0]
        row = db.fetch_one_row(self.id)
        self.ship_name = row[1]
        self.values = row[2]
        self.file_name = row[5]

        if self.file_name == 'twopoint.py':
            top = tk.Toplevel()
            TwoPointDiagrams(master=top, id_from_list=self.id, ship_name=self.ship_name,
                             values=self.values, view=True)
        if self.file_name == 'fourpoint.py':
            top = tk.Toplevel()
            FourPointDiagrams(master=top, id_from_list=self.id, ship_name=self.ship_name,
                              values=self.values, view=True)
        if self.file_name == 'propeller_bv.py':
            top = tk.Toplevel()
            PropellerBV(master=top, id_from_list=self.id, ship_name=self.ship_name,
                        values=self.values, view=True)

        if self.file_name == 'propeller_dnv.py':
            top = tk.Toplevel()
            PropellerDNV(master=top, id_from_list=self.id, ship_name=self.ship_name,
                         values=self.values, view=True)

        if self.file_name == 'propeller_lr.py':
            top = tk.Toplevel()
            PropellerLR(master=top, id_from_list=self.id, ship_name=self.ship_name,
                        values=self.values, view=True)
