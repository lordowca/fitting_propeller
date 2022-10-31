import tkinter as tk

from modules.misc_functions import MiscFunctions
from modules.lang_module import LangTextDisplay
from modules.scroll_frame import VerticalScrolledFrame
from modules.load_window import OpenWindow
from math import pi, pow, sqrt
import pandas as pd


lg = LangTextDisplay(file_name='propeller_lr')

FONT_HEADER = ('Helvetica', 22, 'bold')
FONT_MIDLE_SIZE = ('Helvetica', 16, 'bold')
FONT_NORMAL_BOLD = ('Helvetica', 12, 'bold')
FONT_NORMAL = ('Helvetica', 12)


class PropellerLR(tk.Frame):
    def __init__(self, master, id_from_list=None, ship_name=None, values=None, view=False, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.master = master
        self.mf = MiscFunctions(self.master)
        self.ow = OpenWindow(self.master)

        self.id_from_list = id_from_list
        self.ship_name_text = ship_name
        self.values = values
        self.view = view
        self.type = 'propeller_lr.py'
        self.parameters = ''
        self.id = '0'

        self.master.title(lg.set_lang_text('PROPELLER_LR_TITLE'))
        # window parametrs and position
        self.app_width = 1100
        self.app_height = int(self.winfo_screenheight()-100)
        self.app_center_x = int(
            self.winfo_screenwidth() / 2) - int(self.app_width/2)
        self.master.geometry(
            f'{self.app_width}x{self.app_height}+{self.app_center_x}+{20}')
        self.master.resizable(False, True)

        # Create a frame to put the VerticalScrolledFrame inside
        self.holder_frame = tk.Frame(self.master)
        self.holder_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=tk.TRUE)

        # Create the VerticalScrolledFrame
        self.vs_frame = VerticalScrolledFrame(self.holder_frame)
        self.vs_frame.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=tk.TRUE)

        self.propeller_lr_input_data()

    def propeller_lr_input_data(self):

        # TITLE FRAME
        self.title_frame = tk.Frame(
            self.vs_frame.interior)
        self.title_frame.pack(fill=tk.BOTH, expand=True, ipady=20)

        self.page_title_label = tk.Label(self.title_frame,
                                         text=lg.set_lang_text(
                                             'PROPELLER_LR_TITLE_LABEL'),
                                         font=FONT_HEADER, wraplength=self.app_width)
        self.page_title_label.pack(ipady=10)

        # SHIP NAME FRAME
        self.ship_name_frame = tk.Frame(
            self.vs_frame.interior)
        self.ship_name_frame.pack(fill='x', expand=True)

        self.ship_name = tk.StringVar()
        self.ship_name_label = tk.Label(self.ship_name_frame, text=lg.set_lang_text(
            'PROPELLER_LR_SHIP_NAME_LABEL'), font=FONT_NORMAL_BOLD)
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

        # row 0

        self.label_table_header_1 = tk.Label(self.top_frame, text=lg.set_lang_text(
            'PROPELLER_LR_TABLE_HEADER_1'), font=FONT_NORMAL_BOLD, )
        self.label_table_header_1.grid(
            row=0, column=0, columnspan=14, padx=(5, 15), ipadx=10, ipady=10)

        # row 1

        # k3
        self.text_0 = tk.StringVar()
        self.label_0 = tk.Label(
            self.top_frame, text=lg.set_lang_text('PROPELLER_LR_LABEL_0'), font=FONT_NORMAL_BOLD)
        self.label_0.grid(row=1, column=0, sticky='NE', pady=5, padx=(5, 0))
        self.entry_0 = tk.Entry(
            self.top_frame, font=FONT_NORMAL, textvariable=self.text_0, width=12)
        self.entry_0.grid(row=1, column=1, sticky='NW', pady=5)
        self.label_u_0 = tk.Label(
            self.top_frame, text=lg.set_lang_text('PROPELLER_LR_LABEL_U_NONE'), font=FONT_NORMAL_BOLD)
        self.label_u_0.grid(row=1, column=2, sticky='NW',
                            pady=5, padx=(5,  15))

        # E3
        self.text_1 = tk.StringVar()
        self.label_1 = tk.Label(
            self.top_frame, text=lg.set_lang_text('PROPELLER_LR_LABEL_1'), font=FONT_NORMAL_BOLD)
        self.label_1.grid(row=1, column=3, sticky='NE', pady=5, padx=(5, 0))
        self.entry_1 = tk.Entry(
            self.top_frame, font=FONT_NORMAL, textvariable=self.text_1, width=12)
        self.entry_1.grid(row=1, column=4, sticky='NW', pady=5)
        self.label_u_1 = tk.Label(
            self.top_frame, text=lg.set_lang_text('PROPELLER_LR_LABEL_U_MPA'), font=FONT_NORMAL_BOLD)
        self.label_u_1.grid(row=1, column=5, sticky='NW',
                            pady=5, padx=(5, 15))

        # E2
        self.text_2 = tk.StringVar()
        self.label_2 = tk.Label(
            self.top_frame, text=lg.set_lang_text('PROPELLER_LR_LABEL_2'), font=FONT_NORMAL_BOLD)
        self.label_2.grid(row=1, column=6, sticky='NE',
                          pady=5)
        self.entry_2 = tk.Entry(
            self.top_frame, font=FONT_NORMAL, textvariable=self.text_2, width=12)
        self.entry_2.grid(row=1, column=7, sticky='NW', pady=5)
        self.label_u_2 = tk.Label(
            self.top_frame, text=lg.set_lang_text('PROPELLER_LR_LABEL_U_MPA'), font=FONT_NORMAL_BOLD)
        self.label_u_2.grid(row=1, column=8, sticky='NW',
                            pady=5, padx=(5, 15))

        # v1
        self.text_3 = tk.StringVar()
        self.label_3 = tk.Label(
            self.top_frame, text=lg.set_lang_text('PROPELLER_LR_LABEL_3'), font=FONT_NORMAL_BOLD)
        self.label_3.grid(row=1, column=9, sticky='NE', pady=5,
                          padx=(5, 0))
        self.entry_3 = tk.Entry(
            self.top_frame, font=FONT_NORMAL, textvariable=self.text_3, width=12)
        self.entry_3.grid(row=1, column=10, sticky='NW', pady=5)
        self.label_u_3 = tk.Label(
            self.top_frame, text=lg.set_lang_text('PROPELLER_LR_LABEL_U_NONE'), font=FONT_NORMAL_BOLD)
        self.label_u_3.grid(row=1, column=11, sticky='NW',
                            pady=5, padx=(5, 15))

        # v3
        self.text_4 = tk.StringVar()
        self.label_4 = tk.Label(
            self.top_frame, text=lg.set_lang_text('PROPELLER_LR_LABEL_4'), font=FONT_NORMAL_BOLD)
        self.label_4.grid(row=1, column=12, sticky='NE', pady=5, padx=(5, 0))
        self.entry_4 = tk.Entry(
            self.top_frame, font=FONT_NORMAL, textvariable=self.text_4, width=12)
        self.entry_4.grid(row=1, column=13, sticky='NW', pady=5)
        self.label_u_4 = tk.Label(
            self.top_frame, text=lg.set_lang_text('PROPELLER_LR_LABEL_U_NONE'), font=FONT_NORMAL_BOLD)
        self.label_u_4.grid(row=1, column=14, sticky='NW',
                            pady=5, padx=(5, 15))
        # row 2
        # l
        self.text_5 = tk.StringVar()
        self.label_5 = tk.Label(
            self.top_frame, text=lg.set_lang_text('PROPELLER_LR_LABEL_5'), font=FONT_NORMAL_BOLD)
        self.label_5.grid(row=2, column=0, sticky='NE', pady=5, padx=(5, 0))
        self.entry_5 = tk.Entry(
            self.top_frame, font=FONT_NORMAL, textvariable=self.text_5, width=12)
        self.entry_5.grid(row=2, column=1, sticky='NW', pady=5)
        self.label_u_5 = tk.Label(
            self.top_frame, text=lg.set_lang_text('PROPELLER_LR_LABEL_U_NONE'), font=FONT_NORMAL_BOLD)
        self.label_u_5.grid(row=2, column=2, sticky='NW',
                            pady=5, padx=(5, 15))

        # Q
        self.text_6 = tk.StringVar()
        self.label_6 = tk.Label(
            self.top_frame, text=lg.set_lang_text('PROPELLER_LR_LABEL_6'), font=FONT_NORMAL_BOLD)
        self.label_6.grid(row=2, column=3, sticky='NE', pady=5, padx=(5, 0))
        self.entry_6 = tk.Entry(
            self.top_frame, font=FONT_NORMAL, textvariable=self.text_6, width=12)
        self.entry_6.grid(row=2, column=4, sticky='NW', pady=5)
        self.label_u_6 = tk.Label(
            self.top_frame, text=lg.set_lang_text('PROPELLER_LR_LABEL_U_NM'), font=FONT_NORMAL_BOLD)
        self.label_u_6.grid(row=2, column=5, sticky='NW',
                            pady=5, padx=(5, 15))

        # d1
        self.text_7 = tk.StringVar()
        self.label_7 = tk.Label(
            self.top_frame, text=lg.set_lang_text('PROPELLER_LR_LABEL_7'), font=FONT_NORMAL_BOLD)
        self.label_7.grid(row=2, column=6, sticky='NE', pady=5, padx=(5, 0))
        self.entry_7 = tk.Entry(
            self.top_frame, font=FONT_NORMAL, textvariable=self.text_7, width=12)
        self.entry_7.grid(row=2, column=7, sticky='NW', pady=5)
        self.label_u_7 = tk.Label(
            self.top_frame, text=lg.set_lang_text('PROPELLER_LR_LABEL_U_MM'), font=FONT_NORMAL_BOLD)
        self.label_u_7.grid(row=2, column=8, sticky='NW',
                            pady=5, padx=(5, 15))

        # C
        self.text_8 = tk.StringVar()
        self.label_8 = tk.Label(
            self.top_frame, text=lg.set_lang_text('PROPELLER_LR_LABEL_8'), font=FONT_NORMAL_BOLD)
        self.label_8.grid(row=2, column=9, sticky='NE', pady=5, padx=(5, 0,))
        self.entry_8 = tk.Entry(
            self.top_frame, font=FONT_NORMAL, textvariable=self.text_8, width=12)
        self.entry_8.grid(row=2, column=10, sticky='NW', pady=5)
        self.label_u_8 = tk.Label(
            self.top_frame, text=lg.set_lang_text('PROPELLER_LR_LABEL_U_NONE'), font=FONT_NORMAL_BOLD)
        self.label_u_8.grid(row=2, column=11, sticky='NW',
                            pady=5, padx=(5, 15))

        # M
        self.text_9 = tk.StringVar()
        self.label_9 = tk.Label(
            self.top_frame, text=lg.set_lang_text('PROPELLER_LR_LABEL_9'), font=FONT_NORMAL_BOLD)
        self.label_9.grid(row=2, column=12, sticky='NE', pady=5, padx=(5, 0,))
        self.entry_9 = tk.Entry(
            self.top_frame, font=FONT_NORMAL, textvariable=self.text_9, width=12)
        self.entry_9.grid(row=2, column=13, sticky='NW', pady=5)
        self.label_u_9 = tk.Label(
            self.top_frame, text=lg.set_lang_text('PROPELLER_LR_LABEL_U_N'), font=FONT_NORMAL_BOLD)
        self.label_u_9.grid(row=2, column=14, sticky='NW',
                            pady=5, padx=(5, 15))

        # d row 3
        # A1
        self.text_10 = tk.StringVar()
        self.label_10 = tk.Label(
            self.top_frame, text=lg.set_lang_text('PROPELLER_LR_LABEL_10'), font=FONT_NORMAL_BOLD)
        self.label_10.grid(row=3, column=0, sticky='NE', pady=5, padx=(5, 0))
        self.entry_10 = tk.Entry(
            self.top_frame, font=FONT_NORMAL, textvariable=self.text_10, width=12)
        self.entry_10.grid(row=3, column=1, sticky='NW', pady=5)
        self.label_u_10 = tk.Label(
            self.top_frame, text=lg.set_lang_text('PROPELLER_LR_LABEL_U_MM_2'), font=FONT_NORMAL_BOLD)
        self.label_u_10.grid(row=3, column=2, sticky='NW',
                             pady=5, padx=(5, 15))

        # V1
        self.text_11 = tk.StringVar()
        self.label_11 = tk.Label(
            self.top_frame, text=lg.set_lang_text('PROPELLER_LR_LABEL_11'), font=FONT_NORMAL_BOLD)
        self.label_11.grid(row=3, column=3, sticky='NE', pady=5, padx=(5, 0))
        self.entry_11 = tk.Entry(
            self.top_frame, font=FONT_NORMAL, textvariable=self.text_11, width=12)
        self.entry_11.grid(row=3, column=4, sticky='NW', pady=5)
        self.label_u_11 = tk.Label(
            self.top_frame, text=lg.set_lang_text('PROPELLER_LR_LABEL_U_NONE'), font=FONT_NORMAL_BOLD)
        self.label_u_11.grid(row=3, column=5, sticky='NW',
                             pady=5, padx=(5, 15))

        # theta
        self.text_12 = tk.StringVar()
        self.label_12 = tk.Label(
            self.top_frame, text=lg.set_lang_text('PROPELLER_LR_LABEL_12'), font=FONT_NORMAL_BOLD)
        self.label_12.grid(row=3, column=6, sticky='NE', pady=5, padx=(5, 0))
        self.entry_12 = tk.Entry(
            self.top_frame, font=FONT_NORMAL, textvariable=self.text_12, width=12)
        self.entry_12.grid(row=3, column=7, sticky='NW', pady=5)
        self.label_u_12 = tk.Label(
            self.top_frame, text=lg.set_lang_text('PROPELLER_LR_LABEL_U_NONE'), font=FONT_NORMAL_BOLD)
        self.label_u_12.grid(row=3, column=8, sticky='NW',
                             pady=5, padx=(5, 15))

        # alfa 3
        self.text_13 = tk.StringVar()
        self.label_13 = tk.Label(
            self.top_frame, text=lg.set_lang_text('PROPELLER_LR_LABEL_13'), font=FONT_NORMAL_BOLD)
        self.label_13.grid(row=3, column=9, sticky='NE', pady=5, padx=(5, 0))
        self.entry_13 = tk.Entry(
            self.top_frame, font=FONT_NORMAL, textvariable=self.text_13, width=12)
        self.entry_13.grid(row=3, column=10, sticky='NW', pady=5)
        self.label_u_13 = tk.Label(
            self.top_frame, text=lg.set_lang_text('PROPELLER_LR_LABEL_U_NONE'), font=FONT_NORMAL_BOLD)
        self.label_u_13.grid(row=3, column=11, sticky='NW',
                             pady=5, padx=(5, 15))

        # alfa 1
        self.text_14 = tk.StringVar()
        self.label_14 = tk.Label(
            self.top_frame, text=lg.set_lang_text('PROPELLER_LR_LABEL_14'), font=FONT_NORMAL_BOLD)
        self.label_14.grid(row=3, column=12, sticky='NE', pady=5, padx=(5, 0))
        self.entry_14 = tk.Entry(
            self.top_frame, font=FONT_NORMAL, textvariable=self.text_14, width=12)
        self.entry_14.grid(row=3, column=13, sticky='NW', pady=5)
        self.label_u_14 = tk.Label(
            self.top_frame, text=lg.set_lang_text('PROPELLER_LR_LABEL_U_NONE'), font=FONT_NORMAL_BOLD)
        self.label_u_14.grid(row=3, column=14, sticky='NW',
                             pady=5, padx=(5, 15), columnspan=2)
        # row 4
        #  micro 1
        self.text_15 = tk.StringVar()
        self.label_15 = tk.Label(
            self.top_frame, text=lg.set_lang_text('PROPELLER_LR_LABEL_15'), font=FONT_NORMAL_BOLD)
        self.label_15.grid(row=4, column=0, sticky='NE', pady=5, padx=(5, 0))
        self.entry_15 = tk.Entry(
            self.top_frame, font=FONT_NORMAL, textvariable=self.text_15, width=12)
        self.entry_15.grid(row=4, column=1, sticky='NW', pady=5)
        self.label_u_15 = tk.Label(
            self.top_frame, text=lg.set_lang_text('PROPELLER_LR_LABEL_U_NONE'), font=FONT_NORMAL_BOLD)
        self.label_u_15.grid(row=4, column=2, sticky='NW',
                             pady=3, padx=(5, 15))

        # d3
        self.text_16 = tk.StringVar()
        self.label_16 = tk.Label(
            self.top_frame, text=lg.set_lang_text('PROPELLER_LR_LABEL_16'), font=FONT_NORMAL_BOLD)
        self.label_16.grid(row=4, column=3, sticky='NE', pady=5, padx=(5, 0))
        self.entry_16 = tk.Entry(
            self.top_frame, font=FONT_NORMAL, textvariable=self.text_16, width=12)
        self.entry_16.grid(row=4, column=4, sticky='NW', pady=5)
        self.label_u_16 = tk.Label(
            self.top_frame, text=lg.set_lang_text('PROPELLER_LR_LABEL_U_MM'), font=FONT_NORMAL_BOLD)
        self.label_u_16.grid(row=4, column=5, sticky='NW',
                             pady=5, padx=(5, 15))

        # # dt-
        # self.text_17 = tk.StringVar()
        # self.label_17 = tk.Label(
        #     self.top_frame, text=lg.set_lang_text('PROPELLER_LR_LABEL_17'), font=FONT_NORMAL_BOLD)
        # self.label_17.grid(row=4, column=6, sticky='NE', pady=5, padx=(5, 0))
        # self.entry_17 = tk.Entry(
        #     self.top_frame, font=FONT_NORMAL, textvariable=self.text_17, width=12)
        # self.entry_17.grid(row=4, column=7, sticky='NW',
        #                    pady=5)
        # self.label_u_17 = tk.Label(
        #     self.top_frame, text=lg.set_lang_text('PROPELLER_LR_LABEL_U_MM'), font=FONT_NORMAL_BOLD)
        # self.label_u_17.grid(row=4, column=8, sticky='NW',
        #                      pady=5, padx=(5, 15))

        # dt+
        self.text_18 = tk.StringVar()
        self.label_18 = tk.Label(
            self.top_frame, text=lg.set_lang_text('PROPELLER_LR_LABEL_18'), font=FONT_NORMAL_BOLD)
        self.label_18.grid(row=4, column=9, sticky='NE', pady=5, padx=(5, 0))
        self.entry_18 = tk.Entry(
            self.top_frame, font=FONT_NORMAL, textvariable=self.text_18, width=12)
        self.entry_18.grid(row=4, column=10, sticky='NW', pady=5)
        self.label_u_18 = tk.Label(
            self.top_frame, text=lg.set_lang_text('PROPELLER_LR_LABEL_U_MM'), font=FONT_NORMAL_BOLD)
        self.label_u_18.grid(row=4, column=11, sticky='NW',
                             pady=5, padx=(5, 15))

        # row 5
        # table header 2
        self.label_table_title_1 = tk.Label(self.top_frame, text=lg.set_lang_text(
            'PROPELLER_LR_TABLE_HEADER_2'), font=FONT_NORMAL_BOLD)
        self.label_table_title_1.grid(
            row=5, column=0, columnspan=14, padx=(5, 15), ipadx=10, ipady=10)

        # row 6
        # P
        self.text_19 = tk.StringVar()
        self.text_19.set('0')
        self.label_19 = tk.Label(
            self.top_frame, text=lg.set_lang_text('PROPELLER_LR_LABEL_19'), font=FONT_NORMAL_BOLD)
        self.label_19.grid(row=6, column=0, sticky='NE', pady=5, padx=(5, 0))
        self.entry_19 = tk.Entry(
            self.top_frame, font=FONT_NORMAL, textvariable=self.text_19, width=12)
        self.entry_19.grid(row=6, column=1, sticky='NW', pady=5)
        self.label_u_19 = tk.Label(
            self.top_frame, text=lg.set_lang_text('PROPELLER_LR_LABEL_U_KW'), font=FONT_NORMAL_BOLD)
        self.label_u_19.grid(row=6, column=2, sticky='NW',
                             pady=5, padx=(5, 15))

        # R
        self.text_20 = tk.StringVar()
        self.text_20.set('0')
        self.label_20 = tk.Label(
            self.top_frame, text=lg.set_lang_text('PROPELLER_LR_LABEL_20'), font=FONT_NORMAL_BOLD)
        self.label_20.grid(row=6, column=3, sticky='NE', pady=5, padx=(5, 0))
        self.entry_20 = tk.Entry(
            self.top_frame, font=FONT_NORMAL, textvariable=self.text_20, width=12)
        self.entry_20.grid(row=6, column=4, sticky='NW', pady=5)
        self.label_u_20 = tk.Label(
            self.top_frame, text=lg.set_lang_text('PROPELLER_LR_LABEL_U_OBR_MIN'), font=FONT_NORMAL_BOLD)
        self.label_u_20.grid(row=6, column=5, sticky='NW',
                             pady=5, padx=(5, 15))

        # V
        self.text_21 = tk.StringVar()
        self.text_21.set('0')
        self.label_21 = tk.Label(
            self.top_frame, text=lg.set_lang_text('PROPELLER_LR_LABEL_21'), font=FONT_NORMAL_BOLD)
        self.label_21.grid(row=6, column=6, sticky='NE', pady=5, padx=(5, 0))
        self.entry_21 = tk.Entry(
            self.top_frame, font=FONT_NORMAL, textvariable=self.text_21, width=12)
        self.entry_21.grid(row=6, column=7, sticky='NW', pady=5)
        self.label_u_21 = tk.Label(
            self.top_frame, text=lg.set_lang_text('PROPELLER_LR_LABEL_U_KNOT'), font=FONT_NORMAL_BOLD)
        self.label_u_21.grid(row=6, column=8, sticky='NW',
                             pady=5, padx=(5, 15))

        # di
        self.text_22 = tk.StringVar()
        self.text_22.set('0')
        self.label_22 = tk.Label(
            self.top_frame, text=lg.set_lang_text('PROPELLER_LR_LABEL_22'), font=FONT_NORMAL_BOLD)
        self.label_22.grid(row=6, column=9, sticky='NE', pady=5, padx=(5, 0))
        self.entry_22 = tk.Entry(
            self.top_frame, font=FONT_NORMAL, textvariable=self.text_22, width=12)
        self.entry_22.grid(row=6, column=10, sticky='NW', pady=5)
        self.label_u_22 = tk.Label(
            self.top_frame, text=lg.set_lang_text('PROPELLER_LR_LABEL_U_MM'), font=FONT_NORMAL_BOLD)
        self.label_u_22.grid(row=6, column=11, sticky='NW',
                             pady=5, padx=(5, 15))
        # row 7
        # K3
        self.text_23 = tk.StringVar()
        self.text_23.set('0')
        self.label_23 = tk.Label(
            self.top_frame, text=lg.set_lang_text('PROPELLER_LR_LABEL_23'), font=FONT_NORMAL_BOLD)
        self.label_23.grid(row=7, column=0, sticky='NE',
                           pady=5, padx=(5, 0))
        self.entry_23 = tk.Entry(
            self.top_frame, font=FONT_NORMAL, textvariable=self.text_23, width=12)
        self.entry_23.grid(row=7, column=1, sticky='NW', pady=5)
        self.label_u_23 = tk.Label(
            self.top_frame, text=lg.set_lang_text('PROPELLER_LR_LABEL_U_NONE'), font=FONT_NORMAL_BOLD)
        self.label_u_23.grid(row=7, column=2, sticky='NW',
                             pady=5, padx=(5, 15))
        # l
        self.text_24 = tk.StringVar()
        self.text_24.set('0')
        self.label_24 = tk.Label(
            self.top_frame, text=lg.set_lang_text('PROPELLER_LR_LABEL_24'), font=FONT_NORMAL_BOLD)
        self.label_24.grid(row=7, column=3, sticky='NE',
                           pady=5, padx=(5, 0))
        self.entry_24 = tk.Entry(
            self.top_frame, font=FONT_NORMAL, textvariable=self.text_24, width=12)
        self.entry_24.grid(row=7, column=4, sticky='NW', pady=5)
        self.label_u_24 = tk.Label(
            self.top_frame, text=lg.set_lang_text('PROPELLER_LR_LABEL_U_NONE'), font=FONT_NORMAL_BOLD)
        self.label_u_24.grid(row=7, column=5, sticky='NW',
                             pady=5, padx=(5, 15))

        # Q
        self.text_25 = tk.StringVar()
        self.text_25.set('0')
        self.label_25 = tk.Label(
            self.top_frame, text=lg.set_lang_text('PROPELLER_LR_LABEL_25'), font=FONT_NORMAL_BOLD)
        self.label_25.grid(row=7, column=6, sticky='NE',
                           pady=5, padx=(5, 0))
        self.entry_25 = tk.Entry(
            self.top_frame, font=FONT_NORMAL, textvariable=self.text_25, width=12)
        self.entry_25.grid(row=7, column=7, sticky='NW', pady=5)
        self.label_u_25 = tk.Label(
            self.top_frame, text=lg.set_lang_text('PROPELLER_LR_LABEL_U_NM'), font=FONT_NORMAL_BOLD)
        self.label_u_25.grid(row=7, column=8, sticky='NW',
                             pady=5, padx=(5, 15))

        # M
        self.text_26 = tk.StringVar()
        self.text_26.set('0')
        self.label_26 = tk.Label(
            self.top_frame, text=lg.set_lang_text('PROPELLER_LR_LABEL_26'), font=FONT_NORMAL_BOLD)
        self.label_26.grid(row=7, column=9, sticky='NE',
                           pady=5, padx=(5, 0))
        self.entry_26 = tk.Entry(
            self.top_frame, font=FONT_NORMAL, textvariable=self.text_26, width=12)
        self.entry_26.grid(row=7, column=10, sticky='NW', pady=5)
        self.label_u_26 = tk.Label(
            self.top_frame, text=lg.set_lang_text('PROPELLER_LR_LABEL_U_N'), font=FONT_NORMAL_BOLD)
        self.label_u_26.grid(row=7, column=11, sticky='NW',
                             pady=5, padx=(5, 15))

        # V1
        self.text_27 = tk.StringVar()
        self.text_27.set('0')
        self.label_27 = tk.Label(
            self.top_frame, text=lg.set_lang_text('PROPELLER_LR_LABEL_27'), font=FONT_NORMAL_BOLD)
        self.label_27.grid(row=7, column=12, sticky='NE',
                           pady=5, padx=(5, 0))
        self.entry_27 = tk.Entry(
            self.top_frame, font=FONT_NORMAL, textvariable=self.text_27, width=12)
        self.entry_27.grid(row=7, column=13, sticky='NW', pady=5)
        self.label_u_27 = tk.Label(
            self.top_frame, text=lg.set_lang_text('PROPELLER_LR_LABEL_U_NONE'), font=FONT_NORMAL_BOLD)
        self.label_u_27.grid(row=7, column=14, sticky='NW',
                             pady=5, padx=(5, 15))

        # row 8
        self.button_cal_k3 = tk.Button(self.top_frame,
                                       text=lg.set_lang_text(
                                           'PROPELLER_LR_BUTTON_CAL'),
                                       font=FONT_NORMAL,
                                       command=lambda: self.k3_calculation(
                                           self.text_7.get(),
                                           self.text_16.get()

                                       ))
        self.button_cal_k3.grid(row=8, column=1, sticky='NW',
                                padx=5, pady=5, ipadx=3, ipady=3)

        self.button_cal_l = tk.Button(self.top_frame,
                                      text=lg.set_lang_text(
                                          'PROPELLER_LR_BUTTON_CAL'),
                                      font=FONT_NORMAL,
                                      command=lambda: self.l_calculation(
                                          self.text_7.get(),
                                          self.text_22.get()

                                      ))
        self.button_cal_l.grid(row=8, column=4, sticky='NW',
                               padx=5, pady=5, ipadx=3, ipady=3)

        self.button_cal_Q = tk.Button(self.top_frame,
                                      text=lg.set_lang_text(
                                          'PROPELLER_LR_BUTTON_CAL'),
                                      font=FONT_NORMAL,
                                      command=lambda: self.q_calculation(
                                          self.text_19.get(),
                                          self.text_20.get()

                                      ))
        self.button_cal_Q.grid(row=8, column=7, sticky='NW',
                               padx=5, pady=5, ipadx=3, ipady=3)

        self.button_cal_M = tk.Button(self.top_frame,
                                      text=lg.set_lang_text(
                                          'PROPELLER_LR_BUTTON_CAL'),
                                      font=FONT_NORMAL,
                                      command=lambda: self.m_calculation(
                                          self.text_19.get(),
                                          self.text_21.get()

                                      ))
        self.button_cal_M.grid(row=8, column=10, sticky='NW',
                               padx=5, pady=5, ipadx=3, ipady=3)

        self.button_cal_V1 = tk.Button(self.top_frame,
                                       text=lg.set_lang_text(
                                           'PROPELLER_LR_BUTTON_CAL'),
                                       font=FONT_NORMAL,
                                       command=lambda: self.v1_calculation(
                                           self.text_12.get(),
                                           self.text_15.get()

                                       ))
        self.button_cal_V1.grid(row=8, column=13, sticky='NW',
                                padx=5, pady=5, ipadx=3, ipady=3)

        # row 9
        self.button_insert_k3 = tk.Button(self.top_frame,
                                          text=lg.set_lang_text(
                                              'PROPELLER_LR_BUTTON_INSERT'),
                                          font=FONT_NORMAL,
                                          command=lambda: self.mf.insert_value_to_entry(
                                              [self.entry_0],
                                              [self.text_23.get()]),
                                          state=tk.DISABLED)
        self.button_insert_k3.grid(
            row=9, column=1, sticky='NW', padx=5, pady=5, ipadx=3, ipady=3)

        self.button_insert_l = tk.Button(self.top_frame,
                                         text=lg.set_lang_text(
                                             'PROPELLER_LR_BUTTON_INSERT'),
                                         font=FONT_NORMAL,
                                         command=lambda: self.mf.insert_value_to_entry(
                                             [self.entry_5],
                                             [self.text_24.get()]),
                                         state=tk.DISABLED)
        self.button_insert_l.grid(
            row=9, column=4, sticky='NW', padx=5, pady=5, ipadx=3, ipady=3)

        self.button_insert_Q = tk.Button(self.top_frame,
                                         text=lg.set_lang_text(
                                             'PROPELLER_LR_BUTTON_INSERT'),
                                         font=FONT_NORMAL,
                                         command=lambda: self.mf.insert_value_to_entry(
                                             [self.entry_6],
                                             [self.text_25.get()]),
                                         state=tk.DISABLED)
        self.button_insert_Q.grid(
            row=9, column=7, sticky='NW', padx=5, pady=5, ipadx=3, ipady=3)

        self.button_insert_M = tk.Button(self.top_frame,
                                         text=lg.set_lang_text(
                                             'PROPELLER_LR_BUTTON_INSERT'),
                                         font=FONT_NORMAL,
                                         command=lambda: self.mf.insert_value_to_entry(
                                             [self.entry_9],
                                             [self.text_26.get()]),
                                         state=tk.DISABLED)
        self.button_insert_M.grid(
            row=9, column=10, sticky='NW', padx=5, pady=5, ipadx=3, ipady=3)

        self.button_insert_V1 = tk.Button(self.top_frame,
                                          text=lg.set_lang_text(
                                              'PROPELLER_LR_BUTTON_INSERT'),
                                          font=FONT_NORMAL,
                                          command=lambda: self.mf.insert_value_to_entry(
                                              [self.entry_11],
                                              [self.text_27.get()]),
                                          state=tk.DISABLED)
        self.button_insert_V1.grid(
            row=9, column=13, sticky='NW', padx=5, pady=5, ipadx=3, ipady=3)

        # DATA ACTIONS BUTTONS FRAME
        self.frame_action_buttons = tk.Frame(self.vs_frame.interior)
        self.frame_action_buttons.pack(padx=10, pady=10, expand=True, fill='x')

        self.button_cal_all = tk.Button(self.frame_action_buttons,
                                        text=lg.set_lang_text(
                                            'PROPELLER_LR_BUTTON_CAL'),
                                        font=FONT_NORMAL,
                                        command=lambda: self.all_calculation(
                                            self.text_0.get(),
                                            self.text_1.get(),
                                            self.text_2.get(),
                                            self.text_3.get(),
                                            self.text_4.get(),
                                            self.text_5.get(),
                                            self.text_6.get(),
                                            self.text_7.get(),
                                            self.text_8.get(),
                                            self.text_9.get(),
                                            self.text_10.get(),
                                            self.text_11.get(),
                                            self.text_12.get(),
                                            self.text_13.get(),
                                            self.text_14.get(),
                                            self.text_15.get(),
                                            self.text_16.get(),

                                            self.text_18.get()
                                        ))
        self.button_cal_all.pack(padx=5, pady=5, ipadx=3, ipady=3, side='left')

        self.button_save_all = tk.Button(self.frame_action_buttons,
                                         text=lg.set_lang_text(
                                             'PROPELLER_LR_BUTTON_SAVE'),
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
                                             self.text_7.get(),
                                             self.text_8.get(),
                                             self.text_9.get(),
                                             self.text_10.get(),
                                             self.text_11.get(),
                                             self.text_12.get(),
                                             self.text_13.get(),
                                             self.text_14.get(),
                                             self.text_15.get(),
                                             self.text_16.get(),

                                             self.text_18.get(),
                                             self.text_19.get(),
                                             self.text_20.get(),
                                             self.text_21.get(),
                                             self.text_22.get(),
                                             self.text_23.get(),
                                             self.text_24.get(),
                                             self.text_25.get(),
                                             self.text_26.get(),
                                             self.text_27.get()
                                         ))
        self.button_save_all.pack(
            padx=5, pady=5, ipadx=3, ipady=3, side='left')
        self.button_legend = tk.Button(
            self.frame_action_buttons, font=FONT_NORMAL, text=lg.set_lang_text('PROPELLER_LR_BUTTON_LEGEND'), command=lambda: self.ow.load_top_window('propeller_lr_legend.py'))
        self.button_legend.pack(
            padx=5, pady=5, ipadx=3, ipady=3, side='left')
        self.button_close = tk.Button(
            self.frame_action_buttons, font=FONT_NORMAL, text=lg.set_lang_text('PROPELLER_LR_BUTTON_CLOSE'), command=lambda: self.master.destroy())
        self.button_close.pack(
            padx=5, pady=5, ipadx=3, ipady=3, side='left')

    # INSERT DATA FROM DB

        if self.view == True:
            self.id = self.id_from_list
            entry_position = [self.entry_0, self.entry_1, self.entry_2, self.entry_3, self.entry_4, self.entry_5,
                              self.entry_6, self.entry_7, self.entry_8, self.entry_9, self.entry_10, self.entry_11, self.entry_12,
                              self.entry_13, self.entry_14, self.entry_15, self.entry_16, self.entry_18, self.entry_19,
                              self.entry_20, self.entry_21, self.entry_22, self.entry_23, self.entry_24,  self.entry_25,
                              self.entry_26,  self.entry_27, self.ship_name_entry]
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
                self.text_7.get(),
                self.text_8.get(),
                self.text_9.get(),
                self.text_10.get(),
                self.text_11.get(),
                self.text_12.get(),
                self.text_13.get(),
                self.text_14.get(),
                self.text_15.get(),
                self.text_16.get(),
                self.text_18.get()
            )

    def k3_calculation(self, *args):
        list_args = [arg for arg in args]

        if True in (self.mf.is_empty_or_zero(list_args)):
            tk.messagebox.showerror(lg.set_lang_text(
                'PROPELLER_LR_TITLE_MESSAGEBOX_1'),
                lg.set_lang_text('PROPELLER_LR_INFO_MESSAGEBOX_1'))
        else:
            float_list = self.mf.string_to_float_greater_than_zero(list_args)
            if 'no_float' in float_list or 'below_one' in float_list:
                tk.messagebox.showerror(lg.set_lang_text(
                    'PROPELLER_LR_TITLE_MESSAGEBOX_2'), lg.set_lang_text('PROPELLER_LR_INFO_MESSAGEBOX_2'))
            else:
                self.button_insert_k3['state'] = tk.NORMAL
                k3 = round((float_list[1] / float_list[0]), 4)
                self.mf.insert_value_to_entry([self.entry_23], [k3])

    def l_calculation(self, *args):
        list_args = [arg for arg in args]

        if True in (self.mf.is_empty_or_zero(list_args)):
            tk.messagebox.showerror(lg.set_lang_text(
                'PROPELLER_LR_TITLE_MESSAGEBOX_1'),
                lg.set_lang_text('PROPELLER_LR_INFO_MESSAGEBOX_3'))
        else:
            float_list = self.mf.string_to_float_greater_than_zero(list_args)
            if 'no_float' in float_list or 'below_one' in float_list:
                tk.messagebox.showerror(lg.set_lang_text(
                    'PROPELLER_LR_TITLE_MESSAGEBOX_2'), lg.set_lang_text('PROPELLER_LR_INFO_MESSAGEBOX_2'))
            else:
                self.button_insert_l['state'] = tk.NORMAL
                l = round((float_list[1] / float_list[0]), 4)
                self.mf.insert_value_to_entry([self.entry_24], [l])

    def q_calculation(self, *args):
        list_args = [arg for arg in args]

        if True in (self.mf.is_empty_or_zero(list_args)):
            tk.messagebox.showerror(lg.set_lang_text(
                'PROPELLER_LR_TITLE_MESSAGEBOX_1'),
                lg.set_lang_text('PROPELLER_LR_INFO_MESSAGEBOX_4'))
        else:
            float_list = self.mf.string_to_float_greater_than_zero(list_args)
            if 'no_float' in float_list or 'below_one' in float_list:
                tk.messagebox.showerror(lg.set_lang_text(
                    'PROPELLER_LR_TITLE_MESSAGEBOX_2'), lg.set_lang_text('PROPELLER_LR_INFO_MESSAGEBOX_2'))
            else:
                self.button_insert_Q['state'] = tk.NORMAL
                Q = round((float_list[0] / float_list[1]), 4)
                self.mf.insert_value_to_entry([self.entry_25], [Q])

    def m_calculation(self, *args):
        list_args = [arg for arg in args]

        if True in (self.mf.is_empty_or_zero(list_args)):
            tk.messagebox.showerror(lg.set_lang_text(
                'PROPELLER_LR_TITLE_MESSAGEBOX_1'),
                lg.set_lang_text('PROPELLER_LR_INFO_MESSAGEBOX_5'))
        else:
            float_list = self.mf.string_to_float_greater_than_zero(list_args)
            if 'no_float' in float_list or 'below_one' in float_list:
                tk.messagebox.showerror(lg.set_lang_text(
                    'PROPELLER_LR_TITLE_MESSAGEBOX_2'), lg.set_lang_text('PROPELLER_LR_INFO_MESSAGEBOX_2'))
            else:
                self.button_insert_M['state'] = tk.NORMAL
                M = round(1760*(float_list[0] / float_list[1]), 4)
                self.mf.insert_value_to_entry([self.entry_26], [M])

    def v1_calculation(self, *args):
        list_args = [arg for arg in args]

        if True in (self.mf.is_empty_or_zero(list_args)):
            tk.messagebox.showerror(lg.set_lang_text(
                'PROPELLER_LR_TITLE_MESSAGEBOX_1'),
                lg.set_lang_text('PROPELLER_LR_INFO_MESSAGEBOX_6'))
        else:
            float_list = self.mf.string_to_float_greater_than_zero(list_args)
            if 'no_float' in float_list or 'below_one' in float_list:
                tk.messagebox.showerror(lg.set_lang_text(
                    'PROPELLER_LR_TITLE_MESSAGEBOX_2'), lg.set_lang_text('PROPELLER_LR_INFO_MESSAGEBOX_2'))
            else:
                self.button_insert_V1['state'] = tk.NORMAL
                V1 = round(
                    ((0.51*(pow(float_list[1] / float_list[0], 2))) - 1), 4)
                self.mf.insert_value_to_entry([self.entry_27], [V1])

    def all_calculation(self, *args):
        list_args = [arg for arg in args]
        if True in (self.mf.is_empty_str(list_args)):
            tk.messagebox.showerror(lg.set_lang_text(
                'PROPELLER_LR_TITLE_MESSAGEBOX_1'),
                lg.set_lang_text('PROPELLER_LR_INFO_MESSAGEBOX_5'))
        else:
            float_list = self.mf.string_to_float_greater_than_zero(list_args)
            if 'no_float' in float_list or 'below_one' in float_list:
                tk.messagebox.showerror(lg.set_lang_text(
                    'PROPELLER_LR_TITLE_MESSAGEBOX_2'), lg.set_lang_text('PROPELLER_LR_INFO_MESSAGEBOX_2'))
            else:
                try:
                    F1 = (2*float_list[6] / float_list[7])*(1+float_list[8])

                    p1 = ((2*float_list[9])/(float_list[10]*float_list[12] *
                                             float_list[11]))*(-1+(sqrt((1+float_list[11]*((pow(F1, 2)/pow(float_list[9], 2)+1))))))

                    B3 = (1/float_list[1])*(((pow(float_list[0], 2)+1) /
                                             (pow(float_list[0], 2)-1))+float_list[4])+(1/float_list[2])*(((1+pow(float_list[5], 2)/(1-pow(float_list[5], 2))))-float_list[3])
                    try:
                        self.calculation_all_frame.destroy()
                    except AttributeError:
                        pass

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

                    self.propeller_lr_df = pd.DataFrame()

                    # adding temp col
                    self.propeller_lr_df[lg.set_lang_text(
                        "PROPELLER_LR_DF_COL_TEMP")] = [x for x in range(0, 36)]
                    self.propeller_lr_df[lg.set_lang_text(
                        "PROPELLER_LR_DF_COL_DT_MIN")] = (float_list[7]/float_list[12])*((p1*B3)+(float_list[13]-float_list[14])*(35-self.propeller_lr_df[lg.set_lang_text(
                            "PROPELLER_LR_DF_COL_TEMP")]))
                    if float_list[17] == 0:
                        self.propeller_lr_df[lg.set_lang_text(
                            "PROPELLER_LR_DF_COL_DT_MAX")] = 0
                    else:
                        self.propeller_lr_df[lg.set_lang_text(
                            "PROPELLER_LR_DF_COL_DT_MAX")] = self.propeller_lr_df[lg.set_lang_text(
                                "PROPELLER_LR_DF_COL_DT_MIN")] + float_list[17]

                    # table section

                    self.table_frame = tk.Frame(
                        self.calculation_all_frame)
                    self.table_frame.pack(
                        fill='both', expand=True, padx=10, pady=10)

                    self.mf.tabel_show(
                        self.table_frame, self.propeller_lr_df)

                    self.export_button_frame = tk.Frame(
                        self.calculation_all_frame)
                    self.export_button_frame.pack(
                        fill='both', expand=True, padx=10, pady=10)

                    self.export_button = tk.Button(self.export_button_frame, text=lg.set_lang_text(
                        'PROPELLER_LR_BUTTON_EXPORT'),
                        font=FONT_NORMAL,
                        command=lambda: self.mf.export_df_xlxs(self.propeller_lr_df, self.ship_name.get()))
                    self.export_button.pack()

                    # plot section

                    self.frame_plot_dt = tk.Frame(self.calculation_all_frame)
                    self.frame_plot_dt.pack(
                        fill='both', expand=True, padx=10, pady=10)

                    self.mf.plot_lines(self.frame_plot_dt,
                                       [
                                           self.propeller_lr_df[lg.set_lang_text(
                                               "PROPELLER_LR_DF_COL_TEMP")],
                                           self.propeller_lr_df[lg.set_lang_text(
                                               "PROPELLER_LR_DF_COL_DT_MIN")],
                                           self.propeller_lr_df[lg.set_lang_text(
                                               "PROPELLER_LR_DF_COL_DT_MAX")]
                                       ],
                                       [
                                           lg.set_lang_text(
                                               "PROPELLER_LR_PLOT_MIN_TOLER_LABEL"),
                                           lg.set_lang_text(
                                               "PROPELLER_LR_PLOT_MAX_TOLER_LABEL")
                                       ],
                                       [
                                           lg.set_lang_text(
                                               'PROPELLER_LR_PLOT_TITLE'),
                                           self.ship_name.get(),
                                           lg.set_lang_text(
                                               'PROPELLER_LR_DF_COL_TEMP'),
                                           lg.set_lang_text(
                                               'PROPELLER_LR_DF_COL_DT'),
                                           lg.set_lang_text(
                                               'PROPELLER_LR_DF_COL_DT_MAX')
                                       ]
                                       )
                    self.frame_plot_wt = tk.Frame(self.calculation_all_frame)
                    self.frame_plot_wt.pack(
                        fill='both', expand=True, padx=10, pady=10)

                except ZeroDivisionError:
                    tk.messagebox.showerror(lg.set_lang_text(
                        'PROPELLER_LR_TITLE_MESSAGEBOX_3'), lg.set_lang_text('PROPELLER_LR_INFO_MESSAGEBOX_7'))


if __name__ == "__main__":
    root = tk.Tk()
    app = PropellerLR(master=root)
    app.mainloop()
