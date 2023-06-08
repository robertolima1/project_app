# schedule a function call in the future
import datetime
from kivy.clock import Clock
 
class ClockManager:
  def __init__(self, interval, initial_value, element):
    self.interval = interval
    self.initial_value = initial_value
    self.number = 0
    self.element = element
    # Create the clock and increment the time by .1 ie 1 second.
    Clock.schedule_interval(self.increment_time,self.interval )

    self.increment_time(self.initial_value)
  # To increase the time / count
  def increment_time(self, interval):
    self.number += self.interval
    time = self.build_time()
    self.element.text = time.strftime("%X")
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
    self.element.text = "00:00:00"
    
  def build_time(self):
    numberAux = self.number
    
    hour = int(numberAux/3600); 
    minute = int((numberAux -(3600*hour))/60)    
    second = int(numberAux -(3600*hour)-(minute*60))    
    return datetime.time(int(hour),int(minute),int(second))