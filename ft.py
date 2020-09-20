import mysql.connector
from os import system,name

import os
import datetime
import calendar

def time():
    print("\n")
    print("DATE : ",datetime.date.today())
    print("TODAY'S WEEKDAY : ",calendar.day_name[datetime.date.today().weekday()])
    print("TIME : ",datetime.datetime.now().time().replace(microsecond = 0))
    return


def pc(n,ch):
    print(ch*n,end=' ')
    return
    
def ph():
    pc(75,'*')
    print("\n")
    pc(23,'>')
   
    print("FACULTY LECTURE REMINDER",end=' ')
    
    pc(23,'<')
    print("\n")
    pc(75,'*')
    print("\n")
    return


def intro():
    os.system('cls')
    pc(23,'>')
    print("FACULTY LECTURE REMINDER",end=' ')
    pc(23,'<')
    time()
    pc(75,'_')
    print("\n")
    print("CREATED BY : ALI SYED TANVEER \nENROLLMENT NO. : 0131CS161017\nBRANCH : COMPUTER SCIENCE ENGINEERING\nCOLLEGE : JAI NARAIN COLLEGE OF TECHNOLOGY\n")
    print("SOFTWARE INFORMATION :-\nThis software is basically designed for faculties ,\nthe software will let the faculty know at which time \nthey have to be in which class room.\nThey can use the software by feeding there time table \nin the software only once and after that they can use it by \njust login to the software ")
    o=input("press 'E' for exit or press 'C' for continue : ")
    if o == ('e' or 'E'):
        exit()
    elif o==('c' or 'C'):
        main()
    return
    
    
    
def monday():
    os.system('cls')
    print("ENTER DETAILS FOR MONDAY ")
    lnm = []
    rnm = []
    p = 0
    while(p<8):
        i = int(input("PLEASE ENTER LECTURE NO. : "))
        lnm.insert(p,i)

        j = input("PLEASE ENTER ROOM NO. : ")
        rnm.insert(p,j)
        
        p = p+1
    return lnm,rnm

def tuesday():
    os.system('cls')
    print("ENTER  FOR TUESDAY ")
    lnt = []
    rnt = []
    p = 0
    while(p<8):
        i = int(input("PLEASE ENTER LECTURE NO. : "))
        lnt.insert(p,i)

        j = input("PLEASE ENTER ROOM NO. : ")
        rnt.insert(p,j)
        
        p = p+1
    return lnt,rnt
def wednesday():
    os.system('cls')
    print("PLEASE ENTER DETAILS FOR WEDNESDAY ")
    lnw = []
    rnw = []
    p = 0
    while(p<8):
        i = int(input("PLEASE ENTER LECTURE NO. : "))
        lnw.insert(p,i)

        j = input("PLEASE ENTER ROOM NO. : ")
        rnw.insert(p,j)
        
        p = p+1
    return lnw,rnw
def thusday():
    os.system('cls')
    print("PLEASE ENTER DETAILS FOR THUSDAY ")
    p = 0
    lnth = []
    rnth = []
    p = 0
    while(p<8):
        i = int(input("PLEASE ENTER LECTURE NO. : "))
        lnth.insert(p,i)

        j = input("PLEASE ENTER ROOM NO. : ")
        rnth.insert(p,j)
        
        p = p+1
    return lnth,rnth
def friday():
    os.system('cls')
    print("PLEASE ENTER DETAILS FOR FRIDAY ")
    p = 0
    lnf = []
    rnf = []
    p = 0
    while(p<8):
        i = int(input("PLEASE ENTER LECTURE NO. : "))
        lnf.insert(p,i)

        j = input("PLEASE ENTER ROOM NO. : ")
        rnf.insert(p,j)
        
        p = p+1
    return lnf,rnf

                

