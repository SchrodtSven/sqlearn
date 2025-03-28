CREATE TABLE IF NOT EXISTS "tree" (
		id    INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
		name  NVARCHAR(50)  NOT NULL,
		lft   INTEGER  NOT NULL,
		rgt   INTEGER  NOT NULL
	);

INSERT INTO tree (name,lft,rgt) VALUES ('Säugetiere',1,2);

UPDATE tree SET rgt=rgt+2 WHERE rgt = 2;
INSERT INTO tree (name,lft,rgt) VALUES ('Primaten',2,3);

