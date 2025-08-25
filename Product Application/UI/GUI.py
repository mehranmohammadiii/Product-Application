import sys
sys.path.insert(0, 'C:/Users/digi kala/Desktop/Python/App1')
from tkinter import *
from tkinter import messagebox
from khayyam import JalaliDate
from PL.Services import GetProductList
from tkinter import ttk
from PIL import Image, ImageTk
from PL.Services import *

def fun1(event):
    root2 = Toplevel(root)
    root2.geometry('%dx%d+%d+%d' % (800, 300, (x/2)-(800/2), (y/2)-(300/2)))

    frame = Frame(root2)
    frame.pack(fill="both", expand=True, padx=10, pady=10)
    frame.grid_rowconfigure(0, weight=1)
    frame.grid_columnconfigure(0, weight=1)

    columns = ("id", "name", "city", "score", "price", "delivery")
    tree = ttk.Treeview(frame, columns=columns, show="headings")
    tree.grid(row=0, column=0, sticky="nsew")

    scroll_y = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
    scroll_y.grid(row=0, column=1, sticky="ns")
    scroll_x = ttk.Scrollbar(frame, orient="horizontal", command=tree.xview)
    scroll_x.grid(row=1, column=0, sticky="ew")
    tree.configure(yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)

    tree.heading("id", text="کد محصول", anchor="center")
    tree.column("id", width=90, minwidth=80, anchor="center", stretch=False)
    tree.heading("name", text="نام محصول", anchor="center")
    tree.column("name", width=400, minwidth=250, anchor="center", stretch=True)
    tree.heading("city", text="شهر", anchor="center")
    tree.column("city", width=120, minwidth=100, anchor="center", stretch=False)
    tree.heading("score", text="امتیاز", anchor="center")
    tree.column("score", width=90, anchor="center", stretch=False)
    tree.heading("price", text="قیمت", anchor="center")
    tree.column("price", width=140, anchor="center", stretch=False)
    tree.heading("delivery", text="ارسال", anchor="center")
    tree.column("delivery", width=120, anchor="center", stretch=False)

    data = []
    for item in GetProductList():
        data.append((item[0],item[1],item[2],item[3],item[4],item[5])) 

    max_len = max(len(str(r[1])) for r in data)  
    approx_px = max(400, min(1200, int(max_len * 9)))  
    tree.column("name", width=approx_px)

    for row in data:
        tree.insert("", "end", values=row)

