from ttkbootstrap import *
from ttkbootstrap.constants import *
import ttkbootstrap
import platform
# import module
import subprocess
import pyperclip
from tkinter import messagebox
import psutil


#Total RAM: {psutil.virtual_memory().total / 1024 / 1024 / 1024:.2f} GB

# traverse the info

my_system = platform.uname()


x = ttkbootstrap.Window(themename='darkly')
x.title('customers')
x.geometry('1000x500')
lbl = ttkbootstrap.Labelframe(text='System Information',bootstyle='info',width=350,height=450)
lbl.place(x=1,y=1)

syl = ttkbootstrap.Label(lbl,text=f'System:{my_system.system}')
syl.place(x=1,y=1)
syl1 = ttkbootstrap.Label(lbl,text=f'Node Name: {my_system.node}')
syl1.place(x=1,y=20)
syl2 = ttkbootstrap.Label(lbl,text=f'Release: {my_system.release}')
syl2.place(x=1,y=40)
syl3 = ttkbootstrap.Label(lbl,text=f'Version: {my_system.version}')
syl3.place(x=1,y=60)
syl4 = ttkbootstrap.Label(lbl,text=f'Machine: {my_system.machine}')
syl4.place(x=1,y=80)
syl5 = ttkbootstrap.Label(lbl,text=f'Processor: {my_system.processor}')
syl5.place(x=1,y=100)
syl0 = ttkbootstrap.Label(lbl,text=f'platform:{platform.platform()}')
syl0.place(x=1,y=120)
syj = ttkbootstrap.Label(lbl,text=f"Total RAM: {psutil.virtual_memory().total / 1024 / 1024 / 1024:.2f} GB")
syj.place(x=1,y=140)
su = ttkbootstrap.Label(lbl,text=f"Available RAM: {round(psutil.virtual_memory().available/1000000000, 2)} GB")
su.place(x=1,y=160)
def ctn():
    global new
    # traverse the info
    Id = subprocess.check_output(['systeminfo']).decode('utf-8').split('\n')
    new = []

    # arrange the string into clear info
    for item in Id:
        new.append(str(item.split("\r")[:-1]))

    for i in new:
        print(i[2:-2])
Id = subprocess.check_output(['systeminfo']).decode('utf-8').split('\n')
new = []

    # arrange the string into clear info
for item in Id:
    new.append(str(item.split("\r")[:-1]))
sjl = ttkbootstrap.Label(lbl,text=f'{new[2]}')
sjl.place(x=1,y=180)
sjl1 = ttkbootstrap.Label(lbl,text=f'{new[3]}')
sjl1.place(x=1,y=200)
sjl2 = ttkbootstrap.Label(lbl,text=f'{new[4]}')
sjl2.place(x=1,y=220)
sjl3 = ttkbootstrap.Label(lbl,text=f'{new[5]}')
sjl3.place(x=1,y=220)
#7910
sjl4 = ttkbootstrap.Label(lbl,text=f'{new[7]}')
sjl4.place(x=1,y=240)
sjl5 = ttkbootstrap.Label(lbl,text=f'{new[6]}')
sjl5.place(x=1,y=260)
sjl6 = ttkbootstrap.Label(lbl,text=f'{new[10]}')
sjl6.place(x=1,y=280)
sjl7 = ttkbootstrap.Label(lbl,text=f'{new[11]}')
sjl7.place(x=1,y=300)
sjl8 = ttkbootstrap.Label(lbl,text=f'{new[12]}')
sjl8.place(x=1,y=320)
srh = ttkbootstrap.Label(text='copy:')
srh.pack()
var = StringVar()
cbx = ttkbootstrap.Combobox(textvariable=var)
cbx['values'] = ('processor', 'machine','OS name','OS version')
cbx.pack()

def ztn():
    if var.get()=='processor':
        pyperclip.copy(f'{my_system.processor}')
        messagebox.showinfo(title='info',message=f'your processor: {my_system.processor}\t copied \n Go search don"t make me tired')
    if var.get()=='machine':
        pyperclip.copy(f'{my_system.machine}')
        messagebox.showinfo(title='info',message=f'your machine is: {my_system.machine} \t copied')
    if var.get()=='OS name':
        pyperclip.copy(f'{new[2]}')
        messagebox.showinfo(title='info', message=f'your OS NAME is: {new[2]} \t copied')
    if var.get() == 'OS version':
        pyperclip.copy(f'{new[3]}')
        messagebox.showinfo(title='info', message=f'your OS version is: {new[3]} \t copied')

btn = ttkbootstrap.Button(bootstyle='success-outline',text='copy',command=ztn)
btn.place(x=470,y=52)
vtn=ttkbootstrap.Button(bootstyle="success-outline",text='more infos in cmd',command=ctn)
vtn.place(x=440,y=85)
v=ttkbootstrap.Meter(bootstyle="info", subtextstyle="warning",   padding=5,
    amountused=round(psutil.virtual_memory().available/1000000000, 2),
    metertype="semi",
    subtext=f"GB available ram from {psutil.virtual_memory().total / 1024 / 1024 / 1024:.2f}")
v.place(x=400,y=150)
if __name__=='__main__':
    x.mainloop()
