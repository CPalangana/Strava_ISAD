import tkinter as tk
from tkinter import ttk

import mysql.connector


def konexioa():
        db = mysql.connector.connect(
                host="localhost",
                user= "strava",
                password="stravapassword123",
                database="strava"
        )
        return db


def taulakSortu(db):
        kurtsorea = db.cursor(buffered=True)

        kurtsorea.execute("CREATE TABLE IF NOT EXISTS Entrenamendu (id int(10), mota varchar(50), dataEguna date, "
                          "iraupena time, kmkop float(3),bestelakoDatuak varchar(100), PRIMARY KEY(id));")
        kurtsorea.execute("CREATE TABLE IF NOT EXISTS Segmentuak (izen varchar(30), hasi time, amaitu time, PRIMARY KEY(izen));")
        kurtsorea.execute("CREATE TABLE IF NOT EXISTS Ekipamendua (izen varchar(30), zapatilak varchar(30), erlojua varchar(30), bestelakoak varchar(100), PRIMARY KEY(izen) );")
        kurtsorea.execute("CREATE TABLE IF NOT EXISTS Medizioak (segundua time, posizioa varchar(50), abiadura int(3), pultsazioak int(3), bestelakoak varchar(50), entrenamenduId int(10),FOREIGN KEY(entrenamenduId) REFERENCES Entrenamendu (id) ON DELETE CASCADE);")
        kurtsorea.execute("CREATE TABLE IF NOT EXISTS Jarraitzaile (nickname varchar(30), PRIMARY KEY(nickname) );")
        kurtsorea.execute("CREATE TABLE IF NOT EXISTS Buelta (izen varchar(30), mota varchar(30), km float(3), denbora time,pultsazioak int(3), abiadura int(3), entrenamenduId int(10),FOREIGN KEY(entrenamenduId) REFERENCES Entrenamendu (id) ON DELETE CASCADE);")
        kurtsorea.execute("CREATE TABLE IF NOT EXISTS Kudo (jarraitzaileNickname varchar(30), entrenamenduId int(10), FOREIGN KEY(entrenamenduId) REFERENCES Entrenamendu (id), FOREIGN KEY(jarraitzaileNickname) REFERENCES Jarraitzaile (nickname) ON DELETE CASCADE);")
        kurtsorea.execute("CREATE TABLE IF NOT EXISTS Iruzkin (iruzkina varchar(100), jarraitzaileNickname varchar("
                          "30), entrenamenduId int(10), FOREIGN KEY(entrenamenduId) REFERENCES Entrenamendu (id), "
                          "FOREIGN KEY(jarraitzaileNickname) REFERENCES Jarraitzaile (nickname) ON DELETE CASCADE);")
        kurtsorea.execute("CREATE TABLE IF NOT EXISTS Informazioa (denbora time, segmentuIzen varchar(30), "
                          "entrenamenduId int(10) );")
        kurtsorea.execute("CREATE TABLE IF NOT EXISTS Erabili (ekipamenduIzen varchar(30), entrenamenduId int(10), "
                          "FOREIGN KEY(entrenamenduId) REFERENCES Entrenamendu (id), FOREIGN KEY(ekipamenduIzen) "
                          "REFERENCES Ekipamendua (izen) ON DELETE CASCADE);")

def erakutsiTaulak(db):
        kurtsorea = db.cursor()
        row=True
        lista=[]
        kurtsorea.execute("SHOW TABLES;")
        while row:
                row=kurtsorea.fetchone()
                if row:
                        print(row)
                        text=row[0]
                        lista.append(text)
                        print(text)

        for x in lista:
                kurtsorea.execute(f"SHOW COLUMNS FROM {x};")

                print(x, kurtsorea.fetchall())

                kurtsorea.execute("SELECT * FROM buelta WHERE izen=%s", (x,))

                print(x, kurtsorea.fetchall())

