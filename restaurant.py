'''
1)create an input form for the order details
2)Setup a database for the restaurant management
3)Fetch results from the database and display them in a tree view
4)Do a total for the orders for a single day
5)Create a mechanism to store the above mentioned data for each day
6)Calculate revenue on  a weekly monthly and yearly basis for this app

Deciding the layout:
1)Create a menu bar containing the three fields
a)Input form
b)data base entries
c)Revenue and sales data
'''

import tkinter as tk
from tkinter import ttk
from math import *
from windows import set_dpi_awareness
import tkinter.font as font
import time
from datetime import date
#create Font object
from sql_restaurant import *
set_dpi_awareness()
class main_frame(tk.Tk):
    def __init__(self,*args,**kwargs):
        super().__init__()
        self.title("Restaurant Management")
        self.geometry('1500x800')
        self.resizable(True,True)
        self.frames = dict()
        container=ttk.Frame()
        container.grid(row=4,padx=10, pady=10, sticky="EW")
        frame1 = input_form(container) # this is the input form frame
        frame2 = tree_data(container) # this is the database values frame
        frame3 = revenue_data(container) # this is the revenue and profit data table
        frame3.grid(row=0, column=0, sticky="NSEW")
        frame2.grid(row=0, column=0, sticky="NSEW")
        frame1.grid(row=0, column=0, sticky="NSEW")

        frame1.tkraise()
        self.frames['frame1'] = frame1
        self.frames['frame2'] = frame2
        self.frames['frame3'] = frame3

        menu_bar = tk.Menu()
        menu_bar.add_command(label='Order Entry', command=lambda: self.frames['frame1'].tkraise())
        menu_bar.add_command(label='Orders', command=lambda: self.frames['frame2'].tkraise())
        menu_bar.add_command(label='Revenue', command=lambda: self.frames['frame3'].tkraise())
        self.config(menu=menu_bar)
        self.switch_frames('frame1')

    def switch_frames(self,container):
        frame=self.frames[container] #make sure to pass a string value as parameter for the container value
        frame.tkraise() #this will raise the frame to top position
