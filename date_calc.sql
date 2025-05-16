SELECT
	name,
    DATE('now') - age AS geburtsjahr,
    CASE
    	WHEN DATE('now') - age <= 1964
        	THEN 'Baby Boomer'
        WHEN DATE('now') - age BETWEEN 1965 AND 1980
          	THEN 'Gen X'
        WHEN DATE('now') - age BETWEEN 1981 AND 1996
          	THEN 'Millenial'
        WHEN DATE('now') - age BETWEEN 1997 AND 2012
            THEN 'Gen Z'
        ELSE 'unknown'
    END AS generation
FROM student 