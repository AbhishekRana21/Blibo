from tkinter import *
from PIL import Image, ImageTk
import pymysql
conn=pymysql.connect(host="localhost",user="root",passwd="abhi",db="blibo")
import simpleaudio as sa
import random
mycursor=conn.cursor()
r=Tk()
r.title("BLIBO :)")

a=2
d={1:"white",2:"white",3:"white",4:"white",5:"white",6:"white",7:"white",8:"white",9:"white",10:"white",11:"white",12:"white",13:"white",14:"white",15:"white",16:"white",17:"white",18:"white",19:"white",20:"white",21:"white",22:"white",23:"white",24:"white",25:"white"}
d2={1:[0,0],2:[0,1],3:[0,2],4:[0,3],5:[0,4],6:[1,0],7:[1,1],8:[1,2],9:[1,3],10:[1,4],11:[2,0],12:[2,1],13:[2,2],14:[2,3],15:[2,4],16:[3,0],17:[3,1],18:[3,2],19:[3,3],20:[3,4],21:[4,0],22:[4,1],23:[4,2],24:[4,3],25:[4,4]}
sl=["Andhra Pradesh","Arunachal Pradesh","Assam","Bihar","Chattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jharkhand","Karnataka","Kerela","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands","D&NH and Daman&Diu","Delhi","Jammu and Kashmir","Lakshadweep","Puducherry","Ladakh"]
cap={"Andhra Pradesh":"amarawati","Arunachal Pradesh":"itanagar","Assam":"dispur","Bihar":"patna","Chattisgarh":"raipur","Goa":"panaji","Gujarat":"gandhinagar","Haryana":"chandigarh","Himachal Pradesh":"shimla","Jharkhand":"ranchi","Karnataka":"bengaluru","Kerela":"thiruvananthpuram","Madhya Pradesh":"bhopal","Maharashtra":"mumbai","Manipur":"imphal","Meghalaya":"shillong","Mizoram":"aizawl","Nagaland":"kohima","Odisha":"bhubaneshwar","Punjab":"chandigarh","Rajasthan":"jaipur","Sikkim":"gangtok","Tamil Nadu":"chennai","Telangana":"hyderabad","Tripura":"agartala","Uttar Pradesh":"lucknow","Uttarakhand":"dehradun","West Bengal":"kolkata","Andaman and Nicobar Islands":"port blair","D&NH and Daman&Diu":"daman","Delhi":"new delhi","Jammu and Kashmir":"srinagar","Lakshadweep":"kavaratti","Puducherry":"pondicherry","Ladakh":"leh"}
w11=sa.WaveObject.from_wave_file("b3.wav")
w12=sa.WaveObject.from_wave_file("s3.wav")
w2=sa.WaveObject.from_wave_file("Flip.wav")
w3=sa.WaveObject.from_wave_file("spark.wav")
w4=sa.WaveObject.from_wave_file("s1.wav")


res=0
pn1=""
pn2=""

f1=LabelFrame(r,height=675,width=700,bg="white")
f1.grid(row=0,column=0)

