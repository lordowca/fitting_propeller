
import tkinter as tk


from modules.lang_module import LangTextDisplay
from modules.load_window import OpenWindow


lg = LangTextDisplay(file_name='main')
FONT_HEADER = ('Helvetica', 22, 'bold')
FONT_MIDLE_SIZE = ('Helvetica', 16, 'bold')
FONT_NORMAL_BOLD = ('Helvetica', 12, 'bold')
FONT_NORMAL = ('Helvetica', 12)


class ChoiceCalculation(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.master = master
        self.ow = OpenWindow(self.master)

        self.master.title(lg.set_lang_text('WELCOME_MENU_TITLE'))

        # geometry and window options

        self.window_width = 550
        self.window_height = 600

        self.screen_width = self.winfo_screenwidth()
        self.screen_height = self.winfo_screenheight()

        self.center_x = int(self.screen_width/2 - self.window_width / 2)
        self.center_y = int(self.screen_height/2 - self.window_height/2)

        self.master.geometry(
            f'{self.window_width}x{self.window_height}+{self.center_x}+{self.center_y}')
        self.master.resizable(False, False)

        self.master.columnconfigure(0, weight=1)

        self.label1 = tk.Label(
            self.master, text=lg.set_lang_text('WELCOME_MENU_LABEL1'),
            font=FONT_HEADER, anchor=tk.CENTER)
        self.label1.grid(row=0, column=0, sticky=tk.NSEW, padx=10, pady=20)

        self.lable2 = tk.Label(self.master, text=lg.set_lang_text('WELCOME_MENU_LABEL2'),
                               font=FONT_NORMAL_BOLD, anchor=tk.CENTER)
        self.lable2.grid(row=1, column=0, sticky=tk.NSEW, padx=10, pady=20)
        self.frame_buttons_lable2 = tk.Frame(self.master)
        self.frame_buttons_lable2.grid(
            row=2, column=0, padx=10,)
        # buttons for label 2
        self.button1 = tk.Button(
            self.frame_buttons_lable2,
            text=lg.set_lang_text('WELCOME_MENU_BUTTON1'),
            font=FONT_NORMAL,
            command=lambda: self.ow.open_new_window('python twopoint.py')
        )

        self.button1.pack(padx=5, pady=5, ipadx=3, ipady=3, side='left')

        self.button2 = tk.Button(
            self.frame_buttons_lable2,
            text=lg.set_lang_text('WELCOME_MENU_BUTTON2'),
            font=FONT_NORMAL,
            command=lambda: self.ow.open_new_window('python fourpoint.py')
        )

        self.button2.pack(padx=5, pady=5, ipadx=3, ipady=3, side='left')

        self.label3 = tk.Label(self.master, text=lg.set_lang_text('WELCOME_MENU_LABEL3'),
                               font=FONT_NORMAL_BOLD, anchor=tk.CENTER)
        self.label3.grid(row=3, column=0, sticky=tk.NSEW, padx=10, pady=20)
        self.label3.bind('<Configure>', lambda e: self.label3.config(
            wraplength=self.label3.winfo_width()))

        self.frame_buttons_lable3 = tk.Frame(self.master)
        self.frame_buttons_lable3.grid(
            row=4, column=0, padx=10,)

        self.button2 = tk.Button(
            self.frame_buttons_lable3,
            text=lg.set_lang_text('WELCOME_MENU_BUTTON_BV'),
            font=FONT_NORMAL,
            command=lambda: self.ow.open_new_window('python propeller_bv.py')
        )

        self.button2.pack(padx=5, pady=5, ipadx=3, ipady=3, side='left')

        self.button3 = tk.Button(
            self.frame_buttons_lable3,
            text=lg.set_lang_text('WELCOME_MENU_BUTTON_DNV'),
            font=FONT_NORMAL,
            command=lambda: self.ow.open_new_window('python propeller_dnv.py')
        )

        self.button3.pack(padx=5, pady=5, ipadx=3, ipady=3, side='left')

        self.button4 = tk.Button(
            self.frame_buttons_lable3,
            text=lg.set_lang_text('WELCOME_MENU_BUTTON_LR'),
            font=FONT_NORMAL,
            command=lambda: self.ow.open_new_window('python propeller_lr.py')
        )

        self.button4.pack(padx=5, pady=5, ipadx=3, ipady=3, side='left')

        self.list_lable = tk.Label(self.master, text=lg.set_lang_text('WELCOME_MENU_LIST_LABEL'),
                                   font=FONT_NORMAL_BOLD, anchor=tk.CENTER)
        self.list_lable.grid(row=8, column=0, sticky=tk.NSEW, padx=10, pady=20)

        self.frame_list_button = tk.Frame(self.master)
        self.frame_list_button.grid(
            row=9, column=0, sticky=tk.NSEW, padx=10)

        self.list_button = tk.Button(
            self.frame_list_button,
            text=lg.set_lang_text('WELCOME_MENU_LIST_BUTTON'),
            font=FONT_NORMAL,
            command=lambda: self.ow.open_new_window('python ship_list.py')
        )
        self.list_button.pack(padx=5, pady=5, ipadx=3, ipady=3)

        self.language_lable = tk.Label(self.master, text=lg.set_lang_text('WELCOME_MENU_LANGUAGE_LABEL'),
                                       font=FONT_NORMAL_BOLD, anchor=tk.CENTER)
        self.language_lable.grid(
            row=10, column=0, sticky=tk.NSEW, padx=10, pady=20)
        self.frame_list_language = tk.Frame(self.master)
        self.frame_list_language.grid(
            row=11, column=0, padx=10)

        self.option_list = ['English', 'Polski']
        self.value = tk.StringVar(self.frame_list_language)
        self.value.set(lg.current_language_value())

        self.menu = tk.OptionMenu(
            self.frame_list_language, self.value, *self.option_list)
        self.menu.pack(padx=5, pady=5, ipadx=3, ipady=3, side='left')

        self.save_button = tk.Button(
            self.frame_list_language,
            text=lg.set_lang_text('WELCOME_MENU_SAVE_BUTTON'),
            font=FONT_NORMAL,
            command=lambda: lg.save_language(self.value.get(), self.master)
        )
        self.save_button.pack(padx=5, pady=5, ipadx=3, ipady=3, side='left')


if __name__ == "__main__":
    root = tk.Tk()
    app = ChoiceCalculation(master=root)
    app.mainloop()
