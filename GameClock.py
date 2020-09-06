import time
import tkinter as tk




class Clock:
    def __init__(self,root,Frame):
        self.root = root
        self.label = tk.Label(Frame,text="")
        self.label.pack()
        self.time_start=time.time()
        self.playTime = 0
        self.update_clock()
    
    def getPlayTime(self):
        return self.playTime

    def update_clock(self):
        self.playtime = time.time()-self.time_start
        m, s = divmod(self.playtime, 60)
        h, m = divmod(m, 60)
        now= time.strftime("%d:%02d:%02d" % (h, m, s))
        self.label.configure(text = now)
        self.root.after(1000,self.update_clock)