def ekipamenduaSartu(db,id='we',zapatila='we',erlojua='we',bestelakoak='we'):
        kurtsorea = db.cursor(buffered=True)
        kurtsorea.execute("SELECT * FROM ekipamendua WHERE izen=%s", (id,))
        if (kurtsorea.fetchone()):
                kurtsorea.execute("UPDATE ekipamendua SET zapatilak=%s, erlojua=%s, bestelakoak=%s WHERE id=%i;",(zapatila,erlojua,bestelakoak,id,))
                print("if barruan")
        else:
                kurtsorea.execute("INSERT INTO ekipamendua VALUES (%s,%s,%s,%s)",(id,zapatila,erlojua,bestelakoak,))
                print("kanpo")
        db.commit()
        print(kurtsorea.execute("SELECT * FROM ekipamendua WHERE izen=%s",(id,)))


def segmentuaSartu(db, izen="we", hasi="we", amaitu="we"):
        kurtsorea = db.cursor(buffered=True)
        kurtsorea.execute("SELECT * FROM segmentuak WHERE izen=%s", (izen,))
        if (kurtsorea.fetchone()):
                kurtsorea.execute("UPDATE Segmentuak SET hasi=%s, amaitu=%s WHERE izen = %s;",(hasi,amaitu,izen,))
                print("if barruan")
        else:
                kurtsorea.execute("INSERT INTO segmentuak VALUES (%s,%s,%s)",(izen,hasi,amaitu,))
                print("kanpo")
        db.commit()
        print(kurtsorea.execute("SELECT * FROM Segmentuak WHERE izen=%s",(izen,)))


def entrenamenduaSartu(db, id=1, mota="we", data="2000/12/12", iraupena="06:00:00.000000", km=12.0, bestelakoak="we"):
        kurtsorea = db.cursor(buffered=True)
        kurtsorea.execute("SELECT * FROM entrenamendu WHERE id=%s", (id,))
        if (kurtsorea.fetchone()):
                kurtsorea.execute("UPDATE entrenamendu SET mota=%s, dataEguna=%s, iraupena=%s, kmkop=%s, bestelakoDatuak=%s WHERE id = %s;",(mota, data, iraupena, km, bestelakoak,id,))
                print("if barruan")
        else:
                kurtsorea.execute("INSERT INTO entrenamendu VALUES (%s,%s,%s,%s,%s,%s)",(id,mota, data, iraupena, km, bestelakoak,))
                print("kanpo")
        db.commit()
        kurtsorea.execute("SELECT * FROM entrenamendu WHERE id=%s", (id,))
        print(kurtsorea.fetchone())


def medizioakSartu(db, segundua="we", posizioa="we", abiadura="we", pultsazioak="we", bestelakoak="we", entrenamenduId="we"):
        kurtsorea = db.cursor(buffered=True)
        kurtsorea.execute("SELECT * FROM medizioak WHERE id=%s", (entrenamenduId,))
        if (kurtsorea.fetchone()):
                kurtsorea.execute("UPDATE medizioak SET segundua=%s, posizioa=%s, abiadura=%s, pultsazioak=%s, bestelakoak=%s WHERE id = %s;",(segundua, posizioa, abiadura, pultsazioak, bestelakoak, entrenamenduId,))
                print("if barruan")
        else:
                kurtsorea.execute("INSERT INTO medizioak VALUES (%s,%s,%s,%s,%s,%s)",(segundua, posizioa, abiadura, pultsazioak, bestelakoak, entrenamenduId,))
                print("kanpo")
        db.commit()
        print(kurtsorea.execute("SELECT * FROM medizioak WHERE id=%s",(entrenamenduId,)))


def jarraitzaileaSartu(db, nickname="we"):
        kurtsorea = db.cursor(buffered=True)
        kurtsorea.execute("SELECT * FROM Jarraitzailea WHERE nickname=%s",(nickname,))
        if (kurtsorea.fetchone()):
                kurtsorea.execute("INSERT INTO jarraitzaile VALUES (%s)",(nickname,))
        else:
                kurtsorea.execute("UPDATE Jarraitzailea SET nickname=%s;",(nickname,))
        db.commit()

