import mysql.connector
import tkinter as tk


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

        kurtsorea.execute("CREATE TABLE IF NOT EXISTS Entrenamendu (id int(10), mota varchar(50), dataEguna date, iraupena time, kmkop float(3),bestelakoDatuak varchar(100), PRIMARY KEY(id) ON DELETE CASCADE);")
        kurtsorea.execute("CREATE TABLE IF NOT EXISTS Segmentuak (izen varchar(30), hasi time, amaitu time, PRIMARY KEY(izen) ON DELETE CASCADE);")
        kurtsorea.execute("CREATE TABLE IF NOT EXISTS Ekipamendua (izen varchar(30), zapatilak varchar(30), erlojua varchar(30), bestelakoak varchar(100), PRIMARY KEY(izen) ON DELETE CASCADE);")
        kurtsorea.execute("CREATE TABLE IF NOT EXISTS Medizioak (segundua time, posizioa varchar(50), abiadura int(3), pultsazioak int(3), bestelakoak varchar(50), entrenamenduId int(10),FOREIGN KEY(entrenamenduId) REFERENCES Entrenamendu (id) ON DELETE CASCADE);")
        kurtsorea.execute("CREATE TABLE IF NOT EXISTS Jarraitzaile (nickname varchar(30), PRIMARY KEY(nickname) ON DELETE CASCADE);")
        kurtsorea.execute("CREATE TABLE IF NOT EXISTS Buelta (izen varchar(30), mota varchar(30), km float(3), denbora time,pultsazioak int(3), abiadura int(3), entrenamenduId int(10),FOREIGN KEY(entrenamenduId) REFERENCES Entrenamendu (id) ON DELETE CASCADE);")
        kurtsorea.execute("CREATE TABLE IF NOT EXISTS Kudo (jarraitzaileNickname varchar(30), entrenamenduId int(10), FOREIGN KEY(entrenamenduId) REFERENCES Entrenamendu (id), FOREIGN KEY(jarraitzaileNickname) REFERENCES Jarraitzaile (nickname) ON DELETE CASCADE);")
        kurtsorea.execute("CREATE TABLE IF NOT EXISTS Iruzkin (iruzkina varchar(100), jarraitzaileNickname varchar(30), entrenamenduId int(10), FOREIGN KEY(entrenamenduId) REFERENCES Entrenamendu (id), FOREIGN KEY(jarraitzaileNickname) REFERENCES Jarraitzaile (nickname) ON DELETE CASCADE);")
        kurtsorea.execute("CREATE TABLE IF NOT EXISTS Informazioa (denbora time, segmentuIzen varchar(30), entrenamenduId int(10) ON DELETE CASCADE);")
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
        if (kurtsorea.execute("SELECT * FROM Ekipamendua WHERE izen=%i",(id,))):
                kurtsorea.execute("UPDATE Ekipamendua SET zapatilak=%s, erlojua=%s, bestelakoak=%s WHERE id=%i;",(zapatila,erlojua,bestelakoak,id,))
                print("if barruan")
        else:
                kurtsorea.execute("INSERT INTO Ekipamendua VALUES (%i,%s,%s,%s)",(id,zapatila,erlojua,bestelakoak,))
                print("kanpo")

        print(kurtsorea.execute("SELECT * FROM Ekipamendua WHERE id=%i",(id,)))


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


def update(db):
      ekipamenduaSartu(db)
       # segmentuaSartu(db)
        #entrenamenduaSartu(db)
       # medizioakSartu(db)
        #jarraitzaileaSartu(db)
        #bueltaSartu(db)
        #kudoSartu(db)
        #iruzkinSartu(db)
        #informazioaSartu(db)
        #erabiliSartu(db)
        print("update egin da")


def windowManager():
        db2 = konexioa()
        window = tk.Tk()
        window.title("STRAVA")
        window.geometry('500x400')

        # Widgeta definitu
        testua = tk.Label(window, text="Aplikazioa eguneratzeko hurrengo botoia sakatu")
        botoia = tk.Button(window, text="Eguneratu", command=update(db2))

        # widgeta bistaratu
        testua.pack()
        botoia.pack()
        window.mainloop()
