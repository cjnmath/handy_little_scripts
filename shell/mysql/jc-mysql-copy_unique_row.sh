/opt/lampp/bin/mysql -p -e "
USE douban_imdb_rating;
INSERT INTO unduplicated_douban_index
SELECT *
FROM
(SELECT *
FROM douban_index
GROUP BY movie_douban_url HAVING COUNT(*)=1) as derived_table;
"