def bueltaSartu(db, izen="we", mota="we", km="we", denbora="we",pultsazioak="we", abiadura="we", entrenamenduId="we"):
        kurtsorea = db.cursor(buffered=True)
        kurtsorea.execute("SELECT * FROM buelta WHERE izen=%s", (izen,))
        if (kurtsorea.fetchone()):
                kurtsorea.execute("UPDATE buelta SET mota=%s, km=%s, denbora=%s, pultsazioak=%s, abiadura=%s, entrenamenduId=%s WHERE izen = %s;",(mota, km, denbora,pultsazioak, abiadura, entrenamenduId,izen,))
                print("if barruan")
        else:
                kurtsorea.execute("INSERT INTO buelta VALUES (%s,%s,%s,%s,%s,%s,%s)",(izen, mota, km, denbora,pultsazioak, abiadura, entrenamenduId,))
                print("kanpo")
        db.commit()
        print(kurtsorea.execute("SELECT * FROM buelta WHERE izen=%s",(izen,)))


def kudoSartu(db, jarraitzaileNickname="we", entrenamenduId="we"):
        kurtsorea = db.cursor(buffered=True)
        kurtsorea.execute("SELECT * FROM kudo WHERE jarraitzaileNickname=%s AND entrenamenduId=%s", (jarraitzaileNickname, entrenamenduId,))
        if (not(kurtsorea.fetchone())):
                kurtsorea.execute("INSERT INTO kudo VALUES (%s,%s)",(jarraitzaileNickname, entrenamenduId,))

        db.commit()


def iruzkinSartu(db, iruzkina="we", jarraitzaileNickname="we", entrenamenduId="we"):
        kurtsorea = db.cursor(buffered=True)
        kurtsorea.execute("SELECT * FROM iruzkina WHERE jarraitzaileNickname=%s AND entrenamenduId=%s",(jarraitzaileNickname, entrenamenduId,))
        if (kurtsorea.fetchone()):
                kurtsorea.execute("UPDATE iruzkina SET iruzkina=%s WHERE jarraitzaileNickname=%s AND entrenamenduId=%s",(iruzkina,jarraitzaileNickname,entrenamenduId,))
                print("if barruan")
        else:
                kurtsorea.execute("INSERT INTO iruzkina VALUES (%s,%s,%s)",(iruzkina, jarraitzaileNickname, entrenamenduId,))
                print("kanpo")
        db.commit()



def informazioaSartu(db, denbora="we", entrenamenduId="we", segmentuIzen="we"):
        kurtsorea = db.cursor(buffered=True)
        kurtsorea.execute("SELECT * FROM informazioa WHERE entrenamenduId=%s AND segmentuIzen=%s", (entrenamenduId, segmentuIzen,))
        if (kurtsorea.fetchone()):
                kurtsorea.execute("UPDATE informazioa SET denbora=%s WHERE entrenamenduId=%s AND segmentuIzen=%s",(denbora,entrenamenduId,segmentuIzen,))
                print("if barruan")
        else:
                kurtsorea.execute("INSERT INTO informazioa VALUES (%s,%s,%s)",(denbora,entrenamenduId,segmentuIzen,))
                print("kanpo")
        db.commit()


def erabiliSartu(db, ekipamenduIzen="we", entrenamenduId="we"):
        kurtsorea = db.cursor(buffered=True)
        kurtsorea.execute("SELECT * FROM erabili WHERE ekipamenduIzen=%s AND entrenamenduId=%s",(ekipamenduIzen, entrenamenduId,))
        if (kurtsorea.fetchone()):
                print("if barruan")
        else:
                kurtsorea.execute("INSERT INTO erabili VALUES (%s,%s)",(ekipamenduIzen,entrenamenduId,))
                print("kanpo")
        db.commit()


def hasierakoWindow():
        window = tk.Tk()
        window.title("Hasiera")
        window.geometry('300x200')

        etiketa = tk.Label(window, text="STRAVA", font=("Helvetica", 20, 'bold'), bg="Green")
        etiketa.pack()

        etiketa2 = tk.Label(window, text="Aplikazioa hasieratzeko beheko botoian klik egin")
        botoia1 = tk.Button(window, text="Aplikazioa hasieratu", command=windowManager)
        espacio = tk.Label(window)
        espacio.pack()
        etiketa2.pack()
        botoia1.pack()

        window.mainloop()


