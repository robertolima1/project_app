CREATE TABLE TECNICA(
  tecnica_id guid,
  tecnica_title varchar(30),
  tecnica_describe TEXT,
  insertion_date timestamp
);

INSERT INTO TECNICA
(tecnica_id, tecnica_title, tecnica_describe, insertion_date)
VALUES('b801845d-986b-489c-bed3-1de977ff80a6', 'Tecnica 1', 'Lorem ipsum dolor sit amet, consectetur adipisci elit, sed eiusmod tempor incidunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur.', datetime());