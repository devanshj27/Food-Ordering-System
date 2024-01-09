from tkinter import *
import random
import time;
import datetime
from tkinter import Tk, StringVar, ttk
from tkinter import messagebox

root = Tk()
root.geometry("1350x750+0+0")
root.title("Food Ordering System")

Tops = Frame(root, width=1350, height=100, bd=6, relief="raise")
Tops.pack(side=TOP)
lblTitle = Label(Tops, font=('arial', 50, 'bold'), text="\tFast Food & Beverages\t\t", bg="yellow", fg="red")
lblTitle.grid(row=0, column=0)

BottomMainFrame = Frame(root, width=1350, height=650, bd=6, relief="raise")
BottomMainFrame.pack(side=BOTTOM)

f1 = Frame(BottomMainFrame, width=450, height=650, bd=2, relief="raise")
f1.pack(side=LEFT)
f2 = Frame(BottomMainFrame, width=450, height=650, bd=2, relief="raise")
f2.pack(side=LEFT)
f2TOP = Frame(f2, width=450, height=350, bd=2, relief="raise")
f2TOP.pack(side=TOP)
f2BOTTOM = Frame(f2, width=450, height=300, bd=1, relief="raise")
f2BOTTOM.pack(side=BOTTOM)

f3 = Frame(BottomMainFrame, width=450, height=650, bd=0, relief="raise")
f3.pack(side=RIGHT)

var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()
var5 = IntVar()
var6 = IntVar()
var7 = IntVar()
var8 = IntVar()
var9 = IntVar()
var10 = IntVar()
var11 = IntVar()
var12 = IntVar()
var13 = IntVar()
var14 = IntVar()
var15 = IntVar()
var16 = IntVar()
var17 = IntVar()
var18 = IntVar()
var19 = IntVar()
var20 = IntVar()
var21 = IntVar()
var22 = StringVar()
var23 = IntVar()

var1.set(0)
var2.set(0)
var3.set(0)
var4.set(0)
var5.set(0)
var6.set(0)
var7.set(0)
var8.set(0)
var9.set(0)
var10.set(0)
var11.set(0)
var12.set(0)
var13.set(0)
var14.set(0)
var15.set(0)
var16.set(0)
var17.set(0)
var18.set(0)
var19.set(0)
var20.set(0)
var21.set(0)
var22.set("")
var23.set(0)

varFries = StringVar()
varSoup = StringVar()
varBurger = StringVar()
varPizza = StringVar()
varSandwich = StringVar()
varPasta = StringVar()
varNoodles = StringVar()

varWater = StringVar()
varSoda = StringVar()
varTea = StringVar()
varHotCoffee = StringVar()
varColdCoffee = StringVar()
varDietCoke = StringVar()
varPepsi = StringVar()

varChocoMuffins = StringVar()
varMangoShake = StringVar()
varVanillaIcecream = StringVar()
varPineappleCake = StringVar()
varOreoIcecreamCake = StringVar()
varStrawberryCake = StringVar()
varBlackForest = StringVar()

varChange = StringVar()
varSubTotal = StringVar()
varTotal = StringVar()
varVAT = StringVar()
varTax = StringVar()
varPayment = IntVar()

varFries.set("0")
varSoup.set("0")
varBurger.set("0")
varPizza.set("0")
varSandwich.set("0")
varPasta.set("0")
varNoodles.set("0")

varWater.set("0")
varSoda.set("0")
varTea.set("0")
varHotCoffee.set("0")
varColdCoffee.set("0")
varDietCoke.set("0")
varPepsi.set("0")

varChocoMuffins.set("0")
varMangoShake.set("0")
varVanillaIcecream.set("0")
varPineappleCake.set("0")
varOreoIcecreamCake.set("0")
varStrawberryCake.set("0")
varBlackForest.set("0")

varVAT.set("")
varTax.set("0")
varTotal.set("0")
varChange.set(" ")
varSubTotal.set("0")


def iExit():
    qExit = messagebox.askyesno("Food Ordering System", "Do you want to quit?")
    if qExit > 0:
        root.destroy()
        return


