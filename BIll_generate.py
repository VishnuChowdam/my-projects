from  tkinter import *
root=Tk()
root.geometry("1000x500")
root.resizable(False,False)
#function reset
def reset():
    Tea.delete(0,END)
    Coffee.delete(0,END)
    icecream.delete(0,END)
    Panipor.delete(0, END)
    sprite.delete(0, END)
    goobirice.delete(0, END)
    Kabbabs.delete(0, END)
    biryaani.delete(0, END)
    Mandii.delete(0,END)
def total():
    try:e1=int(Tea.get())*5
    except:e1=0
    try:e2=int(Coffee.get())*10
    except:e2=0
    try:e3=int(icecream.get())*20
    except:e3=0
    try:e4=int(Panipor.get())*30
    except:e4=0
    try:e5=int(sprite.get())*45
    except:e5=0
    try:e6=int(goobirice.get())*50
    except:e6=0
    try:e7=int(Kabbabs.get())*60
    except:e7=0
    try: e8 = int(biryaani.get())*200
    except: e8 = 0
    try: e9 = int(Mandii.get())*500
    except: e9 = 0
    sh =Entry(frame2, bg="burlywood1", fg="Black",textvariable=totalbill,relief=RAISED,font=("arial",15,"bold"),width=20,bd=3)
    sh.place(x=30, y=350)
    total_cost = e1 + e2 + e3 + e4 + e5 + e6 + e7 + e8 + e9
    bil = "RS:", str('%.2f' % total_cost)
    totalbill.set(bil)
#Frame1
s=Label(root,bg="Yellow",fg="Red",text="Bill Generator",font=("Lucid Calligraphy",40,"bold"),width=500).pack()
frame1=Frame(root,bg="lightblue",highlightbackground="blue",highlightthickness=2,height=400,width=300)
frame1.place(x=40,y=90)
Label(frame1,bg="lightblue",fg="Black",text="#Menu Card",font=("arial",30,"bold")).place(x=10,y=20)
Label(frame1,bg="lightblue",fg="Black",text="Tea/cup               -          ₹5",font=("arial",15,"bold")).place(x=10,y=90)
Label(frame1,bg="lightblue",fg="Black",text="cofee/cup            -          ₹10",font=("arial",15,"bold")).place(x=10,y=120)
Label(frame1,bg="lightblue",fg="Black",text="IceCream            -          ₹20",font=("arial",15,"bold")).place(x=10,y=150)
Label(frame1,bg="lightblue",fg="Black",text="PanPoori/plate    -           ₹30",font=("arial",15,"bold")).place(x=10,y=180)
Label(frame1,bg="lightblue",fg="Black",text="Sprite(500ml)      -          ₹45",font=("arial",15,"bold")).place(x=10,y=210)
Label(frame1,bg="lightblue",fg="Black",text="GobiRice/plate    -          ₹50",font=("arial",15,"bold")).place(x=10,y=240)
Label(frame1,bg="lightblue",fg="Black",text="kababs/plate       -          ₹60",font=("arial",15,"bold")).place(x=10,y=270)
Label(frame1,bg="lightblue",fg="Black",text="Biryani/plate        -         ₹200",font=("arial",15,"bold")).place(x=10,y=300)
Label(frame1,bg="lightblue",fg="Black",text="Mandi                   -         ₹500",font=("arial",15,"bold")).place(x=10,y=330)
#frame2
frame2=Frame(root,bg="lightgreen",highlightbackground="green",highlightthickness=2,height=400,width=300)
frame2.place(x=500,y=90)
tea=StringVar()
coffe=StringVar()
Icecream=StringVar()
panipoori=StringVar()
Sprite=StringVar()
gobirice=StringVar()
kababs=StringVar()
biryani=StringVar()
mandi=StringVar()
totalbill=StringVar()
Label(frame2,bg="lightgreen",fg="Blue",text="Item",font=("arial",20,"bold")).place(x=30,y=0)
Label(frame2,bg="lightgreen",fg="Blue",text="Quantity",font=("arial",20,"bold")).place(x=150,y=0)
Label(frame2,bg="lightgreen",fg="Black",text="Tea",font=("arial",15,"bold")).place(x=30,y=30)
Tea=Entry(frame2,bd=3,bg="lightpink",fg="Black",font=("arial",10,"bold"),width="10",textvariable=tea,relief=RAISED)
Tea.place(x=170,y=30)
Label(frame2,bg="lightgreen",fg="Black",text="Coffee",font=("arial",15,"bold")).place(x=30,y=60)
Coffee=Entry(frame2,bd=3,bg="lightpink",fg="Black",font=("arial",10,"bold"),textvariable=coffe,relief=RAISED,width=10)
Coffee.place(x=170,y=60)
Label(frame2,bg="lightgreen",fg="Black",text="IceCream",font=("arial",15,"bold")).place(x=30,y=90)
icecream=Entry(frame2,bd=3,bg="lightpink",fg="Black",font=("arial",10,"bold"),textvariable=Icecream,relief=RAISED,width=10)
icecream.place(x=170,y=90)
Label(frame2,bg="lightgreen",fg="Black",text="PanPoori",font=("arial",15,"bold")).place(x=30,y=120)
Panipor=Entry(frame2,bd=3,bg="lightpink",fg="Black",font=("arial",10,"bold"),textvariable=panipoori,relief=RAISED,width=10)
Panipor.place(x=170,y=120)
Label(frame2,bg="lightgreen",fg="Black",text="Sprite(500ml)",font=("arial",15,"bold")).place(x=30,y=150)
sprite=Entry(frame2,bd=3,bg="lightpink",fg="Black",font=("arial",10,"bold"),textvariable=Sprite,relief=RAISED,width=10)
sprite.place(x=170,y=150)
Label(frame2,bg="lightgreen",fg="Black",text="GobiRice",font=("arial",15,"bold")).place(x=30,y=180)
goobirice=Entry(frame2,bd=3,bg="lightpink",fg="Black",font=("arial",10,"bold"),textvariable=gobirice,relief=RAISED,width=10)
goobirice.place(x=170,y=180)
Label(frame2,bg="lightgreen",fg="Black",text="kababs",font=("arial",15,"bold")).place(x=30,y=210)
Kabbabs=Entry(frame2,bd=3,bg="lightpink",fg="Black",font=("arial",10,"bold"),textvariable=kababs,relief=RAISED,width=10)
Kabbabs.place(x=170,y=210)
Label(frame2,bg="lightgreen",fg="Black",text="Biryani",font=("arial",15,"bold")).place(x=30,y=240)
biryaani=Entry(frame2,bd=3,bg="lightpink",fg="Black",font=("arial",10,"bold"),textvariable=biryani,relief=RAISED,width=10)
biryaani.place(x=170,y=240)
Label(frame2,bg="lightgreen",fg="Black",text="Mandi",font=("arial",15,"bold")).place(x=30,y=270)
Mandii=Entry(frame2,bd=3,bg="lightpink",fg="Black",font=("arial",10,"bold"),textvariable=mandi,relief=RAISED,width=10)
Mandii.place(x=170,y=270)
resett=Button(frame2,bd=3,bg="Gray",font=("arial",10,"bold"),fg="Black",text="Reset",command=reset)
resett.place(x=30,y=310)
totaal=Button(frame2,bd=3,bg="Gray",font=("arial",10,"bold"),fg="Black",text="Total",width=10,command=total)
totaal.place(x=170,y=310)
root.mainloop()
