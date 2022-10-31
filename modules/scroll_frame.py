from sys import platform
import tkinter as tk
import functools
fp = functools.partial


class VerticalScrolledFrame(tk.Frame):
    """
    A pure Tkinter scrollable frame that actually works!
    * Use the 'interior' attribute to place widgets inside the scrollable frame
    * Construct and pack/place/grid normally
    * This frame only allows vertical scrolling
    * This comes from a different naming of the the scrollwheel 'button', on different systems.
    * link to source https://gist.github.com/JackTheEngineer/81df334f3dcff09fd19e4169dd560c59
    """

    def __init__(self, parent, *args, **kw):

        super().__init__(parent, *args, **kw)

        # create a canvas object and a vertical scrollbar for scrolling it
        self.vscrollbar = tk.Scrollbar(self, orient=tk.VERTICAL)
        self.vscrollbar.pack(fill=tk.Y, side=tk.RIGHT, expand=tk.FALSE)
        self.canvas = tk.Canvas(
            self, bd=0, highlightthickness=0, yscrollcommand=self.vscrollbar.set)
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=tk.TRUE)
        self.vscrollbar.config(command=self.canvas.yview)

        # reset the view
        self.canvas.xview_moveto(0)
        self.canvas.yview_moveto(0)

        # create a frame inside the canvas which will be scrolled with it
        self.interior = tk.Frame(self.canvas)
        self.interior_id = self.canvas.create_window(0, 0, window=self.interior,
                                                     anchor=tk.NW)

        self.interior.bind('<Configure>', self._configure_interior)
        self.canvas.bind('<Configure>', self._configure_canvas)
        self.canvas.bind('<Enter>', self._bind_to_mousewheel)
        self.canvas.bind('<Leave>', self._unbind_from_mousewheel)

        # track changes to the canvas and frame width and sync them,
        # also updating the scrollbar

    def _configure_interior(self, event):
        # update the scrollbars to match the size of the inner frame
        size = (self.interior.winfo_reqwidth(),
                self.interior.winfo_reqheight())
        self.canvas.config(scrollregion="0 0 %s %s" % size)

        if self.interior.winfo_reqwidth() != self.winfo_width():
            # update the canvas's width to fit the inner frame
            self.canvas.config(width=self.interior.winfo_reqwidth())

    def _configure_canvas(self, event):
        if self.interior.winfo_reqwidth() != self.winfo_width():
            # update the inner frame's width to fill the canvas
            self.canvas.itemconfigure(
                self.interior_id, width=self.winfo_width())

    # This can now handle either windows or linux platforms
    def _on_mousewheel(self, event, scroll=None):

        if platform == "linux" or platform == "linux2":
            self.canvas.yview_scroll(int(scroll), "units")
        else:
            self.canvas.yview_scroll(int(-1*(event.delta/120)), "units")

    def _bind_to_mousewheel(self, event):
        if platform == "linux" or platform == "linux2":
            self.canvas.bind_all("<MouseWheel>", fp(
                self._on_mousewheel, scroll=-1))
            self.canvas.bind_all(
                "<Button-5>", fp(self._on_mousewheel, scroll=1))
        else:
            self.bind_all("<MouseWheel>", self._on_mousewheel)

    def _unbind_from_mousewheel(self, event):

        if platform == "linux" or platform == "linux2":
            self.canvas.unbind_all("<Button-4>")
            self.canvas.unbind_all("<Button-5>")
        else:
            self.unbind_all("<MouseWheel>")