def Reset():
    var1.set(0)
    var2.set(0)
    var3.set(0)
    var4.set(0)
    var5.set(0)
    var6.set(0)
    var7.set(0)
    var8.set(0)
    var9.set(0)
    var10.set(0)
    var11.set(0)
    var12.set(0)
    var13.set(0)
    var14.set(0)
    var15.set(0)
    var16.set(0)
    var17.set(0)
    var18.set(0)
    var19.set(0)
    var20.set(0)
    var21.set(0)
    var23.set(0)

    varFries.set("0")
    varSoup.set("0")
    varBurger.set("0")
    varPizza.set("0")
    varSandwich.set("0")
    varPasta.set("0")
    varNoodles.set("0")
    varTotal.set("0")

    varWater.set("0")
    varSoda.set("0")
    varTea.set("0")
    varHotCoffee.set("0")
    varColdCoffee.set("0")
    varDietCoke.set("0")
    varPepsi.set("0")

    varChocoMuffins.set("0")
    varMangoShake.set("0")
    varVanillaIcecream.set("0")
    varPineappleCake.set("0")
    varOreoIcecreamCake.set("0")
    varStrawberryCake.set("0")
    varBlackForest.set("0")

    varVAT.set("")
    varTax.set("0")
    varTotal.set("0")
    varChange.set(" ")
    varSubTotal.set("0")
    varPayment.set(" ")

    txtFries.configure(state=DISABLED)
    txtSoup.configure(state=DISABLED)
    txtBurger.configure(state=DISABLED)
    txtPizza.configure(state=DISABLED)
    txtSandwich.configure(state=DISABLED)
    txtPasta.configure(state=DISABLED)
    txtNoodles.configure(state=DISABLED)
    txtWater.configure(state=DISABLED)
    txtSoda.configure(state=DISABLED)
    txtTea.configure(state=DISABLED)
    txtHotCoffee.configure(state=DISABLED)
    txtColdCoffee.configure(state=DISABLED)
    txtDietCoke.configure(state=DISABLED)
    txtPepsi.configure(state=DISABLED)
    txtChocoMuffins.configure(state=DISABLED)
    txtMangoShake.configure(state=DISABLED)
    txtVanillaIcecream.configure(state=DISABLED)
    txtPineappleCake.configure(state=DISABLED)
    txtOreoIcecreamCake.configure(state=DISABLED)
    txtStrawberryCake.configure(state=DISABLED)
    txtBlackForest.configure(state=DISABLED)
    # txtPayment.configure(state =DISABLED)
    txtChange.configure(state=DISABLED)
    txtTax.configure(state=DISABLED)
    txtSubTotal.configure(state=DISABLED)
    txtTotal.configure(state=DISABLED)
    var8.get() == 0


def chkFries():
    if (var1.get() == 1):
        txtFries.configure(state=NORMAL)
        varFries.set("")
    elif (var1.get() == 0):
        txtFries.configure(state=DISABLED)
        varFries.set("0")


def chkSoup():
    if (var2.get() == 1):
        txtSoup.configure(state=NORMAL)
        varSoup.set("")
    elif (var2.get() == 0):
        txtSoup.configure(state=DISABLED)
        varSoup.set("0")


def chkBurger():
    if (var3.get() == 1):
        txtBurger.configure(state=NORMAL)
        varBurger.set("")
    elif (var3.get() == 0):
        txtBurger.configure(state=DISABLED)
        varBurger.set("0")


def chkPizza():
    if (var4.get() == 1):
        txtPizza.configure(state=NORMAL)
        varPizza.set("")
    elif (var4.get() == 0):
        txtPizza.configure(state=DISABLED)
        varPizza.set("0")


def chkSandwich():
    if (var5.get() == 1):
        txtSandwich.configure(state=NORMAL)
        varSandwich.set("")
    elif (var5.get() == 0):
        txtSandwich.configure(state=DISABLED)
        varSandwich.set("0")


