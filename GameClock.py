import time
import tkinter as tk




class Clock:
    def __init__(self,root,Frame):
        self.root = root
        self.label = tk.Label(Frame,text="")
        self.label.pack()
        self.time_start=time.time()
        self.update_clock()

    def update_clock(self):
        seconds= time.time()-self.time_start
        m, s = divmod(seconds, 60)
        h, m = divmod(m, 60)
        now= time.strftime("%d:%02d:%02d" % (h, m, s))
        self.label.configure(text = now)
        self.root.after(1000,self.update_clock)