def windowManager(win=None):
        if win==None:
                window = tk.Tk()
        else:
                window=win
        window.title("STRAVA")
        window.geometry('800x500')

        botoia21 = tk.Button(window, text="API-tik informazioa irakurri")
        botoia22 = tk.Button(window, text="Insert", command=lambda:insertFuntzioa(window))
        botoia221 = tk.Button(window, text="Taulen informazioa ikusi", command=lambda:taulenInfoIkusi(window))
        botoia23 = tk.Button(window, text="Eguneratu", command=update)
        botoia24 = tk.Button(window, text="Datuak bistaratu", command=datuakBistaratu)

        botoia21.pack()
        botoia22.pack()
        botoia221.pack()
        botoia23.pack()
        botoia24.pack()

        botoia21.place(x=0, y=0, height=100, width=800)
        botoia22.place(x=0, y=100, height=100, width=800)
        botoia221.place(x=0,y=200, height=100, width=800)
        botoia23.place(x=0, y=300, height=100, width=800)
        botoia24.place(x=0, y=400, height=100, width=800)

        window.mainloop()

def insertFuntzioa(win):
        for widgets in win.winfo_children():
                widgets.destroy()
        window =win
        window.title("Insert")
        window.geometry('300x200')

        botoiaI1 = tk.Button(window, text="Entrenamendua",command=lambda:insertEntrenamendu(window))
        botoiaI2 = tk.Button(window, text="Segmentua",command=lambda:insertSegmentua(window))
        botoiaI3 = tk.Button(window, text="Ekipamendua",command=lambda:insertEkipamendua(window))
        botoiaI4 = tk.Button(window, text="Buelta", command=lambda: insertBuelta(window))
        botoiaIB = tk.Button(window, text="Atzera", command=lambda: windowManager(window))
        botoiaI1.pack()
        botoiaI2.pack()
        botoiaI3.pack()
        botoiaI4.pack()
        botoiaIB.pack()
        #text = textua.get()
        #return text

def insertEntrenamendu(win):
        for widgets in win.winfo_children():
                widgets.destroy()
        window =win

        window.title("InsertEntrenamendu ")
        window.geometry('300x300')

        textua1 = tk.Entry(window)
        etiketa1 = tk.Label(window, text="Id")
        textua2 = tk.Entry(window)
        etiketa2 = tk.Label(window, text="Mota")
        textua3 = tk.Entry(window)
        etiketa3 = tk.Label(window, text="Data")
        textua4 = tk.Entry(window)
        etiketa4 = tk.Label(window, text="Iraupen")
        textua5 = tk.Entry(window)
        etiketa5 = tk.Label(window, text="Kilometroak")
        textua6 = tk.Entry(window)
        etiketa6 = tk.Label(window, text="Bestelakoak")

        etiketa1.pack()
        textua1.pack()
        etiketa2.pack()
        textua2.pack()
        etiketa3.pack()
        textua3.pack()
        etiketa4.pack()
        textua4.pack()
        etiketa5.pack()
        textua5.pack()
        etiketa6.pack()
        textua6.pack()


        botoiaI1 = tk.Button(window, text="Insert", command=lambda:entrenamenduaSartu(konexioa(),textua1.get(),textua2.get(),textua3.get(),textua4.get(),textua5.get(),textua6.get()))
        botoiaI2 = tk.Button(window, text="Atzera", command=lambda:insertFuntzioa(window))

        botoiaI1.pack()
        botoiaI2.pack()
        window.mainloop()
        #text = textua.get()
        #return text

def insertSegmentua(win):
        for widgets in win.winfo_children():
                widgets.destroy()
        window = win

        window.title("InsertEntrenamendu ")
        window.geometry('300x300')

        textua1 = tk.Entry(window)
        etiketa1 = tk.Label(window, text="Izena")
        textua2 = tk.Entry(window)
        etiketa2 = tk.Label(window, text="Hasiera")
        textua3 = tk.Entry(window)
        etiketa3 = tk.Label(window, text="Amaiera")

        etiketa1.pack()
        textua1.pack()
        etiketa2.pack()
        textua2.pack()
        etiketa3.pack()
        textua3.pack()

        botoiaI1 = tk.Button(window, text="Insert",
                             command=lambda: segmentuaSartu(konexioa(), textua1.get(), textua2.get(), textua3.get()))
        botoiaI2 = tk.Button(window, text="Atzera", command=lambda: insertFuntzioa(window))

        botoiaI1.pack()
        botoiaI2.pack()
        window.mainloop()
        # text = textua.get()
        # return text
