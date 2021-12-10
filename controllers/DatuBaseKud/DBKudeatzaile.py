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

        kurtsorea.execute("CREATE TABLE IF NOT EXISTS Entrenamendu (id int(10), mota varchar(50), dataEguna date, iraupena time, kmkop float(3),bestelakoDatuak varchar(100), PRIMARY KEY(id));")
        kurtsorea.execute("CREATE TABLE IF NOT EXISTS Segmentuak (izen varchar(30), hasi time, amaitu time, PRIMARY KEY(izen));")
        kurtsorea.execute("CREATE TABLE IF NOT EXISTS Ekipamendua (izen varchar(30), zapatilak varchar(30), erlojua varchar(30), bestelakoak varchar(100), PRIMARY KEY(izen) );")
        kurtsorea.execute("CREATE TABLE IF NOT EXISTS Medizioak (segundua time, posizioa varchar(50), abiadura int(3), pultsazioak int(3), bestelakoak varchar(50), entrenamenduId int(10),FOREIGN KEY(entrenamenduId) REFERENCES Entrenamendu (id) ON DELETE CASCADE);")
        kurtsorea.execute("CREATE TABLE IF NOT EXISTS Jarraitzaile (nickname varchar(30), PRIMARY KEY(nickname) );")
        kurtsorea.execute("CREATE TABLE IF NOT EXISTS Buelta (izen varchar(30), mota varchar(30), km float(3), denbora time,pultsazioak int(3), abiadura int(3), entrenamenduId int(10),FOREIGN KEY(entrenamenduId) REFERENCES Entrenamendu (id) ON DELETE CASCADE);")
        kurtsorea.execute("CREATE TABLE IF NOT EXISTS Kudo (jarraitzaileNickname varchar(30), entrenamenduId int(10), FOREIGN KEY(entrenamenduId) REFERENCES Entrenamendu (id), FOREIGN KEY(jarraitzaileNickname) REFERENCES Jarraitzaile (nickname) ON DELETE CASCADE);")
        kurtsorea.execute("CREATE TABLE IF NOT EXISTS Iruzkin (iruzkina varchar(100), jarraitzaileNickname varchar(30), entrenamenduId int(10), FOREIGN KEY(entrenamenduId) REFERENCES Entrenamendu (id), FOREIGN KEY(jarraitzaileNickname) REFERENCES Jarraitzaile (nickname) ON DELETE CASCADE);")
        kurtsorea.execute("CREATE TABLE IF NOT EXISTS Informazioa (denbora time, segmentuIzen varchar(30), entrenamenduId int(10) );")
        kurtsorea.execute("CREATE TABLE IF NOT EXISTS Erabili (ekipamenduIzen varchar(30), entrenamenduId int(10), FOREIGN KEY(entrenamenduId) REFERENCES Entrenamendu (id), FOREIGN KEY(ekipamenduIzen) REFERENCES Ekipamendua (izen) ON DELETE CASCADE);")

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
        if (kurtsorea.execute("SELECT * FROM Ekipamendua WHERE izen=%s",(id,))):
                kurtsorea.execute("UPDATE Ekipamendua SET zapatilak=%s, erlojua=%s, bestelakoak=%s WHERE id=%i;",(zapatila,erlojua,bestelakoak,id,))
                print("if barruan")
        else:
                kurtsorea.execute("INSERT INTO Ekipamendua VALUES (%s,%s,%s,%s)",(id,zapatila,erlojua,bestelakoak,))
                print("kanpo")

        print(kurtsorea.execute("SELECT * FROM Ekipamendua WHERE izen=%s",(id,)))


def segmentuaSartu(db, izen="we", hasi="we", amaitu="we"):
        kurtsorea = db.cursor(buffered=True)
        if (kurtsorea.execute("SELECT * FROM Segmentua WHERE izen=%s",(izen,))):
                kurtsorea.execute("UPDATE Segmentua SET hasi=%s, amaitu=%s WHERE izen = %s;",(hasi,amaitu,izen,))
                print("if barruan")
        else:
                kurtsorea.execute("INSERT INTO Segmentua VALUES (%s,%s,%s)",(izen,hasi,amaitu,))
                print("kanpo")

        print(kurtsorea.execute("SELECT * FROM Segmentua WHERE izen=%s",(izen,)))


def entrenamenduaSartu(db, id="we", mota="we", data="we", iraupena="we", km="we", bestelakoak="we"):
        kurtsorea = db.cursor(buffered=True)
        if (kurtsorea.execute("SELECT * FROM Entrenamendua WHERE id=%s",(id,))):
                kurtsorea.execute("UPDATE Entrenamendua SET mota=%s, data=%s, iraupena=%s, km=%s, bestelakoak=%s WHERE id = %s;",(mota, data, iraupena, km, bestelakoak,id,))
                print("if barruan")
        else:
                kurtsorea.execute("INSERT INTO Entrenamendua VALUES (%s,%s,%s,%s,%s,%s)",(id,mota, data, iraupena, km, bestelakoak,))
                print("kanpo")

        print(kurtsorea.execute("SELECT * FROM Entrenamendua WHERE id=%s",(id,)))


