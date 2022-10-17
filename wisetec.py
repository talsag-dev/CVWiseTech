from tkinter import ttk
import tkinter as tk
from tkinter import *
import os
def runScript():
    os.system('python3 "/home/wisetec/Desktop/project_wisetec/script_dev_realsense_yolo_v3_2d.py"')



root = Tk()
root.title('WiseTec with CV')


##about frame 
def create_about_frame():
    frm_about = tk.Toplevel(root)
    frm_about.title("About")
    frm_about.grid()
    ttk.Label(frm_about,text = "This app was made by Kobi Kuzi, Dan Kavitca, Tomer Yaish, Tomer Choen, Tal Sagie, Nati Mayo ").grid(column=0,row=0,padx=50)
    ttk.Label(frm_about,text = "for WiseTech as part of HIT project which demonstrates the use of OpenCV and Realsense camera").grid(column=0,row=1,padx=50)
    ttk.Label(frm_about,text = "to find an object inside a stack of objects").grid(column=0,row=2,padx=50)

##############
##main frame 

frm = ttk.Frame(root, padding=50)
frm.grid()
ttk.Label(frm, text="WiseTec Stack Project" , font=("Arial",25)).grid(column=0, row=0,pady = 20)
ttk.Label(frm, text="Welcome to our stack porject, the main idea is to find the top elemnt in stack of elements , to start press Play button , to stop press q on keyboard").grid(column=0, row=1 ,pady=20)

ttk.Button(frm, text="Play",command=runScript).grid(column=0, row=2)
ttk.Button(frm, text="About", command=create_about_frame).grid(column=0, row=3)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=0, row=4)
 

###########

root.mainloop()