load=Image.open("blibo.jpg")
width, height = load.size
load = load.resize((width//4, height//4))

render=ImageTk.PhotoImage(load)
img=Label(f1,image=render,height=225,width=225)
img.image=render
img.grid(row=0,columnspan=5)

l=Label(f1,text=" BLIBO ",font=("Goudy Stout",40),fg="black",bg="white").grid(row=1,columnspan=5,padx=225,sticky="s",pady=10)
'''l=Label(f1,text="The TonsBridge",font=("Goudy Stout",25),fg="Blue",bg="white").grid(row=1,columnspan=5,padx=225,sticky="s")'''
l=Label(f1,text="Where LOGIC",font=("Goudy Stout",25),fg="green",bg="white").grid(row=2,columnspan=5,sticky="n")
l=Label(f1,text="Meets Creativity :)",font=("Goudy Stout",25),fg="blue",bg="white").grid(row=3,columnspan=5,pady=10)
u=Label(f1,text="FirstPlayer:",font=("Magneto",25),bg="white").grid(row=4,column=0,padx=15,pady=5,sticky="e")
e1=Entry(f1,font=("Bodoni MT Black",25),borderwidth=5)
e1.grid(row=4,column=1,sticky="w")
p=Label(f1,text="Password:",font=("Magneto",25),bg="white").grid(row=5,column=0,padx=15,sticky="e")
e2=Entry(f1,show="*",font=("Bodoni MT Black",25),borderwidth=5)
e2.grid(row=5,column=1,sticky="w")



f=LabelFrame(r)








def bbb():
             global res
             global a
             res+=1
             if (res==1):
                          if (a%2==0):
                                       l=Label(f,text="[2P=ChoiceLeft]",fg="Brown",font=("cooper black",15),anchor="e",bg="white").grid(row=5,column=3,columnspan=2,sticky="we")
                          else:
                                       l=Label(f,text="[1P=ChoiceLeft]",fg="brown",font=("cooper black",15),anchor="w",bg="white").grid(row=5,columnspan=2,sticky="we")
             if(res==2):
                          g=0
                          b=0
                          global d
                          for x in range(1,26):
                                       if d[x]=="green":
                                                    g+=1
                                       elif d[x]=="blue":
                                                    b+=1
                          g=str(g)
                          b=str(b)
                          f.grid_forget()
                          f3=LabelFrame(r,height=675,width=700,bg="white")
                          x1='''select score from bbid where name="'''+pn1+'''";'''
                          y1='''select score from bbid where name="'''+pn2+'''";'''
                          mycursor.execute(x1)
                          s1=str(mycursor.fetchall())
                          h=s1
                          h=h[2:len(h)-4]
                          print("h=",h)
                          if s1=="((None,),)":
                                       h="0"
                                       
                          s1=str(int(h)+int(g))
                          
                          h=""
                          mycursor.execute(y1)
                          s2=str(mycursor.fetchall())
                          h=s2
                          h=h[2:len(h)-4]
                          if s2=="((None,),)":
                                       h="0"
             
                          s2=str(int(h)+int(b))
                          x2='''update bbid set score="'''+s1+'''" where name="'''+pn1+'''";'''
                          y2='''update bbid set score="'''+s2+'''" where name="'''+pn2+'''";'''
                          mycursor.execute(x2)
                          mycursor.execute(y2)
                          conn.commit()
                          if (g>b):
                                       l=Label(f3,text="THE WINNER",font=("Goudy Stout",25),fg="green",bg="white").grid(row=0,columnspan=5,padx=225)
                                       t="IS "+pn1
                                       l=Label(f3,text=t,font=("Goudy Stout",25),fg="green",bg="white").grid(row=1,columnspan=5,padx=225)
                          elif(b>g):
                                       l=Label(f3,text="THE WINNER",font=("Goudy Stout",25),fg="blue",bg="white").grid(row=0,columnspan=5,padx=225)
                                       t="IS "+pn2
                                       l=Label(f3,text=t,font=("Goudy Stout",25),fg="blue",bg="white").grid(row=1,columnspan=5,padx=225)
                          l=Label(f3,text="SCORE",font=("Goudy Stout",25),fg="brown",bg="white").grid(row=2,columnspan=5,padx=225,pady=5)
                          t=pn1+": "+g
                          l=Label(f3,text=t,font=("Goudy Stout",25),fg="brown",bg="white").grid(row=3,columnspan=5)
                          t=pn2+": "+b
                          l=Label(f3,text=t,font=("Goudy Stout",25),fg="brown",bg="white").grid(row=4,columnspan=5)
                          l=Label(f3,text="Thank You",font=("Goudy Stout",25),fg="grey",bg="white").grid(row=5,columnspan=5)
                          l=Label(f3,text="For Playing....",font=("Goudy Stout",25),fg="grey",bg="white").grid(row=6,columnspan=5)
                          l=Label(f3,text="Your scores",font=("Goudy Stout",25),fg="grey",bg="white").grid(row=7,columnspan=5)
                          l=Label(f3,text="have been updated.",font=("Goudy Stout",25),fg="grey",bg="white").grid(row=8,columnspan=5)
                          l=Label(f3,text="Hope you",font=("Goudy Stout",25),fg="grey",bg="white").grid(row=9,columnspan=5)
                          l=Label(f3,text="had a good time :)",font=("Goudy Stout",25),fg="grey",bg="white").grid(row=10,columnspan=5)
                          def quitt():
                                       r.destroy()
                          bb=Button(f3,text="Good bye.",font=("Magneto",15),bg="white",command=quitt).grid(row=11,columnspan=5)
                          
                          
                         
                          f3.grid(row=0,column=0)        
                                       
                          
                          
                          



def login2():
             pn=str(e1.get())
             pw=str(e2.get())
             mycursor.execute("Select * from bbid;")
             name=str(mycursor.fetchall())
             print(name)
             try:
                          tt='''Select pass from bbid where name="'''+pn+'''";'''
             except Error as e:
                          print("Error occured")
             mycursor.execute(tt)
             pts=str(mycursor.fetchall())
             passs=""
             for x in range(3,len(pts)):
                          if (pts[x]!="'"):
                                       passs+=pts[x]
                          else:
                                       break
             
             print(passs)
             if (pn not in name and pw!=passs):
                          b2.grid_forget()
                          l=Label(f1,text="Incorrect Entry",fg="red",font=("Magneto",15),padx=20,pady=5).grid(row=7,column=0,sticky="we",pady=5)
             elif (pn not in name):
                          b2.grid_forget()
                          l=Label(f1,text="Incorrect Entry!",fg="red",font=("Magneto",15),padx=20,pady=5).grid(row=7,column=1,sticky="we",pady=5)
             elif (pw !=passs):
                          b2.grid_forget()
                          l=Label(f1,text="Incorrect Entry",fg="red",font=("Magneto",15),padx=20,pady=5).grid(row=7,column=1,sticky="we",pady=5)
             elif (pn in name and pw==passs and pn!="" and pw!=""):
                          global pn2
                          pn2=pn
                          f1.grid_forget()
                          f.grid(row=0,column=0)
             
             
def login():
             pn=str(e1.get())
             pw=str(e2.get())
             mycursor.execute("Select * from bbid;")
             name=str(mycursor.fetchall())
             print(name)
             lee=Label(f1,bg="white",padx=25,pady=10).grid(row=6,column=0,sticky="we",pady=5)
             try:
                          tt='''Select pass from bbid where name="'''+pn+'''";'''
             except Error as e:
                          print("Error occured")
             mycursor.execute(tt)
             pts=str(mycursor.fetchall())
             passs=""
             for x in range(3,len(pts)):
                          if (pts[x]!="'"):
                                       passs+=pts[x]
                          else:
                                       break
             
                                         
             print(passs)
             
             if (pn not in name and pw!=passs):
                          lee=Label(f1,text="Incorrect Entry",fg="red",font=("Magneto",15),padx=20,pady=5).grid(row=6,column=0,sticky="e",pady=5)
             elif (pn not in name):
                          lee=Label(f1,text="Incorrect Entry!",fg="red",font=("Magneto",15),padx=20,pady=5).grid(row=6,column=0,sticky="e",pady=5)
             elif (pw!=passs):
                          lee=Label(f1,text="Incorrect Entry",fg="red",font=("Magneto",15),padx=20,pady=5).grid(row=6,column=0,sticky="e",pady=5)
             elif (pn in name and pw==passs and pn!="" and pw!=""):
                          global pn1
                          pn1=pn
                          b1.grid_forget()
                          b2.grid_forget()
                          b3.grid_forget()
                          ll=Label(f1,text="1P confirmed. 2P Enter details.",fg="green",font=("Magneto",15),padx=20,pady=5)
                          ll.grid(row=7,column=1,sticky="we",pady=5)
                          u=Label(f1,text="SecondPlayer:",font=("Magneto",25),bg="white").grid(row=4,column=0,padx=15,pady=5,sticky="e")
                          e1.delete(0,END)
                          p=Label(f1,text="Password:",font=("Magneto",25),bg="white").grid(row=5,column=0,padx=15,sticky="e")
                          e2.delete(0,END)
                          bb3=Button(f1,text="Log in",font=("Magneto",15),command=login2,padx=30,pady=5)
                          bb3.grid(row=6,column=1,sticky="w",pady=5)
                          te=pn1+"'s Turn"
                          dis=Button(f,text=te,bg="white",fg="Green",font=("cooper black",15),anchor="w",command=bbb).grid(row=5,columnspan=5,sticky="we")
                          

def newplay():
             f2=LabelFrame(r,height=675,width=700,bg="white")
             f2.grid(row=0,column=0,sticky="s")
             '''l=Label(f2,text="Bleach Bomb",font=("Goudy Stout",25),fg="grey",bg="white").grid(row=0,columnspan=5,pady=10)'''
             l=Label(f1,text="Meets Creativity :)",font=("Goudy Stout",25),fg="blue",bg="white").grid(row=3,columnspan=5,pady=10)
             u=Label(f2,text="Enter Name:",font=("Magneto",25),bg="white").grid(row=1,column=0,padx=15,pady=5,sticky="e")
             e1=Entry(f2,font=("Bodoni MT Black",25),borderwidth=5)
             e1.grid(row=1,column=1,sticky="w")
             p=Label(f2,text="Enter Password:",font=("Magneto",25),bg="white").grid(row=2,column=0,padx=15,sticky="e")
             e2=Entry(f2,show="*",font=("Bodoni MT Black",25),borderwidth=5)
             e2.grid(row=2,column=1,sticky="w")
             
             mycursor.execute('''Select name from bbid order by score desc;''')
             g=list(mycursor.fetchall())
             h=""
             lt=[]
             for x in range(0,len(g)):
                            h=str(g[x])
                            h=h[2:len(h)-3]
                            lt.append(h)
                            
             print(lt)
             def save():
                          name=str(e1.get())
                          passs=str(e2.get())
                          if (name not in lt):
                                       cc='''insert into bbid(name,pass) values("'''+name+'''","'''+passs+'''");'''
                                       mycursor.execute(cc)
                                       conn.commit()
                                       ll=Label(f2,text="Profile Saved.",font=("Magneto",15),padx=55,pady=5)
                                       ll.grid(row=3,column=0,sticky="e",pady=5)
                          else:
                                       ll=Label(f2,text="Name exists!",font=("Magneto",15),fg="red",padx=55,pady=5)
                                       ll.grid(row=3,column=0,sticky="e",pady=5)
             b1=Button(f2,text="Save",font=("Magneto",15),padx=5,pady=5,command=save)
             b1.grid(row=3,column=1,sticky="w",pady=5)

             def htp():
                          f2.grid_forget()
                          f1.grid_forget()
                          f5=LabelFrame(r,height=675,width=700,bg="white")
                          f5.grid(row=0,column=0)
                          l=Label(f5,text="Here Are The Rules :-",font=("Magneto",15),bg="white").pack()
                          l=Label(f5,text="1. There is a 5*5 board which obviously has 25 square blocks.",font=("Magneto",15),bg="white").pack()
                          l=Label(f5,text="The mission is to cover the maximum blocks with player's coloured(Green/Blue) blocks.",font=("Magneto",15),bg="white").pack()
                          l=Label(f5,text="2. P1(Green) get the first turn to click on any block. On being clicked the block turns Green.",font=("Magneto",15),bg="white").pack()
                          l=Label(f5,text="Similarly, P2(Blue) gets the next turn to click on any block except that of the opponent.",font=("Magneto",15),bg="white").pack()
                          l=Label(f5,text="Now on being clicked the block turns blue.",font=("Magneto",15),bg="white").pack()
                          l=Label(f5,text="3. The process goes on but what's special is that the players can click on their own blocks",font=("Magneto",15),bg="white").pack()
                          l=Label(f5,text="which would then explode like a bomb and affect the blocks attached to them.",font=("Magneto",15),bg="white").pack()
                          l=Label(f5,text="What happens on Explosion....",font=("Magneto",15),bg="white").pack()
                          l=Label(f5,text="Green Card Turned\t\tBlue Card Turned",font=("Magneto",15),bg="white").pack()
                          l=Label(f5,text="Nearby blocks if\t\tNearby blocks if",font=("Magneto",15),bg="white").pack()
                          l=Label(f5,text="White: no effect\t\tWhite:no effect",font=("Magneto",15),bg="white").pack()
                          l=Label(f5,text="Green: no effect\t\tBlue: no effect",font=("Magneto",15),bg="white").pack()
                          l=Label(f5,text="Blue: turns Green\t\tGreen: turns Blue",font=("Magneto",15),bg="white").pack()
                          l=Label(f5,text="4. If a block turns brown, then it gets blocked i.e. it cannot be clicked or turned.",font=("Magneto",15),bg="white").pack()
                          l=Label(f5,text="5. At the end when there are no more white blocks left and/or the players have no possible ways",font=("Magneto",15),bg="white").pack()
                          l=Label(f5,text="to increase their own coloured blocks, then they can decide to finish the game by clicking on their",font=("Magneto",15),bg="white").pack()
                          l=Label(f5,text="own name at the base of the board.",font=("Magneto",15),bg="white").pack()
                          l=Label(f5,text="6. If P1 clicks than P2 gets a chance to overview the situation and click the base the second time to",font=("Magneto",15),bg="white").pack()
                          l=Label(f5,text="end the match and vice versa.",font=("Magneto",15),bg="white").pack()
                          l=Label(f5,text="7. Lastly the winner and the score, based on the number of coloured(Green&Blue) blocks is displayed.",font=("Magneto",15),bg="white").pack()
                          def back3():
                                       f5.grid_forget()
                                       f1.grid(row=0,column=0)
                                       f2.grid(row=0,column=0,sticky="s")
                          b33=Button(f5,text="Back",font=("Magneto",15),command=back3,padx=55).pack()
             b2=Button(f2,text="How To Play?",font=("Magneto",15),padx=55,pady=5,command=htp)
             b2.grid(row=4,column=1,sticky="w",pady=5)
             def back():
                          f2.grid_forget()
                          e1.delete(0,END)
                          e2.delete(0,END)
                          lee=Label(f1,bg="white",padx=25,pady=10).grid(row=6,column=0,sticky="we",pady=5)
             b3=Button(f2,text="Back",font=("Magneto",15),command=back,padx=55,pady=5)
             b3.grid(row=4,column=1,sticky="e",pady=5)
            
                          


b1=Button(f1,text="Log in",font=("Magneto",15),padx=55,pady=5,command=login)
b1.grid(row=6,column=1,sticky="w",pady=5)
b2=Button(f1,text="New Player",font=("Magneto",15),command=newplay,padx=28,pady=5)
b2.grid(row=7,column=1,sticky="w",pady=5)
def hs():
             f1.grid_forget()
             f4=LabelFrame(r,height=675,width=700,bg="white")
             f4.grid(row=0,column=0)
             mycursor.execute('''Select name from bbid order by score desc;''')
             g=list(mycursor.fetchall())
             h=""
             lt=[]
             for x in range(0,len(g)):
                            h=str(g[x])
                            h=h[2:len(h)-3]
                            lt.append(h)
                            
             print(lt)
             l=Label(f4,text="NAME",font=("Magneto",25),padx=25,bg="white").grid(row=0,column=0,sticky="w",padx=10,pady=10)
             l=Label(f4,text="SCORE",font=("Magneto",25),padx=25,bg="white").grid(row=0,column=1,sticky="e",padx=10,pady=10)
             for x in range(0,len(lt)):
                          tt=str(x+1)+". "+lt[x]
                          l=Label(f4,text=tt,font=("Magneto",25),padx=25,bg="white").grid(row=x+1,column=0,sticky="w",padx=10,pady=5)
             mycursor.execute('''Select score from bbid order by score desc;''')
             g=list(mycursor.fetchall())
             h=""
             lt=[]
             print(g)
             for x in range(0,len(g)):
                            h=str(g[x])
                            h=h[1:len(h)-2]
                            lt.append(h)               
             print(lt)
             for x in range(0,len(lt)):
                          if (lt[x]!="None"):
                                       l=Label(f4,text=lt[x],font=("Magneto",25),padx=25,bg="white").grid(row=x+1,column=1,padx=10,pady=5)
                          else:
                                       l=Label(f4,text="0",font=("Magneto",25),padx=25,bg="white").grid(row=x+1,column=1,padx=10,pady=5)
             conn.commit()
             def back2():
                          f4.grid_forget()
                          f1.grid(row=0,column=0)
             b=Button(f4,text="Back",font=("Magneto",25),padx=25,bg="white",command=back2).grid(row=0,column=2,sticky="e",padx=10)
b3=Button(f1,text="High Scores",font=("Magneto",15),padx=20,pady=5,command=hs)
b3.grid(row=7,column=1,sticky="e",pady=5)


def brown(rv,c,n,co):
             global a
             dis=Button(f,fg="Green",bg="white",font=("cooper black",15),anchor="e",state="disabled").grid(row=5,columnspan=5,sticky="we")                                          
             if n==1:
                          lt=[2,6,7]
             elif n==2:
                          lt=[1,3,6,7,8]
             elif n==3:
                          lt=[2,4,7,8,9]
             elif n==4:
                          lt=[3,5,8,9,10]
             elif n==5:
                          lt=[4,9,10]
             elif n==6:
                          lt=[1,2,7,11,12]
             elif n==7:
                          lt=[1,2,3,6,8,11,12,13]
             elif n==8:
                          lt=[2,3,4,7,9,12,13,14]
             elif n==9:
                          lt=[3,4,5,8,10,13,14,15]
             elif n==10:
                          lt=[4,5,9,14,15]
             elif n==11:
                          lt=[6,7,12,16,17]
             elif n==12:
                          lt=[6,7,8,11,13,16,17,18]
             elif n==13:
                          lt=[7,8,9,12,14,17,18,19]
             elif n==14:
                          lt=[8,9,10,13,15,18,19,20]
             elif n==15:
                          lt=[9,10,14,19,20]
             elif n==16:
                          lt=[11,12,17,21,22]
             elif n==17:
                          lt=[11,12,13,16,18,21,22,23]
             elif n==18:
                          lt=[12,13,14,17,19,22,23,24]
             elif n==19:
                          lt=[13,14,15,18,20,23,24,25]
             elif n==20:
                          lt=[14,15,19,24,25]
             elif n==21:
                          lt=[16,17,22]
             elif n==22:
                          lt=[16,17,18,21,23]
             elif n==23:
                          lt=[17,18,19,22,24]
             elif n==24:
                          lt=[18,19,20,23,25]
             elif n==25:
                          lt=[19,20,24]

             def right():
                          if (d[1]!="white" and d[1]!="brown"):
                                       bt1=Button(f,padx=50,pady=45,bg=d[1],borderwidth=10,command=lambda:brown(0,0,1,d[1])).grid(row=0,column=0)
                          if (d[2]!="white"and d[2]!="brown"):
                                       bt2=Button(f,padx=50,pady=45,bg=d[2],borderwidth=10,command=lambda:brown(0,1,2,d[2])).grid(row=0,column=1)
                          if (d[3]!="white"and d[3]!="brown"):
                                       bt3=Button(f,padx=50,pady=45,bg=d[3],borderwidth=10,command=lambda:brown(0,2,3,d[3])).grid(row=0,column=2)
                          if (d[4]!="white"and d[4]!="brown"):
                                       bt4=Button(f,padx=50,pady=45,bg=d[4],borderwidth=10,command=lambda:brown(0,3,4,d[4])).grid(row=0,column=3)
                          if (d[5]!="white"and d[5]!="brown"):
                                       bt5=Button(f,padx=50,pady=45,bg=d[5],borderwidth=10,command=lambda:brown(0,4,5,d[5])).grid(row=0,column=4)
                          if (d[6]!="white"and d[6]!="brown"):
                                       bt6=Button(f,padx=50,pady=45,bg=d[6],borderwidth=10,command=lambda:brown(1,0,6,d[6])).grid(row=1,column=0)
                          if (d[7]!="white"and d[7]!="brown"):
                                       bt7=Button(f,padx=50,pady=45,bg=d[7],borderwidth=10,command=lambda:brown(1,1,7,d[7])).grid(row=1,column=1)
                          if (d[8]!="white"and d[8]!="brown"):
                                       bt8=Button(f,padx=50,pady=45,bg=d[8],borderwidth=10,command=lambda:brown(1,2,8,d[8])).grid(row=1,column=2)
                          if (d[9]!="white"and d[9]!="brown"):
                                       bt9=Button(f,padx=50,pady=45,bg=d[9],borderwidth=10,command=lambda:brown(1,3,9,d[9])).grid(row=1,column=3)
                          if (d[10]!="white"and d[10]!="brown"):
                                       bt10=Button(f,padx=50,pady=45,bg=d[10],borderwidth=10,command=lambda:brown(1,4,10,d[10])).grid(row=1,column=4)
                          if (d[11]!="white"and d[11]!="brown"):
                                       bt11=Button(f,padx=50,pady=45,bg=d[11],borderwidth=10,command=lambda:brown(2,0,11,d[11])).grid(row=2,column=0)
                          if (d[12]!="white"and d[12]!="brown"):
                                       bt12=Button(f,padx=50,pady=45,bg=d[12],borderwidth=10,command=lambda:brown(2,1,12,d[12])).grid(row=2,column=1)
                          if (d[13]!="white"and d[13]!="brown"):
                                       bt13=Button(f,padx=50,pady=45,bg=d[13],borderwidth=10,command=lambda:brown(2,2,13,d[13])).grid(row=2,column=2)
                          if (d[14]!="white"and d[14]!="brown"):
                                       bt14=Button(f,padx=50,pady=45,bg=d[14],borderwidth=10,command=lambda:brown(2,3,14,d[14])).grid(row=2,column=3)
                          if (d[15]!="white"and d[15]!="brown"):
                                       bt15=Button(f,padx=50,pady=45,bg=d[15],borderwidth=10,command=lambda:brown(2,4,15,d[15])).grid(row=2,column=4)
                          if (d[16]!="white"and d[16]!="brown"):
                                       bt16=Button(f,padx=50,pady=45,bg=d[16],borderwidth=10,command=lambda:brown(3,0,16,d[16])).grid(row=3,column=0)
                          if (d[17]!="white"and d[17]!="brown"):
                                       bt17=Button(f,padx=50,pady=45,bg=d[17],borderwidth=10,command=lambda:brown(3,1,17,d[17])).grid(row=3,column=1)
                          if (d[18]!="white"and d[18]!="brown"):
                                       bt18=Button(f,padx=50,pady=45,bg=d[18],borderwidth=10,command=lambda:brown(3,2,18,d[18])).grid(row=3,column=2)
                          if (d[19]!="white"and d[19]!="brown"):
                                       bt19=Button(f,padx=50,pady=45,bg=d[19],borderwidth=10,command=lambda:brown(3,3,19,d[19])).grid(row=3,column=3)
                          if (d[20]!="white"and d[20]!="brown"):
                                       bt20=Button(f,padx=50,pady=45,bg=d[20],borderwidth=10,command=lambda:brown(3,4,20,d[20])).grid(row=3,column=4)
                          if (d[21]!="white"and d[21]!="brown"):
                                       bt21=Button(f,padx=50,pady=45,bg=d[21],borderwidth=10,command=lambda:brown(4,0,21,d[21])).grid(row=4,column=0)
                          if (d[22]!="white"and d[22]!="brown"):
                                       bt22=Button(f,padx=50,pady=45,bg=d[22],borderwidth=10,command=lambda:brown(4,1,22,d[22])).grid(row=4,column=1)
                          if (d[23]!="white"and d[23]!="brown"):
                                       bt23=Button(f,padx=50,pady=45,bg=d[23],borderwidth=10,command=lambda:brown(4,2,23,d[23])).grid(row=4,column=2)
                          if (d[24]!="white"and d[24]!="brown"):
                                       bt24=Button(f,padx=50,pady=45,bg=d[24],borderwidth=10,command=lambda:brown(4,3,24,d[24])).grid(row=4,column=3)
                          if (d[25]!="white"and d[25]!="brown"):
                                       bt25=Button(f,padx=50,pady=45,bg=d[25],borderwidth=10,command=lambda:brown(4,4,25,d[25])).grid(row=4,column=4)
                                       
             if (co=="green" and a%2==0):
                          global sl
                          global cap
                          sn=random.choice(sl)
                          sl.remove(sn)
                          cn=sn+": "
                          te=pn2+"'s Turn"
                          def turn():
                                       cname=str(sz.get())
                                       cname=cname.lower()
                                       lcn=cname.split(": ")
                                       cnn=lcn[1]
                                       if cap[sn]==cnn:
                                                    p3=w3.play()
                                                    for x in lt:
                                                                 if d[x]=="blue":
                                                                              d[x]="green"
                                                    dis=Button(f,text=te,fg="Blue",bg="white",font=("cooper black",15),anchor="e",command=bbb).grid(row=5,columnspan=5,sticky="we")
                                                    right()
                                       else:
                                                    p4=w4.play()
                                                    dis=Button(f,text=te,fg="Blue",bg="white",font=("cooper black",15),anchor="e",command=bbb).grid(row=5,columnspan=5,sticky="we")
                                                    W=Label(f,text="Wrong Capital",fg="Red",font=("cooper black",15),bg="white").grid(row=5,columnspan=5)
                                       
                          d1=Button(f,text="Enter",fg="Brown",bg="white",font=("cooper black",15),command=turn).grid(row=5,column=4,sticky="we")
                          sz=Entry(f,fg="Black",bg="white",font=("cooper black",15))
                          sz.insert(0,cn)
                          sz.grid(row=5,columnspan=4,sticky="we")
                          bb=Button(f,padx=50,pady=45,bg="brown",borderwidth=10,state="disabled").grid(row=rv,column=c)
                          d[n]="brown"
                          p2=w2.play()
                          print(co)
                          print("Brown button:",n)
                          a+=1                                     
                                                                               
             elif(co=="blue" and a%2!=0):
                          global cap
                          sn=random.choice(sl)
                          sl.remove(sn)
                          cn=sn+": "
                          te=pn1+"'s Turn"
                          def turn():
                                       cname=str(sz.get())
                                       cname=cname.lower()
                                       lcn=cname.split(": ")
                                       cnn=lcn[1]
                                       if cap[sn]==cnn:
                                                    p3=w3.play()
                                                    for x in lt:
                                                                 if d[x]=="green":
                                                                              d[x]="blue"
                                                    dis=Button(f,text=te,fg="Green",bg="white",font=("cooper black",15),anchor="w",command=bbb).grid(row=5,columnspan=5,sticky="we")
                                                    right()
                                       else:
                                                    p4=w4.play()
                                                    dis=Button(f,text=te,fg="Green",bg="white",font=("cooper black",15),anchor="w",command=bbb).grid(row=5,columnspan=5,sticky="we")
                                                    W=Label(f,text="Wrong Capital",fg="Red",font=("cooper black",15),bg="white",anchor="e").grid(row=5,columnspan=5)
                                       
                          d1=Button(f,text="Enter",fg="Brown",bg="white",font=("cooper black",15),command=turn).grid(row=5,column=4,sticky="we")
                          sz=Entry(f,fg="Black",bg="white",font=("cooper black",15))
                          sz.insert(0,cn)
                          sz.grid(row=5,columnspan=4,sticky="we")
                          bb=Button(f,padx=50,pady=45,bg="brown",borderwidth=10,state="disabled").grid(row=rv,column=c)
                          d[n]="brown"
                          p2=w2.play()
                          print(co)
                          print("Brown button:",n)
                          a+=1                                     
             else:
                          if(a%2==0):
                                       p4=w4.play()
                                       te="Wrong Move by "+pn1+"!"
                                       W=Label(f,text=te,fg="Red",font=("cooper black",15),anchor="e",bg="white").grid(row=5,column=3,columnspan=2)
                          else:
                                       p4=w4.play()
                                       te="Wrong Move by "+pn2+"!"
                                       W=Label(f,text=te,fg="Red",font=("cooper black",15),anchor="w",bg="white").grid(row=5,columnspan=2)


                         
def c1(rv,c,n):
             global a
             if (a%2==0):
                          p1=w11.play()
                          te=pn2+"'s Turn"
                          dis=Button(f,text=te,bg="white",fg="Blue",font=("cooper black",15),anchor="e",command=bbb).grid(row=5,columnspan=5,sticky="we")
                          bta=Button(f,padx=50,pady=45,bg="green",borderwidth=10,command=lambda:brown(rv,c,n,"green")).grid(row=rv,column=c)
                          d[n]="green"
             else:
                          p1=w12.play()
                          te=pn1+"'s Turn"
                          dis=Button(f,text=te,bg="white",fg="Green",font=("cooper black",15),anchor="w",command=bbb).grid(row=5,columnspan=5,sticky="we")
                          btb=Button(f,padx=50,pady=45,bg="blue",borderwidth=10,command=lambda:brown(rv,c,n,"blue")).grid(row=rv,column=c)
                          d[n]="blue"
             a+=1
bt1=Button(f,text="",padx=50,pady=45,bg="white",borderwidth=10,command=lambda:c1(0,0,1)).grid(row=0,column=0)
bt2=Button(f,text="",padx=50,pady=45,bg="white",borderwidth=10,command=lambda:c1(0,1,2)).grid(row=0,column=1)
bt3=Button(f,text="",padx=50,pady=45,bg="white",borderwidth=10,command=lambda:c1(0,2,3)).grid(row=0,column=2)
bt4=Button(f,text="",padx=50,pady=45,bg="white",borderwidth=10,command=lambda:c1(0,3,4)).grid(row=0,column=3)
bt5=Button(f,text="",padx=50,pady=45,bg="white",borderwidth=10,command=lambda:c1(0,4,5)).grid(row=0,column=4)
bt6=Button(f,text="",padx=50,pady=45,bg="white",borderwidth=10,command=lambda:c1(1,0,6)).grid(row=1,column=0)
bt7=Button(f,text="",padx=50,pady=45,bg="white",borderwidth=10,command=lambda:c1(1,1,7)).grid(row=1,column=1)
bt8=Button(f,text="",padx=50,pady=45,bg="white",borderwidth=10,command=lambda:c1(1,2,8)).grid(row=1,column=2)
bt9=Button(f,text="",padx=50,pady=45,bg="white",borderwidth=10,command=lambda:c1(1,3,9)).grid(row=1,column=3)
bt10=Button(f,text="",padx=50,pady=45,bg="white",borderwidth=10,command=lambda:c1(1,4,10)).grid(row=1,column=4)
bt11=Button(f,text="",padx=50,pady=45,bg="white",borderwidth=10,command=lambda:c1(2,0,11)).grid(row=2,column=0)
bt12=Button(f,text="",padx=50,pady=45,bg="white",borderwidth=10,command=lambda:c1(2,1,12)).grid(row=2,column=1)
bt13=Button(f,text="",padx=50,pady=45,bg="white",borderwidth=10,command=lambda:c1(2,2,13)).grid(row=2,column=2)
bt14=Button(f,text="",padx=50,pady=45,bg="white",borderwidth=10,command=lambda:c1(2,3,14)).grid(row=2,column=3)
bt15=Button(f,text="",padx=50,pady=45,bg="white",borderwidth=10,command=lambda:c1(2,4,15)).grid(row=2,column=4)
bt16=Button(f,text="",padx=50,pady=45,bg="white",borderwidth=10,command=lambda:c1(3,0,16)).grid(row=3,column=0)
bt17=Button(f,text="",padx=50,pady=45,bg="white",borderwidth=10,command=lambda:c1(3,1,17)).grid(row=3,column=1)
bt18=Button(f,text="",padx=50,pady=45,bg="white",borderwidth=10,command=lambda:c1(3,2,18)).grid(row=3,column=2)
bt19=Button(f,text="",padx=50,pady=45,bg="white",borderwidth=10,command=lambda:c1(3,3,19)).grid(row=3,column=3)
bt20=Button(f,text="",padx=50,pady=45,bg="white",borderwidth=10,command=lambda:c1(3,4,20)).grid(row=3,column=4)
bt21=Button(f,text="",padx=50,pady=45,bg="white",borderwidth=10,command=lambda:c1(4,0,21)).grid(row=4,column=0)
bt22=Button(f,text="",padx=50,pady=45,bg="white",borderwidth=10,command=lambda:c1(4,1,22)).grid(row=4,column=1)
bt23=Button(f,text="",padx=50,pady=45,bg="white",borderwidth=10,command=lambda:c1(4,2,23)).grid(row=4,column=2)
bt24=Button(f,text="",padx=50,pady=45,bg="white",borderwidth=10,command=lambda:c1(4,3,24)).grid(row=4,column=3)
bt25=Button(f,text="",padx=50,pady=45,bg="white",borderwidth=10,command=lambda:c1(4,4,25)).grid(row=4,column=4)

r.mainloop()