def medizioakSartu(db, segundua="we", posizioa="we", abiadura="we", pultsazioak="we", bestelakoak="we", entrenamenduId="we"):
        kurtsorea = db.cursor(buffered=True)
        if (kurtsorea.execute("SELECT * FROM Medizioak WHERE id=%s",(entrenamenduId,))):
                kurtsorea.execute("UPDATE Medizioak SET segundua=%s, posizioa=%s, abiadura=%s, pultsazioak=%s, bestelakoak=%s WHERE id = %s;",(segundua, posizioa, abiadura, pultsazioak, bestelakoak, entrenamenduId,))
                print("if barruan")
        else:
                kurtsorea.execute("INSERT INTO Medizioak VALUES (%s,%s,%s,%s,%s,%s)",(segundua, posizioa, abiadura, pultsazioak, bestelakoak, entrenamenduId,))
                print("kanpo")

        print(kurtsorea.execute("SELECT * FROM Medizioak WHERE id=%s",(entrenamenduId,)))


def jarraitzaileaSartu(db, nickname="we"):
        kurtsorea = db.cursor(buffered=True)
        kurtsorea.execute("UPDATE Jarraitzailea SET nickname=%s;",(nickname,))
        print(kurtsorea.execute("SELECT * FROM Jarraitzailea WHERE nickname=%s",(nickname,)))


def bueltaSartu(db, izen="we", mota="we", km="we", denbora="we",pultsazioak="we", abiadura="we", entrenamenduId="we"):
        kurtsorea = db.cursor(buffered=True)
        if (kurtsorea.execute("SELECT * FROM Buelta WHERE izen=%s",(izen,))):
                kurtsorea.execute("UPDATE Buelta SET mota=%s, km=%s, denbora=%s, pultsazioak=%s, abiadura=%s, entrenamenduId=%s WHERE izen = %s;",(mota, km, denbora,pultsazioak, abiadura, entrenamenduId,izen,))
                print("if barruan")
        else:
                kurtsorea.execute("INSERT INTO Buleta VALUES (%s,%s,%s,%s,%s,%s,%s)",(izen, mota, km, denbora,pultsazioak, abiadura, entrenamenduId,))
                print("kanpo")

        print(kurtsorea.execute("SELECT * FROM Buelta WHERE izen=%s",(izen,)))


def kudoSartu(db, jarraitzaileNickname="we", entrenamenduId="we"):
        kurtsorea = db.cursor(buffered=True)
        if (kurtsorea.execute("SELECT * FROM Kudo WHERE izen=%s AND id=%s",(jarraitzaileNickname,entrenamenduId,))):
                kurtsorea.execute("UPDATE Kudo SET hasi=%s, amaitu=%s WHERE izen = %s;",(hasi,amaitu,izen,))
                print("if barruan")
        else:
                kurtsorea.execute("INSERT INTO Segmentua VALUES (%s,%s,%s)",(izen,hasi,amaitu,))
                print("kanpo")

        print(kurtsorea.execute("SELECT * FROM Segmentua WHERE izen=%s",(izen,)))


def iruzkinSartu(db, iruzkina="we", jarraitzaileNickname="we", entrenamenduId="we"):
        kurtsorea = db.cursor(buffered=True)
        if (kurtsorea.execute("SELECT * FROM Iruzkina WHERE izen=%s AND id=%s",(jarraitzaileNickname,entrenamenduId,))):
                kurtsorea.execute("UPDATE Iruzkina SET iruzkina=%s WHERE izen=%s AND id=%s;",(iruzkina,jarraitzaileNickname,entrenamenduId,))
                print("if barruan")
        else:
                kurtsorea.execute("INSERT INTO Iruzkina VALUES (%s,%s,%s)",(iruzkina, jarraitzaileNickname, entrenamenduId,))
                print("kanpo")

        print(kurtsorea.execute("SELECT * FROM Iruzkina WHERE izen=%s AND id=%s",(jarraitzaileNickname,entrenamenduId,)))


def informazioaSartu(db, denbora="we", entrenamenduId="we", segmentuIzen="we"):
        kurtsorea = db.cursor(buffered=True)
        if (kurtsorea.execute("SELECT * FROM Informazioa WHERE id=%s AND izen=%s",(entrenamenduId,segmentuIzen,))):
                kurtsorea.execute("UPDATE Informazioa SET denbora=%s WHERE id=%s AND izen=%s;",(denbora,entrenamenduId,segmentuIzen,))
                print("if barruan")
        else:
                kurtsorea.execute("INSERT INTO Informazioa VALUES (%s,%s,%s)",(denbora,entrenamenduId,segmentuIzen,))
                print("kanpo")

        print(kurtsorea.execute("SELECT * FROM Informazioa WHERE id=%s AND izen=%s",(entrenamenduId,segmentuIzen,)))


def erabiliSartu(db, ekipamenduIzen="we", entrenamenduId="we"):
        kurtsorea = db.cursor(buffered=True)
        if (kurtsorea.execute("SELECT * FROM Erabili WHERE izen=%s AND id=%s",(ekipamenduIzen,entrenamenduId,))):
                print("if barruan")
        else:
                kurtsorea.execute("INSERT INTO Erabili VALUES (%s,%s)",(ekipamenduIzen,entrenamenduId,))
                print("kanpo")

        print(kurtsorea.execute("SELECT * FROM Erabili WHERE izen=%s AND id=%s",(ekipamenduIzen,entrenamenduId,)))

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


def windowManager():
        window = tk.Tk()
        window.title("STRAVA")
        window.geometry('800x500')

        botoia21 = tk.Button(window, text="API-tik informazioa irakurri")
        botoia22 = tk.Button(window, text="Insert", command=insertFuntzioa)
        botoia221 = tk.Button(window, text="Taulen informazioa ikusi", command=taulenInfoIkusi)
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

def insertFuntzioa():
        window =tk.Tk()
        window.title("Insert")
        window.geometry('300x100')
        textua = tk.Entry(window)
        textua.pack()
        #text = textua.get()
        #return text


def taulenInfoIkusi():
        window = tk.Tk()
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