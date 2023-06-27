import sqlite3
import uuid
from domain.alerta import Alerta
from domain.lembrete import Lembrete
from domain.anotacao import Anotacao
from domain.tecnica import Tecnica
from datetime import datetime
class DatabaseManager:
  
  def __init__(self) -> None:
    self.connection = sqlite3.connect('project.bexiga.db')
    
  def getAllAlerta(self):
    c = self.connection.cursor()
    c.execute(f"SELECT * FROM ALERTA")
    records = c.fetchall()
    
    return self.normalize_alerta(records)
  
  def getAllAnotacao(self):
    c = self.connection.cursor()
    c.execute(f"SELECT * FROM ANOTACAO")
    records = c.fetchall()
    
    return self.normalize_anotacao(records)
  
  def getAllTecnica(self):
    c = self.connection.cursor()
    c.execute(f"SELECT * FROM TECNICA")
    records = c.fetchall()
    
    return self.normalize_tecnica(records)
  
  
  def getAllLembrete(self):
    c = self.connection.cursor()
    c.execute(f"SELECT lembrete_id, lembrete_title, lembrete_describe, lembrete_count_repeat, on_start, lembrete_timestamp, insertion_date \
              FROM LEMBRETE")
    records = c.fetchall()
    
    return self.normalize_lembrete(records)
  def get_lembrete_by_id(self, lembrete_id):
    c = self.connection.cursor()
    c.execute(f"SELECT lembrete_id, lembrete_title, lembrete_describe, lembrete_count_repeat, on_start, lembrete_timestamp, insertion_date \
              FROM LEMBRETE WHERE lembrete_id = '{lembrete_id}'")
    records = c.fetchall()
    
    return self.normalize_lembrete(records)[0]

  def get_anotacao_by_id(self, anotacao_id):
    c = self.connection.cursor()
    c.execute(f"SELECT anotacao_id, anotacao_title, anotacao_describe, insertion_date \
              FROM ANOTACAO WHERE anotacao_id = '{anotacao_id}'")
    records = c.fetchall()
    
    return self.normalize_anotacao(records)[0]
    
  def get_tecnica_by_id(self, tecnica_id):
    c = self.connection.cursor()
    c.execute(f"SELECT tecnica_id, tecnica_title, tecnica_describe, path_title, path_ilustration, insertion_date \
              FROM TECNICA WHERE tecnica_id = '{tecnica_id}'")
    records = c.fetchall()
    
    return self.normalize_tecnica(records)[0]
      
  def save_lembrete(self, instance, describe, title, number_repeat):
    c = self.connection.cursor()
    instante_dt = datetime.strptime(instance, '%H:%M:%S')
    
    c.execute(f"INSERT INTO LEMBRETE (lembrete_id, lembrete_title, lembrete_describe, lembrete_count_repeat, on_start,lembrete_timestamp, insertion_date, update_date) \
               VALUES ('{uuid.uuid4()}', '{title}', '{describe}',{number_repeat}, {False}, '{str(instante_dt)}', datetime() ,datetime())")
    self.connection.commit()
    
  def update_lembrete(self,lembrete_id, describe, title, number_repeat):
    c = self.connection.cursor()
    
    c.execute(f"UPDATE  \
              set lembrete_title = '{title}', \
              lembrete_describe = '{describe}' \
              lembrete_count_repeat = {number_repeat}, \
              on_start = {False},\
              update_date = datetime()  WHERE lembrete_id = '{lembrete_id}'")
    self.connection.commit()

      
  def save_anotacao(self, date, describe, title):
    c = self.connection.cursor()
    instante_dt = datetime.strptime(date, '%Y-%m-%d')
    
    c.execute(f"INSERT INTO ANOTACAO (anotacao_id, anotacao_title, anotacao_describe, insertion_date) \
               VALUES ('{uuid.uuid4()}', '{title}', '{describe}', '{str(instante_dt)}')")
    self.connection.commit()
    
  def update_anotacao(self,anotacao_id, describe, title, date):
    c = self.connection.cursor()
    instante_dt = datetime.strptime(date, '%Y-%m-%d')    
    c.execute(f"UPDATE ANOTACAO set anotacao_title = '{title}', anotacao_describe = '{describe}', insertion_date = '{instante_dt}'  WHERE anotacao_id = '{anotacao_id}'")
    self.connection.commit()
        
  def set_lembrete_on_start(self, lembrete_id, on_start):
    c = self.connection.cursor()
    update_dt = str(datetime.now())
    c.execute(f"UPDATE LEMBRETE SET on_start = {on_start}, update_date = '{update_dt}' WHERE lembrete_id = '{lembrete_id}'")
    self.connection.commit()
    
  def set_lembrete_all_on_start(self):
    c = self.connection.cursor()    
    c.execute(f"UPDATE LEMBRETE SET on_start = {False}")
    self.connection.commit()  
    
  def delete_lembrete(self, lembrete_id):
    c = self.connection.cursor()    
    c.execute(f"DELETE FROM LEMBRETE WHERE lembrete_id = '{lembrete_id}'")
    self.connection.commit()  

  def delete_anotacao(self, anotacao_id):
    c = self.connection.cursor()    
    c.execute(f"DELETE FROM ANOTACAO WHERE anotacao_id = '{anotacao_id}'")
    self.connection.commit()  
       
  def normalize_alerta(self, records):
    alertas = []
    for register in records:
      alerta = Alerta(register[0], register[1], register[2], register[3],register[4])
      alertas.append(alerta)
    return alertas

  def normalize_lembrete(self, records):
    lembretes = []
    for register in records:
      lembrete = Lembrete(register[0], register[1], register[2], register[3],register[4],register[5], register[6])
      lembretes.append(lembrete)
    return lembretes

  def normalize_anotacao(self, records):
    anotacoes = []
    for register in records:
      anotacao = Anotacao(register[0], register[1], register[2], register[3])
      anotacoes.append(anotacao)
    return anotacoes

  def normalize_tecnica(self, records):
    tecnicoes = []
    for register in records:
      tecnica = Tecnica(register[0], register[1], register[2], register[3], register[4], register[5])
      tecnicoes.append(tecnica)
    return tecnicoes
                                       