class input_form(ttk.Frame):
    def __init__(self,container):
        super().__init__()

        # defining values to hold the state of each item
        self.val_butter_chicken=tk.DoubleVar()
        self.val_butter_paneer=tk.DoubleVar()
        self.val_kadhai_mushroom=tk.DoubleVar()
        self.val_kadhai_paneer=tk.DoubleVar()
        self.val_kadhai_chicken=tk.DoubleVar()
        self.val_chicken_handi=tk.DoubleVar()
        self.val_mushroom_dopyaza=tk.DoubleVar()
        self.val_paneer_dopyaza=tk.DoubleVar()
        self.val_changeji_chicken=tk.DoubleVar()
        self.val_tandoori_chicken=tk.DoubleVar()
        self.val_chicken_tikka=tk.DoubleVar()
        self.val_Paneer_tikka=tk.DoubleVar()
        self.val_naan=tk.IntVar()
        self.val_roti=tk.IntVar()
        self.val_butter_naan=tk.IntVar()
        self.val_garlic_naan=tk.IntVar()
        self.val_missi_roti=tk.IntVar()
        self.val_lachha_paratha=tk.IntVar()
        self.val_malai_chaap=tk.DoubleVar()
        self.val_tandoori_chaap=tk.DoubleVar()
        self.val_achari_chaap=tk.DoubleVar()
        self.val_mutton=tk.DoubleVar()
        self.val_chowmein=tk.DoubleVar()
        self.val_schezwan_noodles=tk.DoubleVar()
        self.val_spring_roll=tk.DoubleVar()
        self.val_veg_momos=tk.DoubleVar()
        self.val_chilli_potato=tk.DoubleVar()
        self.val_honey_potato=tk.DoubleVar()
        self.val_cutlets=tk.DoubleVar()
        self.val_mutton_momos=tk.DoubleVar()
        self.val_dahi_ke_kebab=tk.DoubleVar()
        self.val_dahi_ke_sholay=tk.DoubleVar()
        self.val_customer=tk.StringVar()
        self.val_number=tk.IntVar()
        self.val_subtotal=tk.DoubleVar()
        self.val_taxes=tk.DoubleVar()
        self.val_total=tk.DoubleVar()
        self.val_result=tk.StringVar()







        frameLeft = tk.Frame(self,width=900,height=750,bg="white",borderwidth=1,
                             highlightbackground="black", highlightcolor="black", highlightthickness=2) # this will contain the order quantity form
        frameRight = tk.Frame(self,width=500,height=750,bg="White",borderwidth=1,
                              highlightbackground="black", highlightcolor="black", highlightthickness=2) # this will contain the calculator for calculating the order
        frameLeft.grid(row=0,column=0,padx=(20,0), pady=(10,10))
        frameRight.grid(row=0,column=1,padx=(40,20), pady=(10,10))
        item_frame1=tk.Frame(frameLeft,width=400,height=350,bg="white",borderwidth=1,
                             highlightbackground="black", highlightcolor="black", highlightthickness=1)
        item_frame2 = tk.Frame(frameLeft, width=400, height=350, bg="white", borderwidth=1,
                               highlightbackground="black", highlightcolor="black", highlightthickness=1)

        item_frame3 = tk.Frame(frameLeft, width=400, height=350, bg="white", borderwidth=1,
                               highlightbackground="black", highlightcolor="black", highlightthickness=1)
        item_frame4 = tk.Frame(frameLeft, width=400, height=350, bg="white", borderwidth=1,
                               highlightbackground="black", highlightcolor="black", highlightthickness=1)

        item_frame1.grid(row=0,column=0,padx=(25,25),pady=(12,25))
        item_frame2.grid(row=0, column=1,padx=(25,25),pady=(12,25))

        item_frame3.grid(row=1, column=0,padx=(25,25),pady=(0,12))
        item_frame4.grid(row=1, column=1,padx=(25,25),pady=(0,12))


        label_butter_chicken=ttk.Label(item_frame1,text="Butter Chicken",background='white',font=('Helvetica',15))
        label_butter_paneer=ttk.Label(item_frame1,text="Butter Panner",background='white',font=('Helvetica',15))
        label_kadhai_paneer=ttk.Label(item_frame1,text="Kadhai Paneer",background='white',font=('Helvetica',15))
        label_kadhai_mushroom=ttk.Label(item_frame1,text="Kadhai Mushroom",background='white',font=('Helvetica',15))
        entry_butter_chicken=ttk.Entry(item_frame1,width=20,font=('Helvetica',10),textvariable=self.val_butter_chicken)
        entry_butter_paneer=ttk.Entry(item_frame1,width=20,font=('Helvetica',10),textvariable=self.val_butter_paneer)
        entry_kadhai_paneer=ttk.Entry(item_frame1,width=20,font=('Helvetica',10),textvariable=self.val_kadhai_paneer)
        entry_kadhai_mushroom=ttk.Entry(item_frame1,width=20,font=('Helvetica',10),textvariable=self.val_kadhai_mushroom)
        label_kadhai_chicken=ttk.Label(item_frame1,text='Kadhai Chicken',background='white',font=('Helvetica',15))
        label_chicken_handi=ttk.Label(item_frame1,text='Handi Chicken',background='white',font=('Helvetica',15))
        label_paneer_dopyaza=ttk.Label(item_frame1,text='Paneer Dopyaza',background='white',font=('Helvetica',15))
        label_mushroom_dopyaza=ttk.Label(item_frame1,text='Mushroom Dopyaza',background='white',font=('Helvetica',15))
        entry_kadhai_chicken=ttk.Entry(item_frame1,width=20,font=('Helvetica',10),textvariable=self.val_kadhai_chicken)
        entry_chiken_handi=ttk.Entry(item_frame1,width=20,font=('Helvetica',10),textvariable=self.val_chicken_handi)
        entry_paneer_dopyaza=ttk.Entry(item_frame1,width=20,font=('Helvetica',10),textvariable=self.val_paneer_dopyaza)
        entry_mushroom_dopyaza=ttk.Entry(item_frame1,width=20,font=('Helvetica',10),textvariable=self.val_mushroom_dopyaza)
        label_butter_chicken.grid(row=0,column=0,pady=(9,9),padx=(25,0))
        label_butter_paneer.grid(row=1,column=0,pady=(9,9),padx=(25,0))
        label_kadhai_paneer.grid(row=2,column=0,pady=(9,9),padx=(25,0))
        label_kadhai_mushroom.grid(row=3,column=0,pady=(9,9),padx=(25,0))
        label_kadhai_chicken.grid(row=4,column=0,pady=(9,9),padx=(25,0))
        label_chicken_handi.grid(row=5,column=0,pady=(9,9),padx=(25,0))
        label_paneer_dopyaza.grid(row=6,column=0,pady=(9,9),padx=(25,0))
        label_mushroom_dopyaza.grid(row=7,column=0,pady=(9,9),padx=(25,0))
        entry_butter_chicken.grid(row=0,column=1,pady=(9,9),padx=(25,10))
        entry_butter_paneer.grid(row=1,column=1,pady=(9,9),padx=(25,10))
        entry_kadhai_paneer.grid(row=2,column=1,pady=(9,9),padx=(25,10))
        entry_kadhai_mushroom.grid(row=3,column=1,pady=(9,9),padx=(25,10))
        entry_kadhai_chicken.grid(row=4,column=1,pady=(9,9),padx=(25,10))
        entry_chiken_handi.grid(row=5,column=1,pady=(9,9),padx=(25,10))
        entry_paneer_dopyaza.grid(row=6,column=1,pady=(9,9),padx=(25,10))
        entry_mushroom_dopyaza.grid(row=7,column=1,pady=(9,9),padx=(25,10))

        font_label=('Helvetica',15)
        font_entry=('Helvetica',10)

        #we will be defining labels and entries for other items as well
        #items frame 2

        label_changeji_chicken=ttk.Label(item_frame2,text='Changeji Chicken',font=font_label,background='white')
        label_tandoori_chicken=ttk.Label(item_frame2,text='Tandoori Chicken',font=font_label,background='white')
        label_chicken_tikka=ttk.Label(item_frame2,text='Tandoori Chicken',font=font_label,background='white')
        label_paneer_tikka=ttk.Label(item_frame2,text='Paneer Tikka',font=font_label,background='white')
        label_naan=ttk.Label(item_frame2,text='Naan',font=font_label,background='white')
        label_tawa_roti=ttk.Label(item_frame2,text='Roti',font=font_label,background='white')
        label_butter_naan=ttk.Label(item_frame2,text='Butter Naan',font=font_label,background='white')
        label_garlic_naan = ttk.Label(item_frame2, text='Garlic Naan', font=font_label,background='white')

        entry_changezi_chicken=ttk.Entry(item_frame2,width=20,font=font_entry,textvariable=self.val_changeji_chicken)
        entry_tandoori_chicken=ttk.Entry(item_frame2,width=20,font=font_entry,textvariable=self.val_tandoori_chicken)
        entry_chicken_tikka=ttk.Entry(item_frame2,width=20,font=font_entry,textvariable=self.val_chicken_tikka)
        entry_paneer_tikka=ttk.Entry(item_frame2,width=20,font=font_entry,textvariable=self.val_Paneer_tikka)
        entry_naan=ttk.Entry(item_frame2,width=20,font=font_entry,textvariable=self.val_naan)
        entry_tawa_roti=ttk.Entry(item_frame2,width=20,font=font_entry,textvariable=self.val_roti)
        entry_butter_naan=ttk.Entry(item_frame2,width=20,font=font_entry,textvariable=self.val_butter_naan)
        entry_garlic_naan= ttk.Entry(item_frame2, width=20, font=font_entry,textvariable=self.val_garlic_naan)
        label_changeji_chicken.grid(row=0, column=0, pady=(9, 9), padx=(25, 0))
        label_tandoori_chicken.grid(row=1, column=0, pady=(9, 9), padx=(25, 0))
        label_chicken_tikka.grid(row=2, column=0, pady=(9, 9), padx=(25, 0))
        label_paneer_tikka.grid(row=3, column=0, pady=(9, 9), padx=(25, 0))
        label_naan.grid(row=4, column=0, pady=(9, 9), padx=(25, 0))
        label_tawa_roti.grid(row=5, column=0, pady=(9, 9), padx=(25, 0))
        label_butter_naan.grid(row=6, column=0, pady=(9, 9), padx=(25, 0))
        label_garlic_naan.grid(row=7, column=0, pady=(9, 9), padx=(25, 0))
        entry_changezi_chicken.grid(row=0, column=1, pady=(9, 9), padx=(25, 10))
        entry_tandoori_chicken.grid(row=1, column=1, pady=(9, 9), padx=(25, 10))
        entry_chicken_tikka.grid(row=2, column=1, pady=(9, 9), padx=(25, 10))
        entry_paneer_tikka.grid(row=3, column=1, pady=(9, 9), padx=(25, 10))
        entry_naan.grid(row=4, column=1, pady=(9, 9), padx=(25, 10))
        entry_tawa_roti.grid(row=5, column=1, pady=(9, 9), padx=(25, 10))
        entry_butter_naan.grid(row=6, column=1, pady=(9, 9), padx=(25, 10))
        entry_garlic_naan.grid(row=7, column=1, pady=(9, 9), padx=(25, 10))

        #items frame3
        label_Missi_roti=ttk.Label(item_frame3,text='Missi Roti',font=font_label,background='white')
        label_lachha_paratha=ttk.Label(item_frame3,text="Lachha Paratha",font=font_label,background='white')
        label_malai_chaap=ttk.Label(item_frame3,text='Malai Chaap',font=font_label,background='white')
        label_Tandoori_chaap=ttk.Label(item_frame3,text='Tandoori Chaap',font=font_label,background='white')
        label_achari_chaap=ttk.Label(item_frame3,text='Achari Chaap',font=font_label,background='white')
        label_mutton_rogan_josh=ttk.Label(item_frame3,text='Mutton',font=font_label,background='white')
        label_chowmein=ttk.Label(item_frame3,text='Chowmein',font=font_label,background='white')
        label_schezwan_noodels=ttk.Label(item_frame3,text='Schezwan Noodles',font=font_label,background='white')
        entry_missii_roti=ttk.Entry(item_frame3,width=20,font=font_entry,textvariable=self.val_missi_roti)
        entry_lachha_paratha=ttk.Entry(item_frame3,width=20,font=font_entry,textvariable=self.val_lachha_paratha)
        entry_malai_chaap=ttk.Entry(item_frame3,width=20,font=font_entry,textvariable=self.val_malai_chaap)
        entry_tandoori_chaap=ttk.Entry(item_frame3,width=20,font=font_entry,textvariable=self.val_tandoori_chaap)
        entry_achari_chaap=ttk.Entry(item_frame3,width=20,font=font_entry,textvariable=self.val_achari_chaap)
        entry_mutton=ttk.Entry(item_frame3,width=20,font=font_entry,textvariable=self.val_mutton)
        entry_chowmein=ttk.Entry(item_frame3,width=20,font=font_entry,textvariable=self.val_chowmein)
        entry_schezwan_noodles=ttk.Entry(item_frame3,width=20,font=font_entry,textvariable=self.val_schezwan_noodles)
        label_Missi_roti.grid(row=0, column=0, pady=(9, 9), padx=(25, 0))
        label_lachha_paratha.grid(row=1, column=0, pady=(9, 9), padx=(25, 0))
        label_malai_chaap.grid(row=2, column=0, pady=(9, 9), padx=(25, 0))
        label_Tandoori_chaap.grid(row=3, column=0, pady=(9, 9), padx=(25, 0))
        label_achari_chaap.grid(row=4, column=0, pady=(9, 9), padx=(25, 0))
        label_mutton_rogan_josh.grid(row=5, column=0, pady=(9, 9), padx=(25, 0))
        label_chowmein.grid(row=6, column=0, pady=(9, 9), padx=(25, 0))
        label_schezwan_noodels.grid(row=7, column=0, pady=(9, 9), padx=(25, 0))
        entry_missii_roti.grid(row=0, column=1, pady=(9, 9), padx=(25, 10))
        entry_lachha_paratha.grid(row=1, column=1, pady=(9, 9), padx=(25, 10))
        entry_malai_chaap.grid(row=2, column=1, pady=(9, 9), padx=(25, 10))
        entry_tandoori_chaap.grid(row=3, column=1, pady=(9, 9), padx=(25, 10))
        entry_achari_chaap.grid(row=4, column=1, pady=(9, 9), padx=(25, 10))
        entry_mutton.grid(row=5, column=1, pady=(9, 9), padx=(25, 10))
        entry_chowmein.grid(row=6, column=1, pady=(9, 9), padx=(25, 10))
        entry_schezwan_noodles.grid(row=7, column=1, pady=(9, 9), padx=(25, 10))

        # items frame4
        label_spring_roll=ttk.Label(item_frame4,text='Spring Roll',font=font_label,background='white')
        label_momos_veg=ttk.Label(item_frame4,text='Veg Momos',font=font_label,background='white')
        label_chilli_potato=ttk.Label(item_frame4,text='Chilli Potato',font=font_label,background='white')
        label_honey_chilli_potato=ttk.Label(item_frame4,text='Honey Potato',font=font_label,background='white')
        label_cutlets=ttk.Label(item_frame4,text='Cutlets',font=font_label,background='white')
        label_mutton_momos=ttk.Label(item_frame4,text='Mutton Momos',font=font_label,background='white')
        label_dahi_ke_sholey=ttk.Label(item_frame4,text='Dahi ke sholey',font=font_label,background='white')
        label_dahi_ke_kebab=ttk.Label(item_frame4,text='Dahi ke kebab',font=font_label,background='white')
        entry_spring_rool=ttk.Entry(item_frame4,width=20,font=font_entry,textvariable=self.val_spring_roll)
        entry_momos_veg=ttk.Entry(item_frame4,width=20,font=font_entry,textvariable=self.val_veg_momos)
        entry_chilli_potato=ttk.Entry(item_frame4,width=20,font=font_entry,textvariable=self.val_chilli_potato)
        entry_honey_potato=ttk.Entry(item_frame4,width=20,font=font_entry,textvariable=self.val_honey_potato)
        entry_cutlets=ttk.Entry(item_frame4,width=20,font=font_entry,textvariable=self.val_cutlets)
        entry_mutton_momos=ttk.Entry(item_frame4,width=20,font=font_entry,textvariable=self.val_mutton_momos)
        entry_dahi_ke_sholay=ttk.Entry(item_frame4,width=20,font=font_entry,textvariable=self.val_dahi_ke_sholay)
        entry_dahi_ke_kebab=ttk.Entry(item_frame4,width=20,font=font_entry,textvariable=self.val_dahi_ke_kebab)
        label_spring_roll.grid(row=0, column=0, pady=(9, 9), padx=(25, 0))
        label_momos_veg.grid(row=1, column=0, pady=(9, 9), padx=(25, 0))
        label_chilli_potato.grid(row=2, column=0, pady=(9, 9), padx=(25, 0))
        label_honey_chilli_potato.grid(row=3, column=0, pady=(9, 9), padx=(25, 0))
        label_cutlets.grid(row=4, column=0, pady=(9, 9), padx=(25, 0))
        label_mutton_momos.grid(row=5, column=0, pady=(9, 9), padx=(25, 0))
        label_dahi_ke_sholey.grid(row=6, column=0, pady=(9, 9), padx=(25, 0))
        label_dahi_ke_kebab.grid(row=7, column=0, pady=(9, 9), padx=(25, 0))
        entry_spring_rool.grid(row=0, column=1, pady=(9, 9), padx=(25, 10))
        entry_momos_veg.grid(row=1, column=1, pady=(9, 9), padx=(25, 10))
        entry_chilli_potato.grid(row=2, column=1, pady=(9, 9), padx=(25, 10))
        entry_honey_potato.grid(row=3, column=1, pady=(9, 9), padx=(25, 10))
        entry_cutlets.grid(row=4, column=1, pady=(9, 9), padx=(25, 10))
        entry_mutton_momos.grid(row=5, column=1, pady=(9, 9), padx=(25, 10))
        entry_dahi_ke_sholay.grid(row=6, column=1, pady=(9, 9), padx=(25, 10))
        entry_dahi_ke_kebab.grid(row=7, column=1, pady=(9, 9), padx=(25, 10))

        # creating the calculator widgets
        frame_calculator=tk.Frame(frameRight, width=500, height=350, bg="white", borderwidth=1,
                               highlightbackground="black", highlightcolor="black", highlightthickness=1)
        frame_bill=tk.Frame(frameRight, width=500, height=350, bg="white", borderwidth=1,
                               highlightbackground="black", highlightcolor="black", highlightthickness=1)
        frame_calculator.grid(row=0,column=0,pady=(0,10))
        frame_bill.grid(row=1,column=0,pady=(10,10))
        result=ttk.Entry(frame_calculator,width=40,font=font_label,background="white",textvariable=self.val_result)

        frame_buttons=tk.Frame(frame_calculator,width=500, height=250, bg="white")
        result.grid(row=0,column=0,pady=(10,10),ipady=60)
        frame_buttons.grid(row=1,column=0)
        # change font size in the styling section
        btn1 = ttk.Button(frame_buttons, text='1',command=self.btn1_fn)
        btn2 = ttk.Button(frame_buttons, text='2',command=self.btn2_fn)
        btn3 = ttk.Button(frame_buttons, text='3',command=self.btn3_fn)
        btn4 = ttk.Button(frame_buttons, text='4',command=self.btn4_fn)
        btn5 = ttk.Button(frame_buttons, text='5',command=self.btn5_fn)
        btn6 = ttk.Button(frame_buttons, text='6',command=self.btn6_fn)
        btn7 = ttk.Button(frame_buttons, text='7',command=self.btn7_fn)
        btn8 = ttk.Button(frame_buttons, text='8',command=self.btn8_fn)
        btn9 = ttk.Button(frame_buttons, text='9',command=self.btn9_fn)
        btnDot = ttk.Button(frame_buttons,text='.',command=self.btnDot_fn)
        btn0 = ttk.Button(frame_buttons, text='0',command=self.btn0_fn)
        clear = ttk.Button(frame_buttons, text='C',command=self.Clear_fn)
        btnAdd = ttk.Button(frame_buttons,text='+',command=self.Add_fn)
        btnSubtract = ttk.Button(frame_buttons,text='-',command=self.Subtract_fn)
        btnMultiply = ttk.Button(frame_buttons,text='X',command=self.Multiply_fn)
        btnDivide = ttk.Button(frame_buttons,text='/',command=self.Divide_fn)
        btnModulous = ttk.Button(frame_buttons,text='%',command=self.Mod_fn)
        btnLeft = ttk.Button(frame_buttons,text='(',command=self.Left_fn)
        btnRight = ttk.Button(frame_buttons,text=')',command=self.Right_fn)
        btnCalculate = ttk.Button(frame_buttons,text='=',command=self.Equal_fn)
        btn1.grid(row=0,column=0)
        btn2.grid(row=0,column=1)
        btn3.grid(row=0,column=2)
        btnAdd.grid(row=0,column=3)
        btn4.grid(row=1, column=0)
        btn5.grid(row=1, column=1)
        btn6.grid(row=1, column=2)
        btnSubtract.grid(row=1, column=3)
        btn7.grid(row=2, column=0)
        btn8.grid(row=2, column=1)
        btn9.grid(row=2, column=2)
        btnMultiply.grid(row=2, column=3)
        btnDot.grid(row=3, column=0)
        btn0.grid(row=3, column=1)
        clear.grid(row=3, column=2)
        btnDivide.grid(row=3, column=3)
        btnLeft.grid(row=4, column=0)
        btnRight.grid(row=4, column=1)
        btnModulous.grid(row=4, column=2)
        btnCalculate.grid(row=4, column=3)
        font_label2=('Helvetica',25)
        font_entry2=('Helvetica',15)
        label_customer = ttk.Label(frame_bill, text='Name', font=font_label2, background='white')
        label_mobile = ttk.Label(frame_bill, text="Contact", font=font_label2, background='white')
        label_subTotal = ttk.Label(frame_bill, text='Sub Total', font=font_label2, background='white')
        label_Taxes = ttk.Label(frame_bill, text="Taxes", font=font_label2, background='white')
        label_Total = ttk.Label(frame_bill, text='Total', font=font_label2, background='white')
        label_customer.grid(row=0, column=0, padx=(20, 20), pady=(30, 0))
        label_mobile.grid(row=1, column=0, padx=(20, 20), pady=(30, 0))
        label_subTotal.grid(row=2,column=0,padx=(20,20),pady=(30,0))
        label_Taxes.grid(row=3,column=0,padx=(20,20),pady=(30,0))
        label_Total.grid(row=4,column=0,padx=(20,20),pady=(30,0))
        entry_customer = ttk.Entry(frame_bill, width=20, font=font_entry2,textvariable=self.val_customer)
        entry_contact = ttk.Entry(frame_bill, width=20, font=font_entry2,textvariable=self.val_number)
        entry_subTotal=ttk.Entry(frame_bill,width=20,font=font_entry2,textvariable=self.val_subtotal)
        entry_taxes=ttk.Entry(frame_bill,width=20,font=font_entry2,textvariable=self.val_taxes)
        entryTotal=ttk.Entry(frame_bill,width=20,font=font_entry2,textvariable=self.val_total)
        entry_customer.grid(row=0, column=1, padx=(0, 20), pady=(30, 0))
        entry_contact.grid(row=1, column=1, padx=(0, 20), pady=(30, 0))
        entry_subTotal.grid(row=2,column=1,padx=(0,20),pady=(30,0))
        entry_taxes.grid(row=3,column=1,padx=(0,20),pady=(30,0))
        entryTotal.grid(row=4,column=1,padx=(0,20),pady=(30,0))

        bill_button=ttk.Button(frame_bill, text='Bill', command=self.get_tk_values)
        bill_button.grid(row=5,column=1,padx=(0,20),pady=(30,0))

    def get_tk_values(self,*args):
        # this is the format of our list quantity,name,price
        butter_chicken=[self.val_butter_chicken.get(),'butter chicken',500]
        butter_paneer=[self.val_butter_paneer.get(),'butter panner',300]
        kadhai_mushroom=[self.val_kadhai_mushroom.get(),'kadhai mushroom',250]
        kadhai_paneer=[self.val_kadhai_paneer.get(),'kadhai paneer',250]
        kadhai_chicken=[self.val_kadhai_chicken.get(),'kadhai chicken',450]
        chicken_handi=[self.val_chicken_handi.get(),'chicken handi',450]
        mushroom_dopyaza=[self.val_mushroom_dopyaza.get(),'mushroom dopyaza',250]
        paneer_dopyaza=[self.val_paneer_dopyaza.get(),'paneer dopyaza',300]
        changezi_chicken=[self.val_changeji_chicken.get(),'changezi chicken',500]
        tandoori_chicken=[self.val_tandoori_chicken.get(),'tandoori chicken',500]
        chicken_tikka=[self.val_chicken_tikka.get(),'chicken tikka',500]
        paneer_tikka=[self.val_Paneer_tikka.get(),'paneer tikka',450]
        naan=[self.val_naan.get(),'naan',20]
        roti=[self.val_roti.get(),'roti',10]
        butter_naan=[self.val_butter_naan.get(),'butter naan',30]
        garlic_naan=[self.val_garlic_naan.get(),'garlic naan',40]
        missi_roti=[self.val_missi_roti.get(),'missi roti',30]
        lachha_paratha=[self.val_lachha_paratha.get(),'lachha paratha',20]
        malai_chaap=[self.val_malai_chaap.get(),'malai chaap',200]
        tandoori_chaap=[self.val_tandoori_chaap.get(),'tandoori chaap',200]
        achari_chaap=[self.val_achari_chaap.get(),'achari chaap',200]
        mutton=[self.val_mutton.get(),'mutton rogan josh',600]
        chowmein=[self.val_chowmein.get(),'chowmein',50]
        schezwan_noodles=[self.val_schezwan_noodles.get(),'schezwan noodles',70]
        spring_roll=[self.val_spring_roll.get(),'spring roll',80]
        veg_momos=[self.val_veg_momos.get(),'veg momos',60]
        chilli_potato=[self.val_chilli_potato.get(),'chilli potato',80]
        honey_potato=[self.val_honey_potato.get(),'honey chilli potato',100]
        cutlets=[self.val_cutlets.get(),'cutlets',60]
        mutton_momos=[self.val_mutton_momos.get(),'mutton momos',100]
        dahi_ke_kebab=[self.val_dahi_ke_kebab.get(),'dahi ke kebab',250]
        dahi_ke_sholey=[self.val_dahi_ke_sholay.get(),'dahi ke sholey',200]
        Customer=self.val_customer.get()
        Number=self.val_number.get()
        Subtotal=self.val_subtotal.get()
        Tax=self.val_taxes.get()
        total=self.val_total.get()


        order_summary=''
        order_cost=0.0
        for order in [butter_chicken,butter_paneer,kadhai_mushroom,kadhai_paneer,
                      kadhai_chicken,chicken_handi,mushroom_dopyaza,paneer_dopyaza,
                      changezi_chicken,tandoori_chicken,chicken_tikka,paneer_tikka,
                      naan,roti,butter_naan,garlic_naan,missi_roti,lachha_paratha,
                      malai_chaap,tandoori_chaap,achari_chaap,mutton,chowmein,
                      schezwan_noodles,spring_roll,veg_momos,
                      chilli_potato,honey_potato,cutlets,mutton_momos,
                      dahi_ke_kebab,dahi_ke_sholey]:
            if order[0] !=0 or order[0] !=0.0:
                order_summary=order_summary + f"{order[1]}X{order[0]},  "
                order_cost=order_cost+(order[0]*order[2])
        #print(order_summary)
        #print(order_cost)
        tax=0.18*order_cost
        #print(tax)
        #print(order_cost+tax)
        self.val_subtotal.set(value=order_cost)
        self.val_taxes.set(value=tax)
        self.val_total.set(value=order_cost+tax)
        self.val_result.set(value=order_summary)
        total_cost=order_cost+tax
        print(len(order_summary))
        print(len(Customer))
        try:
            if  len(order_summary)>0 and len(Customer)>0:
                operation=insert_orders(order_summary, Customer, Number, order_cost, tax, total_cost)
                print(operation)
                if operation == 1:
                    self.order_confirmed()

                else:
                    self.order_failed()
            else:
                self.fill_details()
        except:
            self.order_failed()

    def order_confirmed(self):
        window = tk.Toplevel()
        window.geometry('250x150')
        window.title('Signup failed')
        window.resizable(False, False)
        label = ttk.Label(window, text='Order placed', font=('Helvetica', 11))
        label.pack()


    def order_failed(self):
        window = tk.Toplevel()
        window.geometry('250x150')
        window.title('Signup failed')
        window.resizable(False, False)
        label = ttk.Label(window, text='Order Failed', font=('Helvetica', 11))
        label.pack()
    def fill_details(self):
        window = tk.Toplevel()
        window.geometry('250x150')
        window.title('Signup failed')
        window.resizable(False, False)
        label = ttk.Label(window, text='Fill all details', font=('Helvetica', 11))
        label.pack()


    def btn1_fn(self):
        string_val=self.val_result.get()
        string_val=string_val+'1'
        self.val_result.set(value=string_val)
    def btn2_fn(self):
        string_val=self.val_result.get()
        string_val=string_val+'2'
        self.val_result.set(value=string_val)
    def btn3_fn(self):
        string_val=self.val_result.get()
        string_val=string_val+'3'
        self.val_result.set(value=string_val)
    def btn4_fn(self):
        string_val=self.val_result.get()
        string_val=string_val+'4'
        self.val_result.set(value=string_val)
    def btn5_fn(self):
        string_val=self.val_result.get()
        string_val=string_val+'5'
        self.val_result.set(value=string_val)
    def btn6_fn(self):
        string_val=self.val_result.get()
        string_val=string_val+'6'
        self.val_result.set(value=string_val)
    def btn7_fn(self):
        string_val=self.val_result.get()
        string_val=string_val+'7'
        self.val_result.set(value=string_val)
    def btn8_fn(self):
        string_val=self.val_result.get()
        string_val=string_val+'8'
        self.val_result.set(value=string_val)
    def btn9_fn(self):
        string_val=self.val_result.get()
        string_val=string_val+'9'
        self.val_result.set(value=string_val)

    def btn0_fn(self):
        string_val = self.val_result.get()
        string_val = string_val + '0'
        self.val_result.set(value=string_val)

    def btnDot_fn(self):
        string_val = self.val_result.get()
        string_val = string_val + '.'
        self.val_result.set(value=string_val)

    def Clear_fn(self):
        self.val_result.set(value='')

    def Add_fn(self):
        string_val = self.val_result.get()
        string_val = string_val + '+'
        self.val_result.set(value=string_val)
    def Subtract_fn(self):
        string_val = self.val_result.get()
        string_val = string_val + '-'
        self.val_result.set(value=string_val)
    def Multiply_fn(self):
        string_val = self.val_result.get()
        string_val = string_val + '*'
        self.val_result.set(value=string_val)
    def Divide_fn(self):
        string_val = self.val_result.get()
        string_val = string_val + '/'
        self.val_result.set(value=string_val)
    def Mod_fn(self):
        string_val = self.val_result.get()
        string_val = string_val + '%'
        self.val_result.set(value=string_val)
    def Left_fn(self):
        string_val = self.val_result.get()
        string_val = string_val + '('
        self.val_result.set(value=string_val)
    def Right_fn(self):
        string_val = self.val_result.get()
        string_val = string_val + ')'
        self.val_result.set(value=string_val)
    def Equal_fn(self):
        string_val = self.val_result.get()
        string_val = eval(string_val)
        self.val_result.set(value=string_val)





    # call this function after every 24 hours







    #now call different functions for saving these values into the database


