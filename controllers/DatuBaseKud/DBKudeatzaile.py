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
        kurtsorea.execute("CREATE TABLE IF NOT EXISTS Ekipamendua (izen varchar(30), zapatilak varchar(30), erlojua varchar(30), bestelakoak varchar(100), PRIMARY KEY(izen));")
        kurtsorea.execute("CREATE TABLE IF NOT EXISTS Medizioak (segundua time, posizioa varchar(50), abiadura int(3), pultsazioak int(3), bestelakoak varchar(50), entrenamenduId int(10),FOREIGN KEY(entrenamenduId) REFERENCES Entrenamendu (id));")
        kurtsorea.execute("CREATE TABLE IF NOT EXISTS Jarraitzaile (nickname varchar(30), PRIMARY KEY(nickname));")
        kurtsorea.execute("CREATE TABLE IF NOT EXISTS Buelta (izen varchar(30), mota varchar(30), km float(3), denbora time,pultsazioak int(3), abiadura int(3), entrenamenduId int(10),FOREIGN KEY(entrenamenduId) REFERENCES Entrenamendu (id));")
        kurtsorea.execute("CREATE TABLE IF NOT EXISTS Kudo (jarraitzaileNickname varchar(30), entrenamenduId int(10), FOREIGN KEY(entrenamenduId) REFERENCES Entrenamendu (id), FOREIGN KEY(jarraitzaileNickname) REFERENCES Jarraitzaile (nickname));")
        kurtsorea.execute("CREATE TABLE IF NOT EXISTS Iruzkin (iruzkina varchar(100), jarraitzaileNickname varchar(30), entrenamenduId int(10), FOREIGN KEY(entrenamenduId) REFERENCES Entrenamendu (id), FOREIGN KEY(jarraitzaileNickname) REFERENCES Jarraitzaile (nickname));")
        kurtsorea.execute("CREATE TABLE IF NOT EXISTS Informazioa (denbora time, segmentuIzen varchar(30), entrenamenduId int(10));")
        kurtsorea.execute("CREATE TABLE IF NOT EXISTS Erabili (ekipamenduIzen varchar(30), entrenamenduId int(10), FOREIGN KEY(entrenamenduId) REFERENCES Entrenamendu (id), FOREIGN KEY(ekipamenduIzen) REFERENCES Ekipamendua (izen));")

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

def ekipamenduSartu(db,id,zapatila="we",erlojua="we",bestelakoak="we"):
        kurtsorea = db.cursor(buffered=True)
        if (kurtsorea.execute("SELECT * FROM Ekipamendua WHERE izen=%s",(id,))):
                kurtsorea.execute("UPDATE Ekipamendua SET zapatilak=%s, erlojua=%s, bestelakoak=%s WHERE id = %s;",(zapatila,erlojua,bestelakoak,id,))
                print("if barruan")
        else:
                kurtsorea.execute("INSERT INTO Ekipamendua VALUES (%s,%s,%s,%s)",(id,zapatila,erlojua,bestelakoak,))
                print("kanpo")

        print(kurtsorea.execute("SELECT * FROM Ekipamendua WHERE izen=%s",(id,)))