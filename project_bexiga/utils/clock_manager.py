# schedule a function call in the future
import datetime
from kivy.clock import Clock

# from dialog.dialog_confirmation import DialogConfirmation
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivymd.theming import ThemeManager
import plyer

class ClockManager:
  dialog = None
  
  def __init__(self, interval, initial_value, element, lembrete_timestamp, number_count):
    self.interval = interval
    self.initial_value = initial_value
    self.number = 0
    self.lembrete_timestamp = lembrete_timestamp
    self.number_count = number_count
    self.element = element
    # Create the clock and increment the time by .1 ie 1 second.
    Clock.schedule_interval(self.increment_time,self.interval )

    self.increment_time(self.initial_value)
  # To increase the time / count
  def increment_time(self, interval):
    self.number += self.interval
    time = self.build_time()
    if(time == self.lembrete_timestamp and self.number_count >=1):
      self.number_count-=1
      time = datetime.time(hour = 0,minute = 0)
      self.number = 0
      self.show_confirmation_dialog(self.number_count)
      plyer.notification.notify(title = "Projeto Bexiga", message = f"O lembrete terminou. Faltam {self.number_count}")
    self.element.text = f'[{self.number_count}] {time.strftime("%X")}'
  # To start the count
  def start(self):
        
    Clock.unschedule(self.increment_time)
    Clock.schedule_interval(self.increment_time, self.interval)

  # To stop the count / time
  def stop(self):
    Clock.unschedule(self.increment_time)
    self.reset()  
  def reset(self):
    self.number = 0
    self.element.text = "[0] 00:00:00"
    
  def build_time(self):
    numberAux = self.number
    
    hour = int(numberAux/3600); 
    minute = int((numberAux -(3600*hour))/60)    
    second = int(numberAux -(3600*hour)-(minute*60))    
    return datetime.time(int(hour),int(minute),int(second))
  
      
  
  def confirm_dialog(self,obj):    
    self.dialog.dismiss()
      
  
  def show_confirmation_dialog(self, lembrete_number_count):
    theme_cls = ThemeManager()
    if not self.dialog:
        self.dialog = MDDialog(
            title=f"O lembrete terminou. Faltam {lembrete_number_count}",
            radius=[20, 7, 20, 7],
            type="custom",            
            buttons=[            
                MDFlatButton(
                    id = "input_dialog_minute",
                    text="OK",
                    theme_text_color="Custom",
                    text_color= theme_cls.primary_color,
                    on_release = self.confirm_dialog
                ),
            ],
        )
    self.dialog.open()
    