def chkPasta():
    if (var6.get() == 1):
        txtPasta.configure(state=NORMAL)
        varPasta.set("")
    elif (var6.get() == 0):
        txtPasta.configure(state=DISABLED)
        varPasta.set("0")


def chkNoodles():
    if (var7.get() == 1):
        txtNoodles.configure(state=NORMAL)
        varNoodles.set("")
    elif (var7.get() == 0):
        txtNoodles.configure(state=DISABLED)
        varNoodles.set("0")


def chkWater():
    if (var8.get() == 1):
        txtWater.configure(state=NORMAL)
        varWater.set("")
    elif (var8.get() == 0):
        txtWater.configure(state=DISABLED)
        varWater.set("0")


def chkSoda():
    if (var9.get() == 1):
        txtSoda.configure(state=NORMAL)
        varSoda.set("")
    elif (var9.get() == 0):
        txtSoda.configure(state=DISABLED)
        varSoda.set("0")


def chkTea():
    if (var10.get() == 1):
        txtTea.configure(state=NORMAL)
        varTea.set("")
    elif (var10.get() == 0):
        txtTea.configure(state=DISABLED)
        varTea.set("0")


def chkHotCoffee():
    if (var11.get() == 1):
        txtHotCoffee.configure(state=NORMAL)
        varHotCoffee.set("")
    elif (var11.get() == 0):
        txtHotCoffee.configure(state=DISABLED)
        varHotCoffee.set("0")


def chkColdCoffee():
    if (var12.get() == 1):
        txtColdCoffee.configure(state=NORMAL)
        varColdCoffee.set("")
    elif (var12.get() == 0):
        txtColdCoffee.configure(state=DISABLED)
        varColdCoffee.set("0")


def chkDietCoke():
    if (var13.get() == 1):
        txtDietCoke.configure(state=NORMAL)
        varDietCoke.set("")
    elif (var13.get() == 0):
        txtDietCoke.configure(state=DISABLED)
        varDietCoke.set("0")


def chkPepsi():
    if (var14.get() == 1):
        txtPepsi.configure(state=NORMAL)
        varPepsi.set("")
    elif (var14.get() == 0):
        txtPepsi.configure(state=DISABLED)
        varPepsi.set("0")


def chkChocoMuffins():
    if (var15.get() == 1):
        txtChocoMuffins.configure(state=NORMAL)
        varChocoMuffins.set("")
    elif (var15.get() == 0):
        txtChocoMuffins.configure(state=DISABLED)
        varChocoMuffins.set("0")


def chkMangoShake():
    if (var16.get() == 1):
        txtMangoShake.configure(state=NORMAL)
        varMangoShake.set("")
    elif (var16.get() == 0):
        txtMangoShake.configure(state=DISABLED)
        varMangoShake.set("0")


def chkVanillaIcecream():
    if (var17.get() == 1):
        txtVanillaIcecream.configure(state=NORMAL)
        varVanillaIcecream.set("")
    elif (var17.get() == 0):
        txtVanillaIcecream.configure(state=DISABLED)
        varVanillaIcecream.set("0")


def chkPineappleCake():
    if (var18.get() == 1):
        txtPineappleCake.configure(state=NORMAL)
        varPineappleCake.set("")
    elif (var18.get() == 0):
        txtPineappleCake.configure(state=DISABLED)
        varPineappleCake.set("0")


def chkOreoIcecreamCake():
    if (var19.get() == 1):
        txtOreoIcecreamCake.configure(state=NORMAL)
        varOreoIcecreamCake.set("")
    elif (var19.get() == 0):
        txtOreoIcecreamCake.configure(state=DISABLED)
        varOreoIcecreamCake.set("0")


def chkStrawberryCake():
    if (var20.get() == 1):
        txtStrawberryCake.configure(state=NORMAL)
        varStrawberryCake.set("")
    elif (var20.get() == 0):
        txtStrawberryCake.configure(state=DISABLED)
        varStrawberryCake.set("0")


def chkBlackForest():
    if (var21.get() == 1):
        txtBlackForest.configure(state=NORMAL)
        varBlackForest.set("")
    elif (var21.get() == 0):
        txtBlackForest.configure(state=DISABLED)
        varBlackForest.set("0")


