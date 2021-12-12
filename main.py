from controllers.StravaAPI import stravaApiKud
from controllers.DatuBaseKud import DBKudeatzaile
import datetime
if __name__ == '__main__':
        print("Datubase konexioa.")
        db = DBKudeatzaile.konexioa()
        stravaApiKud.getAccessToTheAPI()
        print(stravaApiKud.getAthlete())
        print()
        print(stravaApiKud.getLoggedInAthleteActivities())
        print()
        emaitza = stravaApiKud.getLoggedInAthleteActivities()
        id = emaitza[0]["id"]
        print(stravaApiKud.getActivityById(id))
        entrenamendua=stravaApiKud.getActivityById(id)


#ENTRENAMENDUA----------------------------------
        print("Entrenamendua sortzen:")
        ide=(entrenamendua['id'])
        print("ID entrenamendu:",ide)
        tipo=entrenamendua['type']
        print("Mota:"+tipo)
        data=str(entrenamendua['start_date']).split('T')[0]
        print("Data:" +data)
        iraupen=str(datetime.timedelta(seconds=entrenamendua['elapsed_time']))
        print("Iraupen:" + iraupen)
        kilometroak=int(entrenamendua['distance']) / 1000
        print("Kilometroak:" , kilometroak)
        print("Bestelakoak:")
        kopia = ide
        DBKudeatzaile.entrenamenduaSartu(db,kopia,tipo,data,iraupen,kilometroak)


        print()
        print(stravaApiKud.getActivityStreams(id,keys=["time","distance"]))


        db = DBKudeatzaile.konexioa()
        DBKudeatzaile.taulakSortu(db)
        DBKudeatzaile.erakutsiTaulak(db)
        zapa=stravaApiKud.getAthlete()
        id = zapa["shoes"][0]["id"]

        DBKudeatzaile.hasierakoWindow()

#to no se pa que esta qui pero bueno....  yo pondria el codigo este arriba (fuck upv)

