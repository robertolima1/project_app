import sqlite3
from domain.alerta import Alerta
from domain.lembrete import Lembrete

class DatabaseManager:
  
  def __init__(self) -> None:
    self.connection = sqlite3.connect('project.bexiga.db')
    
  def getAllAlerta(self):
    c = self.connection.cursor()
    c.execute(f"SELECT * FROM ALERTA")
    records = c.fetchall()
    
    return self.normalize_alerta(records)
   

  def normalize_alerta(self, records):
    alertas = []
    for register in records:
      alerta = Alerta(register[0], register[1], register[2], register[3],register[4])
      alertas.append(alerta)
    return alertas
       