def costofmeal():
    meal1 = float(varFries.get())
    meal2 = float(varSoup.get())
    meal3 = float(varBurger.get())
    meal4 = float(varPizza.get())
    meal5 = float(varSandwich.get())
    meal6 = float(varPasta.get())
    meal7 = float(varNoodles.get())
    meal8 = float(varWater.get())
    meal9 = float(varSoda.get())
    meal10 = float(varTea.get())
    meal11 = float(varHotCoffee.get())
    meal12 = float(varColdCoffee.get())
    meal13 = float(varDietCoke.get())
    meal14 = float(varPepsi.get())
    meal15 = float(varChocoMuffins.get())
    meal16 = float(varMangoShake.get())
    meal17 = float(varVanillaIcecream.get())
    meal18 = float(varPineappleCake.get())
    meal19 = float(varOreoIcecreamCake.get())
    meal20 = float(varStrawberryCake.get())
    meal21 = float(varBlackForest.get())

    iTotal1 = ((meal1 * 45) + (meal2 * 35) + (meal3 * 40) + (meal4 * 50))
    iTotal2 = ((meal5 * 30) + (meal6 * 60) + (meal7 * 65) + (meal8 * 15))
    iTotal3 = ((meal9 * 10) + (meal10 * 10) + (meal11 * 20) + (meal12 * 30))
    iTotal4 = ((meal13 * 40) + (meal14 * 40) + (meal15 * 35) + (meal16 * 35))
    iTotal5 = ((meal17 * 35) + (meal18 * 75) + (meal19 * 90) + (meal20 * 60) + (meal21 * 55))

    if (var22.get() == "Cash"):
        iChange = float(varPayment.get())
        iCost = (iTotal1 + iTotal2 + iTotal3 + iTotal4 + iTotal5)
        iTax = (iCost * 30) / 100
        iTaxq = "$", str('%.2f' % (iTax))
        varTax.set(iTaxq)

        iCostq = "$", str('%.2f' % (iCost))
        varSubTotal.set(iCostq)
        iTotalq = "$", str('%.2f' % ((iCost + iTax)))
        varTotal.set(iTotalq)
        cChange = (iChange - (iChange + iTax))
        cChangeq = "$", str('%.2f' % (cChange))
        varChange.set(cChangeq)
    elif (var22.get() == "Master Card" or "Visa Card" or "Debit Card"):
        varPayment.set("")
        iCost = (iTotal1 + iTotal2 + iTotal3 + iTotal4 + iTotal5)
        iTax = (iCost * 30) / 100
        iTaxq = "$", str('%.2f' % (iTax))
        varTax.set(iTaxq)
        iCostq = "$", str('%.2f' % (iCost))
        varSubTotal.set(iCostq)
        iTotalq = "$", str('%.2f' % ((iCost + iTax)))
        varTotal.set(iTotalq)
        varChange.set("")


lblMeal = Label(f1, font=('arial', 20, 'bold'), text="Starters & Fast Food Meals\t\n", bg="red", fg="white")
lblMeal.grid(row=0, column=0)

Fries = Checkbutton(f1, text="Fries\t\t$45", variable=var1, onvalue=1, offvalue=0, font=('arial', 18, 'bold'),
                    command=chkFries).grid(row=1, column=0, sticky=W)
txtFries = Entry(f1, font=('arial', 18, 'bold'), textvariable=varFries, width=6, justify='right', state=DISABLED)
txtFries.grid(row=1, column=1)

Soup = Checkbutton(f1, text="Soup\t\t$35", variable=var2, onvalue=1, offvalue=0, font=('arial', 18, 'bold'),
                   command=chkSoup).grid(row=2, column=0, sticky=W)
txtSoup = Entry(f1, font=('arial', 18, 'bold'), textvariable=varSoup, width=6, justify='right', state=DISABLED)
txtSoup.grid(row=2, column=1)

