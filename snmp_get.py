import tkinter as tk
import subprocess

app = tk.Tk()
app.title(" snmp get ")
app.geometry("500x350")
app.configure(background="#dde")

# community
tk.Label(app, text="community",background="#dde",foreground="#009" ,anchor="w").place(x=10,y=5,width=100,height=20)
vcommunity = tk.Entry(app)
vcommunity.place(x=110,y=5,width=300,height=20)

# mibs a serem consultadas
tk.Label(app, text="MIBs:",background="#dde",foreground="#009" ,anchor="w").place(x=10,y=30,width=100,height=20)
checkbox1 = tk.Checkbutton(app, text="SysName", background="#dde",foreground="#000", anchor="w")
checkbox1.select()
checkbox2 = tk.Checkbutton(app, text="HostName", background="#dde",foreground="#000", anchor="w")

checkbox1.place(x=10,y=60,width=100,height=20)
checkbox2.place(x=10,y=80,width=100,height=20) 

# IPs a serem consultados
tk.Label(app, text="IPs:",background="#dde",foreground="#009" ,anchor="w").place(x=10,y=110,width=100,height=20)
textbox = tk.Text(app, height="8", width="59").place(x=10,y=150)


app.mainloop()