def fun2(event):

    def checkvalue(listvalue):
        temp=[]
        if listvalue[0] :
            temp.append(listvalue[0])
        else :
            messagebox.showerror("خطای افزودن","عنوان را درست وارد کنید وارد کردید")
            temp.append(1)

        if all(ch.isalpha() or ch.isspace() for ch in listvalue[1]) and bool(listvalue[1])==True :
            temp.append(listvalue[1])
        else: 
            messagebox.showerror("خطای افزودن","شهر را درست وارد کنید وارد کردید")
            temp.append(1)

        temp.append(listvalue[2])

        try :
            int(listvalue[3])
            if bool(str(listvalue[3]))==True:
                temp.append(listvalue[3])
        except:
            messagebox.showerror("خطای افزودن","قیمت  را درست وارد کنید وارد کردید")
            temp.append(1)

        if all(ch.isalpha() or ch.isspace() for ch in listvalue[4]) :
            if bool(listvalue[4])==False:
                temp.append(listvalue[4])
        else: 
            messagebox.showerror("خطای افزودن","نوع ارسال را درست وارد کنید وارد کردید")
            temp.append("")
        return temp

    def funroot3(event,*args):
        temp=[]
        for entry in args:
            temp.append(entry.get())

        check=checkvalue(temp)
        if 1 not in check:
            AddNewProduct(check)
            messagebox.showinfo("افزودن محصول","افزودن محصول با موفیقت انجام شد")
        
    root3=Toplevel(root)
    root3.geometry('%dx%d+%d+%d' % (800, 300, (x/2)-(800/2), (y/2)-(300/2)))

    bg_label = Label(root3)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)
 
    img = Image.open("UI/images/Untitled.jpg")
    img = img.resize((800, 300), Image.Resampling.LANCZOS)  
    bg = ImageTk.PhotoImage(img)
    bg_label = Label(root3, image=bg)
    bg_label.image = bg 
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)

    frame = Frame(root3, bg="", padx=10, pady=10)
    frame.place(relx=0.5, rely=0.5, anchor=CENTER)

    Label4 = Label(frame, text="نام محصول", bg="#D2A679", width=15, anchor="center")
    Label4.grid(row=0, column=0, padx=5, pady=5)
    entry2 = Entry(frame, width=20,bg="#e2e2fb")
    entry2.grid(row=0, column=1, padx=5, pady=5)
    Label5 = Label(frame, text="شهر", bg="#D2A679", width=15, anchor="center")
    Label5.grid(row=1, column=0, padx=5, pady=5)
    entry3 = Entry(frame, width=20,bg="#e2e2fb")
    entry3.grid(row=1, column=1, padx=5, pady=5)
    Label6 = Label(frame, text="امتیاز", bg="#D2A679", width=15, anchor="center")
    Label6.grid(row=2, column=0, padx=5, pady=5)
    entry4 = Entry(frame, width=20,bg="#e2e2fb")
    entry4.grid(row=2, column=1, padx=5, pady=5)
    Label7 = Label(frame, text="قیمت", bg="#D2A679", width=15, anchor="center")
    Label7.grid(row=3, column=0, padx=5, pady=5)
    entry5 = Entry(frame, width=20,bg="#e2e2fb")
    entry5.grid(row=3, column=1, padx=5, pady=5)
    Label8 = Label(frame, text="ارسال", bg="#D2A679", width=15, anchor="center")
    Label8.grid(row=4, column=0, padx=5, pady=5)
    entry6 = Entry(frame, width=20,bg="#e2e2fb")
    entry6.grid(row=4, column=1, padx=5, pady=5)

    btn = Button(frame, text="ثبت کالا", bg="#0ebd5b", fg="white", font=("tahoma", 16), width=30)
    btn.bind("<Button>",lambda e :funroot3(event,entry2,entry3,entry4,entry5,entry6))
    btn.grid(row=6, columnspan=2, padx=5, pady=5)

def fun3(ecent):

    def show_question(val,productid):
        flag=messagebox.askyesno("آیا از حذف مطمعن هستید",""+val)
        if flag :
            deletproduct(productid)
            messagebox.showinfo("حذف محصول","حذف محصول با موفقیت انجام شد")

    def checkentry(event,productid):
        if productid.isdigit() :
            val=chacksrarchvalu(int(productid))
            if val==[] :
                messagebox.showerror("حذف محصول","محصول با این کد وجود ندارد") 
            else :
                val[0][0]=str(val[0][0])
                val[0][4]=str(val[0][4])
                res="\n".join(val[0])
                show_question(res,productid)            
        else :
            messagebox.showwarning("حذف محصول","کد محصول را درست وارد کنید")

    root4=Toplevel(root)
    root4.geometry('%dx%d+%d+%d' % (800, 300, (x/2)-(800/2), (y/2)-(300/2)))

    img = Image.open("UI/images/Untitled.jpg")
    img = img.resize((800, 300), Image.Resampling.LANCZOS)  
    bg = ImageTk.PhotoImage(img)
    bg_label = Label(root4, image=bg)
    bg_label.image = bg 
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)

    frame = Frame(root4, bg="", padx=10, pady=10)
    frame.place(relx=0.5, rely=0.5, anchor=CENTER)

    Label3 = Label(frame, text="کد محصول", bg="#D2A679", width=15, anchor="center")
    Label3.grid(row=0, column=0, padx=5, pady=5)
    entry = Entry(frame, width=20,bg="#e2e2fb")
    entry.grid(row=0, column=1, padx=5, pady=5)
    btn1 = Button(frame, text=" حذف محصول", bg="#F60C0C", width=15, anchor="center")
    btn1.grid(row=1, columnspan=2, padx=5, pady=5)
    btn1.bind("<Button>",lambda e : checkentry(Event,entry.get()))

