import customtkinter
import mysql.connector as sql
import serial

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

root=customtkinter.CTk()
root.geometry("500x350")
ser = serial.Serial('COM3', 9600)

def reset(counter):
    return 300 

def update(values,counter):
            flag=True
            
            if counter==0:
                 flag=False
                 values= values[0:len(values)-3]
                 print(values)
                 values=round((((9/5)*float(values))+36),1)
                 print(values)

                 cur.execute("SELECT Overall_Health FROM HealthCare WHERE Temp = %s AND BP=120 ;",(values,))
                 result=cur.fetchone()
                 label2.configure(text="{}".format(result[0]))

                 if(result==None):
                          label2.configure(text="{}".format("Take reading again"))

                 else:
                        label2.configure(text="{}".format(result[0])) 
                 
                  #  on buzzer
                 ser.write(b'1')
                 
                #  OFF BUZZER
                 ser.write(b'0')

                 button.configure(text="Start")
                 button['state']=customtkinter.NORMAL 


            if ser.in_waiting > 0:
                values = ser.readline().decode('utf-8').rstrip()
                label1.configure(text="{}".format(values))
               
            if flag:
                #renders customTk() window every 100ms
                root.after(100,update,values,counter-1)

def fetch():
        button["state"]=customtkinter.DISABLED
        button.configure(text="Waiting")
        values=0
        counter=300
        update(values,counter)

#main
conn = sql.connect(host="localhost", user="root", passwd="", database="health")
if conn.is_connected:
    print("Database Connection is Successful")
    cur=conn.cursor()

    font=customtkinter.CTkFont(family='Roboto',size=24)

    label=customtkinter.CTkLabel(master=root,text="Temperature Readings taken below".capitalize(),font=font)
    label.pack(pady=12,padx=10)

    label1=customtkinter.CTkLabel(master=root,text="0.00°C".capitalize(),font=font)
    label1.pack(pady=12,padx=10)

    label2=customtkinter.CTkLabel(master=root,text="FeedBack is displayed here",font=font)
    
    label2.pack(pady=12,padx=10)

    button=customtkinter.CTkButton(master=root,text="Start",command=fetch)
    button.pack(pady=12,padx=10)

    root.mainloop()

else:
    print("Database not connected")
