import datetime
from kivymd.app import MDApp
from kivymd.uix.screenmanager import MDScreenManager
from screens.ScreenMain.screen_main import ScreenMainView
from screens.ScreenWelcome.screen_welcome import ScreenWelcomeView
from screens.ScreenAlerta.screen_alerta import ScreenAlertaView
from screens.ScreenAlertaDescricao.screen_alerta_descricao import ScreenAlertaDescricao
from screens.ScreenLembreteDescricao.screen_lembrete_descricao import ScreenLembreteDescricao
from kivymd.uix.list import TwoLineAvatarIconListItem, IconRightWidget,IconLeftWidget, TwoLineListItem
from kivymd.uix.pickers import MDDatePicker,MDTimePicker
from repository.database_manager import DatabaseManager
from utils.clock_manager import ClockManager
from domain.lembrete import Lembrete

class MainApp(MDApp):
  def __init__(self, **kwargs):
    super().__init__(**kwargs)
    self.sm = MDScreenManager()  
    self.load_all_kv_files(self.directory) 
    self.db = DatabaseManager()   
    self.clock = None
    self.last_lembrete_start = None

  def build(self):
    self.sm.add_widget(ScreenWelcomeView())
    self.sm.add_widget(ScreenMainView())
    self.sm.add_widget(ScreenAlertaView())
    self.sm.add_widget(ScreenAlertaDescricao())
    self.sm.add_widget(ScreenLembreteDescricao())
    # self.sm.get_screen("main").ids.bottom_navigation.first_widget = "Screen Home"
    
    return self.sm
  
  def on_start(self):    
    self.db.set_lembrete_all_on_start()
    alertas = self.db.getAllAlerta()
    for alerta in alertas:
       self.sm.get_screen("alerta").ids.list_alert.add_widget(TwoLineListItem(text=alerta.alerta_title, secondary_text = alerta.alerta_describe , on_release= self.setAlertDescribe))
  
  def welcome(self):
    self.sm.get_screen("main").ids.bottom_navigation.switch_tab("Screen Home")    
           
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
    self.sm.get_screen("lembrete-descricao").ids.input_lembrete_instance.text = str(time)    
    
  def show_time_picker(self):
    
    previous_time = datetime.datetime.strptime("00:00:00", '%H:%M:%S').time()
    time_dialog = MDTimePicker()
    time_dialog.bind(on_cancel = self.cancel_time,time = self.get_time, on_save = self.on_save_time)
    time_dialog.set_time(previous_time)
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
      self.populate_lembrete(parent) 

  def populate_lembrete(self, parent):
      lembretes = self.db.getAllLembrete()
      parent.children[1].ids.list_lembrete.clear_widgets()
      
      for lembrete in lembretes:      
        icon_play =IconLeftWidget(icon = "play", on_release = self.start_lembrete, id = lembrete.lembrete_id)
        icon_stop =IconLeftWidget(icon = "stop", on_release = self.start_lembrete, id = lembrete.lembrete_id)
        icon_delete =IconRightWidget(icon = "trash-can-outline", on_release = self.delete_lembrete, id = lembrete.lembrete_id)
        element = TwoLineAvatarIconListItem(text=lembrete.lembrete_title, secondary_text = lembrete.lembrete_describe,  on_release= self.setLembreteDescribe)
        if(lembrete.on_start):
          element.add_widget(icon_stop)
        else:
          element.add_widget(icon_play)
        element.add_widget(icon_delete)
        parent.children[1].ids.list_lembrete.add_widget(element)      
        
  def setLembreteDescribeListItem(self, TwoLineAvatarIconListItem):    
    self.setLembreteDescribe()
            
  def setLembreteDescribe(self):    
    self.sm.transition.direction = "left"
    self.sm.current = "lembrete-descricao"     
    
  def save_lembrete(self):
    instance = self.sm.get_screen("lembrete-descricao").ids.input_lembrete_instance.text
    title = self.sm.get_screen("lembrete-descricao").ids.input_lembrete_title.text
    number_repeat = self.sm.get_screen("lembrete-descricao").ids.input_lembrete_number_repeat.text
    describe = self.sm.get_screen("lembrete-descricao").ids.input_lembrete_describe.text
    self.sm.get_screen("main").ids.bottom_navigation.switch_tab("Screen Home")
    self.db.save_lembrete(instance, describe, title, number_repeat)
    
  def start_lembrete(self, element):
    if(element.icon == 'play'):
      if(self.last_lembrete_start is not None and self.last_lembrete_start != element):
        self.db.set_lembrete_on_start(self.last_lembrete_start.id, False)
        self.last_lembrete_start.icon = 'play'        
      self.start_clock()
      self.db.set_lembrete_on_start(element.id, True)
      element.icon = 'stop'
      self.last_lembrete_start = element
    else:
      self.stop_clock()
      element.icon = 'play'
  def delete_lembrete(self,element):
    self.db.delete_lembrete(element.id)
    self.sm.get_screen("main").ids.bottom_navigation.switch_tab("Screen 4")
MainApp().run()