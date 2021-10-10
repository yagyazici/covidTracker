import os,requests,json
os.system("cls")
class CoronaStats(object):
    def __init__(self):
        self.countries_url = "https://disease.sh/v3/covid-19/countries"
        self.world_url = "https://disease.sh/v3/covid-19/all"
    def countryStats(self):
        self.response = requests.get(url=self.countries_url)
        return json.loads(self.response.text)
    def continentFilter(self, continent):
        response = filter(lambda x: x["continent"] == f"{continent}", self.countryStats())
        return json.loads(json.dumps(list(response)))
    def wholeWorld(self):
        self.response = requests.get(url=self.world_url)
        return json.loads(self.response.text)

continents = ['Australia-Oceania', '', 'Asia', 'Africa','South America', 'North America', 'Europe']