Burger = Checkbutton(f1, text="Burger\t\t$40", variable=var3, onvalue=1, offvalue=0, font=('arial', 18, 'bold'),
                     command=chkBurger).grid(row=3, column=0, sticky=W)
txtBurger = Entry(f1, font=('arial', 18, 'bold'), textvariable=varBurger, width=6, justify='right', state=DISABLED)
txtBurger.grid(row=3, column=1)

Pizza = Checkbutton(f1, text="Pizza\t\t$50", variable=var4, onvalue=1, offvalue=0, font=('arial', 18, 'bold'),
                    command=chkPizza).grid(row=4, column=0, sticky=W)
txtPizza = Entry(f1, font=('arial', 18, 'bold'), textvariable=varPizza, width=6, justify='right', state=DISABLED)
txtPizza.grid(row=4, column=1)

Sandwich = Checkbutton(f1, text="Sandwich\t$30", variable=var5, onvalue=1, offvalue=0, font=('arial', 18, 'bold'),
                       command=chkSandwich).grid(row=5, column=0, sticky=W)
txtSandwich = Entry(f1, font=('arial', 18, 'bold'), textvariable=varSandwich, width=6, justify='right', state=DISABLED)
txtSandwich.grid(row=5, column=1)

Pasta = Checkbutton(f1, text="Pasta\t\t$60", variable=var6, onvalue=1, offvalue=0, font=('arial', 18, 'bold'),
                    command=chkPasta).grid(row=6, column=0, sticky=W)
txtPasta = Entry(f1, font=('arial', 18, 'bold'), textvariable=varPasta, width=6, justify='right', state=DISABLED)
txtPasta.grid(row=6, column=1)

Noodles = Checkbutton(f1, text="Noodles\t\t$65", variable=var7, onvalue=1, offvalue=0, font=('arial', 18, 'bold'),
                      command=chkNoodles).grid(row=7, column=0, sticky=W)
txtNoodles = Entry(f1, font=('arial', 18, 'bold'), textvariable=varNoodles, width=6, justify='right', state=DISABLED)
txtNoodles.grid(row=7, column=1)

lblspace = Label(f1, text="\n\n\n\n\n\n\n\n")
lblspace.grid(row=8, column=0)

lblMeal = Label(f2TOP, font=('arial', 18, 'bold'), text="Beverages\n", bg="blue", fg="white")
lblMeal.grid(row=0, column=0)

Water = Checkbutton(f2TOP, text="Water\t\t$15", variable=var8, onvalue=1, offvalue=0, font=('arial', 18, 'bold'),
                    command=chkWater).grid(row=1, column=0, sticky=W)
txtWater = Entry(f2TOP, font=('arial', 18, 'bold'), textvariable=varWater, width=6, justify='right', state=DISABLED)
txtWater.grid(row=1, column=1)

Soda = Checkbutton(f2TOP, text="Soda\t\t$10", variable=var9, onvalue=1, offvalue=0, font=('arial', 18, 'bold'),
                   command=chkSoda).grid(row=2, column=0, sticky=W)
txtSoda = Entry(f2TOP, font=('arial', 18, 'bold'), textvariable=varSoda, width=6, justify='right', state=DISABLED)
txtSoda.grid(row=2, column=1)

Tea = Checkbutton(f2TOP, text="Tea\t\t$10", variable=var10, onvalue=1, offvalue=0, font=('arial', 18, 'bold'),
                  command=chkTea).grid(row=3, column=0, sticky=W)
txtTea = Entry(f2TOP, font=('arial', 18, 'bold'), textvariable=varTea, width=6, justify='right', state=DISABLED)
txtTea.grid(row=3, column=1)

HotCoffee = Checkbutton(f2TOP, text="HotCoffee\t$20", variable=var11, onvalue=1, offvalue=0, font=('arial', 18, 'bold'),
                        command=chkHotCoffee).grid(row=4, column=0, sticky=W)
txtHotCoffee = Entry(f2TOP, font=('arial', 18, 'bold'), textvariable=varHotCoffee, width=6, justify='right',
                     state=DISABLED)
txtHotCoffee.grid(row=4, column=1)

