import requests

class GetMoviesInstance():
    def __init__(self, *movies):
        self.movies_list = [*movies] 

    def get_tastedive(self, movieName, key="410571-StudyApl-00U59XXC"):
        baseurl="https://tastedive.com/api/similar"
        params_d = {}
        params_d["q"]= movieName
        params_d["k"]= key
        params_d["type"]= "movies"
        params_d["limit"] = "5"
        resp = requests.get(baseurl, params=params_d)
        print(resp.url)
        respDic = resp.json()
        return respDic 

    def extract_titles(self, movieName):
        result=[]
        for listRes in movieName['Similar']['Results']:
            result.append(listRes['Name'])
        return result

    def get_related_titles(self, listMovieName):
        print(listMovieName)
        if listMovieName != []:
            auxList=[]
            relatedList=[]
            for movieName in listMovieName:
                auxList = self.extract_titles(self.get_tastedive(movieName))
                for movieNameAux in auxList:
                    if movieNameAux not in relatedList:
                        relatedList.append(movieNameAux)
            
            return relatedList
        return listMovieName

    def get_movie_data(self, movieName, key="546c6742"):
        baseurl= "http://www.omdbapi.com/"
        params_d = {}
        params_d["t"]= movieName
        params_d["apikey"]= key
        params_d["r"]= "json"
        resp = requests.get(baseurl, params=params_d)
        # print(resp.url)
        respDic = resp.json()
        # print("----->", respDic)
        return respDic

    def get_movie_rating(self, movieNameJson):
        strRanting=""
        #print(movieNameJson)
        for typeRantingList in movieNameJson["Ratings"]:
            if typeRantingList["Source"]== "Rotten Tomatoes":
                strRanting = typeRantingList["Value"]
        if strRanting != "":
            ranting = int(strRanting[:2])
        else: ranting = 0
        return ranting

    def get_sorted_recommendations(self):
        listMovie = self.get_related_titles(self.movies_list)
        self.obj_list = []
        for movie in listMovie:
            obj = self.get_movie_data(movie)
            self.obj_list.append(obj)
        # listMovie = sorted(listMovie, key = lambda movieName: (self.get_movie_rating(self.get_movie_data(movieName)), movieName), reverse=True)
        
        return self.obj_list

prova = GetMoviesInstance("The Great Silence", "Keoma")
p = prova.get_sorted_recommendations()
print(p)