# Dictionary of movies

movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]

'''
def above(movie):
    return movie.get('imdb') > 5.5

print(above(movies[0])) #movies[x] x=number of movie
'''

'''
def above_55(movie):
    return [movie for movie in movies if movie.get('imdb') > 5.5]

print(above_55(movies), end='') #output all movies that above 5.5 
'''

'''
def one_category(movie, name):
    return [movie for movie in movies if movie.get('category') == name]

print(one_category(movies, 'Romance')) #output all movies with same category
'''

'''
def average_rates(movie):
    summa = sum(movie.get('imdb') for movie in movies)
    result = summa/len(movie)
    return result

print(average_rates(movies)) #all imdb rates sum divided by all movies sum
'''

'''
def average_rate_category(movie, name):
    result = sum(mov.get('imdb') for mov in one_category(movie,name))
    return result/len(one_category(movie,name))

print(average_rate_category(movies, 'Thriller')) #take one category and find average
'''