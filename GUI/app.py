from tkinter import *
import tkinter.font as tkFont
from DepthSensor.ultrasonic import dustbin
from cloud_integration import transfer_data as transfer_data

class app():
    
    def __init__(self, obj):
        self.obj = obj
        self.obj.title("User Interface")
        self.height = self.obj.winfo_screenheight() 
        self.width = self.obj.winfo_screenwidth()
        self.app_width = int(0.5*self.width)
        self.app_length = int(0.5*self.height)
        self.obj.geometry(str(self.app_width)+"x"+str(self.app_length))
        self.data = { }
        self.b=dustbin() #to invoke the dustbin object
        
    def senddata(self):
        print(self.data)
        transfer_data.send_data(self.data)
    
    
    def co_ordinate(self):
        
        def printdata(entrybox):
            text = entrybox.get()
            print(str(text))
            l=[]
            for cordinate in text.split(','):
                l.append(float(cordinate))
            self.data['xcoor']=float(l[0])
            self.data['ycoor']=float(l[1])
            print(self.data)
        
        cordinate = Tk()
        
        cordinate.geometry(str(int(0.5*self.height))+"x"+str(int(0.3*self.width)))
        cordinate.title("enter the co_ordinte values")
        
        label1 = Label(cordinate, text= "Enter the co ordinates seperated by comma" )
        label1.pack()
        
        textin = StringVar()
        e=Entry(cordinate, width=30)
        button = Button(cordinate,text='okay',command=lambda:printdata(e))
        button.pack(side='bottom')
        
        e.pack()            
        cordinate.mainloop()
        
    def getarea(self):
        
        def printdata(entrybox):
            text = entrybox.get()
            self.data['area']=str(text)
            print(self.data)
            
            
        area=Tk()
        area.geometry(str(int(0.5*self.height))+"x"+str(int(0.3*self.width)))
        
        label1 = Label(area, text= "Enter the Area" )
        label1.pack()
        
        e=Entry(area, width=30)
        button = Button(area,text='okay',command= lambda: printdata(e))
        button.pack(side='bottom')
        
        e.pack()            
        area.mainloop()
        
    def get_depth(self,setup):
        if setup:
            current_data = Tk()
            current_data.geometry(str(int(0.5*self.height))+"x"+str(int(0.3*self.width)))
            current_data.title("Info Page") 
           
            current = self.b.update_Initial()
            
            self.data['initialDepth']=float(current)
            
            label1 = Label(current_data, text= "current depth in cm = "+str(current))
            label2 = Label(current_data, text= "percentage filled now= "+str(0))
            
            label1.pack()
            label2.pack()
            
            print(self.data)

        else:
            current_data = Tk()
            current_data.geometry(str(int(0.5*self.height))+"x"+str(int(0.3*self.width)))
            current_data.title("Info Page") 
           
            current=self.b.current_Depth() 
            current_percentage=self.b.percentage_Filled(self.b.initial_Depth,current)
            
            self.data['currentDepth']=float(current)
            
            label1 = Label(current_data, text= "current depth in cm = "+str(current))
            label2 = Label(current_data, text= "percentage filled now= "+str(current_percentage))
            
            label1.pack()
            label2.pack()
            
            print(self.data)

    def start_app(self,object1):
        
        #To start the APP
        
        welcome = tkFont.Font(family='arial', size=55)
        welcome = Label(self.obj, text='Garbage collection \n App \n\n\n',font=welcome,background="green")
        welcome.pack(fill='both', expand=True, anchor=CENTER)
        
        initial_display_button = Button(object1,text="Initial Data",background="white",command=lambda: self.get_depth(True) )
        initial_display_button.place(relx=0.5, rely=0.5, anchor=CENTER)
        
        current_display_button = Button(object1,text="current Data",background="white",command=lambda: self.get_depth(False) )
        current_display_button.place(relx=0.5, rely=0.6, anchor=CENTER)
        
        return_button = Button(object1,text="Return Data",background="white",command=self.senddata) 
        return_button.place(relx=0.5, rely=0.9, anchor=CENTER)
        
        co_ordinate_button = Button(object1,text="Enter Co-Ordinates",background="white",command=self.co_ordinate )  
        co_ordinate_button.place(relx=0.5, rely=0.8, anchor=CENTER)
        
        area_button = Button(object1,text="Enter Area",background="white",command=self.getarea )  
        area_button.place(relx=0.5, rely=0.7, anchor=CENTER)
 
if __name__ == "__main__": 
    object1 = Tk()
    object2 = app(object1)
    object2.start_app(object1)
    object1.mainloop()
