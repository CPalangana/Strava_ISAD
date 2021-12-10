from controllers.StravaAPI import stravaApiKud
from controllers.DatuBaseKud import DBKudeatzaile

if __name__ == '__main__':
        db = DBKudeatzaile.konexioa()
        DBKudeatzaile.hasierakoWindow()

else:
        #esto no se pa que esta qui pero bueno....  yo pondria el codigo este arriba
        stravaApiKud.getAccessToTheAPI()
        print(stravaApiKud.getAthlete())
        print()
        print(stravaApiKud.getLoggedInAthleteActivities())
        print()
        emaitza = stravaApiKud.getLoggedInAthleteActivities()
        id= emaitza[0]["id"]
        print(stravaApiKud.getActivityById(id))
        print()
        print(stravaApiKud.getActivityStreams(id,keys=["time","distance"]))
        print()
        db = DBKudeatzaile.konexioa()
        DBKudeatzaile.taulakSortu(db)
        DBKudeatzaile.erakutsiTaulak(db)
        zapa=stravaApiKud.getAthlete()
        id = zapa["shoes"][0]["id"]
        DBKudeatzaile.ekipamenduSartu(db)