def fun4(event):

    def show_windo(res):
        root6=Toplevel(root5)
        root6.geometry('%dx%d+%d+%d' % (800, 300, (x/2)-(800/2), (y/2)-(300/2)))

        Label6=Label(root6,text="کد محصول",bg="#D2A679",padx=5, pady=5,width=20)
        Label6.grid(row=0,column=0,padx=5, pady=5)
        Label7=Label(root6,text=res[0][0])
        Label7.grid(row=0,column=1)
        Label8=Label(root6,text="عنوان محصول",bg="#D2A679",padx=5, pady=5,width=20)
        Label8.grid(row=1,column=0,padx=5, pady=5)
        Label9=Label(root6,text=res[0][1])
        Label9.grid(row=1,column=1)
        Label10=Label(root6,text="شهر محصول",bg="#D2A679",padx=5, pady=5,width=20)
        Label10.grid(row=2,column=0,padx=5, pady=5)
        Label11=Label(root6,text=res[0][2])
        Label11.grid(row=2,column=1)
        Label12=Label(root6,text="امتیاز محصول",bg="#D2A679",padx=5, pady=5,width=20)
        Label12.grid(row=3,column=0,padx=5, pady=5)
        Label13=Label(root6,text=res[0][3])
        Label13.grid(row=3,column=1)
        Label14=Label(root6,text="قیمت محصول",bg="#D2A679",padx=5, pady=5,width=20)
        Label14.grid(row=4,column=0,padx=5, pady=5)
        Label15=Label(root6,text=res[0][4])
        Label15.grid(row=4,column=1)
        Label16=Label(root6,text="نوع ارسال",bg="#D2A679",padx=5, pady=5,width=20)
        Label16.grid(row=5,column=0,padx=5, pady=5)
        Label17=Label(root6,text=res[0][5])
        Label17.grid(row=5,column=1)

    def btn1fun(event,productid):
        if productid.isdigit() :
            val=chacksrarchvalu(int(productid))
            if val==[] :
                messagebox.showerror("حذف محصول","محصول با این کد وجود ندارد") 
            else :
                show_windo(val)            
        else :
            messagebox.showwarning("حذف محصول","کد محصول را درست وارد کنید")

    def btn2fun(event,productcity):

        if all(ch.isalpha() or ch.isspace() for ch in productcity) and bool(productcity)==True :
            data = []
            val=GetProductcitylist(productcity)
            if val!=[] :
                for item in val:
                    data.append((item[0],item[1],item[2],item[3],item[4],item[5])) 
                root6=Toplevel(root5)
                root6.geometry('%dx%d+%d+%d' % (800, 300, (x/2)-(800/2), (y/2)-(300/2)))
                frame = Frame(root6)
                frame.pack(fill="both", expand=True, padx=10, pady=10)
                frame.grid_rowconfigure(0, weight=1)
                frame.grid_columnconfigure(0, weight=1)

                columns = ("id", "name", "city", "score", "price", "delivery")
                tree = ttk.Treeview(frame, columns=columns, show="headings")
                tree.grid(row=0, column=0, sticky="nsew")

                scroll_y = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
                scroll_y.grid(row=0, column=1, sticky="ns")
                scroll_x = ttk.Scrollbar(frame, orient="horizontal", command=tree.xview)
                scroll_x.grid(row=1, column=0, sticky="ew")
                tree.configure(yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)

                tree.heading("id", text="کد محصول", anchor="center")
                tree.column("id", width=90, minwidth=80, anchor="center", stretch=False)
                tree.heading("name", text="نام محصول", anchor="center")
                tree.column("name", width=400, minwidth=250, anchor="center", stretch=True)
                tree.heading("city", text="شهر", anchor="center")
                tree.column("city", width=120, minwidth=100, anchor="center", stretch=False)
                tree.heading("score", text="امتیاز", anchor="center")
                tree.column("score", width=90, anchor="center", stretch=False)
                tree.heading("price", text="قیمت", anchor="center")
                tree.column("price", width=140, anchor="center", stretch=False)
                tree.heading("delivery", text="ارسال", anchor="center")
                tree.column("delivery", width=120, anchor="center", stretch=False)

                max_len = max(len(str(r[1])) for r in data)  
                approx_px = max(400, min(1200, int(max_len * 9)))  
                tree.column("name", width=approx_px)

                for row in data:
                    tree.insert("", "end", values=row)

            else:
                messagebox.showerror("جستجو","نتیجه ای یافت نشد")
        else:
            messagebox.showerror("جستجو","شهر را درست وارد کنید")

    root5=Toplevel(root)
    root5.geometry('%dx%d+%d+%d' % (800, 300, (x/2)-(800/2), (y/2)-(300/2)))

    img = Image.open("UI/images/Untitled.jpg")
    img = img.resize((800, 300), Image.Resampling.LANCZOS)  
    bg = ImageTk.PhotoImage(img)
    bg_label = Label(root5, image=bg)
    bg_label.image = bg 
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)

    frame = Frame(root5, bg="", padx=10, pady=10)
    frame.place(relx=0.5, rely=0.5, anchor=CENTER)

    btn1=Button(frame,text="جستجو",padx=5, pady=5,bg="#09F91D")
    btn1.bind("<Button>",lambda e : btn1fun(Event,entry2.get()))
    btn1.grid(row=0,column=0)
    entry2 = Entry(frame, width=20,bg="#e2e2fb")
    entry2.grid(row=0, column=1, padx=5, pady=5)
    Label4 = Label(frame, text="کد محصول", bg="#D2A679", width=15, anchor="center")
    Label4.grid(row=0, column=2, padx=5, pady=5)

    btn2=Button(frame,text="جستجو",padx=5, pady=5,bg="#09F91D")
    btn2.bind("<Button>",lambda e : btn2fun(Event,entry3.get()))
    btn2.grid(row=1,column=0)
    entry3 = Entry(frame, width=20,bg="#e2e2fb")
    entry3.grid(row=1, column=1, padx=5, pady=5)
    Label5 = Label(frame, text="شهر محصول", bg="#D2A679", width=15, anchor="center")
    Label5.grid(row=1, column=2, padx=5, pady=5)

