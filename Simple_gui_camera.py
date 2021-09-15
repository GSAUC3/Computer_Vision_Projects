from tkinter.constants import CENTER, NW
import numpy as np
from ttkbootstrap import *
import cv2,threading
from win10toast import ToastNotifier
from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk

class window:
    i=0
    def __init__(self,root):
        self.root=root
        self.root.title('Color Detector')
        # self.root.geometry('500x500')
        self.root.resizable(False,False)
        # ttk.Button(self.root,text='QUIT',command=self.root.quit).pack()

        self.root.bind("<q>",lambda x:self.root.quit()) #press q to quit
        self.root.bind("<s>",lambda x:self.snapshot()) #press q to quit
        
        self.t1=threading.Thread(target=self.notify)

        self.l1=ttk.Label(self.root)
        self.l1.pack()
        self.cap=cv2.VideoCapture(0)
        # self.can=Canvas(self.root,width=cv2.CAP_PROP_FRAME_WIDTH,height=cv2.CAP_PROP_FRAME_HEIGHT).pack()
        ttk.Button(self.root,text='Click',width=30,command=self.snapshot).pack(anchor=CENTER,expand=True)
        self.update()

    def __del__(self):
        if self.cap.isOpened():
            self.cap.release()

    def get_frame(self):    
        if not self.cap.isOpened():
            raise ValueError('Unable to open camera, LOL!')
        else:
            ret,frame = self.cap.read()
            if ret:
                return (ret,cv2.cvtColor(frame,cv2.COLOR_BGR2RGB))
            
    def update(self):
        ret,frame=self.get_frame()    
        if ret:
            self.pic=ImageTk.PhotoImage(image=Image.fromarray(frame))
            # self.can.create_image(0,0,image=self.pic,anchor=NW)
            self.l1['image']=self.pic
        
        self.root.after(10,self.update)

    def snapshot(self):
        ret,frame=self.get_frame()
        if ret:
            img= str(self.i)+'.jpg'
            cv2.imwrite(img,cv2.cvtColor(frame,cv2.COLOR_BGR2RGB))
        if not self.t1.is_alive():
            try:
                self.t1.start()
            except RuntimeError:
                self.t1=threading.Thread(target=self.notify)
        self.i+=1    
    
    def notify(self):
        lmao=ToastNotifier()
        lmao.show_toast("Picture Taken | Chitro neoa hoye gache!")

        pass
if __name__ == '__main__':
    win=Style(theme='darkly').master
    app=window(win)
    
    win.mainloop()