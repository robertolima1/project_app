CREATE TABLE LEMBRETE(
  lembrete_id guid,
  lembrete_title varchar(30),
  lembrete_timestamp timestamp,
  insertion_date timestamp,
  update_date timestamp
);

INSERT INTO LEMBRETE
(lembrete_id, lembrete_title, lembrete_describe,lembrete_timestamp, insertion_date, update_date)
VALUES('0292fca3-550d-47cc-b199-69fcb754a303', 'LEMBRETE 1','Lorem ipsum dolor sit amet, consectetur adipisci elit, sed eiusmod tempor incidunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur.', datetime(), datetime(), datetime());
