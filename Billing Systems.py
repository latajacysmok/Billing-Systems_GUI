from tkinter import *
import random
import time
import datetime
from tkinter import messagebox

Bill_Sys = Tk()
Bill_Sys.geometry("1350x650")
Bill_Sys.resizable(0, 0)
Bill_Sys.title("Billing Systems")

def Total():
    CarpetPrice = float(Carpets.get())
    FabricPrice = float(Fabric.get())
    BlindsPrice = float(Blinds.get())
    HomeDeliverPrice = float(HomeDeliver.get())

    CarpetCost = "pln", str('%.2f'%((CarpetPrice * 27.98)))
    CostofCarpet.set(CarpetCost)

    FabricCost = "pln", str('%.2f'%((FabricPrice * 19.75)))
    CostofFabric.set(FabricCost)

    BlindsCost = "pln", str('%.2f'%((BlindsPrice * 11.24)))
    CostofBlinds.set(BlindsCost)

    DeliverCost = "pln", str('%.2f'%((HomeDeliverPrice * 9.99)))
    CostofHomeDeliver.set(DeliverCost)

    ToC = "pln", str('%.2f'%((CarpetPrice * 27.98) + (FabricPrice * 19.75) + (BlindsPrice * 11.24) + (HomeDeliverPrice * 9.99)))
    SubTotal.set(ToC)
    Tax = "pln", str('%.2f'%(float((CarpetPrice * 27.98) + (FabricPrice * 19.75) + (BlindsPrice * 11.24) + (HomeDeliverPrice * 9.99))*0.2))
    PaidTax.set(Tax)
    TaxPay = (((CarpetPrice * 27.98) + (FabricPrice * 19.75) + (BlindsPrice * 11.24) + (HomeDeliverPrice * 9.99)) * 0.22)
    Cost = ((CarpetPrice * 27.98) + (FabricPrice * 19.75) + (BlindsPrice * 11.24) + (HomeDeliverPrice * 9.99))
    CostofItems = "pln", str('%.2f'%((TaxPay + Cost)))
    TotalCost.set(CostofItems)

    x = random.randint(10000, 700000)
    randomRef = str(x)
    PaymentRef.set("Bill" + randomRef)

def SalesReference():
    x = random.randint(10000, 700000)
    randomRef = str(x)
    PaymentRef.set("Bill" + randomRef)


def Reset():
    PaymentRef.set("")
    Carpets.set(0)
    Fabric.set(0)
    Blinds.set(0)
    HomeDeliver.set(0)
    # DateofOrder.set("")
    CostofCarpet.set("")
    CostofFabric.set("")
    CostofBlinds.set("")
    CostofHomeDeliver.set("")
    PaidTax.set("")
    SubTotal.set("")
    TotalCost.set("")

def Exit():
    qExit = messagebox.askyesno("Billing System", "Do you want to exit the system")
    if qExit > 0:
        Bill_Sys.destroy()


Tops = Frame(Bill_Sys, width=1350, height=100, bd=8, relief="raise")
Tops.pack(side=TOP)

f1 = Frame(Bill_Sys, width=900, height=650, bd=8, relief="raise")
f1.pack(side=LEFT)

f2 = Frame(Bill_Sys, width=440, height=650, bd=8, relief="raise")
f2.pack(side=LEFT)

#---f1
f1a = Frame(f1, width=900, height=330, bd=8, relief="raise")
f1a.pack(side=TOP)

f2a = Frame(f1, width=900, height=320, bd=8, relief="raise")
f2a.pack(side=BOTTOM)

#---f1a

f1aa = Frame(f1a, width=400, height=430, bd=8, relief="raise")
f1aa.pack(side=LEFT)

f1ab = Frame(f1a, width=400, height=430, bd=8, relief="raise")
f1ab.pack(side=RIGHT)

#---f2a
f2aa = Frame(f2a, width=450, height=320, bd=8, relief="raise")
f2aa.pack(side=LEFT)

f2ab = Frame(f2a, width=450, height=320, bd=8, relief="raise")
f2ab.pack(side=RIGHT)

#---Tops
lblInfo = Label(Tops, font=('arial', 52, 'bold'), text="    Online Billing Systems      ",
                bd=10, anchor='w')
lblInfo.grid(row=0, column=0)

#---Order Information f1aa

PaymentRef  = StringVar()
Carpets     = StringVar()
Fabric      = StringVar()
Blinds      = StringVar()
HomeDeliver = StringVar()

Carpets.set(0)
Fabric.set(0)
Blinds.set(0)
HomeDeliver.set(0)

lblRef = Label(f1aa, font=('arial', 16, 'bold'), text="Sales Reference",
                 bd=16, justify='left')
lblRef.grid(row=0, column=0)

txtRef = Entry(f1aa, font=('arial', 16, 'bold'), textvariable=PaymentRef,
                 bd=10, insertwidth=2, justify='left')
txtRef.grid(row=0, column=1)

lblCarpets = Label(f1aa, font=('arial', 16, 'bold'), text="Carpets",
                 bd=16, justify='left')
