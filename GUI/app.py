from tkinter import *
import tkinter.font as tkFont
#from nodemcu import initial

class app():
    
    def __init__(self, obj):
        self.obj = obj
        self.obj.title("User Interface")
        
        self.x=0
        self.y=0
        self.a=0
        self.b=0
        
        
        self.x = self.obj.winfo_screenheight() 
        self.y = self.obj.winfo_screenwidth()
        self.a = int(0.5*self.x)
        self.b = int(0.3*self.y)
        self.obj.geometry(str(self.a)+"x"+str(self.b))
        
        
    def start_app(self,object1):
        
        welcome = tkFont.Font(family='arial', size=55)
        welcome = Label(self.obj, text='*** \n App \n\n\n',font=welcome,background="green")
        welcome.pack(fill='both', expand=True, anchor=CENTER)
        
        display_button = Button(object1,text="Get Data",background="white" ) #command= from node mcu
        display_button.place(relx=0.5, rely=0.5, anchor=CENTER)
        
        return_button = Button(object1,text="Return Data",background="white" ) #command= from node mcu
        return_button.place(relx=0.5, rely=0.6, anchor=CENTER)
        

object1 = Tk()
object2 = app(object1)
object2.start_app(object1)
object1.mainloop()
