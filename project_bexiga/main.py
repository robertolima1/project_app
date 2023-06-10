import datetime
from kivymd.app import MDApp
from kivymd.uix.screenmanager import MDScreenManager
from dialog_content.instant_content.instant_content import InstantContent
from screens.ScreenMain.screen_main import ScreenMainView
from screens.ScreenWelcome.screen_welcome import ScreenWelcomeView
from screens.ScreenAlerta.screen_alerta import ScreenAlertaView
from screens.ScreenAlertaDescricao.screen_alerta_descricao import ScreenAlertaDescricao
from screens.ScreenLembreteDescricao.screen_lembrete_descricao import ScreenLembreteDescricao
from kivymd.uix.list import TwoLineAvatarIconListItem, IconRightWidget,IconLeftWidget, TwoLineListItem
from kivymd.uix.pickers import MDDatePicker,MDTimePicker
from repository.database_manager import DatabaseManager
from utils.clock_manager import ClockManager
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton

class MainApp(MDApp):
  def __init__(self, **kwargs):
    super().__init__(**kwargs)
    self.sm = MDScreenManager()  
    self.load_all_kv_files(self.directory) 
    self.db = DatabaseManager()   
    self.clock = None
    self.last_lembrete_start = None
    self.dialog = None


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

  def start_clock(self, lembrete_timestamp, number_count):
    timestamp = datetime.datetime.strptime(lembrete_timestamp, '%Y-%m-%d %H:%M:%S').time()
    self.clock = ClockManager(1, 0, self.sm.get_screen("main").ids.count, timestamp, number_count)    
    self.clock.start()
    
  def stop_clock(self):
    self.clock.stop()
    
  def on_save_time(self,instance, time):
    self.sm.get_screen("lembrete-descricao").ids.input_lembrete_instance.text = str(time)    
  
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
      lembrete = self.db.get_lembrete_by_id(element.id)
      self.start_clock(lembrete.lembrete_timestamp, lembrete.lembrete_count_repeat)
      self.db.set_lembrete_on_start(element.id, True)
      element.icon = 'stop'
      self.last_lembrete_start = element
    else:
      self.stop_clock()
      element.icon = 'play'
  def delete_lembrete(self,element):
    self.db.delete_lembrete(element.id)
    self.sm.get_screen("main").ids.bottom_navigation.switch_tab("Screen 4")
  
  def cancel_dialog(self, obj):
    if self.dialog:
      self.dialog.dismiss()
  
  def confirm_dialog(self,obj):
    if self.dialog:
      minutes = int(self.dialog.content_cls.children[0].text)
      hours = int(self.dialog.content_cls.children[2].text)      
      self.sm.get_screen("lembrete-descricao").ids.input_lembrete_instance.text = str(datetime.time(hour=hours,minute=minutes))
      self.dialog.dismiss()
      
  def show_confirmation_dialog(self):
    if not self.dialog:
        self.dialog = MDDialog(
            title="Digite o tempo do lembrete",
            radius=[20, 7, 20, 7],
            type="custom",
            content_cls=InstantContent(),
            buttons=[
                MDFlatButton(
                    id = "input_dialog_hours",
                    text="CANCEL",
                    theme_text_color="Custom",
                    text_color=self.theme_cls.primary_color,
                    on_release = self.cancel_dialog
                ),
                MDFlatButton(
                    id = "input_dialog_minute",
                    text="OK",
                    theme_text_color="Custom",
                    text_color=self.theme_cls.primary_color,
                    on_release = self.confirm_dialog
                ),
            ],
        )
    self.dialog.open()
    


MainApp().run()