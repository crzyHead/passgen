from tkinter import *
from tkinter import font
from tkinter import ttk
import pyperclip as pc
from generator import *
from NoRes import *
from Mode import Mode
from checker import CheckPassword
from win10toast import ToastNotifier

class TkGUI:
    def __init__(self):
        self.root = Tk()
        self.root.wm_title("Password Generator")
        self.root.iconbitmap("icon.ico")
        self.root.geometry("310x250")
        self.root.resizable(False, False)

        thm = font.Font(family='Georgia', size=16)
        gnrl = font.Font(family='Arial', size=13)
        self.theme = Button(self.root, text="☽", bd=0, font=thm, height = 0, width = 1, command=self.Process)
        self.theme.pack(anchor=NE,padx=5)

        self.btn = Button(self.root, text="Generate Password!", bd=0, font=gnrl, command=self.Exec)
        self.btn.pack()

        self.f = Frame(self.root, width = 315, height = 115)
        self.xf = Frame(self.f, bd=0, padx = 10, pady = 10, highlightbackground="#000000",
            highlightthickness=1)
        self.lf = Frame(self.xf, bd=0)
        self.rf = Frame(self.xf, bd=0)

        # Left Frame (Checkbuttons):
        self.let_u = BooleanVar()
        self.let_u.set(True)
        self.cb_lu = Checkbutton(self.lf, text="Use capital letters [A-Z]", variable=self.let_u, onvalue=True, offvalue=False)
        self.cb_lu.pack(anchor = NW)

        self.sym = BooleanVar()
        self.cb_sym = Checkbutton(self.lf, text="Use symbols [~!@#$%^*-_=+[{]}/;:,.?]",
            variable=self.sym, onvalue=True, offvalue=False)
        self.cb_sym.pack(anchor = NW)

        self.num = BooleanVar()
        self.num.set(True)
        self.cb_num = Checkbutton(self.lf, text="Use numbers [0-9]", variable=self.num, onvalue=True, offvalue=False)
        self.cb_num.pack(anchor = NW)

        #Right Frame (Radiobuttons):

        self.var = IntVar()
        self.r1 = Radiobutton(self.rf, text = "20", value=20, variable=self.var)
        self.r2 = Radiobutton(self.rf, text = "12", value=12, variable=self.var)
        self.r3 = Radiobutton(self.rf, text = "8", value=8, variable=self.var)

        self.var.set(20)

        self.r1.pack(anchor=NW)
        self.r2.pack(anchor=NW)
        self.r3.pack(anchor=NW)

        #Center Frame (visual stuff):
        self.cf = Frame(self.xf, bd = 0)
        self.cf.grid(column=2, row=0, padx=7)

        self.xf.place(relx = 0.01, rely = 0.125, anchor = NW)
        self.lf.grid(column=0, row=0)
        self.rf.grid(column=3, row=0, sticky=E)
        self.lbl = Label(self.f, text='Options'); self.lbl.place(relx=.06, rely=0.125,anchor=W)
        self.f.pack()

        self.lbl1 = Label(self.root, text="Generated password:"); self.lbl1.pack()
        self.ent_txt = StringVar()
        self.ent = Entry(self.root, width = 40, state = "disabled", textvariable = self.ent_txt, justify = 'center')
        self.ent.pack(); self.ent.bind("<1>", self.Copy)

        self.s = ttk.Style()
        self.s.theme_use("default")
        self.s.configure("TProgressbar", thickness=5, troughcolor="#f0f0f0")
        self.security = ttk.Progressbar(self.root, orient="horizontal", mode="determinate", length=244, style="TProgressbar")
        self.security.pack()

    def Exec(self): # execute Generate and add result text to entry;
        self.ent_txt.set(Generate(self.let_u.get(), True, self.sym.get(), self.num.get(), self.var.get()))
        self.security['value'] = CheckPassword(self.ent_txt.get())
        color = ""
        if self.security['value'] > 75: color = "#32a852"
        elif self.security['value'] >= 45: color = "#e0b72d"
        else: color = "#a83232"
        self.s.configure("TProgressbar", foreground=color, background=color)


    def Process(self): # process theme button press to execute Mode;
        Mode(self)

    def Copy(self, event):
        pc.copy(self.ent_txt.get())
        toast = ToastNotifier()
        toast.show_toast(
            "Password Generator",
            "Password copied to clipboard!",
            duration = 3,
            icon_path = "icon.ico",
            threaded = True
        )

    def start(self):
        self.root.after(10, lambda:NoRes(self.root))
        self.root.mainloop()