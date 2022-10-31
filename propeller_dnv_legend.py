import tkinter as tk

from modules.lang_module import LangTextDisplay
from modules.scroll_frame import VerticalScrolledFrame
from modules.misc_functions import MiscFunctions

lg = LangTextDisplay(file_name='propeller_dnv_legend')

FONT_HEADER = ('Helvetica', 22, 'bold')
FONT_MIDLE_SIZE = ('Helvetica', 16, 'bold')
FONT_NORMAL_BOLD = ('Helvetica', 12, 'bold')
FONT_NORMAL = ('Helvetica', 12)


class PropellerDNVLegend(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master

        self.master.title(lg.set_lang_text('PROPELLER_DNV_LEDEND_TITLE'))
        # window parametrs and position
        self.app_width = 600
        self.app_height = int(self.winfo_screenheight()-100)
        self.app_center_x = int(
            self.winfo_screenwidth() / 2) - int(self.app_width/2)
        self.master.geometry(
            f'{self.app_width}x{self.app_height}+{self.app_center_x}+{20}')
        self.master.resizable(False, True)
        self.mf = MiscFunctions(self.master)

        # Create a frame to put the VerticalScrolledFrame inside
        self.holder_frame = tk.Frame(self.master)
        self.holder_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=tk.TRUE)

        # Create the VerticalScrolledFrame
        self.vs_frame = VerticalScrolledFrame(self.holder_frame)
        self.vs_frame.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=tk.TRUE)

        self.propeller_bv_lagend_table()

    def propeller_bv_lagend_table(self):

        self.frame_legend = tk.Frame(self.vs_frame.interior)
        self.frame_legend.pack(padx=10, pady=10)
        self.frame_legend.columnconfigure(0, weight=1)
        self.frame_legend.columnconfigure(1, weight=1)

        self.label_title = tk.Label(
            self.frame_legend, text=lg.set_lang_text('PROPELLER_DNV_LEDEND_TITLE'), font=FONT_HEADER)
        self.label_title.grid(row=0, column=0, columnspan=2,
                              sticky=tk.NSEW, padx=10, pady=10, ipadx=5)

        self.label_0 = tk.Label(
            self.frame_legend, text=f"{lg.set_lang_text('PROPELLER_DNV_LEDEND_LABEL_0')} - ", font=FONT_NORMAL_BOLD)
        self.label_0.grid(
            row=1, column=0, sticky=tk.NSEW, padx=10, pady=10, ipadx=5)
        self.label_0_desc = tk.Label(
            self.frame_legend, text=lg.set_lang_text('PROPELLER_DNV_LEDEND_LABEL_0_DESC'), font=FONT_NORMAL)
        self.label_0_desc.grid(
            row=1, column=1, sticky=tk.W, padx=10, pady=10, ipadx=5)

        self.label_1 = tk.Label(
            self.frame_legend, text=f"{lg.set_lang_text('PROPELLER_DNV_LEDEND_LABEL_1')} - ", font=FONT_NORMAL_BOLD)
        self.label_1.grid(
            row=2, column=0, sticky=tk.NSEW, padx=10, pady=10, ipadx=5)
        self.label_1_desc = tk.Label(
            self.frame_legend, text=lg.set_lang_text('PROPELLER_DNV_LEDEND_LABEL_1_DESC'), font=FONT_NORMAL)
        self.label_1_desc.grid(
            row=2, column=1, sticky=tk.W, padx=10, pady=10, ipadx=5)

        self.label_2 = tk.Label(
            self.frame_legend, text=f"{lg.set_lang_text('PROPELLER_DNV_LEDEND_LABEL_2')} - ", font=FONT_NORMAL_BOLD)
        self.label_2.grid(
            row=3, column=0, sticky=tk.NSEW, padx=10, pady=10, ipadx=5)
        self.label_2_desc = tk.Label(
            self.frame_legend, text=lg.set_lang_text('PROPELLER_DNV_LEDEND_LABEL_2_DESC'), font=FONT_NORMAL)
        self.label_2_desc.grid(
            row=3, column=1, sticky=tk.W, padx=10, pady=10, ipadx=5)

        self.label_3 = tk.Label(
            self.frame_legend, text=f"{lg.set_lang_text('PROPELLER_DNV_LEDEND_LABEL_3')} - ", font=FONT_NORMAL_BOLD)
        self.label_3.grid(
            row=4, column=0, sticky=tk.NSEW, padx=10, pady=10, ipadx=5)
        self.label_3_desc = tk.Label(
            self.frame_legend, text=lg.set_lang_text('PROPELLER_DNV_LEDEND_LABEL_3_DESC'), font=FONT_NORMAL, wraplength=480)
        self.label_3_desc.grid(
            row=4, column=1, sticky=tk.W, padx=10, pady=10, ipadx=5)

        self.label_4 = tk.Label(
            self.frame_legend, text=f"{lg.set_lang_text('PROPELLER_DNV_LEDEND_LABEL_4')} - ", font=FONT_NORMAL_BOLD)
        self.label_4.grid(
            row=5, column=0, sticky=tk.NSEW, padx=10, pady=10, ipadx=5)
        self.label_4_desc = tk.Label(
            self.frame_legend, text=lg.set_lang_text('PROPELLER_DNV_LEDEND_LABEL_4_DESC'), font=FONT_NORMAL,  wraplength=480)
        self.label_4_desc.grid(
            row=5, column=1, sticky=tk.W, padx=10, pady=10, ipadx=5)

        self.label_5 = tk.Label(
            self.frame_legend, text=f"{lg.set_lang_text('PROPELLER_DNV_LEDEND_LABEL_5')} - ", font=FONT_NORMAL_BOLD)
        self.label_5.grid(
            row=6, column=0, sticky=tk.NSEW, padx=10, pady=10, ipadx=5)
        self.label_5_desc = tk.Label(
            self.frame_legend, text=lg.set_lang_text('PROPELLER_DNV_LEDEND_LABEL_5_DESC'), font=FONT_NORMAL)
        self.label_5_desc.grid(
            row=6, column=1, sticky=tk.W, padx=10, pady=10, ipadx=5)

        self.label_6 = tk.Label(
            self.frame_legend, text=f"{lg.set_lang_text('PROPELLER_DNV_LEDEND_LABEL_6')} - ", font=FONT_NORMAL_BOLD)
        self.label_6.grid(
            row=7, column=0, sticky=tk.NSEW, padx=10, pady=10, ipadx=5)
        self.label_6_desc = tk.Label(
            self.frame_legend, text=lg.set_lang_text('PROPELLER_DNV_LEDEND_LABEL_6_DESC'), font=FONT_NORMAL, wraplength=480)
        self.label_6_desc.grid(
            row=7, column=1, sticky=tk.W, padx=10, pady=10, ipadx=5)

        self.label_7 = tk.Label(
            self.frame_legend, text=f"{lg.set_lang_text('PROPELLER_DNV_LEDEND_LABEL_7')} - ", font=FONT_NORMAL_BOLD)
        self.label_7.grid(
            row=8, column=0, sticky=tk.NSEW, padx=10, pady=10, ipadx=5)
        self.label_7_desc = tk.Label(
            self.frame_legend, text=lg.set_lang_text('PROPELLER_DNV_LEDEND_LABEL_7_DESC'), font=FONT_NORMAL)
        self.label_7_desc.grid(
            row=8, column=1, sticky=tk.W, padx=10, pady=10, ipadx=5)

        self.label_8 = tk.Label(
            self.frame_legend, text=f"{lg.set_lang_text('PROPELLER_DNV_LEDEND_LABEL_8')} - ", font=FONT_NORMAL_BOLD)
        self.label_8.grid(
            row=9, column=0, sticky=tk.NSEW, padx=10, pady=10, ipadx=5)
        self.label_8_desc = tk.Label(
            self.frame_legend, text=lg.set_lang_text('PROPELLER_DNV_LEDEND_LABEL_8_DESC'), font=FONT_NORMAL)
        self.label_8_desc.grid(
            row=9, column=1, sticky=tk.W, padx=10, pady=10, ipadx=5)

        self.label_9 = tk.Label(
            self.frame_legend, text=f"{lg.set_lang_text('PROPELLER_DNV_LEDEND_LABEL_9')} - ", font=FONT_NORMAL_BOLD)
        self.label_9.grid(
            row=10, column=0, sticky=tk.NSEW, padx=10, pady=10, ipadx=5)
        self.label_9_desc = tk.Label(
            self.frame_legend, text=lg.set_lang_text('PROPELLER_DNV_LEDEND_LABEL_9_DESC'), font=FONT_NORMAL)
        self.label_9_desc.grid(
            row=10, column=1, sticky=tk.W, padx=10, pady=10, ipadx=5)

        self.label_10 = tk.Label(
            self.frame_legend, text=f"{lg.set_lang_text('PROPELLER_DNV_LEDEND_LABEL_10')} - ", font=FONT_NORMAL_BOLD)
        self.label_10.grid(
            row=11, column=0, sticky=tk.NSEW, padx=10, pady=10, ipadx=5)
        self.label_10_desc = tk.Label(
            self.frame_legend, text=lg.set_lang_text('PROPELLER_DNV_LEDEND_LABEL_10_DESC'), font=FONT_NORMAL)
        self.label_10_desc.grid(
            row=11, column=1, sticky=tk.W, padx=10, pady=10, ipadx=5)

        self.label_11 = tk.Label(
            self.frame_legend, text=f"{lg.set_lang_text('PROPELLER_DNV_LEDEND_LABEL_11')} - ", font=FONT_NORMAL_BOLD)
        self.label_11.grid(
            row=12, column=0, sticky=tk.NSEW, padx=10, pady=10, ipadx=5)
        self.label_11_desc = tk.Label(
            self.frame_legend, text=lg.set_lang_text('PROPELLER_DNV_LEDEND_LABEL_11_DESC'), font=FONT_NORMAL)
        self.label_11_desc.grid(
            row=12, column=1, sticky=tk.W, padx=10, pady=10, ipadx=5)

        self.label_12 = tk.Label(
            self.frame_legend, text=f"{lg.set_lang_text('PROPELLER_DNV_LEDEND_LABEL_12')} - ", font=FONT_NORMAL_BOLD)
        self.label_12.grid(
            row=13, column=0, sticky=tk.NSEW, padx=10, pady=10, ipadx=5)
        self.label_12_desc = tk.Label(
            self.frame_legend, text=lg.set_lang_text('PROPELLER_DNV_LEDEND_LABEL_12_DESC'), font=FONT_NORMAL)
        self.label_12_desc.grid(
            row=13, column=1, sticky=tk.W, padx=10, pady=10, ipadx=5)

        self.label_13 = tk.Label(
            self.frame_legend, text=f"{lg.set_lang_text('PROPELLER_DNV_LEDEND_LABEL_13')} - ", font=FONT_NORMAL_BOLD)
        self.label_13.grid(
            row=14, column=0, sticky=tk.NSEW, padx=10, pady=10, ipadx=5)
        self.label_13_desc = tk.Label(
            self.frame_legend, text=lg.set_lang_text('PROPELLER_DNV_LEDEND_LABEL_13_DESC'), font=FONT_NORMAL)
        self.label_13_desc.grid(
            row=14, column=1, sticky=tk.W, padx=10, pady=10, ipadx=5)

        self.label_14 = tk.Label(
            self.frame_legend, text=f"{lg.set_lang_text('PROPELLER_DNV_LEDEND_LABEL_14')} - ", font=FONT_NORMAL_BOLD)
        self.label_14.grid(
            row=15, column=0, sticky=tk.NSEW, padx=10, pady=10, ipadx=5)
        self.label_14_desc = tk.Label(
            self.frame_legend, text=lg.set_lang_text('PROPELLER_DNV_LEDEND_LABEL_14_DESC'), font=FONT_NORMAL, wraplength=480)
        self.label_14_desc.grid(
            row=15, column=1, sticky=tk.W, padx=10, pady=10, ipadx=5)

        self.label_15 = tk.Label(
            self.frame_legend, text=f"{lg.set_lang_text('PROPELLER_DNV_LEDEND_LABEL_15')} - ", font=FONT_NORMAL_BOLD)
        self.label_15.grid(
            row=16, column=0, sticky=tk.NSEW, padx=10, pady=10, ipadx=5)
        self.label_15_desc = tk.Label(
            self.frame_legend, text=lg.set_lang_text('PROPELLER_DNV_LEDEND_LABEL_15_DESC'), font=FONT_NORMAL)
        self.label_15_desc.grid(
            row=16, column=1, sticky=tk.W, padx=10, pady=10, ipadx=5)

        self.label_16 = tk.Label(
            self.frame_legend, text=f"{lg.set_lang_text('PROPELLER_DNV_LEDEND_LABEL_16')} - ", font=FONT_NORMAL_BOLD)
        self.label_16.grid(
            row=17, column=0, sticky=tk.NSEW, padx=10, pady=10, ipadx=5)
        self.label_16_desc = tk.Label(
            self.frame_legend, text=lg.set_lang_text('PROPELLER_DNV_LEDEND_LABEL_16_DESC'), font=FONT_NORMAL)
        self.label_16_desc.grid(
            row=17, column=1, sticky=tk.W, padx=10, pady=10, ipadx=5)

        self.label_17 = tk.Label(
            self.frame_legend, text=f"{lg.set_lang_text('PROPELLER_DNV_LEDEND_LABEL_17')} - ", font=FONT_NORMAL_BOLD)
        self.label_17.grid(
            row=18, column=0, sticky=tk.NSEW, padx=10, pady=10, ipadx=5)
        self.label_17_desc = tk.Label(
            self.frame_legend, text=lg.set_lang_text('PROPELLER_DNV_LEDEND_LABEL_17_DESC'), font=FONT_NORMAL)
        self.label_17_desc.grid(
            row=18, column=1, sticky=tk.W, padx=10, pady=10, ipadx=5)

        self.label_18 = tk.Label(
            self.frame_legend, text=f"{lg.set_lang_text('PROPELLER_DNV_LEDEND_LABEL_18')} - ", font=FONT_NORMAL_BOLD)
        self.label_18.grid(
            row=19, column=0, sticky=tk.NSEW, padx=10, pady=10, ipadx=5)
        self.label_18_desc = tk.Label(
            self.frame_legend, text=lg.set_lang_text('PROPELLER_DNV_LEDEND_LABEL_18_DESC'), font=FONT_NORMAL)
        self.label_18_desc.grid(
            row=19, column=1, sticky=tk.W, padx=10, pady=10, ipadx=5)

        self.label_19 = tk.Label(
            self.frame_legend, text=f"{lg.set_lang_text('PROPELLER_DNV_LEDEND_LABEL_19')} - ", font=FONT_NORMAL_BOLD)
        self.label_19.grid(
            row=20, column=0, sticky=tk.NSEW, padx=10, pady=10, ipadx=5)
        self.label_19_desc = tk.Label(
            self.frame_legend, text=lg.set_lang_text('PROPELLER_DNV_LEDEND_LABEL_19_DESC'), font=FONT_NORMAL)
        self.label_19_desc.grid(
            row=20, column=1, sticky=tk.W, padx=10, pady=10, ipadx=5)

        self.label_20 = tk.Label(
            self.frame_legend, text=f"{lg.set_lang_text('PROPELLER_DNV_LEDEND_LABEL_20')} - ", font=FONT_NORMAL_BOLD)
        self.label_20.grid(
            row=21, column=0, sticky=tk.NSEW, padx=10, pady=10, ipadx=5)
        self.label_20_desc = tk.Label(
            self.frame_legend, text=lg.set_lang_text('PROPELLER_DNV_LEDEND_LABEL_20_DESC'), font=FONT_NORMAL)
        self.label_20_desc.grid(
            row=21, column=1, sticky=tk.W, padx=10, pady=10, ipadx=5)

        self.frame_formula = tk.Frame(self.vs_frame.interior)
        self.frame_formula.pack(padx=10, pady=10)
        self.frame_formula.columnconfigure(0, weight=1)

        self.label_title = tk.Label(
            self.frame_formula, text=lg.set_lang_text('PROPELLER_DNV_LEDEND_FORMULA_TITLE'), font=FONT_HEADER)
        self.label_title.grid(row=0, column=0,
                              sticky=tk.NSEW, padx=10, pady=10, ipadx=5)

        self.label_0 = tk.Label(
            self.frame_formula, text=f"{lg.set_lang_text('PROPELLER_DNV_LEDEND_LABEL_FORMULA_0')} ", font=FONT_NORMAL_BOLD, wraplength=480)
        self.label_0.grid(
            row=1, column=0, sticky=tk.NSEW, padx=10, pady=10, ipadx=5)

        self.img_1 = self.mf.image_to_label(
            'images/propeller_dnv/image_1.png', 500)
        self.label_1 = tk.Label(
            self.frame_formula,  image=self.img_1)
        self.label_1.grid(
            row=2, column=0, sticky=tk.NSEW, padx=10, pady=10, ipadx=5)

        self.label_2 = tk.Label(
            self.frame_formula, text=f"{lg.set_lang_text('PROPELLER_DNV_LEDEND_LABEL_FORMULA_1')} ", font=FONT_NORMAL_BOLD, wraplength=480)
        self.label_2.grid(
            row=3, column=0, sticky=tk.NSEW, padx=10, pady=10, ipadx=5)

        self.img_2 = self.mf.image_to_label(
            'images/propeller_dnv/image_2.png', 500)
        self.label_3 = tk.Label(
            self.frame_formula,  image=self.img_2)
        self.label_3.grid(
            row=4, column=0, sticky=tk.NSEW, padx=10, pady=10, ipadx=5)

        self.label_4 = tk.Label(
            self.frame_formula, text=f"{lg.set_lang_text('PROPELLER_DNV_LEDEND_LABEL_FORMULA_2')} ", font=FONT_NORMAL_BOLD, wraplength=480)
        self.label_4.grid(
            row=5, column=0, sticky=tk.NSEW, padx=10, pady=10, ipadx=5)

        self.img_3 = self.mf.image_to_label(
            'images/propeller_dnv/image_3.png')
        self.label_5 = tk.Label(
            self.frame_formula,  image=self.img_3)
        self.label_5.grid(
            row=6, column=0, sticky=tk.NSEW, padx=10, pady=10, ipadx=5)

        self.label_6 = tk.Label(
            self.frame_formula, text=f"{lg.set_lang_text('PROPELLER_DNV_LEDEND_LABEL_FORMULA_3')} ", font=FONT_NORMAL_BOLD, wraplength=480)
        self.label_6.grid(
            row=7, column=0, sticky=tk.NSEW, padx=10, pady=10, ipadx=5)

        self.img_4 = self.mf.image_to_label(
            'images/propeller_dnv/image_4.png')
        self.label_7 = tk.Label(
            self.frame_formula,  image=self.img_4)
        self.label_7.grid(
            row=8, column=0, sticky=tk.NSEW, padx=10, pady=10, ipadx=5)

        self.label_8 = tk.Label(
            self.frame_formula, text=f"{lg.set_lang_text('PROPELLER_DNV_LEDEND_LABEL_FORMULA_4')} ", font=FONT_NORMAL_BOLD, wraplength=480)
        self.label_8.grid(
            row=9, column=0, sticky=tk.NSEW, padx=10, pady=10, ipadx=5)

        self.img_5 = self.mf.image_to_label(
            'images/propeller_dnv/image_5.png')
        self.label_9 = tk.Label(
            self.frame_formula,  image=self.img_5)
        self.label_9.grid(
            row=10, column=0, sticky=tk.NSEW, padx=10, pady=10, ipadx=5)

        self.label_10 = tk.Label(
            self.frame_formula, text=f"{lg.set_lang_text('PROPELLER_DNV_LEDEND_LABEL_FORMULA_5')} ", font=FONT_NORMAL_BOLD, wraplength=480)
        self.label_10.grid(
            row=11, column=0, sticky=tk.NSEW, padx=10, pady=10, ipadx=5)

        self.img_6 = self.mf.image_to_label(
            'images/propeller_dnv/image_6.png', 500)
        self.label_11 = tk.Label(
            self.frame_formula,  image=self.img_6)
        self.label_11.grid(
            row=12, column=0, sticky=tk.NSEW, padx=10, pady=10, ipadx=5)

        self.label_12 = tk.Label(
            self.frame_formula, text=f"{lg.set_lang_text('PROPELLER_DNV_LEDEND_LABEL_FORMULA_6')} ", font=FONT_NORMAL_BOLD, wraplength=480)
        self.label_12.grid(
            row=13, column=0, sticky=tk.NSEW, padx=10, pady=10, ipadx=5)

        self.img_7 = self.mf.image_to_label(
            'images/propeller_dnv/image_7.png')
        self.label_13 = tk.Label(
            self.frame_formula,  image=self.img_7)
        self.label_13.grid(
            row=14, column=0, sticky=tk.NSEW, padx=10, pady=10, ipadx=5)


if __name__ == "__main__":
    root = tk.Tk()
    app = PropellerDNVLegend(master=root)
    app.mainloop()