def main():
    os.system('cls')
    ph()
    x=int(input("\n\n1.NEW USER \n\n2.EXISTING USER \n\n3.SOFTWARE INFORMATION\n\n4.Exit\n\nyour choice : "))
    
    if x==1 :
        os.system('cls')
        fid = str(input("PLEASE ENTER YOUR FACULTY ID NO. (for eg : ali001): \n"))
        try :
            con = mysql.connector.connect(user = 'root',password = 'root',host = '127.0.0.1')  #connecting to the database
            cur = con.cursor()                      #creating a cursor object
            cur.execute("create database "+fid)     #creting new database according to teachers id
            cur.execute("use "+fid)                 #useing the perticular database
        except Exception as e:
            os.system('cls')
            ph()
            print("failed to connect to the database....")
            print("Exception caught :",e)
            os.system('pause')
            main()
        try:
            cur.execute("create table monday(lecture int, room Varchar(20), start_time time, end_time time)")    #creating tables according to days 
            cur.execute("create table tuesday(lecture int,room varchar(5),start_time time(6),end_time time(6))")
            cur.execute("create table wednesday(lecture int,room varchar(5),start_time time(6),end_time time(6))")
            cur.execute("create table thusday(lecture int,room varchar(5),start_time time(6),end_time time(6))")
            cur.execute("create table friday(lecture int,room varchar(5),start_time time(6),end_time time(6))")
            print("enter details according to your days start enterting details from monday till friday and also enter the lecture no. from 1 to 7 ....")
           
            x,y=monday()        #for taking details for monday
            a,b=tuesday()         #for taking details for tuesday
            c,d=wednesday()       #for taking details for wednesday
            e,f=thusday()         #for taking details for thusday
            g,h=friday()          #for taking details for friday
            i=0
                #for entering details to database for monday
            while(i<8):    
                if i==0 :
                    cur.execute("insert into monday values("+str(x[i])+",'"+y[i]+"','09:00:00','09:44:59')")
                    con.commit()
                elif i==1 :
                    cur.execute("insert into monday values("+str(x[i])+",'"+y[i]+"','09:45:00','10:29:59')")
                    con.commit()
                elif i==2:
                    cur.execute("insert into monday values("+str(x[i])+",'"+y[i]+"','10:30:00','11:14:59')")
                    con.commit()
                elif i==3:
                    cur.execute("insert into monday values("+str(x[i])+",'"+y[i]+"','11:15:00','11:59:59')")
                    con.commit()
                elif i==4:
                    cur.execute("insert into monday values("+str(x[i])+",'"+y[i]+"','12:25:00','13:04:59')")
                    con.commit()
                elif i==5:
                    cur.execute("insert into monday values("+str(x[i])+",'"+y[i]+"','13:05:00','13:44:59')")
                    con.commit()
                elif i==6:
                    cur.execute("insert into monday values("+str(x[i])+",'"+y[i]+"','13:45:00','14:29:59')")
                    con.commit()
                elif i==7:
                    cur.execute("insert into monday values("+str(x[i])+",'"+y[i]+"','14:30:00','15:14:59')")
                    con.commit()
                elif i==8:
                    cur.execute("insert into monday values("+str(x[i])+",'"+y[i]+"','15:15:00','15:59:59')")
            
                i+=1

                 #for entering details to database for tuesday
            i=0      
            while(i<8):             
                if i==0 :
                    cur.execute("insert into tuesday values("+str(a[i])+",'"+b[i]+"','09:00:00','09:44:59')")
                    con.commit()
                elif i==1 :
                    cur.execute("insert into tuesday values("+str(a[i])+",'"+b[i]+"','09:45:00','10:29:59')")
                    con.commit()
                elif i==2:
                    cur.execute("insert into tuesday values("+str(a[i])+",'"+b[i]+"','10:30:00','11:14:59')")
                    con.commit()
                elif i==3:
                    cur.execute("insert into tuesday values("+str(a[i])+",'"+b[i]+"','11:15:00','11:59:59')")
                    con.commit()
                elif i==4:
                    cur.execute("insert into tuesday values("+str(a[i])+",'"+b[i]+"','12:25:00','13:04:59')")
                    con.commit()
                elif i==5:
                    cur.execute("insert into tuesday values("+str(a[i])+",'"+b[i]+"','13:05:00','13:44:59')")
                    con.commit()
                elif i==6:
                    cur.execute("insert into tuesday values("+str(a[i])+",'"+b[i]+"','13:45:00','14:29:59')")
                    con.commit()
                elif i==7:
                    cur.execute("insert into tuesday values("+str(a[i])+",'"+b[i]+"','14:30:00','15:14:59')")
                    con.commit()
                elif i==8:
                    cur.execute("insert into tuesday values("+str(a[i])+",'"+b[i]+"','15:15:00','15:59:59')")
                    con.commit()
                i+=1
                
            #for wednesday
            i=0
            while(i<8):             
                if i==0 :
                    cur.execute("insert into wednesday values("+str(c[i])+",'"+d[i]+"','09:00:00','09:44:59')")
                    con.commit()
                elif i==1 :
                    cur.execute("insert into wednesday values("+str(c[i])+",'"+d[i]+"','09:45:00','10:29:59')")
                    con.commit()
                elif i==2:
                    cur.execute("insert into wednesday values("+str(c[i])+",'"+d[i]+"','10:30:00','11:14:59')")
                    con.commit()
                elif i==3:
                    cur.execute("insert into wednesday values("+str(c[i])+",'"+d[i]+"','11:15:00','11:59:59')")
                    con.commit()
                elif i==4:
                    cur.execute("insert into wednesday values("+str(c[i])+",'"+d[i]+"','12:25:00','13:04:59')")
                    con.commit()
                elif i==5:
                    cur.execute("insert into wednesday values("+str(c[i])+",'"+d[i]+"','13:05:00','13:44:59')")
                    con.commit()
                elif i==6:
                    cur.execute("insert into wednesday values("+str(c[i])+",'"+d[i]+"','13:45:00','14:29:59')")
                    con.commit()
                elif i==7:
                    cur.execute("insert into wednesday values("+str(c[i])+",'"+d[i]+"','14:30:00','15:14:59')")
                    con.commit()
                elif i==8:
                    cur.execute("insert into wednesday values("+str(c[i])+",'"+d[i]+"','15:15:00','15:59:59')")
                    con.commit()
                i+=1

            #for thusday
            i=0
            while(i<8):             
                if i==0 :
                    cur.execute("insert into thusday values("+str(e[i])+",'"+f[i]+"','09:00:00','09:44:59')")
                    con.commit()
                elif i==1 :
                    cur.execute("insert into thusday values("+str(e[i])+",'"+f[i]+"','09:45:00','10:29:59')")
                    con.commit()
                elif i==2:
                    cur.execute("insert into thusday values("+str(e[i])+",'"+f[i]+"','10:30:00','11:14:59')")
                    con.commit()
                elif i==3:
                    cur.execute("insert into thusday values("+str(e[i])+",'"+f[i]+"','11:15:00','11:59:59')")
                    con.commit()
                elif i==4:
                    cur.execute("insert into thusday values("+str(e[i])+",'"+f[i]+"','12:25:00','13:04:59')")
                    con.commit()
                elif i==5:
                    cur.execute("insert into thusday values("+str(e[i])+",'"+f[i]+"','13:05:00','13:44:59')")
                    con.commit()
                elif i==6:
                    cur.execute("insert into thusday values("+str(e[i])+",'"+f[i]+"','13:45:00','14:29:59')")
                    con.commit()
                elif i==7:
                    cur.execute("insert into thusday values("+str(e[i])+",'"+f[i]+"','14:30:00','15:14:59')")
                    con.commit()
                elif i==8:
                    cur.execute("insert into thusday values("+str(e[i])+",'"+f[i]+"','15:15:00','15:59:59')")
                    con.commit()
                i+=1

            #for friday
            i=0
            while(i<8):             
                if i==0 :
                    cur.execute("insert into friday values("+str(g[i])+",'"+h[i]+"','09:00:00','09:44:59')")
                    con.commit()
                elif i==1 :
                    cur.execute("insert into friday values("+str(g[i])+",'"+h[i]+"','09:45:00','10:29:59')")
                    con.commit()
                elif i==2:
                    cur.execute("insert into friday values("+str(g[i])+",'"+h[i]+"','10:30:00','11:14:59')")
                    con.commit()
                elif i==3:
                    cur.execute("insert into friday values("+str(g[i])+",'"+h[i]+"','11:15:00','11:59:59')")
                    con.commit()
                elif i==4:
                    cur.execute("insert into friday values("+str(g[i])+",'"+h[i]+"','12:25:00','13:04:59')")
                    con.commit()
                elif i==5:
                    cur.execute("insert into friday values("+str(g[i])+",'"+h[i]+"','13:05:00','13:44:59')")
                    con.commit()
                elif i==6:
                    cur.execute("insert into friday values("+str(g[i])+",'"+h[i]+"','13:45:00','14:29:59')")
                    con.commit()
                elif i==7:
                    cur.execute("insert into friday values("+str(g[i])+",'"+h[i]+"','14:30:00','15:14:59')")
                    con.commit()
                elif i==8:
                    cur.execute("insert into friday values("+str(g[i])+",'"+h[i]+"','15:15:00','15:59:59')")
                    con.commit()
                i+=1

            
                
                
            print("your info saved succesfull\nnew database is created")
            os.system('pause')
            main()            
        except Exception as e:
            os.system('cls')
            ph()
            cur.execute("drop database "+fid)
            print("failed to create your database......")
            print("Exception caught :",e)
            main()
        
        
    elif x==2 :
        os.system('cls')
        ph()
        fid = str(input("PLEASE ENTER YOUR FACULTY ID NO. (for eg : ali001): \n"))

        try :
            con = mysql.connector.connect(user = 'root',password = 'root', host = '127.0.0.1',database = fid)
            cur = con.cursor()
            cur.execute("use "+fid)
            print("You are connected ...")
            os.system('pause')
            my_date=datetime.date.today()
            my_day = calendar.day_name[my_date.weekday()]
            time_c = datetime.datetime.now().time().replace(microsecond = 0)
           
            
            time_c=str(time_c)
            time_c=datetime.datetime.strptime(time_c,'%H:%M:%S')
            time_c=time_c.strftime('%H:%M:%S')
            
           
            
            
            if my_day == 'Monday':
                os.system('cls')
                ph()
                try:
                    cur.execute("select lecture,room from monday where ('"+time_c+"'>=start_time and '"+time_c+"'<=end_time)" )
                    l,r=cur.fetchone()
                    print("TIME : ",time_c)
                    print("DAY : ",my_day)
                    print("This is lecture no : ",l)
                    print("you have to be in room no. : ",r)

                except Exception as e:
                    print("WORKING TIME IS FROM 09:00 TO 04:00")
                   # print("Exception Caught : ",e)
                os.system('pause')
                main()
                

            elif my_day == 'Tuesday':
                os.system('cls')
                ph()
                try:
                    cur.execute("select lecture,room from tuesday where ('"+time_c+"'>=start_time and '"+time_c+"'<=end_time)" )
                    l,r=cur.fetchone()
                    print("TIME : ",time_c)
                    print("DAY : ",my_day)
                    print("This is lecture no : ",l)
                    print("you have to be in room no. : ",r)
                    
                except Exception as e:
                    print("WORKING TIME IS FROM 09:00 TO 04:00")
                    #print("Exception Caught : ",e)
                os.system('pause')
                main()

            elif my_day == 'Wednesday':
                os.system('cls')
                ph()
                try:
                    
                    cur.execute("select lecture,room from wednesday where ('"+time_c+"'>=start_time and '"+time_c+"'<=end_time)" )
                    l,r=cur.fetchone()
                    print("TIME : ",time_c)
                    print("DAY : ",my_day)
                    print("This is lecture no : ",l)
                    print("you have to be in room no. : ",r)

                except Exception as e:
                    print("WORKING TIME IS FROM 09:00 TO 04:00")
                    #print("Exception Caught : ",e)
                os.system('pause')
                main()

            elif my_day == 'Thursday':
                os.system('cls')
                ph()

                try:
                    cur.execute("select lecture,room from thusday where('"+time_c+"'>=start_time and '"+time_c+"'<=end_time)" )
                    l,r=cur.fetchone()
                    print("TIME : ",time_c)
                    print("DAY : ",my_day)
                    print("This is lecture no : ",l)
                    print("you have to be in room no. : ",r)
           
                

                except Exception as e:
                    print("WORKING TIME IS FROM 09:00 TO 04:00")
                    #print("Exception Caught : ",e)
                os.system('pause')
                main()

            elif my_day == 'Friday':
                os.system('cls')
                ph()

                try:
                    
                    cur.execute("select lecture,room from friday where ('"+time_c+"'>=start_time and '"+time_c+"'<=end_time)" )
                    l,r=cur.fetchone()
                    print("TIME : ",time_c)
                    print("DAY : ",my_day)
                    print("This is lecture no : ",l)
                    print("you have to be in room no. : ",r)

                except Exception as e:
                    print("WORKING TIME IS FROM 09:00 TO 04:00 \nWorking days are from MONDAY to FRIDAY ")
                    #print("Exception Caught : ",e)
                os.system('pause')
                main()
            else:
                time()
                print("WORKING TIME IS FROM 09:00 TO 04:00\nWorking days are from Monday to Friday")
                os.system('cls')
                main()

            
            

        except Exception as e:
            os.system('cls')
            ph()
            print("Exception caught : ",e)
            main()
            
                

    elif x==4:
        os.system('cls')
        ph()
        time()
        input("press enter to exit")
        exit()

    elif x==3:
        os.system('cls')
        ph()
        
        intro()
        
            
    else :
        os.system('cls')
        ph()
        x = input("YOU HAVE ENTERED A WRONG CHOICE \n Want to try again ? (y/n)")
        if x == ('y' or 'Y'):
            os.system('cls')
            main()
        elif x == ('n' or 'N'):
            os.system('cls')
            ph()
            time()
            
            print("Thank You")
            os.system('pause')
            exit()
    return
main()
