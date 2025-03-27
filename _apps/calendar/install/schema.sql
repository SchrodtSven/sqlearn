-- db schema for cappy
-- SINCE: 2025-03-27

PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;


CREATE TABLE IF NOT EXISTS "location"
(
    [id] INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    [title] NVARCHAR(160)  NOT NULL,
    [description] TEXT  NULL,
    [lat] REAL  NULL,
    [lng] REAL  NULL
);

INSERT INTO location VALUES(1,'* PLACEHOLDER *', 'This is just a meta location ', null, null);
INSERT INTO location VALUES(2,'Secret place', 'Somewhere in DE-47445', 51.48655975, 6.613861508182158);
--
CREATE TABLE IF NOT EXISTS "status"
(
    [id] INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    [title] NVARCHAR(160)  NOT NULL
    
);

INSERT INTO status VALUES(1,'RESERVED');
INSERT INTO status VALUES(2,'PLANNED');
INSERT INTO status VALUES(3,'CANCELED');
INSERT INTO status VALUES(4,'N/A');
INSERT INTO status VALUES(5,'????');
INSERT INTO status VALUES(6,'DONE');

-- cat(egory) level == 0 ? is_parent : is_parent_id 
CREATE TABLE IF NOT EXISTS "cat"
(
    [id] INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    [title] NVARCHAR(160)  NOT NULL,
    [level] INTEGER NOT NULL DEFAULT 0
    
);
INSERT INTO cat VALUES(1,'Sport National Football', 0);
INSERT INTO cat VALUES(2,'** PLACEHOLDER', 0);
INSERT INTO cat VALUES(3,'2. Bundesliga', 1);



CREATE TABLE IF NOT EXISTS "event"
(
    [id] INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    [title] NVARCHAR(160)  NOT NULL,
    [loc_id] INTEGER  NOT NULL,
    [e_from] REAL  NOT NULL,
    [e_until] REAL  NOT NULL,
    [cat_id] INTEGER  NOT NULL,
    [comment] TEXT NULL,
    [status_id] INTEGER NULL,
    FOREIGN KEY ([loc_id]) REFERENCES "location" ([id]) 
		ON DELETE NO ACTION ON UPDATE NO ACTION,
    FOREIGN KEY ([status_id]) REFERENCES "status" ([id]) 
		ON DELETE NO ACTION ON UPDATE NO ACTION
);


COMMIT;