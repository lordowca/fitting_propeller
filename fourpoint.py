import tkinter as tk

from modules.misc_functions import MiscFunctions
from modules.lang_module import LangTextDisplay
from modules.scroll_frame import VerticalScrolledFrame
import pandas as pd


lg = LangTextDisplay(file_name='fourpoint')

FONT_HEADER = ('Helvetica', 22, 'bold')
FONT_MIDLE_SIZE = ('Helvetica', 16, 'bold')
FONT_NORMAL_BOLD = ('Helvetica', 12, 'bold')
FONT_NORMAL = ('Helvetica', 12)


class FourPointDiagrams(tk.Frame):
    def __init__(self, master, id_from_list=None, ship_name=None, values=None, view=False, *args, **kwargs):
        super().__init__(master,  *args, **kwargs)
        self.master = master
        self.mf = MiscFunctions(self.master)

        self.id_from_list = id_from_list
        self.ship_name_text = ship_name
        self.values = values
        self.view = view
        self.type = 'fourpoint.py'
        self.parameters = ''
        self.id = '0'

        self.master.title(lg.set_lang_text('FOURPOINT_TITLE'))
        # window parametrs and position
        self.app_width = 900
        self.app_height = 750
        self.app_center_x = int(
            self.winfo_screenwidth() / 2 - self.app_width/2)
        self.app_center_y = int(
            self.winfo_screenheight() / 2 - self.app_height/2)
        self.master.geometry(
            f'{self.app_width}x{self.app_height}+{self.app_center_x}+{self.app_center_y}')

        # Create a frame to put the VerticalScrolledFrame inside
        self.holder_frame = tk.Frame(self.master)
        self.holder_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=tk.TRUE)

        # Create the VerticalScrolledFrame
        self.vs_frame = VerticalScrolledFrame(self.holder_frame)
        self.vs_frame.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=tk.TRUE)

        # create option frame
        self.options_to_calculations()

    def options_to_calculations(self):

        # TITLE FRAME
        self.title_frame = tk.Frame(
            self.vs_frame.interior)
        self.title_frame.pack(fill=tk.BOTH, expand=True, ipady=20)

        self.page_title_label = tk.Label(self.title_frame,
                                         text=lg.set_lang_text(
                                             'FOURPOINT_PAGE_TITLE_LABEL'),
                                         font=FONT_HEADER, wraplength=self.app_width)
        self.page_title_label.pack(ipady=10)

        # SHIP NAME FRAME
        self.ship_name_frame = tk.Frame(
            self.vs_frame.interior)
        self.ship_name_frame.pack(fill='x', expand=True)

        self.ship_name = tk.StringVar()
        self.ship_name_label = tk.Label(self.ship_name_frame, text=lg.set_lang_text(
            'FOURPOINT_SHIP_NAME_LABEL'), font=FONT_NORMAL_BOLD)
        self.ship_name_label.pack(
            side='left',  padx=5, pady=5, ipadx=3, ipady=3)

        self.ship_name_entry = tk.Entry(
            self.ship_name_frame,  font=FONT_NORMAL, textvariable=self.ship_name)
        self.ship_name_entry.pack(
            side='left', padx=5, pady=5, ipadx=3, ipady=3)

        # DATA INPUT TO MAIN CALCULATION - LEFT FRAME

        self.top_frame = tk.Frame(self.vs_frame.interior)
        self.top_frame.pack(padx=10, pady=10)

        # configure grid
        self.top_frame.columnconfigure(0, weight=1)
        self.top_frame.columnconfigure(1, weight=1)
        self.top_frame.columnconfigure(2, weight=1)
        self.top_frame.columnconfigure(3, weight=1)
        self.top_frame.columnconfigure(4, weight=1)
        self.top_frame.columnconfigure(5, weight=1)
        self.top_frame.columnconfigure(6, weight=1)
        self.top_frame.columnconfigure(7, weight=1)
        self.top_frame.columnconfigure(8, weight=1)
        self.top_frame.columnconfigure(9, weight=1)
        self.top_frame.columnconfigure(10, weight=1)
        self.top_frame.columnconfigure(11, weight=1)
        self.top_frame.columnconfigure(12, weight=1)
        self.top_frame.columnconfigure(13, weight=1)
        self.top_frame.columnconfigure(14, weight=1)
        self.top_frame.columnconfigure(15, weight=1)
        self.top_frame.columnconfigure(16, weight=1)
        self.top_frame.columnconfigure(17, weight=1)

        # row 0

        self.label_table_header_1 = tk.Label(self.top_frame, text=lg.set_lang_text(
            'FOURPOINT_PAGE_TITLE_LABEL'), font=FONT_NORMAL_BOLD, )
        self.label_table_header_1.grid(
            row=0, column=0, columnspan=17, padx=(5, 15), ipadx=10, ipady=10)

        # row 1

        self.label_line_header_1 = tk.Label(self.top_frame, text=lg.set_lang_text(
            'FOURPOINT_LINE_HEADER_LABEL'), font=FONT_NORMAL_BOLD, )
        self.label_line_header_1.grid(
            row=1, column=0, columnspan=17, padx=(5, 15), ipadx=10, ipady=10)

        # row 2

        # X1 - temp [C]
        self.text_0 = tk.StringVar()
        self.label_0 = tk.Label(
            self.top_frame, text=lg.set_lang_text('FOURPOINT_X1_LABEL'), font=FONT_NORMAL_BOLD)
        self.label_0.grid(row=2, column=0, sticky='NE', pady=5, padx=(5, 0))
        self.entry_0 = tk.Entry(
            self.top_frame, font=FONT_NORMAL, textvariable=self.text_0, width=12)
        self.entry_0.grid(row=2, column=1, sticky='NW', pady=5)
        self.label_u_0 = tk.Label(
            self.top_frame, text=lg.set_lang_text('FOURPOINT_C_LABEL'), font=FONT_NORMAL_BOLD)
        self.label_u_0.grid(row=2, column=2, sticky='NW',
                            pady=5, padx=(5,  15))

        # Y - [mm]
        self.text_1 = tk.StringVar()
        self.label_1 = tk.Label(
            self.top_frame, text=lg.set_lang_text('FOURPOINT_Y1_LABEL'), font=FONT_NORMAL_BOLD)
        self.label_1.grid(row=2, column=3, sticky='NE', pady=5, padx=(5, 0))
        self.entry_1 = tk.Entry(
            self.top_frame, font=FONT_NORMAL, textvariable=self.text_1, width=12)
        self.entry_1.grid(row=2, column=4, sticky='NW', pady=5)
        self.label_u_1 = tk.Label(
            self.top_frame, text=lg.set_lang_text('FOURPOINT_MM_LABEL'), font=FONT_NORMAL_BOLD)
        self.label_u_1.grid(row=2, column=5, sticky='NW',
                            pady=5, padx=(5, 15))

        # X2 -[C]
        self.text_2 = tk.StringVar()
        self.label_2 = tk.Label(
            self.top_frame, text=lg.set_lang_text('FOURPOINT_X2_LABEL'), font=FONT_NORMAL_BOLD)
        self.label_2.grid(row=2, column=6, sticky='NE',
                          pady=5)
        self.entry_2 = tk.Entry(
            self.top_frame, font=FONT_NORMAL, textvariable=self.text_2, width=12)
        self.entry_2.grid(row=2, column=7, sticky='NW', pady=5)
        self.label_u_2 = tk.Label(
            self.top_frame, text=lg.set_lang_text('FOURPOINT_C_LABEL'), font=FONT_NORMAL_BOLD)
        self.label_u_2.grid(row=2, column=8, sticky='NW',
                            pady=5, padx=(5, 15))

        # Y2 - [mm]
        self.text_3 = tk.StringVar()
        self.label_3 = tk.Label(
            self.top_frame, text=lg.set_lang_text('FOURPOINT_Y2_LABEL'), font=FONT_NORMAL_BOLD)
        self.label_3.grid(row=2, column=9, sticky='NE', pady=5,
                          padx=(5, 0))
        self.entry_3 = tk.Entry(
            self.top_frame, font=FONT_NORMAL, textvariable=self.text_3, width=12)
        self.entry_3.grid(row=2, column=10, sticky='NW', pady=5)
        self.label_u_3 = tk.Label(
            self.top_frame, text=lg.set_lang_text('FOURPOINT_MM_LABEL'), font=FONT_NORMAL_BOLD)
        self.label_u_3.grid(row=2, column=11, sticky='NW',
                            pady=5, padx=(5, 15))
        # row 3

        self.label_line_header_2 = tk.Label(self.top_frame, text=lg.set_lang_text(
            'FOURPOINT_LINE2_HEADER_LABEL'), font=FONT_NORMAL_BOLD, )
        self.label_line_header_2.grid(
            row=3, column=0, columnspan=17, padx=(5, 15), ipadx=10, ipady=10)

        # row 4

        # X3 - temp [C]
        self.text_4 = tk.StringVar()
        self.label_4 = tk.Label(
            self.top_frame, text=lg.set_lang_text('FOURPOINT_X3_LABEL'), font=FONT_NORMAL_BOLD)
        self.label_4.grid(row=4, column=0, sticky='NE', pady=5, padx=(5, 0))
        self.entry_4 = tk.Entry(
            self.top_frame, font=FONT_NORMAL, textvariable=self.text_4, width=12)
        self.entry_4.grid(row=4, column=1, sticky='NW', pady=5)
        self.label_u_4 = tk.Label(
            self.top_frame, text=lg.set_lang_text('FOURPOINT_C_LABEL'), font=FONT_NORMAL_BOLD)
        self.label_u_4.grid(row=4, column=2, sticky='NW',
                            pady=5, padx=(5,  15))

        # Y3 - [mm]
        self.text_5 = tk.StringVar()
        self.label_5 = tk.Label(
            self.top_frame, text=lg.set_lang_text('FOURPOINT_Y3_LABEL'), font=FONT_NORMAL_BOLD)
        self.label_5.grid(row=4, column=3, sticky='NE', pady=5, padx=(5, 0))
        self.entry_5 = tk.Entry(
            self.top_frame, font=FONT_NORMAL, textvariable=self.text_5, width=12)
        self.entry_5.grid(row=4, column=4, sticky='NW', pady=5)
        self.label_u_5 = tk.Label(
            self.top_frame, text=lg.set_lang_text('FOURPOINT_MM_LABEL'), font=FONT_NORMAL_BOLD)
        self.label_u_5.grid(row=4, column=5, sticky='NW',
                            pady=5, padx=(5, 15))

        # X4 -[C]
        self.text_6 = tk.StringVar()
        self.label_6 = tk.Label(
            self.top_frame, text=lg.set_lang_text('FOURPOINT_X4_LABEL'), font=FONT_NORMAL_BOLD)
        self.label_6.grid(row=4, column=6, sticky='NE',
                          pady=5)
        self.entry_6 = tk.Entry(
            self.top_frame, font=FONT_NORMAL, textvariable=self.text_6, width=12)
        self.entry_6.grid(row=4, column=7, sticky='NW', pady=5)
        self.label_u_6 = tk.Label(
            self.top_frame, text=lg.set_lang_text('FOURPOINT_C_LABEL'), font=FONT_NORMAL_BOLD)
        self.label_u_6.grid(row=4, column=8, sticky='NW',
                            pady=5, padx=(5, 15))

        # Y4 - [mm]
        self.text_7 = tk.StringVar()
        self.label_7 = tk.Label(
            self.top_frame, text=lg.set_lang_text('FOURPOINT_Y4_LABEL'), font=FONT_NORMAL_BOLD)
        self.label_7.grid(row=4, column=9, sticky='NE', pady=5,
                          padx=(5, 0))
        self.entry_7 = tk.Entry(
            self.top_frame, font=FONT_NORMAL, textvariable=self.text_7, width=12)
        self.entry_7.grid(row=4, column=10, sticky='NW', pady=5)
        self.label_u_7 = tk.Label(
            self.top_frame, text=lg.set_lang_text('FOURPOINT_MM_LABEL'), font=FONT_NORMAL_BOLD)
        self.label_u_7.grid(row=4, column=11, sticky='NW',
                            pady=5, padx=(5, 15))

        # DATA ACTIONS BUTTONS FRAME
        self.frame_action_buttons = tk.Frame(self.vs_frame.interior)
        self.frame_action_buttons.pack(padx=10, pady=10, expand=True, fill='x')

        self.button_cal_all = tk.Button(self.frame_action_buttons,
                                        text=lg.set_lang_text(
                                            'FOURPOINT_COMPUTE_BUTTON'),
                                        font=FONT_NORMAL,
                                        command=lambda: self.all_calculation(
                                            self.text_0.get(),
                                            self.text_1.get(),
                                            self.text_2.get(),
                                            self.text_3.get(),
                                            self.text_4.get(),
                                            self.text_5.get(),
                                            self.text_6.get(),
                                            self.text_7.get()
                                        ))
        self.button_cal_all.pack(padx=5, pady=5, ipadx=3, ipady=3, side='left')

        self.button_save_all = tk.Button(self.frame_action_buttons,
                                         text=lg.set_lang_text(
                                             'FOURPOINT_SAVE_BUTTON'),
                                         font=FONT_NORMAL,
                                         command=lambda: self.mf.add_items(
                                             self.id,
                                             self.ship_name.get(),
                                             self.type,
                                             self.text_0.get(),
                                             self.text_1.get(),
                                             self.text_2.get(),
                                             self.text_3.get(),
                                             self.text_4.get(),
                                             self.text_5.get(),
                                             self.text_6.get(),
                                             self.text_7.get()
                                         ))
        self.button_save_all.pack(
            padx=5, pady=5, ipadx=3, ipady=3, side='left')
        self.button_close = tk.Button(
            self.frame_action_buttons, font=FONT_NORMAL, text=lg.set_lang_text('FOURPOINT_MAIN_VIEW_BUTTON'), command=lambda: self.master.destroy())
        self.button_close.pack(
            padx=5, pady=5, ipadx=3, ipady=3, side='left')

        # INSERT DATA FROM DB

        if self.view == True:
            self.id = self.id_from_list
            entry_position = [self.entry_0, self.entry_1, self.entry_2,
                              self.entry_3, self.entry_4, self.entry_5, self.entry_6, self.entry_7, self.ship_name_entry]
            value_list = self.values.split(';')
            value_list.append(self.ship_name_text)

            self.mf.insert_value_to_entry(entry_position, value_list)

            self.all_calculation(
                self.text_0.get(),
                self.text_1.get(),
                self.text_2.get(),
                self.text_3.get(),
                self.text_4.get(),
                self.text_5.get(),
                self.text_6.get(),
                self.text_7.get()
            )

    def all_calculation(self, *args):
        list_args = [arg for arg in args]
        if True in (self.mf.is_empty_str(list_args)):
            tk.messagebox.showerror(lg.set_lang_text(
                'FOURPOINT_TITLE_MESSAGEBOX_1'),
                lg.set_lang_text('FOURPOINT_INFO_MESSAGEBOX_1'))
        else:
            float_list = self.mf.string_to_float_greater_than_zero(
                list_args)
            if 'no_float' in float_list or 'below_one' in float_list:
                tk.messagebox.showerror(lg.set_lang_text(
                    'FOURPOINT_TITLE_MESSAGEBOX_CONVERT'), lg.set_lang_text('FOURPOINT_INFO_MESSAGEBOX_CONVERT'))
            else:
                try:

                    a1 = (float_list[3]-float_list[1]) / \
                        (float_list[2]-float_list[0])
                    b1 = float_list[1] - a1 * float_list[0]

                    a2 = (float_list[7]-float_list[5]) / \
                        (float_list[6]-float_list[4])
                    b2 = float_list[5] - a2 * float_list[4]

                    try:
                        self.calculation_all_frame.destroy()
                    except AttributeError:
                        pass

                    # print(self.calculation_all_frame.winfo_exists())

                    self.calculation_all_frame = tk.Frame(
                        self.vs_frame.interior)
                    self.calculation_all_frame.pack(
                        padx=10, pady=10, ipadx=10, ipady=10, expand=True, fill='both')
                    # self.calculation_all_frame.destroy()

                    self.calculation_frame = tk.Frame(
                        self.calculation_all_frame)
                    self.calculation_frame.pack(
                        padx=10, pady=10, expand=True, fill='both')

                    # DataFrame section

                    self.fourpoint_df = pd.DataFrame()

                    self.fourpoint_df[lg.set_lang_text(
                        'FOURPOINT_DF_COL_TEMP')] = [x for x in range(0, 36)]
                    self.fourpoint_df[lg.set_lang_text('FOURPOINT_DF_COL_PRZES_MIN')] = a1 * self.fourpoint_df[lg.set_lang_text(
                        'FOURPOINT_DF_COL_TEMP')] + b1
                    self.fourpoint_df[lg.set_lang_text('FOURPOINT_DF_COL_PRZES_MAX')] = a2 * self.fourpoint_df[lg.set_lang_text(
                        'FOURPOINT_DF_COL_TEMP')] + b2

                    # table section

                    self.table_frame = tk.Frame(
                        self.calculation_all_frame)
                    self.table_frame.pack(
                        fill='both', expand=True, padx=10, pady=10)

                    self.mf.tabel_show(
                        self.table_frame, self.fourpoint_df)

                    self.export_button_frame = tk.Frame(
                        self.calculation_all_frame)
                    self.export_button_frame.pack(
                        fill='both', expand=True, padx=10, pady=10)

                    self.export_button = tk.Button(self.export_button_frame, text=lg.set_lang_text(
                        'FOURPOINT_MAIN_VIEW_EXPORT'),
                        font=FONT_NORMAL,
                        command=lambda: self.mf.export_df_xlxs(self.fourpoint_df, self.ship_name.get()))
                    self.export_button.pack()

                    # plot section

                    self.frame_plot_dt = tk.Frame(
                        self.calculation_all_frame)
                    self.frame_plot_dt.pack(
                        fill='both', expand=True, padx=10, pady=10)

                    self.data_list = [self.fourpoint_df[lg.set_lang_text("FOURPOINT_DF_COL_TEMP")],
                                      self.fourpoint_df[lg.set_lang_text(
                                          "FOURPOINT_DF_COL_PRZES_MIN")],
                                      self.fourpoint_df[lg.set_lang_text(
                                          "FOURPOINT_DF_COL_PRZES_MAX")],
                                      ]

                    self.label_list = [lg.set_lang_text("FOURPOINT_DF_COL_PRZES_MIN"),
                                       lg.set_lang_text(
                                           'FOURPOINT_DF_COL_PRZES_MAX')]

                    self.description_list = [lg.set_lang_text('FOURPOINT_PLOT_TITLE'),
                                             self.ship_name.get(),
                                             lg.set_lang_text(
                        'FOURPOINT_DF_COL_TEMP'),
                        lg.set_lang_text('FOURPOINT_DF_COL_PRZES')]

                    self.mf.plot_lines(self.frame_plot_dt,
                                       self.data_list,
                                       self.label_list,
                                       self.description_list
                                       )
                    self.frame_plot_wt = tk.Frame(
                        self.calculation_all_frame)
                    self.frame_plot_wt.pack(
                        fill='both', expand=True, padx=10, pady=10)

                except ZeroDivisionError:
                    tk.messagebox.showerror(lg.set_lang_text(
                        'FOURPOINT_BV_TITLE_MESSAGEBOX_3'), lg.set_lang_text('FOURPOINT_BV_INFO_MESSAGEBOX_6'))


if __name__ == "__main__":
    root = tk.Tk()
    app = FourPointDiagrams(master=root)
    app.mainloop()
