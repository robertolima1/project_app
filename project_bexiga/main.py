import datetime
from kivymd.app import MDApp
from kivymd.uix.screenmanager import MDScreenManager
from screens.ScreenMain.screen_main import ScreenMainView
from screens.ScreenAlerta.screen_alerta import ScreenAlertaView
from screens.ScreenAlertaDescricao.screen_alerta_descricao import ScreenAlertaDescricao
from screens.ScreenLembreteDescricao.screen_lembrete_descricao import ScreenLembreteDescricao
from kivymd.uix.list import TwoLineAvatarIconListItem, IconRightWidget, TwoLineListItem
from kivymd.uix.pickers import MDDatePicker,MDTimePicker
from repository.database_manager import DatabaseManager
from utils.clock_manager import ClockManager

class MainApp(MDApp):
  def __init__(self, **kwargs):
    super().__init__(**kwargs)
    self.sm = MDScreenManager()  
    self.load_all_kv_files(self.directory) 
    self.db = DatabaseManager()   
    self.clock = None

  def build(self):
    self.sm.add_widget(ScreenMainView())
    self.sm.add_widget(ScreenAlertaView())
    self.sm.add_widget(ScreenAlertaDescricao())
    self.sm.add_widget(ScreenLembreteDescricao())
    # self.sm.get_screen("main").ids.bottom_navigation.first_widget = "Screen Home"
    
    return self.sm
  
  def on_start(self):    
    alertas = self.db.getAllAlerta()
    for alerta in alertas:
       self.sm.get_screen("alerta").ids.list_alert.add_widget(TwoLineListItem(text=alerta.alerta_title, secondary_text = alerta.alerta_describe , on_release= self.setAlertDescribe))
         
  def setAlertDescribe(self, TwoLineListItem):
    print(TwoLineListItem.text, TwoLineListItem.secondary_text)
    self.sm.transition.direction = "left"
    self.sm.current = "alerta-descricao"

  def start_clock(self):
    self.clock = ClockManager(1, 0, self.sm.get_screen("main").ids.count)    
    self.clock.start()
    
  def stop_clock(self):
    self.clock.stop()
    
  def on_save(self, instance, value, date_range):
    '''
    Events called when the "OK" dialog box button is clicked.

    :type instance: <kivymd.uix.picker.MDDatePicker object>;
    :param value: selected date;
    :type value: <class 'datetime.date'>;
    :param date_range: list of 'datetime.date' objects in the selected range;
    :type date_range: <class 'list'>;
    '''

    print(instance, value, date_range)

  def on_cancel(self, instance, value):
      '''Events called when the "CANCEL" dialog box button is clicked.'''

  def show_date_picker(self):
    date_dialog = MDDatePicker(
      title= "Selecione o Dia",
       min_year = datetime.date.today().year,                                 
    )
    date_dialog.bind(on_save=self.on_save, on_cancel=self.on_cancel)
    date_dialog.open()
  
  def cancel_time(self,instance, time):
    print("TESTE CANCLE")
    
  def on_save_time(self,instance, time):
    print("TESTE CANCL123123E")
    
  def show_time_picker(self):
    
    # previous_time = datetime.datetime.strptime("03:20:00", '%H:%M:%S').time()
    time_dialog = MDTimePicker()
    time_dialog.bind(on_cancel = self.cancel_time,time = self.get_time, on_save = self.on_save_time)
    # time_dialog.set_time(previous_time)
    time_dialog.open()

  def get_time(self, instance, time):
    '''
    The method returns the set time.

    :type instance: <kivymd.uix.picker.MDTimePicker object>
    :type time: <class 'datetime.time'>
    '''

    return time  
  
  def populate_screen(self, parent, screen_name):
    print(screen_name)
    
    
    if(screen_name == 'anotacao'):
      anotacoes = self.db.getAllAnotacao()
      
      for anotacao in anotacoes:      
        parent.children[1].ids.list_anotacao.clear_widgets()
        parent.children[1].ids.list_anotacao.add_widget(TwoLineListItem(text=anotacao.anotacao_title, secondary_text = anotacao.anotacao_describe))       
    elif(screen_name == 'lembrete'):    
      icon_play =IconRightWidget(icon = "play")
      icon_stop =IconRightWidget(icon = "stop")
      lembrete = self.db.getAllLembrete()
      
      for lembrete in lembrete:      
        parent.children[1].ids.list_lembrete.clear_widgets()
        element = TwoLineAvatarIconListItem(text=lembrete.lembrete_title, secondary_text = lembrete.lembrete_describe,  on_release= self.setLembreteDescribe)
        element.add_widget(icon_play)
        parent.children[1].ids.list_lembrete.add_widget(element)       
        
  def setLembreteDescribe(self, TwoLineListItem):    
    self.sm.transition.direction = "left"
    self.sm.current = "lembrete-descricao"        
MainApp().run()