lblCarpets.grid(row=1, column=0)

txtCarpets = Entry(f1aa, font=('arial', 16, 'bold'), textvariable=Carpets,
                 bd=10, insertwidth=2, justify='left')
txtCarpets.grid(row=1, column=1)

lblFabric = Label(f1aa, font=('arial', 16, 'bold'), text="Fabric",
                 bd=16, justify='left')
lblFabric.grid(row=2, column=0)

txtFabric = Entry(f1aa, font=('arial', 16, 'bold'), textvariable=Fabric,
                 bd=10, insertwidth=2, justify='left')
txtFabric.grid(row=2, column=1)

lblBlinds = Label(f1aa, font=('arial', 16, 'bold'), text="Blinds",
                 bd=16, justify='left')
lblBlinds.grid(row=3, column=0)

txtBlinds = Entry(f1aa, font=('arial', 16, 'bold'), textvariable=Blinds,
                 bd=10, insertwidth=2, justify='left')
txtBlinds.grid(row=3, column=1)

lblHomeDeliver = Label(f1aa, font=('arial', 16, 'bold'), text="Home Deliver",
                 bd=16, justify='left')
lblHomeDeliver.grid(row=4, column=0)

txtHomeDeliver = Entry(f1aa, font=('arial', 16, 'bold'), textvariable=HomeDeliver,
                 bd=10, insertwidth=2, justify='left')
txtHomeDeliver.grid(row=4, column=1)

#---Order Information f1ab

DateofOrder         = StringVar()
CostofCarpet        = StringVar()
CostofFabric        = StringVar()
CostofBlinds        = StringVar()
CostofHomeDeliver   = StringVar()
DateofOrder.set(time.strftime("%d-%m-%Y"))


lblDateofOrder = Label(f1ab, font=('arial', 16, 'bold'), text="Date of Order",
                 bd=16, justify='left')
lblDateofOrder.grid(row=0, column=0)

txtDateofOrder = Entry(f1ab, font=('arial', 16, 'bold'), textvariable=DateofOrder,
                 bd=10, insertwidth=2, justify='left')
txtDateofOrder.grid(row=0, column=1)

lblCostofCarpets = Label(f1ab, font=('arial', 16, 'bold'), text="Cost of Carpet",
                 bd=16, justify='left')
lblCostofCarpets.grid(row=1, column=0)

txtCostofCarpet = Entry(f1ab, font=('arial', 16, 'bold'), textvariable=CostofCarpet,
                 bd=10, insertwidth=2, justify='left')
txtCostofCarpet.grid(row=1, column=1)

lblCostofFabric = Label(f1ab, font=('arial', 16, 'bold'), text="Cost of Fabric",
                 bd=16, justify='left')
lblCostofFabric.grid(row=2, column=0)

txtCostofFabric = Entry(f1ab, font=('arial', 16, 'bold'), textvariable=CostofFabric,
                 bd=10, insertwidth=2, justify='left')
txtCostofFabric.grid(row=2, column=1)

lblCostofBlinds = Label(f1ab, font=('arial', 16, 'bold'), text="Cost of Blinds",
                 bd=16, justify='left')
lblCostofBlinds.grid(row=3, column=0)

txtCostofBlinds = Entry(f1ab, font=('arial', 16, 'bold'), textvariable=CostofBlinds,
                 bd=10, insertwidth=2, justify='left')
txtCostofBlinds.grid(row=3, column=1)

lblCostofHomeDeliver = Label(f1ab, font=('arial', 16, 'bold'), text="Cost of Deliver",
                 bd=16, justify='left')
lblCostofHomeDeliver.grid(row=4, column=0)

txtCostofHomeDeliver = Entry(f1ab   , font=('arial', 16, 'bold'), textvariable=CostofHomeDeliver,
                 bd=10, insertwidth=2, justify='left')
txtCostofHomeDeliver.grid(row=4, column=1)

#---Order Information f2aa

PaidTax         = StringVar()
SubTotal        = StringVar()
TotalCost       = StringVar()


lblPaidTax = Label(f2aa, font=('arial', 16, 'bold'), text="Paid Tax",
                 bd=8, justify='left')
lblPaidTax.grid(row=0, column=0)

txtPaidTax = Entry(f2aa, font=('arial', 16, 'bold'), textvariable=PaidTax,
                 bd=8, insertwidth=2, justify='left')
txtPaidTax.grid(row=0, column=1)

lblSubTotal = Label(f2aa, font=('arial', 16, 'bold'), text="Sub Total",
                 bd=8, justify='left')
lblSubTotal.grid(row=1, column=0)

txtSubTotal = Entry(f2aa, font=('arial', 16, 'bold'), textvariable=SubTotal,
                 bd=8, insertwidth=2, justify='left')
txtSubTotal.grid(row=1, column=1)

lblTotalCost = Label(f2aa, font=('arial', 16, 'bold'), text="Total Cost",
                 bd=8, justify='left')
lblTotalCost.grid(row=2, column=0)

