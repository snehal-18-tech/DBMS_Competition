from tkinter import *
from tkinter import ttk
#FUNCTIONALITY
def employee_form():
    global back_img
    employee_frame=Frame(window,width=1070,height=567,bg='white')
    employee_frame.place(x=200,y=100)
    heading_label=Label(employee_frame,text='Manage Employee Details',font=('times new roman',16,'bold'),bg='#0f4d7d',fg='white')
    heading_label.place(x=0,y=0,relwidth=1)
    back_img=PhotoImage(file='back.png')
    back_button=Button(employee_frame,image=back_img,bd=0,cursor='hand2',bg='white',command=lambda:employee_frame.place_forget())
    back_button.place(x=10,y=30)

    top_frame=Frame(employee_frame,bg='white')
    top_frame.place(x=8,y=68,relwidth=1,height=235)
    search_frame=Frame(top_frame,bg='white')
    search_frame.pack()
    search_combobox=ttk.Combobox(search_frame,values=('Id','Name','Email'),font=('times new roman',12),state='readonly')
    search_combobox.grid(row=0,column=0,padx=20)
    search_combobox.set('Search By')
    search_entry=Entry(search_frame,font=('times new roman',12),bg='lightyellow')
    search_entry.grid(row=0,column=1)
    search_button=Button(search_frame,text='Search',font=('times new roman',12),width=10,cursor='hand2',fg='white',bg='#074d7d')
    search_button.grid(row=0,column=2,padx=20)
    show_button=Button(search_frame,text='Show All',font=('times new roman',12),width=10,cursor='hand2',fg='white',bg='#074d7d')
    show_button.grid(row=0,column=3,padx=20)

    horizontal_scrollbar=Scrollbar(top_frame,orient=HORIZONTAL)
    vertical_scollbar=Scrollbar(top_frame,orient=VERTICAL)
    employee_treeview=ttk.Treeview(top_frame,columns=('empid','name','email','gender','dob','contact','employement_type','education','work_shift',
    'address','doj','salary','usertype'),show='headings',yscrollcommand=vertical_scollbar.set,xscrollcommand=horizontal_scrollbar.set)
    horizontal_scrollbar.pack(side=BOTTOM)
    vertical_scollbar.pack(side=RIGHT)
    employee_treeview.pack(pady=10)
    employee_treeview.heading('empid',text='EmpId')
    employee_treeview.heading('name',text='Name')
    employee_treeview.heading('email',text='Email')
    employee_treeview.heading('gender',text='Gender')
    employee_treeview.heading('dob',text='Date of Birth')
    employee_treeview.heading('contact',text='Contact') 
    employee_treeview.heading('employement_type',text='Employement Type')
    employee_treeview.heading('education',text='Education')
    employee_treeview.heading('work_shift',text='Work Shift')
    employee_treeview.heading('address',text='Address')
    employee_treeview.heading('doj',text='Date of Joining')
    employee_treeview.heading('salary',text='Salary')
    employee_treeview.heading('usertype',text='User Type')

    employee_treeview.column('empid',width=60)
    employee_treeview.column('name',width=60)
    employee_treeview.column('email',width=100)
    employee_treeview.column('gender',width=80)
    employee_treeview.column('dob',width=100)
    employee_treeview.column('contact',width=100)
    employee_treeview.column('employement_type',width=120)
    employee_treeview.column('education',width=120)
    employee_treeview.column('work_shift',width=100)
    employee_treeview.column('address',width=200)
    employee_treeview.column('doj',width=100)
    employee_treeview.column('salary',width=140)
    employee_treeview.column('usertype',width=120)

       

#GUI
window =Tk()
window.title('Dashboard')
window.geometry("1270x700")
window.resizable(0,0)
window.config(bg='white')

bg_img=PhotoImage(file='inventory.png')
titleLabel=Label(window,image=bg_img,compound=LEFT,text='  Inventory Managemet System  ',font=('times new roman',40,'bold'),bg='#010c48',fg='white',anchor='w',padx='20px')
titleLabel.place(x=0,y=0,relwidth=1)

logoutButton=Button(window,text='Logout',font=('times new roman',20,'bold'),fg='#010c48')
logoutButton.place(x=1100,y=10)

subtitleLabel=Label(window,text='Welcome Admin \t\t Date: 15-10-2024\t\t Time: 12:36:17 pm',font=('times new roman',20),bg='#6e8c96')
subtitleLabel.place(x=0,y=70,relwidth=1)
leftFrame=Frame(window)
leftFrame.place(x=0,y=102,width=200,height=555)

logoImg=PhotoImage(file='logo.png')
imgLabel=Label(leftFrame,image=logoImg)
imgLabel.pack()
menuLabel=Label(leftFrame,text='Menu',font=('times new roman',20),bg='#009688')
menuLabel.pack(fill=X)
employe_icon=PhotoImage(file='employee.png')
employe_button=Button(leftFrame,image=employe_icon,compound=LEFT,text='  Employee',font=('times new roman',20,'bold'),anchor='w',padx='10px',command=employee_form)
employe_button.pack(fill=X)

