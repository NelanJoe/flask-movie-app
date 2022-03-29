from flask import Flask, render_template
import urllib.request, json

app = Flask(__name__)

key = "acafdeae2e2064b3f9c66c78d0e38cf8"

@app.route('/home')

def getMovie():
   url = f"https://api.themoviedb.org/3/discover/movie?api_key={key}&language=id"
   response = urllib.request.urlopen(url)
   data = response.read()
   dict = json.loads(data)
   return render_template('movie.html', movies=dict['results'])

@app.route("/movies")
def get_movies_list():
    url = f"https://api.themoviedb.org/3/discover/movie?api_key={key}&language=id"

    response = urllib.request.urlopen(url)
    movies = response.read()
    dict = json.loads(movies)

    movies = []

    for movie in dict["results"]:
        movie = {
            "title": movie["title"],
            "overview": movie["overview"],
        }
        
        movies.append(movie)

    return {"results": movies}


if __name__ == '__main__':
    app.run(debug=True)
    