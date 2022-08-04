# managmentsystem
# bank

# welcome to suprime bank
# 1.open acount ->insert
# 2.cash deposit->update
# 3.cash withdrawl->update
# 4.acount details->fatch
# 5.exit
# run infinite

from tkinter import *
import mysql.connector as c

con = c.connect(host='localhost',
                user="root",
                passwd="lucky",
                database='cetpa')
cursor = con.cursor()
window = Tk()

window.title("bank_managment_system")

# lable

Label(window, text="welcome to suprime bank:", width=100, bg='yellow', font = 'none 12 bold').grid(row=1, column=0)

Label(window, text="choose one from the following option:", width=100, bg='green', font = 'none 12 bold').grid(row=2, column=0)
Label(window, text="@##  project created by : Lokesh singh  ##@", width=150, bg='white').grid(row=9, column=0)

def account():
    acco = Tk()

    acco.title("open account")
    Label(acco, text="enter your information to create new acoount:", width=100, bg='yellow', font = 'none 12 bold').grid(row=0, column=0)
    Label(acco, text="name:", width=50, bg='gray',font = 'none 12 bold').grid(row=1, column=0)
    Label(acco, text="age:", width=50, bg='gray',font = 'none 12 bold').grid(row=2, column=0)
    Label(acco, text="addr:", width=50, bg='gray',font = 'none 12 bold').grid(row=3, column=0)
    Label(acco, text="gender:", width=50, bg='gray',font = 'none 12 bold').grid(row=4, column=0)
    Label(acco, text="amount:", width=50, bg='gray',font = 'none 12 bold').grid(row=5, column=0)


    # textbox
    textentry1 = Entry(acco, width=50, bg='white')
    textentry1.grid(row=1, column=1)
    textentry2 = Entry(acco, width=50, bg='white')
    textentry2.grid(row=2, column=1)
    textentry3 = Entry(acco, width=50, bg='white')
    textentry3.grid(row=3, column=1)
    textentry4 = Entry(acco, width=50, bg='white')
    textentry4.grid(row=4, column=1)
    textentry5 = Entry(acco, width=50, bg='white')
    textentry5.grid(row=5, column=1)
    output = Text(acco, width=100, height=10, bg='white')
    output.grid(row=7, column=0)
    def click():
        entertext1 = str(textentry1.get())
        entertext2 = int(textentry2.get())
        entertext3 = str(textentry3.get())
        entertext4 = str(textentry4.get())
        entertext5 = str(textentry5.get())
        output.delete(0.0, END)
        # query->insert
        query = "insert into account values('{}',{},'{}','{}',{})".format(entertext1, entertext2, entertext3, entertext4, entertext5)

        con.commit()

        output.insert(END, "sumit complete -------> your acount is created")

    def quit_p():
        exit()

    Label(acco, text="press button to quit window:", width=35, height=5, bg='gray', font = 'none 12 bold').grid(row=7, column=1)
    Button(acco, text='quit', command=quit_p, width=50, bg='red', fg='black').grid(row=8, column=1)
    Button(acco, text='sumit', command=click, width=50, bg='white', fg='black').grid(row=6, column=1)

    #output box
    output = Text(acco, width=100, height=10, bg='white')
    output.grid(row=7, column=0)


def cash_deposit():
    cash_d = Tk()
    cash_d.title("cash_deposit")
    Label(cash_d, text="enter your name :", width=50, bg='gray',font = 'none 12 bold').grid(row=0, column=0)
    Label(cash_d, text="enter how much cash you want to deposit:", width=50, bg='gray',font = 'none 12 bold').grid(row=1, column=0)
    textentry1 = Entry(cash_d, width=50, bg='white')
    textentry1.grid(row=0, column=1)
    textentry2 = Entry(cash_d, width=50, bg='white')
    textentry2.grid(row=1, column=1)

    def on_click():
        enter_text1 = str(textentry1.get())
        enter_text2 = str(textentry1.get())
        output.delete(0.0, END)

        # query->update
        query = "update account set amount = {} where name = '{}'".format(enter_text2, enter_text1)
        cursor.execute(query)

        con.commit()
        output.insert(END, "your amount is update successfully!!")

    def quit_p():
        exit()

    Label(cash_d, text="press button to quit window:", width=35, height=5, bg='gray',font = 'none 12 bold').grid(row=7, column=1)
    Button(cash_d, text='quit', command=quit_p, width=50, bg='red', fg='black').grid(row=8, column=1)
    Button(cash_d, text='update', command=on_click, width=50, bg='white', fg='black').grid(row=2, column=0)
    output = Text(cash_d, width=50, bg='white')
    output.grid(row=3, column=0)

