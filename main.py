import Tester as test
from tkinter import *
window = Tk()

window.title('Attendance system')
window.geometry("700x800+500+50")
data=test.get_path()
#recognizer()
lb= Listbox(window, height=5,selectmode='single')
for i in data:
    lb.insert(END,i)
lb.grid(row=10,column=10)
window.mainloop()