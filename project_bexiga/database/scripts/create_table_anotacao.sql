CREATE TABLE ANOTACAO(
  anotacao_id guid,
  anotacao_title varchar(30),
  anotacao_describe TEXT,
  insertion_date timestamp
)

INSERT INTO ANOTACAO
(anotacao_id, anotacao_title, anotacao_describe, insertion_date)
VALUES('b801845d-986b-489c-bed3-1de977ff80a6', 'ANOTAÇÃO 1', 'Lorem ipsum dolor sit amet, consectetur adipisci elit, sed eiusmod tempor incidunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur.', datetime());