ColdCoffee = Checkbutton(f2TOP, text="ColdCoffee\t$30", variable=var12, onvalue=1, offvalue=0,
                         font=('arial', 18, 'bold'), command=chkColdCoffee).grid(row=5, column=0, sticky=W)
txtColdCoffee = Entry(f2TOP, font=('arial', 18, 'bold'), textvariable=varColdCoffee, width=6, justify='right',
                      state=DISABLED)
txtColdCoffee.grid(row=5, column=1)

DietCoke = Checkbutton(f2TOP, text="DietCoke\t\t$40", variable=var13, onvalue=1, offvalue=0, font=('arial', 18, 'bold'),
                       command=chkDietCoke).grid(row=6, column=0, sticky=W)
txtDietCoke = Entry(f2TOP, font=('arial', 18, 'bold'), textvariable=varDietCoke, width=6, justify='right',
                    state=DISABLED)
txtDietCoke.grid(row=6, column=1)

Pepsi = Checkbutton(f2TOP, text="Pepsi\t\t$40", variable=var14, onvalue=1, offvalue=0, font=('arial', 18, 'bold'),
                    command=chkPepsi).grid(row=7, column=0, sticky=W)
txtPepsi = Entry(f2TOP, font=('arial', 18, 'bold'), textvariable=varPepsi, width=6, justify='right', state=DISABLED)
txtPepsi.grid(row=7, column=1)

lblMeal = Label(f3, font=('arial', 18, 'bold'), text="DESSERTS\n", bg="brown", fg="white")
lblMeal.grid(row=0, column=0)

ChocoMuffins = Checkbutton(f3, text="ChocoMuffins\t$35", variable=var15, onvalue=1, offvalue=0,
                           font=('arial', 18, 'bold'), command=chkChocoMuffins).grid(row=1, column=0, sticky=W)
txtChocoMuffins = Entry(f3, font=('arial', 18, 'bold'), textvariable=varChocoMuffins, width=6, justify='right',
                        state=DISABLED)
txtChocoMuffins.grid(row=1, column=1)

MangoShake = Checkbutton(f3, text="MangoShake\t$75", variable=var16, onvalue=1, offvalue=0, font=('arial', 18, 'bold'),
                         command=chkMangoShake).grid(row=2, column=0, sticky=W)
txtMangoShake = Entry(f3, font=('arial', 18, 'bold'), textvariable=varMangoShake, width=6, justify='right',
                      state=DISABLED)
txtMangoShake.grid(row=2, column=1)

VanillaIcecream = Checkbutton(f3, text="VanillaIcecream\t$35", variable=var17, onvalue=1, offvalue=0,
                              font=('arial', 18, 'bold'), command=chkVanillaIcecream).grid(row=3, column=0, sticky=W)
txtVanillaIcecream = Entry(f3, font=('arial', 18, 'bold'), textvariable=varVanillaIcecream, width=6, justify='right',
                           state=DISABLED)
txtVanillaIcecream.grid(row=3, column=1)

PineappleCake = Checkbutton(f3, text="PineappleCake\t$75", variable=var18, onvalue=1, offvalue=0,
                            font=('arial', 18, 'bold'), command=chkPineappleCake).grid(row=4, column=0, sticky=W)
txtPineappleCake = Entry(f3, font=('arial', 18, 'bold'), textvariable=varPineappleCake, width=6, justify='right',
                         state=DISABLED)
txtPineappleCake.grid(row=4, column=1)

OreoIcecreamCake = Checkbutton(f3, text="OreoIcecreamCake$90", variable=var19, onvalue=1, offvalue=0,
                               font=('arial', 18, 'bold'), command=chkOreoIcecreamCake).grid(row=5, column=0, sticky=W)
txtOreoIcecreamCake = Entry(f3, font=('arial', 18, 'bold'), textvariable=varOreoIcecreamCake, width=6, justify='right',
                            state=DISABLED)
txtOreoIcecreamCake.grid(row=5, column=1)

