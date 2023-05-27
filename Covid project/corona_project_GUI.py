def disp():
    
    new=pd.DataFrame({"cough":[(a1.get())],"fever":[(a2.get())],"sore_throat":[(a3.get())],"shortness_of_breathe":[(a4.get())],"headache":[(a5.get())],"age_60_and_above":[(a6.get())],"gender":[(a7.get())],"test_indication":[(a8.get())],"month":[(a9.get())],"day":[(a10.get())]})
    print(new)
    
    new["gender"] = lo.transform(new["gender"])
    new["test_indication"] = le.transform(new["test_indication"])
    new["age_60_and_above"] = li.transform(new["age_60_and_above"])
    # new["cough"] = ly.transform(new["cough"])
    
    new = sc.transform(new)
    #new = si.transform(new)     
    ans = Classifier.predict(new)
    print(ans)
    if ans==[0]:
        Final_l.config(text='Negative')
        messagebox.showinfo("Message","Congratulations, your result is negative but you should take necessary precautions to avoid coronavirus")
        
    elif ans==[1]:
        Final_l.config(text='Positive')
        messagebox.showwarning("Warning","You may be infected by Coronavirus, consult a doctor immediately !")
    else:
        Final_l.config(text='Not able to predict')

def clear():
    
    a1.set("")
    a2.set("")
    a3.set("")
    a4.set("")
    a5.set("")
    a6.set("")
    a7.set("")
    a8.set("")
    a9.set("")
    a10.set("")
    
def on_enter(e):
    e.widget['background'] = 'lightgrey'

def on_leave(e):
    e.widget['background'] = '#6bdacf'
    
    
from tkinter import *
root= Tk()
root.geometry("2000x2000")
root.title("Coronavirus Predictor")

bg = PhotoImage(file = r"C:/Users/robin/Downloads/Download free vector of Clean medical background vector 2292437-imresizer (1).png")
labelA1 = Label( root, image = bg)
labelA1.place(x = 0, y = 0)

a1=StringVar()

a2=StringVar()

a3=StringVar()

a4=StringVar()

a5=StringVar()

a6=StringVar()

a7=StringVar()

a8=StringVar()

a9=StringVar()

a10=StringVar()

l = Label(root,text = "Coronavirus Predictor",fg="black",bg="#6bdacf" ,font=("Pacifico","40")).place(x=450,y=12)

label1 = Label(root,text = "Do you have cough : ",fg="black",bg="white",font=("Slabo 27px","23")).place(x= 70,y=150)
cough=Entry(root,textvariable=a1,width=23).place(x=480,y=160,height=30)

label2 = Label(root,text = "Do you have fever : ",fg="black",bg="white" ,font=("Slabo 27px","23")).place(x= 70,y=240)
fever=Entry(root,textvariable=a2,width=23).place(x=480,y=250,height=30)

label3 = Label(root,text = "Do you have sore throat : ",fg="black",bg="white" ,font=("Slabo 27px","23")).place(x= 70,y=330)
sore_throat=Entry(root,textvariable=a3,width=23).place(x=480,y=340,height=30)

label4 = Label(root,text = "Do you have short breathe : ",fg="black",bg="white" ,font=("Slabo 27px","23")).place(x= 70,y=420)
shortness_of_breathe=Entry(root,textvariable=a4,width=23).place(x=480,y=430,height=30)

label5 = Label(root,text = "Do you have headache : ",fg="black",bg="white" ,font=("Slabo 27px","23")).place(x= 70,y=510)
headache=Entry(root,textvariable=a5,width=23).place(x=480,y=520,height=30)

label6 = Label(root,text = "Is your age 60 or above : ",fg="black",bg="white" ,font=("Slabo 27px","23")).place(x= 700,y=150)
age_60_and_above=Entry(root,textvariable=a6,width=23).place(x=1170,y=160,height=30)

label7 = Label(root,text = "Enter male/female : ",fg="black",bg="white" ,font=("Slabo 27px","23")).place(x= 700,y=240)
gender=Entry(root,textvariable=a7,width=23).place(x=1170,y=250,height=30)

label8 = Label(root,text = "Enter what your test indicates : ",fg="black",bg="white" ,font=("Slabo 27px","23")).place(x= 700,y=330)
test_indication=Entry(root,textvariable=a8,width=23).place(x=1170,y=340,height=30)

label9 = Label(root,text = "Enter your month of vaccination :" ,fg="black",bg="white" ,font=("Slabo 27px","23")).place(x=700,y=420)
month=Entry(root,textvariable=a9,width=23).place(x=1170,y=430,height=30)

label10 = Label(root,text = "Enter your day of vaccination : ",fg="black",bg="white" ,font=("Slabo 27px","23") ).place(x= 700,y=510)
day=Entry(root,textvariable=a10,width=23).place(x=1170,y=520,height=30)


submit=Button(root,text="SUBMIT",fg="black",bg="#6bdacf",command = disp,font=("Slabo 27px",20))
submit.place(x=630,y=600)

Clear=Button(root,text="CLEAR",fg="black",bg='#6bdacf',command = clear,font=("Slabo 27px",20))
Clear.place(x=250,y=600)
    
submit.bind("<Enter>", on_enter)
submit.bind("<Leave>", on_leave)

Clear.bind("<Enter>", on_enter)
Clear.bind("<Leave>", on_leave)


l1 = Label(root,text="MY PREDICTION : " ,fg="black",bg="#6bdacf" ,font=("Slabo 27px","20")).place(x=1000,y=610)

Final_l = Label(root,fg="black",bg="#6bdacf" ,font=("Ariel",20))
Final_l.place(x=1200,y=610)


root.mainloop()