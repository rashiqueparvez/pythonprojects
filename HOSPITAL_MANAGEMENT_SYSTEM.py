from tkinter import ttk
from tkinter import*
import random
import time
import datetime
from tkinter import messagebox
import mysql.connector

class Hospital:
    def __init__(self,root):
        self.root=root
        self.root.title("Hospital management system")
        root.geometry("1540x800+0+0")
        
        self.Nameoftablets=StringVar()
        self.ref=StringVar()
        self.Dose=StringVar()
        self.Patientid=StringVar()
        self.Nameoftablets=StringVar()
        self.Lot=StringVar()
        self.issuedate=StringVar()
        self.expdate=StringVar()
        self.dailydose=StringVar()
        self.sideeffect=StringVar()
        self.patientname=StringVar()
        self.bloodpressure=StringVar()
        self.Storage=StringVar()
        self.DOB=StringVar()
        self.further=StringVar()
        self.add=StringVar()
        self.numb=StringVar()
        self.med=StringVar()
        
        lbltitle=Label(self.root,bd=20,relief=RIDGE,text="Hospital Management System",fg="red",bg="white",font=("times new roman",50,"bold"))
        lbltitle.pack(side=TOP,fill=X)   
 
        Dataframe=Frame(self.root,bd=20,relief=RIDGE)
        Dataframe.place(x=0,y=130,width=1530,height=400)    

        dataframeleft=LabelFrame(Dataframe,bd=10,relief=RIDGE,padx=10,
                                           font=("times new roman",12,"bold" ),text="Patient Information")
        dataframeleft.place(x=0,y=5,width=980,height=350)
        
        Dataframeright=LabelFrame(Dataframe,bd=10,relief=RIDGE,padx=10,
                                           font=("times new roman",12,"bold" ),text="Prescription")
        Dataframeright.place(x=990,y=5,width=460,height=350)
        
        
        Buttonframe=Frame(self.root,bd=20,relief=RIDGE)
        Buttonframe.place(x=0,y=530,width=1530,height=70) 
        
        Detailsframe=Frame(self.root,bd=20,relief=RIDGE)
        Detailsframe.place(x=0,y=600,width=1530,height=190) 
        
        lblNameTablet=Label(dataframeleft,text="Names of Tablet", font=("arial",12,"bold" ),padx=2,pady=6)
        lblNameTablet.grid(row=0,column=0)
        
        comNametablet=ttk.Combobox(dataframeleft,font=("arial",12,"bold" ),state="randonly",
                                width=33)
        comNametablet["values"]=("Nice","Corona vaccine","Acetaminophen","Amoldopine","Ativan")
        comNametablet.current(0)
        comNametablet.grid(row=0,column=1)
        
        lblref=Label(dataframeleft,font=("arial",12,"bold"),text="Refrence No:",padx=2)
        lblref.grid(row=1,column=0,sticky=W)
        txtref=Entry(dataframeleft,font=("arial",13,"bold"),textvariable=self.ref,width=35)
        txtref.grid(row=1,column=1)
        
        lblDose=Label(dataframeleft,font=("arial",12,"bold"),text="Dose:",padx=2,pady=4)
        lblDose.grid(row=2,column=0,sticky=W)
        txtDose=Entry(dataframeleft,font=("arial",12,"bold"),textvariable=self.Dose,width=35)
        txtDose.grid(row=2,column=1)
        
        lblNoofTablets=Label(dataframeleft,font=("arial",12,"bold"),text="No Of Tablets:",padx=2,pady=6)
        lblNoofTablets.grid(row=3,column=0,sticky=W)
        txtNoOfTablets=Entry(dataframeleft,font=("arial",12,"bold"),textvariable=self.Nameoftablets,width=35)
        txtNoOfTablets.grid(row=3,column=1)
        
        lblLot=Label(dataframeleft,font=("arial",12,"bold"),text="Lot:",padx=2,pady=6)
        lblLot.grid(row=4,column=0,sticky=W)
        txtLot=Entry(dataframeleft,font=("arial",12,"bold"),textvariable=self.Lot,width=35)
        txtLot.grid(row=4,column=1)
        
        lblissuedate=Label(dataframeleft,font=("arial",12,"bold"),text="Issue Date:",padx=2,pady=6)
        lblissuedate.grid(row=5,column=0,sticky=W)
        txtissuedate=Entry(dataframeleft,font=("arial",12,"bold"),textvariable=self.issuedate,width=35)
        txtissuedate.grid(row=5,column=1)
        
        lblexpdate=Label(dataframeleft,font=("arial",12,"bold"),text="Expiry Date:",padx=2,pady=6)
        lblexpdate.grid(row=6,column=0,sticky=W)
        txtexpdate=Entry(dataframeleft,font=("arial",12,"bold"),textvariable=self.expdate,width=35)
        txtexpdate.grid(row=6,column=1)
        
        
        lbldailydose=Label(dataframeleft,font=("arial",12,"bold"),text="Daily Dose:",padx=2,pady=6)
        lbldailydose.grid(row=7,column=0,sticky=W)
        txtdailydoze=Entry(dataframeleft,font=("arial",12,"bold"),textvariable=self.dailydose,width=35)
        txtdailydoze.grid(row=7,column=1)
        
        lblsideeffect=Label(dataframeleft,font=("arial",12,"bold"),text="Side Effect:",padx=2,pady=6)
        lblsideeffect.grid(row=8,column=0,sticky=W)
        txtsideeffect=Entry(dataframeleft,font=("arial",12,"bold"),textvariable=self.sideeffect,width=35)
        txtsideeffect.grid(row=8,column=1)
        
        lblpatientname=Label(dataframeleft,font=("arial",12,"bold"),text="Patient name:",padx=2,pady=6)
        lblpatientname.grid(row=0,column=2,sticky=W)
        txtpatientname=Entry(dataframeleft,font=("arial",12,"bold"),textvariable=self.patientname,width=35)
        txtpatientname.grid(row=0,column=3)
        
        lblbloodpressure=Label(dataframeleft,font=("arial",12,"bold"),text="Blood Pressure:",padx=2,pady=6)
        lblbloodpressure.grid(row=1,column=2,sticky=W)
        txtbloodpressure=Entry(dataframeleft,font=("arial",12,"bold"),textvariable=self.bloodpressure,width=35)
        txtbloodpressure.grid(row=1,column=3)
        
        lblStorage=Label(dataframeleft,font=("arial",12,"bold"),text="Storage Advice:",padx=2,pady=6)
        lblStorage.grid(row=2,column=2,sticky=W)
        txtStorage=Entry(dataframeleft,font=("arial",12,"bold"),textvariable=self.Storage,width=35)
        txtStorage.grid(row=2,column=3)
        
        lblPatientid=Label(dataframeleft,font=("arial",12,"bold"),text="Patient Id:",padx=2,pady=6)
        lblPatientid.grid(row=3,column=2,sticky=W)
        txtPatientid=Entry(dataframeleft,font=("arial",12,"bold"),textvariable=self.Patientid,width=35)
        txtPatientid.grid(row=3,column=3)
        
        lblDOB=Label(dataframeleft,font=("arial",12,"bold"),text="Date of Birth:",padx=2,pady=6)
        lblDOB.grid(row=4,column=2,sticky=W)
        txtDOB=Entry(dataframeleft,font=("arial",12,"bold"),textvariable=self.DOB,width=35)
        txtDOB.grid(row=4,column=3)
        
        lblfurther=Label(dataframeleft,font=("arial",12,"bold"),text="Further Info:",padx=2,pady=8)
        lblfurther.grid(row=5,column=2,sticky=W)
        txtfurther=Entry(dataframeleft,font=("arial",12,"bold"),textvariable=self.further,width=35)
        txtfurther.grid(row=5,column=3)
        
        lbladd=Label(dataframeleft,font=("arial",12,"bold"),text="Address :",padx=2,pady=8)
        lbladd.grid(row=6,column=2,sticky=W)
        txtadd=Entry(dataframeleft,font=("arial",12,"bold"),textvariable=self.add,width=35)
        txtadd.grid(row=6,column=3)
        
        lblnumb=Label(dataframeleft,font=("arial",12,"bold"),text="Mobile no :",padx=2,pady=8)
        lblnumb.grid(row=7,column=2,sticky=W)
        txtnumb=Entry(dataframeleft,font=("arial",12,"bold"),textvariable=self.numb,width=35)
        txtnumb.grid(row=7,column=3)
        
        lblmed=Label(dataframeleft,font=("arial",12,"bold"),text="Medication:",padx=2,pady=8)
        lblmed.grid(row=8,column=2,sticky=W)
        txtmed=Entry(dataframeleft,font=("arial",12,"bold"),textvariable=self.med,width=35)
        txtmed.grid(row=8,column=3)
        
        self.txtPrescription=Text(Dataframeright,font=("arial",12,"bold"),width=25,height=16,padx=2,pady=6)
        self.txtPrescription.grid(row=0,column=0)
        
        btnprescriptiondata=Button(Buttonframe,command=self.iPrescription,text="Priscription",bd=3,bg="green",fg="white",font=("Arial", 12),padx=2,pady=6,width=23,wraplength=1000)
        btnprescriptiondata.grid(row=0,column=1)
        
        btnprescription=Button(Buttonframe,text="Prescription Data",command=self.iPrescriptionData,bd=3,bg="green",fg="white",font=("Arial", 12),padx=2,pady=6,width=23,wraplength=1000)
        btnprescription.grid(row=0,column=2)
        
        btnupdate=Button(Buttonframe,text="Update",command=self.update_data,bd=3,bg="green",fg="white",font=("Arial", 12),padx=2,pady=6,width=23,wraplength=1000)
        btnupdate.grid(row=0,column=3)
        
        btnDelete=Button(Buttonframe,text="Delete",bd=3,bg="green",fg="white",font=("Arial", 12),padx=2,pady=6,width=23,wraplength=1000)
        btnDelete.grid(row=0,column=4)
        
        btnClear=Button(Buttonframe,text="Clear",bd=3,bg="green",fg="white",font=("Arial", 12),padx=2,pady=6,width=23,wraplength=1000)
        btnClear.grid(row=0,column=5)
        
        btnexit=Button(Buttonframe,text="Exit",bd=3,bg="green",fg="white",font=("Arial", 12),padx=2,pady=6,width=23,wraplength=1000)
        btnexit.grid(row=0,column=6)
        
        
        #==============================================================================================================================
        
        scroll_x=ttk.Scrollbar(Detailsframe,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(Detailsframe,orient=VERTICAL)
        
        self.hospital_table=ttk.Treeview(Detailsframe,column=("ref","Pateintid","Dose","NoofTablet","Lot","issuedate","expdate","dailydose","sideeffect","patientname",
                                                              "bloodpressure","Storage","DOB","further","add","numb","med"),
                                xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        
        scroll_x=ttk.Scrollbar(command=self.hospital_table.xview)
        scroll_y=ttk.Scrollbar(command=self.hospital_table.yview)
        
        
        self.hospital_table.heading("ref",text="Reference No")
        self.hospital_table.heading("Pateintid",text="Pateint Id")
        self.hospital_table.heading("Dose",text="Daily dose")
        self.hospital_table.heading("NoofTablet",text="No of Tablets")
        self.hospital_table.heading("Lot",text="Lot")
        self.hospital_table.heading("issuedate",text="Issue Date")
        self.hospital_table.heading("expdate",text="Expiry Date")
        self.hospital_table.heading("dailydose",text="Daily Dose")
        self.hospital_table.heading("sideeffect",text="Side Effect")
        self.hospital_table.heading("patientname",text="Patient Name")
        self.hospital_table.heading("bloodpressure",text="Blood Pressure")
        self.hospital_table.heading("Storage",text="Storage")
        self.hospital_table.heading("DOB",text="Date of Birth")
        self.hospital_table.heading("further",text="Further info")
        self.hospital_table.heading("add",text="Address")
        self.hospital_table.heading("numb",text="Number")
        self.hospital_table.heading("med",text="Medication")
       
        
        
        
        self.hospital_table["show"]="headings"
        
        
        self.hospital_table.column("ref",width=100)
        self.hospital_table.column("Dose",width=100)
        self.hospital_table.column("Pateintid",width=100)
        self.hospital_table.column("NoofTablet",width=100)
        self.hospital_table.column("Lot",width=100)
        self.hospital_table.column("issuedate",width=100)
        self.hospital_table.column("expdate",width=100)
        self.hospital_table.column("dailydose",width=100)
        self.hospital_table.column("sideeffect",width=100)
        self.hospital_table.column("patientname",width=100)
        self.hospital_table.column("bloodpressure",width=100)
        self.hospital_table.column("Storage",width=100)
        self.hospital_table.column("DOB",width=100)
        self.hospital_table.column("further",width=100)
        self.hospital_table.column("add",width=100)
        self.hospital_table.column("numb",width=100)
        self.hospital_table.column("med",width=100)
        
        self.hospital_table.pack(fill=BOTH,expand=1)
        self.hospital_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()
        
    #===========================================================================================
    def iPrescriptionData(self):
        if self.Nameoftablets.get()=="" or self.ref.get()=="":
            messagebox.showerror("Error","All fields are required")
            
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="Rashique@123",database="mydata")
            my_cursor=conn.cursor()
            my_cursor.execute("insert into hospital values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",("rashique","hello"
               # self.Nameoftablets.get(),self.ref.get(),self.Dose.get(),
               # self.Patientid.get(),self.Nameoftablets.get(),self.Lot.get(),
               # self.issuedate.get(),self.issuedate.get(),self.expdate.get(),
               # self.dailydose.get(),self.sideeffect.get(),self.patientname.get(),
               # self.bloodpressure.get(),self.DOB.get(),self.further.get(),self.add.get(),self.numb.get(),self.med.get()
                
            ))
            
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("success","record has been inserted")
        
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Rashique@123",database="mydata")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from hospital")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.hospital_table.delete(*self.hospital_table.get_children())
            for i in rows:
                self.hospital_table.insert("",END,values=i)
            conn.commit()
        conn.close()
        
    def update_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Rashique@123",database="mydata")
        my_cursor=conn.execute("update hospital set NameofTablets=%s where Reference_No=%s",(
            self.Nameoftablets.get(),
        ))
    
    
    def get_cursor(self,event=""):
        cursor_row=self.hospital_table.focus()
        content=self.hospital_table.item(cursor_row)
        row=content["values"]
        self.Nameoftablets.set(row[0])
        self.ref.set(row[1])
        self.dailydose.set(row[2])
        
        
    def iPrescription(self):
        self.txtPrescription.insert(END,"name of Tablets:\t\t\t"+self.Nameoftablets+"\n")
        self.txtPrescription.insert(END,"Daily dose:\t\t\t"+self.dailydose+"\n")

        
                
        
        
        
        
root=Tk()
ob=Hospital(root)
root.mainloop()        