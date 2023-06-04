CREATE TABLE ALERTA(
  alerta_id guid,
  alerta_title varchar(30),
  alerta_describe TEXT,
  insertion_date timestamp,
  update_date timestamp

);

INSERT INTO ALERTA
(alerta_id, alerta_title, alerta_describe, insertion_date, update_date)
VALUES ('d445ac62-05e9-4add-88db-d9a523b02b67', 'ALERTA 1', 'Lorem ipsum dolor sit amet, consectetur adipisci elit, sed eiusmod tempor incidunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur.',datetime() , datetime())
('ffe49a6f-9426-4058-b360-f4221acef83b', 'ALERTA 2', 'Lorem ipsum dolor sit amet, consectetur adipisci elit, sed eiusmod tempor incidunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur.', datetime() ,  datetime()),
('c9f8bfd9-0c8a-45bb-88d3-bbbcc31fc05d', 'ALERTA 3', 'Lorem ipsum dolor sit amet, consectetur adipisci elit, sed eiusmod tempor incidunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur.', datetime() ,  datetime()),
('070b21dc-be86-46c2-9a7c-5e4d2ff366ab', 'ALERTA 4', 'Lorem ipsum dolor sit amet, consectetur adipisci elit, sed eiusmod tempor incidunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur.',datetime() ,  datetime()),
('39a58823-56f0-4f09-bf6e-5a800c524a1e', 'ALERTA 5', 'Lorem ipsum dolor sit amet, consectetur adipisci elit, sed eiusmod tempor incidunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur.',datetime() ,  datetime()),
('7f792447-f19a-42ff-9610-366479cb3e31', 'ALERTA 6', 'Lorem ipsum dolor sit amet, consectetur adipisci elit, sed eiusmod tempor incidunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur.',datetime() ,  datetime()),
('2e965840-531f-44e8-8726-91d788888fdf', 'ALERTA 7', 'Lorem ipsum dolor sit amet, consectetur adipisci elit, sed eiusmod tempor incidunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur.',datetime() ,  datetime()),
('fcca4f1d-3091-437b-93ce-91df6fa8468a', 'ALERTA 8', 'Lorem ipsum dolor sit amet, consectetur adipisci elit, sed eiusmod tempor incidunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur.',datetime() ,  datetime());
