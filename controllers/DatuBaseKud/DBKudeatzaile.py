import mysql.connector

db = mysql.connector.connect(
        host="localhost",
        user= "strava",
        password="stravapassword123",
        database="strava"
)

kurtsorea = db.cursor()


if kurtsorea.execute("SHOW TABLES;"):
        kurtsorea.execute("CREATE TABLE Entrenamendu (id int(10), mota varchar(50), dataEguna date, iraupena time, kmkop float(3),bestelakoDatuak varchar(100), PRIMARY KEY(id));")
        kurtsorea.execute("CREATE TABLE Segmentuak (izen varchar(30), hasi time, amaitu time, PRIMARY KEY(izen));")
        kurtsorea.execute("CREATE TABLE Ekipamendua (izen varchar(30), zapatilak varchar(30), erlojua varchar(30), bestelakoak varchar(100), PRIMARY KEY(izen));")
        kurtsorea.execute("CREATE TABLE Medizioak (segundua time, posizioa varchar(50), abiadura int(3), pultsazioak int(3), bestelakoak varchar(50), entrenamenduId int(10),FOREIGN KEY(entrenamenduId) REFERENCES Entrenamendu (id));")
        kurtsorea.execute("CREATE TABLE Jarraitzaile (nickname varchar(30), PRIMARY KEY(nickname));")
        kurtsorea.execute("CREATE TABLE Buelta (izen varchar(30), mota varchar(30), km float(3), denbora time,pultsazioak int(3), abiadura int(3), entrenamenduId int(10),FOREIGN KEY(entrenamenduId) REFERENCES Entrenamendu (id));")
        kurtsorea.execute("CREATE TABLE Kudo (jarraitzaileNickname varchar(30), entrenamenduId int(10), FOREIGN KEY(entrenamenduId) REFERENCES Entrenamendu (id), FOREIGN KEY(jarraitzaileNickname) REFERENCES Jarraitzaile (nickname));")
        kurtsorea.execute("CREATE TABLE Iruzkin (iruzkina varchar(100), jarraitzaileNickname varchar(30), entrenamenduId int(10), FOREIGN KEY(entrenamenduId) REFERENCES Entrenamendu (id), FOREIGN KEY(jarraitzaileNickname) REFERENCES Jarraitzaile (nickname));")
        kurtsorea.execute("CREATE TABLE Informazioa (denbora time, segmentuIzen varchar(30), entrenamenduId int(10));")
        kurtsorea.execute("CREATE TABLE Erabili (ekipamenduIzen varchar(30), entrenamenduId int(10), FOREIGN KEY(entrenamenduId) REFERENCES Entrenamendu (id), FOREIGN KEY(ekipamenduIzen) REFERENCES Ekipamendua (izen));")


row=True
while row:
        row=kurtsorea.fetchall()
        print(row)
kurtsorea.execute("SHOW COLUMNS FROM Segmentuak;")
