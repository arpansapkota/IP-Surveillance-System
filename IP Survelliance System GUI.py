import tkinter as tk                # python 3
import subprocess
from tkinter import font  as tkfont # python 3
#import Tkinter as tk     # python 2
#import tkFont as tkfont  # python 2
from PIL import Image,ImageTk
x = 0
def run():
    p = subprocess.Popen("main.exe", creationflags=subprocess.CREATE_NEW_CONSOLE)


def close():
    app.destroy()
class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        tk.Tk.iconbitmap(self, default="detective.ico")

        self.frames = {}
        for F in (StartPage, PageOne, PageTwo):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="IP SURVEILLANCE SYSTEM", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button1 = tk.Button(self, text="Go to Settings",
                            command=lambda: controller.show_frame("PageOne"))
        button2 = tk.Button(self, text="Go to About us",
                            command=lambda: controller.show_frame("PageTwo"))
        button3 = tk.Button(self, text="Run the program",
                            command=run)
        button_4 = tk.Button(self, text="Quit", command=close)
        button3.pack(pady=15)
        button1.pack(pady=15)
        button2.pack(side=tk.LEFT,pady=15)
        button_4.pack(side=tk.RIGHT,pady=15)


class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Settings", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)


        def save():
            name = entry_1.get()
            email = entry_2.get()
            # Open new data file
            if name=='keclite':
            	f = open("data2.txt", "w")
            	f.write(str(email))  # str() converts to string
            	f.close()
        x=tk.IntVar()
        def check():
            print(x.get())
            if x.get() == 1: save()

        label_1 = tk.Label(self, text="User Name")
        label_2 = tk.Label(self, text="Email-id")
        label_3 = tk.Label(self, text="The destination email will be changed")
        entry_1 = tk.Entry(self)
        entry_2 = tk.Entry(self)
        label_1.pack()
        entry_1.pack() # north east west
        label_2.pack()  # aligns perfectly
        entry_2.pack()
        label_3.pack()
        # we nedd name ant then input consecutively

         # if column not mentioned then it would have overlaped
        c = tk.Checkbutton(self, text="I accept the terms and agreements.", variable=x)
        c.pack()

        #c.grid()  # column span will take 2 celss merge together
        button_1 = tk.Button(self, text="Submit", command=check)
        button_1.pack()
        button = tk.Button(self, text="Go back to the Home",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack(side=tk.LEFT)
        button_2 = tk.Button(self, text="Quit", command=close)
        button_2.pack(side=tk.RIGHT)
        # fg=foreground i.e text colour




class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="About", font=controller.title_font)
        label = tk.Label(self, text=" Permission to use, copy, modify, and/or distribute this software \n for any purpose with or without fee is hereby granted, provided that \nthe below copyright notice and this permission notice appear in all copies.\nTHE SOFTWARE IS PROVIDED AS IS AND THE AUTHOR DISCLAIMS ALL WARRANTIES \nWITH REGARD IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY  \nDAMAGES ,ILLEGAL ACTIVITIES AROUSED  \nBY CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.\n SPECIAL THANKS TO:\n Kusal Dura , Gaurav Karki for programming  backend code and GUI\n Arpan Sapkota for debugging and Nayan Rizal and Prakash Thapa for designing!!!\n\n\nIP Surveillance 1.0.0 Copyright (c) 2074 B.S(2018 A.D)")
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go back to the Home",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()


if __name__ == "__main__":
    app = SampleApp()
    #def quit():
        #global app
        #app.quit()
    im = Image.open("l.ico")
    photo = ImageTk.PhotoImage(im)
    cv = tk.Canvas()
    cv.pack(side='left', fill='both', expand='no')
    cv.create_image(1, 4, image=photo, anchor='nw')
    im2 = Image.open("k.ico")
    photo2 = ImageTk.PhotoImage(im2)
    cv2 = tk.Canvas()
    cv2.pack(side='bottom', fill='both', expand='no')
    cv2.create_image(1,1, image=photo2, anchor='nw')
    app.geometry("650x550")
    app.mainloop()