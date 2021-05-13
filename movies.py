import requests

class GetMoviesInstance():
    def __init__(
        self, *movies, limit=5,
        tdk="410571-StudyApl-00U59XXC",
        omdbk="546c6742"):

        self.movies_list = [*movies]
        self.limit = limit
        self.taste_dive_key = tdk
        self.omdb_key = omdbk

    def __str__(self):
        return self.movies_list

    def get_tastedive(self, movieName):
        baseurl = "https://tastedive.com/api/similar"
        params_d = {}
        params_d["q"] = movieName
        params_d["k"] = self.taste_dive_key
        params_d["type"] = "movies"
        params_d["limit"] = self.limit
        resp = requests.get(baseurl, params=params_d)
        print(resp.url)
        respDic = resp.json()
        return respDic

    def extract_titles(self, movieName):
        result = []
        for listRes in movieName['Similar']['Results']:
            result.append(listRes['Name'])
        return result

    def get_related_titles(self, listMovieName):
        print(listMovieName)
        if listMovieName != []:
            auxList = []
            relatedList = []
            for movieName in listMovieName:
                auxList = self.extract_titles(self.get_tastedive(movieName))
                for movieNameAux in auxList:
                    if movieNameAux not in relatedList:
                        relatedList.append(movieNameAux)

            return relatedList
        return listMovieName

    def get_movie_data(self, movieName):
        baseurl = "http://www.omdbapi.com/"
        params_d = {}
        params_d["t"] = movieName
        params_d["apikey"] = self.omdb_key
        params_d["r"] = "json"
        resp = requests.get(baseurl, params=params_d)
        # print(resp.url)
        respDic = resp.json()
        # print("----->", respDic)
        return respDic

    def get_sorted_recommendations(self):
        listMovie = self.get_related_titles(self.movies_list)
        self.obj_list = []
        for movie in listMovie:
            obj = self.get_movie_data(movie)
            self.obj_list.append(obj)

        return self.obj_list