# fetch all the entries from the orders table and display them in the form of tree view
class tree_data(ttk.Frame):
    def __init__(self,container,*args,**kwargs):
        super().__init__()
        self.tree = ttk.Treeview(self, columns=(1, 2, 3,4,5), show='headings', height=37)
        self.tree.grid(row=0, column=0,padx=(30,0))
        self.tree.heading(1, text="Order Number")
        self.tree.column(1, minwidth=0, width=150, stretch='no')
        self.tree.heading(2, text="Order Details")
        self.tree.column(2, minwidth=0, width=500, stretch='no')
        self.tree.heading(3, text="Customer")
        self.tree.column(3, minwidth=0, width=150, stretch='no')
        self.tree.heading(4, text="Contact")
        self.tree.column(4, minwidth=0, width=150, stretch='no')
        self.tree.heading(5, text="Price")
        self.tree.column(5, minwidth=0, width=150,stretch='no')
        frameRight = tk.Frame(self, width=300, height=750, bg="White", borderwidth=1,
                              highlightbackground="black", highlightcolor="black",
                              highlightthickness=2)  # this will contain the combo boxes and buttons
        frameRight.grid(row=0, column=1, padx=(40, 20), pady=(10, 10))

        self.customer = tk.StringVar()
        self.number = tk.StringVar()
        label_customer=ttk.Label(frameRight,text='Name',font=('Helvetica',25),background='white')
        label_number = ttk.Label(frameRight, text='Number', font=('Helvetica', 25),background='white')
        label_customer.grid(row=0,column=0,padx=(20,20),pady=(40,20))
        label_number.grid(row=2,column=0,padx=(20,20),pady=(40,20))
        entry_customer=ttk.Entry(frameRight,width=20,font=('Helvetica',15),textvariable=self.customer)
        entry_number=ttk.Entry(frameRight,width=20,font=('Helvetica',15),textvariable=self.number)
        entry_customer.grid(row=1,column=0,padx=(20,20),pady=(0,40))
        entry_number.grid(row=3,column=0,padx=(20,20),pady=(0,40))
        refresh = ttk.Button(frameRight, text='Refresh', command=self.refresh_vals)
        refresh.grid(row=5, column=0, padx=(20, 20), pady=(40, 40))
        submit=ttk.Button(frameRight,text='Check',command=self.get_values)
        submit.grid(row=4,column=0,padx=(20,20),pady=(40,40))
        self.orders=fetch_orders()
        self.fill_tree(self.orders)



    def refresh_vals(self):
        self.tree.delete(*self.tree.get_children())
        self.orders = fetch_orders()
        self.fill_tree(self.orders)

    def get_values(self):
        customer=self.customer.get()
        number=self.number.get()
        self.customer.set(value='')
        self.number.set(value='')
        try:
            self.orders = fetch_specific_order(customer,number)
            print(f"The fetched orders are : {self.orders}")
            self.tree.delete(*self.tree.get_children())
            self.fill_tree(self.orders)
        except:
            window = tk.Toplevel()
            window.geometry('250x150')
            window.title('No data found')
            window.resizable(False, False)
            label = ttk.Label(window, text='No data found', font=('Helvetica', 11))
            label.pack()



    def fill_tree(self,orders):
        print(orders)
        i = 0
        for order in orders:
            #print(f"Order_id:{order[0]},OrderDetails:{order[1]},Customer:{order[2]},Contact:{order[3]},Price:{order[6]}")
            self.tree.insert(parent='',index=i, iid=order[0], values=(order[0],order[1], order[2], order[3], order[6]))
            i=i+1


