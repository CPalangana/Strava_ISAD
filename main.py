from controllers.StravaAPI import stravaApiKud
from controllers.DatuBaseKud import DBKudeatzaile


if __name__ == '__main__':
    stravaApiKud.getAccessToTheAPI()
    print(stravaApiKud.getAthlete())
    print(stravaApiKud.getLoggedInAthleteActivities())
    emaitza = stravaApiKud.getLoggedInAthleteActivities()
    id= emaitza[0]["id"]
    print(stravaApiKud.getActivityById(id))
    print(stravaApiKud.getActivityStreams(id,keys=["time","distance"]))

