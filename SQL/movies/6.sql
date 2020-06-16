--determine avg rating of all movies from 2012
SELECT AVG(rating) FROM ratings JOIN movies ON movies.id = ratings.movie_id
WHERE year = 2012;