class revenue_data(ttk.Frame):
    def __init__(self,container,*args,**kwargs):
        super().__init__()
        self.day_val=tk.IntVar()
        self.month_val=tk.IntVar()
        self.year_val=tk.IntVar()
        days=[]
        month=[1,2,3,4,5,6,7,8,9,10,11,12]
        year=[]
        for i in range(2021,2032):
            year.append(i)

        for i in range(1,32):
            days.append(i)

        frameLeft = tk.Frame(self, width=1100, height=750, bg="white", borderwidth=1,
                             highlightbackground="black", highlightcolor="black",
                             highlightthickness=2)  # this will contain the tree view details
        frameRight = tk.Frame(self, width=300, height=750, bg="White", borderwidth=1,
                              highlightbackground="black", highlightcolor="black",
                              highlightthickness=2)  # this will contain the combo boxes and buttons

        frameLeft.grid(row=0, column=0, padx=(20, 0), pady=(10, 10))
        frameRight.grid(row=0, column=1, padx=(20, 20), pady=(10, 10))
        frame_top=tk.Frame(frameRight, width=300, height=350, bg="White", borderwidth=1,
                              highlightbackground="black", highlightcolor="black",
                              highlightthickness=2)
        frame_bottom=tk.Frame(frameRight, width=300, height=350, bg="White", borderwidth=1,
                              highlightbackground="black", highlightcolor="black",
                              highlightthickness=2)
        frame_top.grid(row=0, column=0, padx=(10, 10), pady=(10, 20))
        frame_bottom.grid(row=3, column=0, padx=(10, 10), pady=(20, 10))
        combo_days = ttk.Combobox(frame_top , values=days,textvariable=self.day_val)
        combo_days.set(1)
        combo_months = ttk.Combobox(frame_top, values=month,textvariable=self.month_val)
        combo_months.set("1")
        combo_years = ttk.Combobox(frame_top, values=year,textvariable=self.year_val)
        combo_years.set(2021)
        combo_days.grid(row=0, column=0, pady=(50, 50))
        combo_months.grid(row=0, column=1, pady=(50, 50))
        combo_years.grid(row=0, column=2, pady=(50, 50))
        submit = ttk.Button(frameRight, text='Check', command=self.get_values)
        submit.grid(row=1, column=0, pady=(50, 50), padx=(50, 50))

        refresh = ttk.Button(frameRight, text='Refresh', command=self.refresh_table)
        refresh.grid(row=2, column=0, pady=(50, 50), padx=(50, 50))
        # tree view
        self.tree = ttk.Treeview(frameLeft, columns=(1, 2, 3,4), show='headings', height=35)
        self.tree.grid(row=0, column=0, padx=10, pady=10)
        self.tree.heading(1, text="Date")
        self.tree.column(1, minwidth=0, width=200, stretch='no')
        self.tree.heading(2, text="Revenue")
        self.tree.column(2, minwidth=0, width=350, stretch='no')
        self.tree.heading(3, text="Expense")
        self.tree.column(3, minwidth=0, width=200, stretch='no')
        self.tree.heading(4, text="Profit")
        self.tree.column(4, minwidth=0, width=200, stretch='no')
        self.revenue=tk.DoubleVar()
        self.profit=tk.DoubleVar()
        self.expense=tk.DoubleVar()
        label_revenue = ttk.Label(frame_bottom,text='Revenue',font=('Helvetica',20),background='white')
        label_expense = ttk.Label(frame_bottom, text='Expense', font=('Helvetica', 20),background='white')
        label_profit = ttk.Label(frame_bottom, text='Profit', font=('Helvetica', 20),background='white')
        label_revenue.grid(row=0,column=0,padx=(10,20),pady=(20,20))
        label_expense.grid(row=1,column=0,padx=(10,20),pady=(20,20))
        label_profit.grid(row=2,column=0,padx=(10,20),pady=(20,20))
        entry_revnenue = ttk.Entry(frame_bottom,width=20,font=('Helvetica',15),textvariable=self.revenue)
        entry_expense = ttk.Entry(frame_bottom, width=20, font=('Helvetica', 15),textvariable=self.expense)
        entry_profit = ttk.Entry(frame_bottom, width=20, font=('Helvetica', 15),textvariable=self.profit)
        entry_revnenue.grid(row=0,column=1,padx=(10,20),pady=(20,20))
        entry_expense.grid(row=1,column=1,padx=(10,20),pady=(20,20))
        entry_profit.grid(row=2,column=1,padx=(10,20),pady=(20,20))
        submit=ttk.Button(frame_bottom,text='Enter',command=self.enter_revenue)
        submit.grid(row=3,column=1,padx=(10,20),pady=(20,20))
        self.revenue_data=fetch_revenue()
        self.fill_tree(self.revenue_data)


    def refresh_table(self):
        self.tree.delete(*self.tree.get_children())
        self.revenue_data = fetch_revenue()
        self.fill_tree(self.revenue_data)

    def get_values(self):
        day=self.day_val.get()
        month=self.month_val.get()
        year=self.year_val.get()
        date_val=date(year,month,day)
        result=fetch_specific_revenue(date_val)
        print(result)
        if len(result) > 0:
            self.tree.delete(*self.tree.get_children())
            self.fill_tree(result)
        else:
            window = tk.Toplevel()
            window.geometry('250x150')
            window.title('No data found')
            window.resizable(False, False)
            label = ttk.Label(window, text='No data found', font=('Helvetica', 11))
            label.pack()


    def enter_revenue(self):
        revenue=self.revenue.get()
        expense=self.expense.get()
        self.profit.set(value=revenue-expense)
        insert_revenue(revenue,expense,self.profit.get())
        self.revenue.set(value=0.0)
        self.expense.set(value=0.0)
        self.profit.set(value=0.0)
    def fill_tree(self,revenue_data):

        i = 0
        for revenue in revenue_data:
            self.tree.insert(parent='', index=i, iid=revenue[0],
                             values=(revenue[1],revenue[2],revenue[3],revenue[4]))
            i = i + 1






root=main_frame()
root.columnconfigure(0,weight=1)
style = ttk.Style(root)  # Pass in which application this style is for.

# Get the themes available in your system
print(style.theme_names())
print(style.theme_use("xpnative"))
root.mainloop()