StrawberryCake = Checkbutton(f3, text="StrawberryCake\t$60", variable=var20, onvalue=1, offvalue=0,
                             font=('arial', 18, 'bold'), command=chkStrawberryCake).grid(row=6, column=0, sticky=W)
txtStrawberryCake = Entry(f3, font=('arial', 18, 'bold'), textvariable=varStrawberryCake, width=6, justify='right',
                          state=DISABLED)
txtStrawberryCake.grid(row=6, column=1)

BlackForest = Checkbutton(f3, text="BlackForest\t$55", variable=var21, onvalue=1, offvalue=0,
                          font=('arial', 18, 'bold'), command=chkBlackForest).grid(row=7, column=0, sticky=W)
txtBlackForest = Entry(f3, font=('arial', 18, 'bold'), textvariable=varBlackForest, width=6, justify='right',
                       state=DISABLED)
txtBlackForest.grid(row=7, column=1)

lblspace = Label(f3, text="\n\n\n\n\n\n\n\n")
lblspace.grid(row=8, column=0)

lblPaymentMethod = Label(f2BOTTOM, font=('arial', 14, 'bold'), text="Payment Method", bd=10, width=16, anchor='w')
lblPaymentMethod.grid(row=0, column=0)

lblChange = Label(f2BOTTOM, font=('arial', 14, 'bold'), text="Change", bd=10, anchor='w')
lblChange.grid(row=0, column=1)
txtChange = Entry(f2BOTTOM, font=('arial', 18, 'bold'), textvariable=varChange, width=6, justify='right',
                  state=DISABLED)
txtChange.grid(row=0, column=2)

cmbPaymentMethod = ttk.Combobox(f2BOTTOM, textvariable=var22, state='readonly', font=('arial', 10, 'bold'), width=20)
cmbPaymentMethod['value'] = ('Cash', 'Master Card', 'Visa card', 'Debit card')
cmbPaymentMethod.current(0)
cmbPaymentMethod.grid(row=1, column=0)

lblTax = Label(f2BOTTOM, font=('arial', 14, 'bold'), text="Tax   ", bd=10, anchor='w')
lblTax.grid(row=1, column=1)
txtTax = Entry(f2BOTTOM, font=('arial', 18, 'bold'), textvariable=varTax, width=6, justify='right', state=DISABLED)
txtTax.grid(row=1, column=2)

txtPayment = Entry(f2BOTTOM, font=('arial', 18, 'bold'), textvariable=varPayment, width=6,
                   justify='right')  # , state =DISABLED)
txtPayment.grid(row=2, column=0)
lblSubTotal = Label(f2BOTTOM, font=('arial', 14, 'bold'), text="SubTotal", bd=10, width=8, anchor='w')
lblSubTotal.grid(row=2, column=1)
txtSubTotal = Entry(f2BOTTOM, font=('arial', 18, 'bold'), textvariable=varSubTotal, width=6, justify='right',
                    state=DISABLED)
txtSubTotal.grid(row=2, column=2)

lblTotal = Label(f2BOTTOM, font=('arial', 14, 'bold'), text="Total", bd=10, width=6, anchor='w')
lblTotal.grid(row=3, column=1)
txtTotal = Entry(f2BOTTOM, font=('arial', 18, 'bold'), textvariable=varTotal, width=6, justify='right', state=DISABLED)
txtTotal.grid(row=3, column=2)

btnTotal = Button(f2BOTTOM, padx=16, pady=1, bd=4, fg="black", font=('arial', 16, 'bold'), width=5, text="Total",
                  command=costofmeal).grid(row=4, column=0)

btnReset = Button(f2BOTTOM, padx=16, pady=1, bd=4, fg="black", font=('arial', 16, 'bold'), width=5, text="Reset",
                  command=Reset).grid(row=4, column=1)

btnExit = Button(f2BOTTOM, padx=16, pady=1, bd=4, fg="black", font=('arial', 16, 'bold'), width=5, text="Exit",
                 command=iExit).grid(row=4, column=2)

lblspace = Label(f2BOTTOM, text="\n\n\n\n\n\n\n")
lblspace.grid(row=5, column=0)

root.mainloop()
