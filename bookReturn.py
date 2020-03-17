import tkinter as tk
import globalVar
class bookreturn :
    def onclick( self, Entry1, br, lable3, row1, column1):
        lable3.configure(text="")
        if Entry1.get() == '' or not Entry1.get().isdigit() :
            if Entry1.get()=='':
                lable3.configure(text = "Entry cannot be empty .")
            else :
                lable3.configure(text="Invalid ID")
        else :
            idNo=Entry1.get()
            sql="SELECT * FROM issue WHERE idNo=%s"
            val=(idNo,)
            c = globalVar.db1.cursor()
            c.execute(sql, val)
            res = c.fetchall()
            if len(res)!=0:
                lable = []
                ++column1
                for i in res :
                    lable3.configure(text="")
                    row = i
                    row1 = row1+1
                    lablen = tk.Label(br, text="idNo : "+str(row[0])+" "+"Name : "+row[1]+" "+"bookId : "+str(row[2])+" "+"bookName : "+row[3]+" "+"IssueDate : "+str(row[4]))
                    lablen.grid(row=row1, column=column1)
                    lable.append(lablen)
                lable4 = tk.Label(br, text="Enter bookId ")
                lable4.grid(row=1, column=0)
                Entry2 = tk.Entry(br, width="15")
                Entry2.grid(row=1, column=1)
                button2 = tk.Button(br, text="Return", command=lambda : bookreturn.onclick1(bookreturn, Entry2, res, br, lable3), width="10", height="1")
                button2.grid(row=1, column=2)
            else :
                lable3.configure(text="Student not found.")
    def onclick1( self, Entry2, res, br, lable3 ):
        lable3.configure(text="")
        if Entry2 ==''or not Entry2.get().isdigit():
            if Entry2.get()=='':
                lable3.configure(text="This field Cannot be Empty : ")
            else :
                lable3.configure(text="Invalid BookID")
        else :
            bookId=Entry2.get()

    def ui( self ):
        br = tk.Tk()
        br.geometry('1000x350+350+300')
        Entry1 = tk.Entry(br, width="15")
        Entry1.grid(row=0, column=1)
        br.title("Book Entry")
        lable1 = tk.Label(br, text="Student Id")
        lable1.grid(row=0, column=0)
        button1 = tk.Button(br, text="Search Student", command=lambda : bookreturn.onclick(bookreturn, Entry1, br, lable3, 0, 4), width="10", height="1")
        button1.grid(column=2, row=0)
        lable3 = tk.Label(br, text="")
        lable3.grid(row=4, column=2)
        br.mainloop()