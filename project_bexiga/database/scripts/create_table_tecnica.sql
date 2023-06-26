CREATE TABLE TECNICA(
  tecnica_id guid,
  tecnica_title varchar(30),
  path_title varchar(100),
  path_ilustration TEXT,
  insertion_date timestamp
);

INSERT INTO TECNICA
	(tecnica_id, tecnica_title, path_ilustration, insertion_date)
VALUES

	('b801845d-986b-489c-bed3-1de977ff80a6', 'Tecnica 1', 'images/title-container-1.png','images/figura-container-1.png', datetime()),
	('ad91998a-28a3-43c4-b7d4-028b5b97ebea', 'Tecnica 2', 'images/title-container-2.png','images/figura-container-2.png', datetime()),
	('3391bd42-ef1b-41f7-b44b-a5d1cf87a14d', 'Tecnica 3', 'images/title-container-3.png','images/figura-container-3.png', datetime()),
	('f79f577d-7574-48ad-a6f8-e52707bbff62', 'Tecnica 4', 'images/title-container-4.png','images/figura-container-4.png', datetime()),
	('e94ffa7d-47b7-4faa-a298-fdf0f83dd803', 'Tecnica 5', 'images/title-container-5.png','images/figura-container-5.png', datetime()),
	('2eb8bbe6-194d-4f16-a380-393e7f9cf61a', 'Tecnica 6', 'images/title-container-6.png','images/figura-container-6.png', datetime()),
	('d76f42bd-fa48-436c-9c56-17317fd0d588', 'Tecnica 7', 'images/title-container-7.png','images/figura-container-7.png', datetime()),
	('26c6d34a-eec0-4f85-95b7-bf6e9f9c86f0', 'Tecnica 8', 'images/title-container-8.png','images/figura-container-8.png', datetime()),
	('5fdc370f-3cc9-4d5e-8be7-14dd6072ef8a', 'Tecnica 9', 'images/title-container-9.png','images/figura-container-9.png', datetime()),
	('39369648-2277-49be-9c84-217db7f8e551', 'Tecnica 10', 'images/title-container-10.png','images/figura-container-10.png', datetime()),
	('b1371ba6-c6bd-41bb-9923-69fb3c5b7747', 'Tecnica 11', 'images/title-container-11.png','images/figura-container-11.png', datetime());