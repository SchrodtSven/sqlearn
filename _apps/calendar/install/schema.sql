-- db schema for cappy
-- AUTHOR: Sven Schrodt
-- SINCE: 2025-03-27



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


CREATE TABLE IF NOT EXISTS "role"
(
    [id] INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    [rle_name] NVARCHAR(155)  NOT NULL,
    [descript] NVARCHAR(255)  NULL
    
);

INSERT INTO role VALUES(1, 'God', 'Eating Admins for breakfast');
INSERT INTO role VALUES(2, 'Admin_bofh', 'Admins');
INSERT INTO role VALUES(3, 'Admin_gen', 'Admins pretending to work');
INSERT INTO role VALUES(4, 'Staff', 'Working people');
INSERT INTO role VALUES(5, 'Organiser', 'Planning people');
INSERT INTO role VALUES(6, 'Customer', 'Enjoying people');

CREATE TABLE IF NOT EXISTS "user"
(
    [id] INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    [usr_name] NVARCHAR(155)  NOT NULL,
    [descript] NVARCHAR(255)  NULL
    
);

CREATE TABLE IF NOT EXISTS "usr_plus" -- to be defined l8er
(
    [id] INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    [usr_first_name] NVARCHAR(155)  NOT NULL,
    [usr_last_name] NVARCHAR(155)  NOT NULL,
    [description] NVARCHAR(255)  NULL
    
);

CREATE TABLE IF NOT EXISTS "usr_to_rle"
(
      [usr_id] INTEGER NOT NULL,
      [rle_id] INTEGER NOT NULL,
      PRIMARY KEY(usr_id, rle_id)
      FOREIGN KEY ([rle_id]) REFERENCES "role" ([id]) 
		  ON DELETE NO ACTION ON UPDATE NO ACTION,
      FOREIGN KEY ([usr_id]) REFERENCES "user" ([id]) 
		  ON DELETE NO ACTION ON UPDATE NO ACTION

);

CREATE TABLE IF NOT EXISTS "entity_class"
(
    [id] INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    [ety_cls_name] NVARCHAR(160)  NULL
);

INSERT INTO entity_class VALUES(1, 'Event');
INSERT INTO entity_class VALUES(2, 'User');
INSERT INTO entity_class VALUES(3, 'EventApplication');
INSERT INTO entity_class VALUES(4, 'N/A');
INSERT INTO entity_class VALUES(5, '????');
INSERT INTO entity_class VALUES(6, 'DONE');


CREATE TABLE IF NOT EXISTS "status"
(
    [id] INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    [ety_cls_id] INTEGER,
    [title] NVARCHAR(160)  NOT NULL,
    FOREIGN KEY ([ety_cls_id]) REFERENCES "entity_class" ([id]) 
		ON DELETE NO ACTION ON UPDATE NO ACTION
    
);

INSERT INTO status VALUES(1, 1, 'RESERVED');
INSERT INTO status VALUES(2, 1, 'PLANNED');
INSERT INTO status VALUES(3, 1, 'CANCELED');
INSERT INTO status VALUES(4, 1, 'N/A');
INSERT INTO status VALUES(5, 1, '????');
INSERT INTO status VALUES(6, 1, 'DONE');

-- cat(egory) level == 0 ? is_parent : is_parent_id 
CREATE TABLE IF NOT EXISTS "category"
(
    [id] INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    [title] NVARCHAR(160)  NOT NULL,
    [level] INTEGER NOT NULL DEFAULT 0
);
INSERT INTO category VALUES(1,'Free style event', 0);
INSERT INTO category VALUES(2,'Sport National Football', 0);
INSERT INTO category VALUES(3,'** PLACEHOLDER', 0);
INSERT INTO category VALUES(4,'2. Bundesliga', 1);



CREATE TABLE IF NOT EXISTS "event"
(
    [id] INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    [title] NVARCHAR(160)  NOT NULL,
    [evt_start] REAL  NOT NULL,
    [evt_end] REAL  NOT NULL,
    [cat_id] INTEGER  NOT NULL,
    [loc_id] INTEGER  NOT NULL,
    [sts_id] INTEGER NULL,
    [comment] TEXT NULL,
    FOREIGN KEY ([loc_id]) REFERENCES "location" ([id]) 
		ON DELETE NO ACTION ON UPDATE NO ACTION,
    FOREIGN KEY ([sts_id]) REFERENCES "status" ([id]) 
		ON DELETE NO ACTION ON UPDATE NO ACTION
    FOREIGN KEY ([cat_id]) REFERENCES "category" ([id]) 
		ON DELETE NO ACTION ON UPDATE NO ACTION
);




COMMIT;