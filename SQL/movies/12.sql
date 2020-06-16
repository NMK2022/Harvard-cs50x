--list titles pf all movies where Johnny Depp & Helena Bonham Carter starred
SELECT title FROM people
JOIN stars ON people.id = stars.person_id
JOIN movies ON movies.id = stars.movie_id
WHERE name = "Johnny Depp"
INTERSECT
SELECT title FROM people
JOIN stars ON people.id = stars.person_id
JOIN movies ON movies.id = stars.movie_id
WHERE name = "Helena Bonham Carter";