txtTotalCost = Entry(f2aa, font=('arial', 16, 'bold'), textvariable=TotalCost,
                 bd=8, insertwidth=2, justify='left')
txtTotalCost.grid(row=2, column=1)

#---f2ab Buttons

btnTotal = Button(f2ab, padx = 16, pady=16, bd=8, fg="black", font=('arial', 16, 'bold'), width=15,
                        text="Total Cost", command=Total).grid(row=0, column=0)

btnRefer = Button(f2ab, padx = 16, pady=16, bd=8, fg="black", font=('arial', 16, 'bold'), width=15,
                        text="Sales Reference", command=SalesReference).grid(row=0, column=1)

btnReset = Button(f2ab, padx = 16, pady=16, bd=8, fg="black", font=('arial', 16, 'bold'), width=15,
                        text="Reset", command=Reset).grid(row=1, column=0)

btnExit = Button(f2ab, padx = 16, pady=16, bd=8, fg="black", font=('arial', 16, 'bold'), width=15,
                        text="Exit", command=Exit).grid(row=1, column=1)




#---Calculator

def btnClick(numbers):
    global operator
    operator=operator + str(numbers)
    text_Input.set(operator)

def btnClearDisplay():
    global operator
    operator = ""
    text_Input.set(operator)

def btnEquals():
    global operator
    solution = str(eval(operator))
    text_Input.set(solution)
    operator = ""

operator = ""
text_Input = StringVar()

txtDisplay = Entry(f2, font=('arial', 20, 'bold'), textvariable=text_Input, bd = 40, insertwidth=6,
                   bg='powder blue', justify='right').grid(columnspan=4)

btn7 = Button(f2, padx=17, pady=17,bd=8, fg="black", font=('arial', 20, 'bold'), text="7", bg='powder blue', command=lambda:btnClick(7)).grid(row=1, column=0)
btn8 = Button(f2, padx=17, pady=17, bd=8, fg="black", font=('arial', 20, 'bold'), text="8", bg='powder blue', command=lambda:btnClick(8)).grid(row=1, column=1)
btn9 = Button(f2, padx=17, pady=17, bd=8, fg="black", font=('arial', 20, 'bold'), text="9", bg='powder blue', command=lambda:btnClick(9)).grid(row=1, column=2)
Addition = Button(f2, padx=17, pady=17, bd=8, fg="black", font=('arial', 20, 'bold'), text="+", bg='powder blue', command=lambda:btnClick("+")).grid(row=1, column=3)
btn4 = Button(f2, padx=17, pady=17, bd=8, fg="black", font=('arial', 20, 'bold'), text="4", bg='powder blue', command=lambda:btnClick(4)).grid(row=2, column=0)
btn5 = Button(f2, padx=17, pady=17, bd=8, fg="black", font=('arial', 20, 'bold'), text="5", bg='powder blue', command=lambda:btnClick(5)).grid(row=2, column=1)
btn6 = Button(f2, padx=17, pady=17, bd=8, fg="black", font=('arial', 20, 'bold'), text="6", bg='powder blue', command=lambda:btnClick(6)).grid(row=2, column=2)
Subraction = Button(f2, padx=18, pady=17, bd=8, fg="black", font=('arial', 20, 'bold'), text="-", bg='powder blue', command=lambda:btnClick("-")).grid(row=2, column=3)
btn1 = Button(f2, padx=17, pady=17, bd=8, fg="black", font=('arial', 20, 'bold'), text="1", bg='powder blue', command=lambda:btnClick(1)).grid(row=3, column=0)
btn2 = Button(f2, padx=17, pady=17, bd=8, fg="black", font=('arial', 20, 'bold'), text="2", bg='powder blue', command=lambda:btnClick(2)).grid(row=3, column=1)
btn3 = Button(f2, padx=17, pady=17, bd=8, fg="black", font=('arial', 20, 'bold'), text="3", bg='powder blue', command=lambda:btnClick(3)).grid(row=3, column=2)
Multiplication = Button(f2, padx=18, pady=17, bd=8, fg="black", font=('arial', 20, 'bold'), text="*", bg='powder blue', command=lambda:btnClick("*")).grid(row=3, column=3)
btnClear = Button(f2, padx=17, pady=17, bd=8, fg="black", font=('arial', 20, 'bold'), text="C", bg='powder blue', command=btnClearDisplay).grid(row=4, column=0)
btn0 = Button(f2, padx=18, pady=17, bd=8, fg="black", font=('arial', 20, 'bold'), text="0", bg='powder blue', command=lambda:btnClick(0)).grid(row=4, column=1)
btnEquals = Button(f2, padx=17, pady=17, bd=8, fg="black", font=('arial', 20, 'bold'), text="=", bg='powder blue', command=btnEquals).grid(row=4, column=2)
Division = Button(f2, padx=17, pady=17, bd=8, fg="black", font=('arial', 20, 'bold'), text="/", bg='powder blue', command=lambda:btnClick("/")).grid(row=4, column=3)

Bill_Sys.mainloop()