def insertBuelta(win):
        for widgets in win.winfo_children():
                widgets.destroy()
        window = win

        window.title("InsertBuelta ")
        window.geometry('300x300')

        textuaK = tk.Entry(window)
        etiketaK = tk.Label(window, text="Id")
        textua1 = tk.Entry(window)
        etiketa1 = tk.Label(window, text="Izena")
        textua2 = tk.Entry(window)
        etiketa2 = tk.Label(window, text="Mota")
        textua3 = tk.Entry(window)
        etiketa3 = tk.Label(window, text="km")
        textua4 = tk.Entry(window)
        etiketa4 = tk.Label(window, text="Denbora")
        textua5 = tk.Entry(window)
        etiketa5 = tk.Label(window, text="Pultsazioak")
        textua6 = tk.Entry(window)
        etiketa6 = tk.Label(window, text="abiadura")

        etiketaK.pack()
        textuaK.pack()
        etiketa1.pack()
        textua1.pack()
        etiketa2.pack()
        textua2.pack()
        etiketa3.pack()
        textua3.pack()
        etiketa4.pack()
        textua4.pack()
        etiketa5.pack()
        textua5.pack()
        etiketa6.pack()
        textua6.pack()

        botoiaI1 = tk.Button(window, text="Insert",
                             command=lambda: bueltaSartu(konexioa(), textua1.get(), textua2.get(), textua3.get(),
                                                                textua4.get(), textua5.get(), textua6.get(),textuaK.get()))
        botoiaI2 = tk.Button(window, text="Atzera", command=lambda: insertFuntzioa(window))

        botoiaI1.pack()
        botoiaI2.pack()
        window.mainloop()
        # text = textua.get()
        # return text

def insertEkipamendua(win):
        for widgets in win.winfo_children():
                widgets.destroy()
        window = win

        window.title("InsertEntrenamendu ")
        window.geometry('300x300')

        textua1 = tk.Entry(window)
        etiketa1 = tk.Label(window, text="izen")
        textua2 = tk.Entry(window)
        etiketa2 = tk.Label(window, text="zapatilak")
        textua3 = tk.Entry(window)
        etiketa3 = tk.Label(window, text="erlojua")
        textua4 = tk.Entry(window)
        etiketa4 = tk.Label(window, text="bestelakoak")

        etiketa1.pack()
        textua1.pack()
        etiketa2.pack()
        textua2.pack()
        etiketa3.pack()
        textua3.pack()
        etiketa4.pack()
        textua4.pack()

        botoiaI1 = tk.Button(window, text="Insert",
                command=lambda: ekipamenduaSartu(konexioa(), textua1.get(), textua2.get(),
                                                                        textua3.get(),
                                                                        textua4.get()))
        botoiaI2 = tk.Button(window, text="Atzera", command=lambda: insertFuntzioa(window))

        botoiaI1.pack()
        botoiaI2.pack()
        window.mainloop()
                # text = textua.get()
                # return text