root=Tk()
root.title("فروشگاه")
root.iconbitmap("UI/images/shop_icon-icons.com_51010.ico")
x=root.winfo_screenwidth() 
y=root.winfo_screenheight()
root.geometry('%dx%d+%d+%d'%(800,500,(x/2)-(800/2),(y/2)-(500/2)))

bg=PhotoImage(file="UI/images/ChatGPT Image Aug 21, 2025, 07_41_45 PM.png")
bg_label = Label(root, image=bg)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

Frame1=Frame(root,bg="",width=800,height=100,pady=5)
Frame1.pack(fill=X)
Frame2=Frame(root,bg="",width=800,height=100,pady=20,padx=10)
Frame2.pack(fill=X)
Frame3=Frame(root,bg="",width=800,height=100,pady=20,padx=10)
Frame3.pack(fill=X)
Frame4=Frame(root,bg="",width=800,height=100,pady=20,padx=10)
Frame4.pack(fill=X)
Frame5=Frame(root,bg="",width=800,height=100,pady=20,padx=10)
Frame5.pack(fill=X)
Frame6=Frame(root,bg="",width=800,height=100,pady=20,padx=10)
Frame6.pack(fill=X)

Label1=Label(Frame1,text="به فروشگاه ما خوش آمدید",bg="#ffc567",font=("tahoma",20),pady=0)
Label1.pack()
Label2=Label(Frame1,text=JalaliDate.today(),bg="#172929",foreground="#ffffd6")
Label2.pack(side=LEFT,padx=10)

Button1=Button(Frame2,text="نمایش همه محصولات",bg="#36d16c",pady=10,padx=10)
Button1.bind("<Button>",fun1)
Button1.pack(side=RIGHT)

Button2=Button(Frame3,text="افزودن محصول جدید",bg="#36d16c",pady=10,padx=10)
Button2.bind("<Button>",fun2)
Button2.pack(side=RIGHT)

Button3=Button(Frame4,text="حذف کردن محصول",bg="#36d16c",pady=10,padx=10)
Button3.bind("<Button>",fun3)
Button3.pack(side=RIGHT)

Button4=Button(Frame5,text="جستجو محصول",bg="#36d16c",pady=10,padx=10)
Button4.bind("<Button>",fun4)
Button4.pack(side=RIGHT)

Button5=Button(Frame6,text="خروج",bg="#f72c2c",pady=10,padx=20,command=root.destroy)
Button5.pack(side=LEFT)

root.mainloop()