def account_deital():

    acco_d= Tk()
    acco_d.title("cash_deposit")
    Label(acco_d, text="enter your name :", width=50, bg='green',font = 'none 12 bold').grid(row=0, column=0)
    Label(acco_d, text="information about your account:", width=50, bg='green',font = 'none 12 bold').grid(row=1, column=0)
    textentry1 = Entry(acco_d, width=50, bg='white')
    textentry1.grid(row=0, column=1)


    def on_click1():
        enter_text1 = str(textentry1.get())
        output.delete(0.0, END)

        # query->insert
        query = "Select * from account where name='{}'".format(enter_text1)
        cursor.execute(query)
        x = cursor.fetchone()

        print(x)


        con.commit()
        output.insert(END,"name|age| addr |gender|amount\n")
        output.insert(END,x)

    def quit_p():
        exit()

    Label(acco_d, text="press button to quit window:", width=35, height=5, bg='gray',font = 'none 12 bold').grid(row=7, column=1)
    Button(acco_d, text='quit', command=quit_p, width=50, bg='red', fg='black').grid(row=8, column=1)
    Button(acco_d, text='search', command=on_click1, width=50, bg='white', fg='black').grid(row=2, column=0)
    output = Text(acco_d, width=100,height=10, bg='white')
    output.grid(row=3, column=0)




def cash_withdrawal():
        cash_w = Tk()
        cash_w.title("cash_withdrawal")
        Label(cash_w, text="enter your name :", width=50, bg='yellow',font = 'none 12 bold').grid(row=0, column=0)
        Label(cash_w, text="enter how much cash you want to withdraw:", width=50, bg='yellow',font = 'none 12 bold').grid(row=1, column=0)
        textentry1 = Entry(cash_w, width=50, bg='white')
        textentry1.grid(row=0, column=1)
        textentry2 = Entry(cash_w, width=50, bg='white')
        textentry2.grid(row=1, column=1)

        def on_click2():
            enter_text1 = str(textentry1.get())
            enter_text2 = str(textentry1.get())
            output.delete(0.0, END)

            # query->update
            query = "update account set amount = amount - {} where name = '{}'".format(enter_text2, enter_text1)
            cursor.execute(query)
            con.commit()

            output.insert(END, "your amount is update successfully!!")

        def quit_p():
            exit()

        Label(cash_w, text="press button to quit window:", width=35, height=5, bg='gray',font = 'none 12 bold').grid(row=7, column=1)
        Button(cash_w, text='quit', command=quit_p, width=50, bg='red', fg='black').grid(row=8, column=1)
        Button(cash_w, text='update', command=on_click2, width=50, bg='white', fg='black').grid(row=2, column=0)
        output = Text(cash_w, width=50, bg='white')
        output.grid(row=3, column=0)



def stop():
    st = Tk()
    st.title("exit window")
    Label(st, text="if you want to exit from project press quit button", width=50, bg='white',font = 'none 12 bold').grid(row=0, column=0)
    def quit_p():
        exit()
    Button(st, text='quit', command=quit_p, width=50, bg='red', fg='black').grid(row=2, column=0)


Button(window, text='1.open account', command=account, width=50, bg='white', fg='black').grid(row=3, column=0)
Button(window, text='2.cash deposit', command=cash_deposit, width=50, bg='white', fg='black').grid(row=4, column=0)
Button(window, text='3.cash withdrawl', command=cash_withdrawal, width=50, bg='white', fg='black').grid(row=5, column=0)
Button(window, text='4.account detail', command=account_deital, width=50, bg='white', fg='black').grid(row=6, column=0)
Button(window, text='5.exit', width=50, command= stop,bg='white', fg='black').grid(row=7, column=0)

window.mainloop()
