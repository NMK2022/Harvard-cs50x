--lists movies released in 2010 + their ratings; descending
--if same rating order alphabetically
SELECT title, rating FROM movies JOIN ratings ON movies.id = ratings.movie_id
WHERE year = 2010 ORDER BY rating DESC, title;