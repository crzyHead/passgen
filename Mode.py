import ctypes as ct
from NoRes import *

def Mode(tk): # function to change theme of application:
    global dark_ # global variable, that contains name of color that will be set on next function exec;
    if 'dark_' not in globals():
        dark_ = 'dark'
    if dark_ == 'dark':
        # dark theme;
        NoRes(tk.root)
        DarkMode(tk, 20)
        foreground="#f1f1f1"
        dforeground="#f1f1f1"
        background="#121212"
        dbackground="#1e1e1e"
        string = "☀"
        dark_ = 'light'

    elif dark_ == 'light':
        # light theme;
        tk.root.resizable(False, False)
        NoRes(tk.root)
        foreground="#060606"
        dforeground="#9b858a"
        background="#f0f0f0"
        dbackground="#f0f0f0"
        string = "☽"
        dark_ = 'dark'

    tk.root.configure(background=background)
    tk.theme.configure(
        fg=foreground, bg=background,
        activeforeground=foreground,
        activebackground=background,
        text=string)
    tk.btn.configure(
        fg=foreground, bg=background,
        activeforeground=foreground,
        activebackground=background)
    tk.f.configure(background = background)
    tk.xf.configure(
        highlightbackground=foreground,
        highlightthickness=1,
        background = background
    )
    tk.cb_lu.configure(
    fg=foreground, bg=background,
        activeforeground=foreground,
        activebackground=background,
        selectcolor=background)
    tk.cb_num.configure(
        fg=foreground, bg=background,
        activeforeground=foreground,
        activebackground=background,
        selectcolor=background)
    tk.cb_sym.configure(
        fg=foreground, bg=background,
        activeforeground=foreground,
        activebackground=background,
        selectcolor=background)
    tk.rf.configure(bg=background)
    tk.lf.configure(bg=background)
    tk.cf.configure(bg=background)
    tk.r1.configure(
        fg=foreground, bg=background,
        activeforeground=foreground,
        activebackground=background,
        selectcolor=background)
    tk.r2.configure(
        fg=foreground, bg=background,
        activeforeground=foreground,
        activebackground=background,
        selectcolor=background)
    tk.r3.configure(
        fg=foreground, bg=background,
        activeforeground=foreground,
        activebackground=background,
        selectcolor=background)
    tk.lbl.configure(fg=foreground, bg=background)
    tk.lbl1.configure(fg=foreground, bg=background)
    tk.ent.configure(
    disabledforeground=dforeground, disabledbackground=dbackground)
    tk.s.configure("TProgressbar", troughcolor=dbackground)
    tk.root.update()

def DarkMode(tk, k):
    set_window_attribute = ct.windll.dwmapi.DwmSetWindowAttribute
    get_parent = ct.windll.user32.GetParent
    hwnd = get_parent(tk.root.winfo_id())
    rendering_policy = k
    value = 2
    value = ct.c_int(value)
    set_window_attribute(hwnd, rendering_policy, ct.byref(value), ct.sizeof(value))
