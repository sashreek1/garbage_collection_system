#Tkinter is used to develop the GUI
from tkinter import *
import tkinter.font as tkFont
from DepthSensor.ultrasonic import dustbin #From ultrasonic.py file we import the dustbin class
from cloud_integration import transfer_data as transfer_data  
from google.cloud import firestore

class app():
    
    def __init__(self, obj):
        self.obj = obj
        self.obj.title("User Interface")
        self.height = self.obj.winfo_screenheight() 
        self.width = self.obj.winfo_screenwidth()
        self.app_width = int(0.5*self.width)
        self.app_length = int(0.5*self.height)
        self.obj.geometry(str(self.app_width)+"x"+str(self.app_length))#Geometry is defined
        self.data = { }# This dictinary stores the data with key values which are to be sent to the cloud
        self.b=dustbin() #to invoke the dustbin object from the dustbin class of ultrasonic.py file
        
      # senddata function sends data to the database with key values  
    def senddata(self):
        print(self.data)#prints the data with key values 
        transfer_data.send_data(self.data)
    
    #co_ordinate function takes the comma seperated values from user which is lattitude and longitude of the place where dustbin is located  
    def co_ordinate(self):
        
        def printdata(entrybox):#Entrybox which takes the input cordinate from the user
            text = entrybox.get()
            print(str(text))
            l=[] # list to store x and y cordinated at the index 0 and one respectively
            for cordinate in text.split(','):
                l.append(float(cordinate))
                
            self.data['location']= firestore.GeoPoint(float(l[0]), float(l[1]))
            print(self.data)
        
        cordinate = Tk() # this object is used to create the new window
        
        cordinate.geometry(str(int(0.5*self.height))+"x"+str(int(0.3*self.width)))
        cordinate.title("enter the co_ordinte values")
        
        label1 = Label(cordinate, text= "Enter the co ordinates seperated by comma" )
        label1.pack()
        
        textin = StringVar() #String variable
        e=Entry(cordinate, width=30)
        button = Button(cordinate,text='okay',command=lambda:printdata(e))
        button.pack(side='bottom')
        
        e.pack()            
        cordinate.mainloop()
        
    # getarea function takes the area where dustbin is located   
    def getarea(self):
        
        def printdata(entrybox):#Entrybox which takes the input area from the user
            text = entrybox.get()
            self.data['area']=str(text)
            print(self.data)
            
            
        area=Tk() # this object is used to create the new window
        area.geometry(str(int(0.5*self.height))+"x"+str(int(0.3*self.width)))
        
        label1 = Label(area, text= "Enter the Area" )
        label1.pack()
        
        e=Entry(area, width=30)
        button = Button(area,text='okay',command= lambda: printdata(e))
        button.pack(side='bottom')
        
        e.pack()            
        area.mainloop()
     # get_depth functon takes the initial depth of the dustbin
    def get_depth(self,setup):
        
        # if setup is True then initial depth is obtained else current depth is obtained.
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
