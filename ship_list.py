import tkinter as tk
from tkinter import ttk, messagebox
from modules.load_view import OpenView
from modules.lang_module import LangTextDisplay
from database.db import Database


lg = LangTextDisplay(file_name='ship_list')
db = Database('database/ships.db')

FONT_HEADER = ('Helvetica', 22, 'bold')
FONT_MIDLE_SIZE = ('Helvetica', 16, 'bold')
FONT_NORMAL_BOLD = ('Helvetica', 12, 'bold')
FONT_NORMAL = ('Helvetica', 12)


class ShipList(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.ov = OpenView(self.master)
        self.record = ''

        self.master.title(lg.set_lang_text('SHIP_LIST_TITLE'))
        # window parametrs and position
        self.app_width = 900
        self.app_height = 750
        self.app_center_x = int(
            self.winfo_screenwidth() / 2 - self.app_width/2)
        self.app_center_y = int(
            self.winfo_screenheight() / 2 - self.app_height/2)
        self.master.geometry(
            f'{self.app_width}x{self.app_height}+{self.app_center_x}+{self.app_center_y}')

        self.list_box()

    def list_box(self):
        self.upper_frame = tk.Frame(self.master)
        self.upper_frame.place(height=150, x=10, relwidth=0.95)
        self.title_label = tk.Label(
            self.upper_frame, text=lg.set_lang_text('SHIP_LIST_LISTBOX_HEADER'), font=FONT_HEADER)
        self.title_label.place(y=10, relwidth=1)

        self.load_item_tree = tk.Button(
            self.upper_frame, text='Load', command=self.load_ship)
        self.load_item_tree.place(x=10, width=100, y=100)
        self.deleted_item_tree = tk.Button(
            self.upper_frame, text=lg.set_lang_text('SHIP_LIST_DELETE_BUTTON'), command=self.delete_record)
        self.deleted_item_tree.place(x=120, width=100, y=100)

        self.refresh_tree = tk.Button(
            self.upper_frame, text=lg.set_lang_text('SHIP_LIST_REFRESH_BUTTON'), command=self.polulate_list)
        self.refresh_tree.place(x=230, width=100, y=100)

        self.ship_list_frame = tk.Frame(self.master)
        self.ship_list_frame.place(relheight=1, y=150, relwidth=1)

        self.ship_list()

    def ship_list(self):
        self.columns = ('id', 'ship', 'creat_date', 'update_date')

        self.style_tree = ttk.Style()
        self.style_tree.theme_use('default')
        self.style_tree.configure("Treeview",
                                  font=FONT_NORMAL,
                                  rowheight=30,
                                  bordercolor='#bdbdbd',
                                  borderwidth=2)

        self.style_tree.configure(
            "Treeview.Heading", font=FONT_NORMAL_BOLD)

        self.tree = ttk.Treeview(self.ship_list_frame,
                                 columns=self.columns, show="headings", height=18)
        self.tree.heading('id', text=lg.set_lang_text('SHIP_LIST_TREE_COL1'))
        self.tree.heading('ship', text=lg.set_lang_text('SHIP_LIST_TREE_COL2'))
        self.tree.heading(
            'creat_date', text=lg.set_lang_text('SHIP_LIST_TREE_COL3'))
        self.tree.heading(
            'update_date', text=lg.set_lang_text('SHIP_LIST_TREE_COL4'))

        self.tree.column('id', width=60, anchor=tk.CENTER)
        self.tree.column('ship', width=200, anchor=tk.CENTER)
        self.tree.column('creat_date', width=295, anchor=tk.CENTER)
        self.tree.column('update_date', width=295, anchor=tk.CENTER)

        self.tree.bind('<<TreeviewSelect>>', self.selected_item_tree_id)

        self.polulate_list()
        self.tree.grid(row=0, column=0, sticky='nsew', padx=10, pady=10)

        self.scrollbar_tree = ttk.Scrollbar(
            self.ship_list_frame, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscrollcommand=self.scrollbar_tree.set)
        # self.scrollbar_tree.place(x=590)
        self.scrollbar_tree.grid(
            row=0, column=1, sticky='ns')

    def polulate_list(self):
        for i in self.tree.get_children():
            self.tree.delete(i)
        for row in db.fetch():
            self.tree.insert('', tk.END, values=(
                row[0], row[1], row[3], row[4]))

    def selected_item_tree_id(self, event):
        for seleted_item in self.tree.selection():
            item = self.tree.item(seleted_item)
            self.record = item

    def delete_record(self):
        if self.record == '':
            messagebox.showerror(lg.set_lang_text(
                'SHIP_LIST_TITLE_MESSAGEBOX_1'), lg.set_lang_text('SHIP_LIST_INFO_MESSAGEBOX_1'))
        else:
            question = messagebox.askyesno(lg.set_lang_text(
                'SHIP_LIST_TITLE_MESSAGEBOX_2'), lg.set_lang_text('SHIP_LIST_INFO_MESSAGEBOX_2'))
            if question == True:
                db.remove_item(self.record['values'][0])
                messagebox.showinfo(lg.set_lang_text(
                    'SHIP_LIST_TITLE_MESSAGEBOX_3'), lg.set_lang_text('SHIP_LIST_INFO_MESSAGEBOX_3'))
                self.ship_list()
                self.record = ''
            elif question == False:
                self.record = ''

    def load_ship(self):
        if self.record == '':
            messagebox.showerror(lg.set_lang_text(
                'SHIP_LIST_TITLE_MESSAGEBOX_1'), lg.set_lang_text('SHIP_LIST_INFO_MESSAGEBOX_1'))
        else:
            self.ov.open_view_window(self.record)


if __name__ == "__main__":
    root = tk.Tk()
    app = ShipList(master=root)
    app.mainloop()
