import tkinter as tk
import studentEntry as s
class dashboard :
    def onClick1() :
        objs = s.studententry
        objs.ui(s.studententry)
    def onClick2() :
        import bookEntry
    def onClick3() :
        import bookIssue
    def onClick4() :
        import bookReturn
    def ui(self):
        d = tk.Tk()
        d.title("DashBoard")
        button1 = tk.Button(d, width="10", height="1", text="Student Entry", command=dashboard.onClick1)
        button1.grid(row=1, column=0)
        button2 = tk.Button(d, width="10", height="1", text="Book Entry", command=dashboard.onClick2)
        button2.grid(row=1, column=1)
        button3 = tk.Button(d, width="10", height="1", text="Book issue", command=dashboard.onClick3)
        button3.grid(row=1, column=2)
        button4 = tk.Button(d, width="10", height="1", text="Book Return", command=dashboard.onClick4)
        button4.grid(row=1, column=3)
        d.mainloop()