supplier_icon=PhotoImage(file='supplier.png')
supplier_button=Button(leftFrame,image=supplier_icon,compound=LEFT,text='  Supplier',font=('times new roman',20,'bold'),anchor='w',padx='10px')
supplier_button.pack(fill=X)

category_icon=PhotoImage(file='category.png')
category_button=Button(leftFrame,image=category_icon,compound=LEFT,text='  Category',font=('times new roman',20,'bold'),anchor='w',padx='10px')
category_button.pack(fill=X)

product_icon=PhotoImage(file='product.png')
product_button=Button(leftFrame,image=product_icon,compound=LEFT,text='  Product',font=('times new roman',20,'bold'),anchor='w',padx='10px')
product_button.pack(fill=X)

sales_icon=PhotoImage(file='sales.png')
sales_button=Button(leftFrame,image=sales_icon,compound=LEFT,text='  Sales',font=('times new roman',20,'bold'),anchor='w',padx='10px')
sales_button.pack(fill=X)

Exit_icon=PhotoImage(file='exit.png')
Exit_button=Button(leftFrame,image=Exit_icon,compound=LEFT,text='  Exit',font=('times new roman',20,'bold'),anchor='w',padx='10px')
Exit_button.pack(fill=X)

emp_frame=Frame(window,bg='#2C3E50',bd=3,relief=RIDGE)
emp_frame.place(x=400,y=125,height=170,width=280)
total_emp_icon=PhotoImage(file='total_emp.png')
total_emp_icon_label=Label(emp_frame,image=total_emp_icon,bg='#2C3E50')
total_emp_icon_label.pack(pady=10)
total_emp_label=Label(emp_frame,text='Total Employees',bg='#2C3E50',fg='white',font=('times new roman',15,'bold'))
total_emp_label.pack()
total_emp_count_label=Label(emp_frame,text=0,bg='#2C3E50',fg='white',font=('times new roman',30,'bold'))
total_emp_count_label.pack()

sup_frame=Frame(window,bg='#8E44AD',bd=3,relief=RIDGE)
sup_frame.place(x=800,y=125,height=170,width=280)
total_sup_icon=PhotoImage(file='total_sup.png')
total_sup_icon_label=Label(sup_frame,image=total_sup_icon,bg='#8E44AD')
total_sup_icon_label.pack(pady=10)
total_sup_label=Label(sup_frame,text='Total Suppliers',bg='#8E44AD',fg='white',font=('times new roman',15,'bold'))
total_sup_label.pack()
total_sup_count_label=Label(sup_frame,text=0,bg='#8E44AD',fg='white',font=('times new roman',30,'bold'))
total_sup_count_label.pack()

cat_frame=Frame(window,bg='#27AE60',bd=3,relief=RIDGE)
cat_frame.place(x=400,y=310,height=170,width=280)
total_cat_icon=PhotoImage(file='total_cat.png')
total_cat_icon_label=Label(cat_frame,image=total_cat_icon,bg='#27AE60')
total_cat_icon_label.pack(pady=10)
total_cat_label=Label(cat_frame,text='Total Categories',bg='#27AE60',fg='white',font=('times new roman',15,'bold'))
total_cat_label.pack()
total_cat_count_label=Label(cat_frame,text=0,bg='#27AE60',fg='white',font=('times new roman',30,'bold'))
total_cat_count_label.pack()

prod_frame=Frame(window,bg='#2C3E50',bd=3,relief=RIDGE)
prod_frame.place(x=800,y=310,height=170,width=280)
total_prod_icon=PhotoImage(file='total_prod.png')
total_prod_icon_label=Label(prod_frame,image=total_prod_icon,bg='#2C3E50')
total_prod_icon_label.pack(pady=10)
total_prod_label=Label(prod_frame,text='Total Products',bg='#2C3E50',fg='white',font=('times new roman',15,'bold'))
total_prod_label.pack()
total_prod_count_label=Label(prod_frame,text=0,bg='#2C3E50',fg='white',font=('times new roman',30,'bold'))
total_prod_count_label.pack()

sales_frame=Frame(window,bg='#E74C3C',bd=3,relief=RIDGE)
sales_frame.place(x=600,y=495,height=170,width=280)
total_sales_icon=PhotoImage(file='total_sales.png')
total_sales_icon_label=Label(sales_frame,image=total_sales_icon,bg='#E74C3C')
total_sales_icon_label.pack(pady=10)
total_sales_label=Label(sales_frame,text='Total Sales',bg='#E74C3C',fg='white',font=('times new roman',15,'bold'))
total_sales_label.pack()
total_sales_count_label=Label(sales_frame,text=0,bg='#E74C3C',fg='white',font=('times new roman',30,'bold'))
total_sales_count_label.pack()






window.mainloop()
