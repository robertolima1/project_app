class Lembrete:
  def __init__(self, lembrete_id, lembrete_title, lembrete_describe,lembrete_count_repeat,on_start, lembrete_timestamp, insertion_date) -> None:
    self.lembrete_id = lembrete_id
    self.lembrete_title = lembrete_title
    self.lembrete_describe = lembrete_describe
    self.lembrete_count_repeat = lembrete_count_repeat
    self.on_start = on_start
    self.lembrete_timestamp = lembrete_timestamp
    self.insertion_date = insertion_date              