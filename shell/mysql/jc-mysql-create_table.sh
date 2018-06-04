/opt/lampp/bin/mysql -p -e "
USE douban_imdb_rating;
CREATE TABLE duplicated_douban_index (
movie_douban_url VARCHAR(2083),
movie_name_cn TEXT,
movie_region_id VARCHAR(50),
movie_cast_cn TEXT,
movie_director_cn TEXT,
movie_douban_score VARCHAR(2083)
)ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
"
