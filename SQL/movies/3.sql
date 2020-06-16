--list titles of movies with date after 2018 in alphabetical order
SELECT title FROM movies WHERE year >= 2018
ORDER BY title ASC;