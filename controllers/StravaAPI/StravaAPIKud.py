import json
import sys

import time
import urllib3
import webbrowser


class StravaAPIKud:
    host = "https://www.strava.com/api/v3"

    def __init__(self):
        print(sys.path)
        with open("StravaConfig.json") as f:
            self.stravaConfig = json.load(f)
        self.http = urllib3.PoolManager()

    def setConfigurationProperty(self, key, value):
        self.stravaConfig[key] = value
        with open("StravaConfig.json", 'w') as outfile:
            json.dump(self.stravaConfig, outfile, indent=4, sort_keys=True)

    def getAccessToTheAPI(self):
        if 'code' not in self.stravaConfig:
            print("Aplikazioari baimena eskatu")

            url = "http://www.strava.com/oauth/authorize?" + \
                  "client_id=" + str(self.stravaConfig.get('ClientID')) + \
                  "&response_type=code" + \
                  "&redirect_uri=http://localhost/" + \
                  "&approval_prompt=auto" + \
                  "&scope=read_all,profile:read_all,activity:read_all"

            webbrowser.open(url)
            print("Nabigatzailean stravako datuak eskatzeko baimena agertuko da. Baimenak eman eta gero, localhost serbitzarira eskaera bat egingo da. Zerbitzaria sortu ez dugunez, urlean dagoen 'code' parametro kopiatu eta 'StravaConfig.json' fitxategian sartu.")
            quit()

        expires = self.stravaConfig.get("expires_at", None)

        if expires is None or expires < time.time():
            print("sarbidea berritzen")

            parametroak = {
                "client_id": self.stravaConfig.get("ClientID"),
                "client_secret": self.stravaConfig.get("ClientSecret")
            }
            if expires is None:
                print("authorization_code")
                parametroak["code"] = self.stravaConfig.get("code")
                parametroak["grant_type"] = "authorization_code"
            else:
                print("refresh_token")
                parametroak["grant_type"] = "refresh_token"
                parametroak["refresh_token"] = self.stravaConfig.get("refresh_token")

            url = "https://www.strava.com/oauth/token"
            resp = self.http.request('POST', url, fields=parametroak)
            result = json.loads(resp.data)
            if 'errors' in result:
                del self.stravaConfig['code']
                self.getAccessToTheAPI()
                return
            self.setConfigurationProperty("access_token", result["access_token"])
            self.setConfigurationProperty("refresh_token", result["refresh_token"])
            self.setConfigurationProperty("expires_at", result["expires_at"])
            self.setConfigurationProperty("token_type", result["token_type"])

    def tojson(func):
        def wrapper(self, *args, **kwargs):
            goiburu_berriak = {
                "Authorization": "Bearer " + self.stravaConfig["access_token"],
                "Content-Type": "application/json"
            }
            if "goiburuak" in kwargs:
                kwargs['goiburuak'].update(goiburu_berriak)
            else:
                kwargs['goiburuak'] = goiburu_berriak
            em = func(self, *args, **kwargs)
            return json.loads(em.data)

        return wrapper

    @tojson
    def getAthlete(self, goiburuak={}):
        return self.http.request('GET', self.host + "/athlete", None, goiburuak)


    @tojson
    def getLoggedInAthleteActivities(self, before=None, after=None, page=1, per_page=30, goiburuak={}):
        hiztegia={
            "page": page,
            "per_page": per_page
        }
        if before != None:
            hiztegia["before"]= before

        if after != None:
            hiztegia["after"]= after

        return self.http.request('GET', self.host + "/athlete/activities", hiztegia, goiburuak)

    @tojson
    def getActivityById(self, id, include_all_efforts=None, goiburuak={}):
        hiztegia={}

        if include_all_efforts != None:
            hiztegia["include_all_efforts"]= include_all_efforts

        return self.http.request('GET', self.host + "/activities/"+ str(id),hiztegia, goiburuak)


    @tojson
    def getActivityStreams(self, id, keys=None, key_by_type=True, goiburuak={}):
        hiztegia={
            "key_by_type": key_by_type
        }

        if keys != None:
            hiztegia["keys"]= ','.join(keys)

        return self.http.request('GET', self.host + f"/activities/{id}/streams", hiztegia, goiburuak)
