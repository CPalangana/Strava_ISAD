import mysql.connector

db = mysql.connector.connect(
        host="localhost",
        user= "strava",
        password="stravapassword123",
        database="strava"
)

kurtsorea = db.cursor()
kurtsorea.execute("SHOW DATABASES")
row=True
while row:
        row=kurtsorea.fetchall()
        print(row)

kurtsorea.execute("SHOW COLUMNS FROM Segmentuak;")