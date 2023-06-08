import sqlite3
from domain.alerta import Alerta
from domain.lembrete import Lembrete
from domain.anotacao import Anotacao

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
  
  def getAllLembrete(self):
    c = self.connection.cursor()
    c.execute(f"SELECT * FROM LEMBRETE")
    records = c.fetchall()
    
    return self.normalize_lembrete(records)
   

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
                     