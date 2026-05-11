class Movie:
    def set_rating(self,rating):
        if not (1 <= rating <= 10):
            return
        self.rating = rating
    
    def is_high_rated(self):
        if self.rating >= 8:
            return True
        else:
            return False
    
    def __init__(self, title, director, year, genre):
        if not (1888 <= year <= 2024):
            return
        self.title = title
        self.director = director
        self.year = year
        self.genre = genre
        self.rating = None
    
    def __str__(self):
        string = ""
        title = self.title
        year = self.year
        director = self.director
        genre = self.genre
        rating = self.rating


        return f"Название: {title}, {year} - {director} [{genre}] {rating}★"

class MovieCollection:
    def add_movie(self,movie):
        self.movies.append(movie)

    def remove_movie(self,title):
        index = 0
        for movie in self.movies:
            if movie.title == title:
                return self.movies.pop(index)
            index += 1
        print(f"Не получилось найти фильм с названием: {title}")

    def get_movie_by_title(self, title):
        genre_list = []
        for movie in self.movies:
            if movie.title == title:
                genre_list.append(movie)
        return genre_list

    def rate_movie(self, title, rating):
        for movie in self.movies:
            if movie.title == title:
                movie.set_rating(rating)
                return

    def get_top_movies(self, limit=5):
        top_list = self.movies.copy()
        top_list_sorted = {}
        top_list_return = []

        for name in top_list:
            rating = name.rating
            if rating != None:
                if top_list_sorted.get(str(rating)) == None:
                    top_list_sorted[str(rating)] = []

                top_list_sorted[str(rating)].append(name)
        
        limit_index = 1

        for index in range(0,10):
            if limit_index <= 5:
                limit_index += 1
            else:
                break
            index = 10 - index
            if top_list_sorted.get(str(index)) != None:
                for movie in top_list_sorted.get(str(index)):
                    top_list_return.append(movie)

        return top_list_return

    def get_movies_by_genre(self, genre):
        genre_list = []
        for movie in self.movies:
            if movie.genre == genre:
                genre_list.append(movie)
        return genre_list
        

    def get_stats(self):
        total_movies = 0
        rated_movies = 0
        average_rating = None
        most_common_genre = ""
        high_rated_count = 0

        genre_list = {}

        for movie in self.movies:
            total_movies += 1
            if movie.rating != None:
                rated_movies += 1

                if average_rating == None:
                    average_rating = movie.rating
                else:
                    average_rating = (average_rating + movie.rating) / 2

                if genre_list.get(movie.genre) == None:
                    genre_list[movie.genre] = 1
                else:
                    genre_list[movie.genre] += 1
                
                if movie.is_high_rated() == True:
                    high_rated_count += 1
        
        most_common_genre_count = 0
        for genre in genre_list:
            data = genre_list[genre]
            if most_common_genre_count > data:
                most_common_genre_count = data
                most_common_genre = genre
        
        stats = {
            "total_movies": total_movies,
            "rated_movies": rated_movies,
            "average_rating": average_rating,
            "most_common_genre": most_common_genre,
            "high_rated_count": high_rated_count
        }

        return stats

    def __init__(self,name):
        self.name = name
        self.movies = []

    def __str__(self):
        pass


# Создаем коллекцию
my_collection = MovieCollection("Мои любимые фильмы")

film1 = Movie("Начало", "Кристофер Нолан", 2010, "фантастика")
film2 = Movie("Крестный отец", "Фрэнсис Форд Коппола", 1972, "драма")

# Добавляем в коллекцию
my_collection.add_movie(film1)
my_collection.add_movie(film2)

# Оцениваем фильмы
my_collection.rate_movie("Начало", 9)
my_collection.rate_movie("Крестный отец", 10)


# Получаем статистику
stats = my_collection.get_stats()
print(f"Всего фильмов: {stats['total_movies']}")
print(f"Средний рейтинг: {stats['average_rating']}")

# Ищем фильмы по жанру
fantasy_movies = my_collection.get_movies_by_genre("фантастика")

# Топ лист

top_movies = my_collection.get_top_movies()

limit_index = 0
for movie in top_movies:
    limit_index += 1
    print("="*40)
    print(f"Топ: {limit_index}, {movie.__str__()}")
    print("="*40)
