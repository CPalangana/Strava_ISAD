from controllers.StravaAPI import stravaApiKud
from controllers.DatuBaseKud import DBKudeatzaile
import datetime
if __name__ == '__main__':

        print("Datubase konexioa.")
        db = DBKudeatzaile.konexioa()
        DBKudeatzaile.taulakSortu(db)
        stravaApiKud.getAccessToTheAPI()
        print(stravaApiKud.getAthlete())
        print()
        print(stravaApiKud.getLoggedInAthleteActivities())
        print()
        emaitza = stravaApiKud.getLoggedInAthleteActivities()
        id = emaitza[0]["id"]
        print(stravaApiKud.getActivityById(id))
        entrenamendua=stravaApiKud.getActivityById(id)
        cont=0

        for e in emaitza:
            #ENTRENAMENDUA----------------------------------
                print("")
                print("Entrenamendua sortzen:")
                ide=(e['id'])
                print("ID entrenamendu:",ide)
                tipo=entrenamendua['type']
                print("Mota:"+tipo)
                data=str(e['start_date']).split('T')[0]
                print("Data:" +data)
                iraupen=str(datetime.timedelta(seconds=e['elapsed_time']))
                print("Iraupen:" + iraupen)
                kilometroak=int(e['distance']) / 1000
                print("Kilometroak:" , kilometroak)
                print("Bestelakoak:")
                kopia = ide
                print("ID-a aldatu egin da. Ezin dugu zenbaki handiak jarri.")
                DBKudeatzaile.entrenamenduaSartu(db,cont,tipo,data,iraupen,kilometroak)

            #Medizioak-------------------------------------
                print("")
                pos=e['start_latlng']
                print("Posizioa:",pos)
                abiadura=e['average_speed']
                print("Abiadura:",abiadura)
                if e['has_heartrate'] is False:
                    e['average_heartrate'] = 0.0
                pults=e['average_heartrate']
                print("Pultsazio:",pults)
                entrenaId=e["id"]
                print("ID:",entrenaId)
                bestelakoak="none"
                latilng=' '.join(str(f) for f in e['start_latlng'])
                DBKudeatzaile.medizioakSartu(db,iraupen,latilng,abiadura,int(pults),bestelakoak,cont)

            #Segmentuak--------------------------------------------------------------------------------------
                eId = stravaApiKud.getActivityById(e["id"])
                if not eId['segment_efforts']:
                    print("Hutsik")
                else:
                    izen=eId['segment_efforts'][0]['name']
                    print("Izen:",izen)
                    hasi=str(eId['start_date']).split('T')[1]
                    hasi2=hasi.split('Z')[0]
                    print("Hasi:",hasi2)
                    amaitu=eId['elapsed_time']
                    print("Amaitu:",amaitu)
                    if (izen=="stroomversnelling op de Ardèche"):
                        print("Arazoak ditugu stroomversnelling op de Ardèche sartzerakoan")
                    else:
                        DBKudeatzaile.segmentuaSartu(db,izen,hasi,amaitu)
                cont += 1

        DBKudeatzaile.hasierakoWindow()

#to no se pa que esta qui pero bueno....  yo pondria el codigo este arriba (fuck upv)
#https://www.youtube.com/watch?v=dQw4w9WgXcQ&ab_channel=RickAstley

