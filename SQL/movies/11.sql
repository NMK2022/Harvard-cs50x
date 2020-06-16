--list titles of 5 highest rated movies (in order high->low) that Chadwick Boseman starred in
SELECT DISTINCT title FROM people
JOIN stars ON people.id = stars.person_id
JOIN ratings ON ratings.movie_id = stars.movie_id
JOIN movies ON movies.id = stars.movie_id
WHERE name = "Chadwick Boseman"
ORDER BY rating DESC
Limit 5;