def taulenInfoIkusi(win):
        window = win
        window.title("Taulen informazioa")

        goiburuak = ["Taula","Atributua","Mota"]
        datuak = [
                ["Entrenamendu","id","int"],["Entrenamendu","mota","varchar"],
                ["Entrenamendu","data","date"],["Entrenamendu","iraupena","time"],
                ["Entrenamendu","kmkop","int"],["Entrenamendu","bestelakoDatuak","varchar"],
                ["Segmentuak", "izena", "varchar"],["Segmentuak", "hasi", "time"],
                ["Segmentuak", "amaitu", "time"],
                ["Ekipamendua", "izen", "varchar"],["Ekipamendua", "zapatilak", "varchar"],
                ["Ekipamendua", "erlojua", "varchar"],["Ekipamendua", "bestelakoak", "varchar"],
                ["Medizioak", "segundua", "time"],["Medizioak", "posizioa", "int"],
                ["Medizioak", "abiadura", "int"],["Medizioak", "pultsazioak", "varchar"],
                ["Medizioak", "bestelakoak", "varchar"],["Medizioak", "entrenamenduId", "int"],
                ["Jarraitzaile", "nickname", "varchar"],
                ["Buelta", "izena", "varchar"],["Buelta", "mota", "varchar"],
                ["Buelta", "km", "int"],["Buelta", "denbora", "time"],
                ["Buelta", "pultsazio", "int"],["Buelta", "abiadura", "int"],
                ["Buelta", "entrenamentuId", "int"],
                ["Kudo", "jarraitzaileNickname", "varchar"],["Kudo", "entrenamenduId", "int"],
                ["Iruzkin", "iruzkina", "varchar"],["Iruzkin", "nickname", "varchar"],
                ["Iruzkin", "entrenamenduId", "int"],
                ["Informazioa", "denbora", "time"],["Informazioa", "segmentuIzen", "varchar"],
                ["Informazioa", "entrenamenduId", "int"],
                ["Erabili", "ekipamenduIzen", "varchar"],["Erabili", "entrenamenduId", "int"]
                ]

        window.taula = ttk.Treeview(window,columns=(0,1,2),show='headings')

        for i,g in enumerate(goiburuak):
                window.taula.column(f"#{i}",minwidth=0,width=100)
                window.taula.heading(i,text=g)

        for i,d in enumerate(datuak):
                window.taula.insert(parent='',index=i,iid=i,values=d)

        window.taula.pack()
        window.mainloop()


def update():
        #db = konexioa()
        # ekipamenduaSartu(db)
        #segmentuaSartu(db)
        #entrenamenduaSartu(db)
        #medizioakSartu(db)
        #jarraitzaileaSartu(db)
        #bueltaSartu(db)
        #kudoSartu(db)
        #iruzkinSartu(db)
        #informazioaSartu(db)
        #erabiliSartu(db)
      print("update egin da")

def datuakBistaratu():
        window = tk.Tk()
        window.title("Strava hasiera")
        window.geometry('600x500')

        botoia1 = tk.Button(window, text="Datuak eguneratu")
        botoia2 = tk.Button(window, text="Ekipamendua ikusi", command=ekipamenduInfo)

        botoia1.pack()
        botoia2.pack()

        goiburuak = ["Izena", "Hasi", "Iraun", "Mota"]
        datuak = []

        window.taula = ttk.Treeview(window, columns=(0, 1, 2, 3), show='headings')

        for i,g in enumerate(goiburuak):
                window.taula.column(f"#{i}",minwidth=0,width=100)
                window.taula.heading(i,text=g)

        for i,d in enumerate(datuak):
                window.taula.insert(parent='',index=i,iid=i,values=d)

        textua = tk.Entry(window)
        etiketa = tk.Label(window, text="Data bidezko bilaketa egin")
        etiketa.pack()
        textua.pack()

        textua2 = tk.Entry(window)
        etiketa2 = tk.Label(window, text="Mota bidezko bilaketa egin")
        etiketa2.pack()
        textua2.pack()

        etiketa3 = tk.Label(window)
        etiketa3.pack()

        window.taula.pack()
        window.mainloop()

        #text = textua.get()
        #return text

def ekipamenduInfo():
        window = tk.Tk()
        window.title("Ekipamenduen informazioa")
        window.geometry('700x300')

        goiburuak = ["Izena", "Ezizena", "Distantzia"]
        datuak = []

        window.taula = ttk.Treeview(window, columns=(0, 1, 2), show='headings')

        for i, g in enumerate(goiburuak):
                window.taula.column(f"#{i}", minwidth=0, width=200)
                window.taula.heading(i, text=g)

        for i,d in enumerate(datuak):
                window.taula.insert(parent='',index=i,iid=i,values=d)

        window.taula.pack()
        window.mainloop()


#def nireTopLevel():
        #new_window = tk.Toplevel()