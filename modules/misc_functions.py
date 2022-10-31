
from genericpath import isdir
import tkinter as tk
from datetime import datetime
from modules.lang_module import LangTextDisplay
from database.db import Database
from pandastable import Table, config
from PIL import ImageTk, Image
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg,
    NavigationToolbar2Tk
)
import os

lg = LangTextDisplay(file_name='misc_functions')
db = Database('database/ships.db')


class MiscFunctions(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        date = datetime.now()
        self.date = date.strftime("%Y-%m-%d %H:%M:%S")

    def is_empty_str(self, list):
        return [True if i == '' else False for i in list]

    def is_empty_or_zero(self, list):
        return [True if i == '' or i == '0' else False for i in list]

    def prepare_parameters(self, list):
        return ';'.join(map(str, list[3:]))

    def insert_value_to_entry(self, entry_position, value_list):
        for i in range(len(entry_position)):
            entry_position[i].delete(0, tk.END)
            entry_position[i].insert(tk.END, value_list[i])

    def tabel_show(self, location, dataframe):
        self.table = Table(
            location, dataframe=dataframe, enable_menus=False)

        options = {'align': 'center', 'cellwidth': 180}
        config.apply_options(options, self.table)
        self.table.show()

    def string_to_float_greater_than_zero(self, list):
        float_list = []
        for i in list:
            try:
                i = i.replace(',', '.')
                i = float(i)
                if i >= 0:
                    float_list.append(float(i))
                else:
                    float_list.append('below_one')
                    break
            except ValueError:
                float_list.append('no_float')
                break
        return float_list

    def add_items(self, *args):
        list_args = [arg for arg in args]
        self.id = list_args[0]

        if True in self.is_empty_str(list_args[1:]):
            tk.messagebox.showerror(lg.set_lang_text(
                'MISC_FUNCTIONS_TITLE_MESSAGEBOX_1'), lg.set_lang_text('MISC_FUNCTIONS_INFO_MESSAGEBOX_1'))
        elif self.id == '0':
            self.parameters = self.prepare_parameters(list_args)

            db.insert(
                list_args[1],
                self.parameters,
                self.date,
                '-',
                list_args[2]
            )

            tk.messagebox.showinfo(lg.set_lang_text(
                'MISC_FUNCTIONS_TITLE_MESSAGEBOX_2'), lg.set_lang_text('MISC_FUNCTIONS_INFO_MESSAGEBOX_2'))

        else:
            self.parameters = self.prepare_parameters(list_args)

            db.update(self.id,
                      list_args[1],
                      self.parameters,
                      self.date,
                      list_args[2]
                      )

            tk.messagebox.showerror(lg.set_lang_text(
                'MISC_FUNCTIONS_TITLE_MESSAGEBOX_3'), lg.set_lang_text('MISC_FUNCTIONS_INFO_MESSAGEBOX_3'))

    def plot_lines(self, position, list_data, list_labels, plot_labels):

        fig_name = Figure(figsize=(8, 6), dpi=100)
        figure_canvas = FigureCanvasTkAgg(fig_name, position)
        NavigationToolbar2Tk(figure_canvas, position)

        line_style_list = [':', '-', '-.']

        axes = fig_name.add_subplot()
        for i in range(1, len(list_data)):
            if sum(list_data[i]) != 0:
                axes.plot(list_data[0],
                          list_data[i],
                          label=list_labels[i-1],
                          linestyle=line_style_list[i-1]
                          )
        # Show the major grid lines with dark grey lines
        axes.grid(visible=True, which='major',
                  color='#666666', linestyle='-')
        # Show the minor grid lines with very faint and almost transparent grey lines
        axes.minorticks_on()
        axes.grid(visible=True, which='minor', color='#999999',
                  linestyle='-', alpha=0.2)
        axes.set_title(f'{plot_labels[0]} {plot_labels[1]}')
        axes.set_xlabel(plot_labels[2])
        axes.set_ylabel(plot_labels[3])
        axes.legend()

        figure_canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    def image_to_label(self, path, max_width=0):

        self.image = Image.open(path)
        if max_width > 0:
            width_precent = (max_width/float(self.image.size[0]))
            new_height = int(float(self.image.size[1]*float(width_precent)))
            self.image = self.image.resize(
                (max_width, new_height))
        self.img = ImageTk.PhotoImage(self.image)
        return self.img

    def export_df_xlxs(self, df, ship_name):
        date = datetime.now()
        date = date.strftime("%Y-%m-%d")

        file_name = f'export/{ship_name}_{date}.xlsx'
        check_file = os.path.exists(file_name)

        if os.path.isdir('export') == False:
            path = os.path.join(os.getcwd(), 'export')
            os.mkdir(path)

        if check_file == True:
            answer = tk.messagebox.askyesno(lg.set_lang_text(
                'MISC_FUNCTIONS_TITLE_MESSAGEBOX_5'), lg.set_lang_text('MISC_FUNCTIONS_INFO_MESSAGEBOX_5'))
            if answer == True:
                df.to_excel(file_name)
                tk.messagebox.showinfo(lg.set_lang_text(
                    'MISC_FUNCTIONS_TITLE_MESSAGEBOX_4'), lg.set_lang_text('MISC_FUNCTIONS_INFO_MESSAGEBOX_4'))
                path = "export"
                path = os.path.realpath(path)
                os.startfile(path)
            elif answer == False:
                pass
        elif check_file == False:
            df.to_excel(file_name)
            tk.messagebox.showinfo(lg.set_lang_text(
                'MISC_FUNCTIONS_TITLE_MESSAGEBOX_4'), lg.set_lang_text('MISC_FUNCTIONS_INFO_MESSAGEBOX_4'))
            path = "export"
            path = os.path.realpath(path)
            os.startfile(path)
