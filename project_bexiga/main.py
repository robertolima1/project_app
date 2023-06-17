import datetime
from kivymd.app import MDApp
from kivymd.uix.screenmanager import MDScreenManager
from dialog.validate_dialog import ValidateDialog
from dialog_content.instant_content.instant_content import InstantContent
from screens.ScreenMain.screen_main import ScreenMainView
from screens.ScreenWelcome.screen_welcome import ScreenWelcomeView
from screens.ScreenAlerta.screen_alerta import ScreenAlertaView
from screens.ScreenAlertaDescricao.screen_alerta_descricao import ScreenAlertaDescricao
from screens.ScreenLembreteDescricao.screen_lembrete_descricao import ScreenLembreteDescricao
from screens.ScreenTecnicaDescricao.screen_tecnica_descricao import ScreenTecnicaDescricao
from screens.ScreenAnotacaoDescricao.screen_anotacao_descricao import ScreenAnotacaoDescricao
from screens.ScreenNotificacao.screen_notificacao import ScreenNotificacao
from kivymd.uix.list import ThreeLineAvatarIconListItem,TwoLineAvatarIconListItem, IconRightWidget,IconLeftWidget, TwoLineListItem
from kivymd.uix.pickers import MDDatePicker
from repository.database_manager import DatabaseManager
from utils.clock_manager import ClockManager
from kivymd.uix.dialog import MDDialog
from kivymd.uix.label import MDLabel
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
    self.validateDialog = ValidateDialog()


  def build(self):
    self.theme_cls.theme_style = "Light"
    self.theme_cls.primary_palette = "Teal"
    
    self.sm.add_widget(ScreenWelcomeView())
    self.sm.add_widget(ScreenMainView())
    self.sm.add_widget(ScreenNotificacao())
    self.sm.add_widget(ScreenAlertaDescricao())
    self.sm.add_widget(ScreenLembreteDescricao())
    self.sm.add_widget(ScreenTecnicaDescricao())    
    self.sm.add_widget(ScreenAnotacaoDescricao())    
    
    return self.sm
  
  def on_start(self):    
    self.db.set_lembrete_all_on_start()

  def welcome(self):
    self.sm.get_screen("main").ids.bottom_navigation.switch_tab("Screen Home")    
           
  def setAlertDescribe(self, TwoLineListItem):    
    self.sm.get_screen("alerta-descricao").ids.alerta_title.text = TwoLineListItem.text
    self.sm.get_screen("alerta-descricao").ids.alerta_describe.text = TwoLineListItem.secondary_text
    self.sm.transition.direction = "left"
    self.sm.current = "alerta-descricao"

  def start_clock(self, lembrete_timestamp, number_count, element_item, lembrete_title):
    timestamp = datetime.datetime.strptime(lembrete_timestamp, '%Y-%m-%d %H:%M:%S').time()
    self.clock = ClockManager(1, 0, self.sm.get_screen("main"), timestamp, number_count, element_item, self.sm.get_screen("notificacao"), lembrete_title)    
    self.clock.start()
    
  def stop_clock(self):
    self.clock.stop()
    
  def on_save_time(self,instance, time):
    self.sm.get_screen("lembrete-descricao").ids.input_lembrete_instance.text = str(time)    
  
  def limpar_notificacao(self):
    self.sm.get_screen("notificacao").ids.list_notificacao.clear_widgets()
    self.sm.get_screen("main").ids.lembrete_alert.icon = f"images/icon-alert-love.png"
  def populate_screen(self, parent, screen_name):

    if(screen_name == "alerta"):
      alertas = self.db.getAllAlerta()
      parent.children[1].ids.list_alert.clear_widgets()
      for alerta in alertas:
        parent.children[1].ids.list_alert.add_widget(TwoLineListItem(text=alerta.alerta_title, secondary_text = alerta.alerta_describe , on_release= self.setAlertDescribe))
    
    elif(screen_name == 'anotacao'):
      anotacoes = self.db.getAllAnotacao()      
      parent.children[1].ids.list_anotacao.clear_widgets()
      
      for anotacao in anotacoes:
        icon_delete =IconRightWidget(icon = "trash-can-outline", on_release = self.delete_anotacao, id = anotacao.anotacao_id)      
        element = TwoLineAvatarIconListItem(id= anotacao.anotacao_id, text=anotacao.anotacao_title, secondary_text = f"{datetime.datetime.strptime(anotacao.insertion_date, '%Y-%m-%d %H:%M:%S').strftime('%d/%m/%Y')}", on_release = self.setAnotacaoDescribeListItem)       
        element.add_widget(icon_delete)
        parent.children[1].ids.list_anotacao.add_widget(element)
    elif(screen_name == 'tecnica'):          
      tecnicas = self.db.getAllTecnica()
      parent.children[1].ids.list_tecnica.clear_widgets()
      
      for tecnica in tecnicas:      
        parent.children[1].ids.list_tecnica.add_widget(TwoLineListItem(id= tecnica.tecnica_id, text=tecnica.tecnica_title, secondary_text = tecnica.tecnica_describe, on_release = self.setTecnicaDescribeListItem))       
        
    elif(screen_name == 'lembrete'):    
      self.populate_lembrete(parent) 

  def populate_lembrete(self, parent):
      lembretes = self.db.getAllLembrete()
      parent.children[1].ids.list_lembrete.clear_widgets()
      
      for lembrete in lembretes:      
        icon_play =IconLeftWidget(icon = "play", on_release = self.start_lembrete, id = lembrete.lembrete_id)
        icon_stop =IconLeftWidget(icon = "stop", on_release = self.start_lembrete, id = lembrete.lembrete_id)
        icon_delete =IconRightWidget(icon = "trash-can-outline", on_release = self.delete_lembrete, id = lembrete.lembrete_id)
        element = ThreeLineAvatarIconListItem(id = lembrete.lembrete_id, text=lembrete.lembrete_title, secondary_text = f"Repetições: {lembrete.lembrete_count_repeat}",tertiary_text = f"Tempo: {datetime.datetime.strptime(lembrete.lembrete_timestamp, '%Y-%m-%d %H:%M:%S').strftime('%H:%M:%S')}" ,  on_release= self.setLembreteDescribeListItem)
        if(lembrete.on_start):
          element.add_widget(icon_stop)
        else:
          element.add_widget(icon_play)
        element.add_widget(icon_delete)
        parent.children[1].ids.list_lembrete.add_widget(element)      
  
  def setAnotacaoDescribeListItem(self, TwoLineAvatarIconListItem):    
    anotacao = self.db.get_anotacao_by_id(TwoLineAvatarIconListItem.id)     
    insertion_date = datetime.datetime.strptime(anotacao.insertion_date, '%Y-%m-%d %H:%M:%S').date()
    self.sm.get_screen("anotacao-descricao").ids.input_title.text = anotacao.anotacao_title
    self.sm.get_screen("anotacao-descricao").ids.input_anotacao_id.text = anotacao.anotacao_id
    self.sm.get_screen("anotacao-descricao").ids.input_describe.text = anotacao.anotacao_describe
    self.sm.get_screen("anotacao-descricao").ids.input_data.text = str(insertion_date)
    
    self.setAnotacaoDescribe()

  def setAnotacaoDescribe(self, is_clear = False):    
    self.sm.transition.direction = "left"
    self.sm.current = "anotacao-descricao"     
    if(is_clear):
      self.sm.get_screen("anotacao-descricao").ids.input_title.text = ""
      self.sm.get_screen("anotacao-descricao").ids.input_describe.text = ""
      self.sm.get_screen("anotacao-descricao").ids.input_data.text = ""
      
  
  def setTecnicaDescribeListItem(self, TwoLineAvatarIconListItem):    
    tecnica = self.db.get_tecnica_by_id(TwoLineAvatarIconListItem.id)     
    self.sm.get_screen("tecnica-descricao").ids.tecnica_title.text = tecnica.tecnica_title
    self.sm.get_screen("tecnica-descricao").ids.tecnica_describe.text = tecnica.tecnica_describe
    self.sm.transition.direction = "left"
    self.sm.current = "tecnica-descricao"     
            
  def setLembreteDescribeListItem(self, TwoLineAvatarIconListItem):    
    lembrete = self.db.get_lembrete_by_id(TwoLineAvatarIconListItem.id) 
    timestamp = datetime.datetime.strptime(lembrete.lembrete_timestamp, '%Y-%m-%d %H:%M:%S').time()
    self.sm.get_screen("lembrete-descricao").ids.input_lembrete_id.text = lembrete.lembrete_id
    self.sm.get_screen("lembrete-descricao").ids.input_lembrete_title.text = lembrete.lembrete_title
    self.sm.get_screen("lembrete-descricao").ids.input_lembrete_instance.text = str(timestamp)
    self.sm.get_screen("lembrete-descricao").ids.input_lembrete_describe.text = lembrete.lembrete_describe
    self.sm.get_screen("lembrete-descricao").ids.input_lembrete_number_repeat.text = str(lembrete.lembrete_count_repeat)
    
    
    self.setLembreteDescribe()
            
  def setLembreteDescribe(self, is_clear = False):    
    self.sm.transition.direction = "left"
    self.sm.current = "lembrete-descricao"     
    if(is_clear):
      self.sm.get_screen("lembrete-descricao").ids.input_lembrete_id.text = ""
      self.sm.get_screen("lembrete-descricao").ids.input_lembrete_title.text = ""
      self.sm.get_screen("lembrete-descricao").ids.input_lembrete_instance.text = ""
      self.sm.get_screen("lembrete-descricao").ids.input_lembrete_describe.text = ""
      self.sm.get_screen("lembrete-descricao").ids.input_lembrete_number_repeat.text = ""
      
    
  def save_anotacao(self):
    anotacao_id = self.sm.get_screen("anotacao-descricao").ids.input_anotacao_id.text
      
    title = self.sm.get_screen("anotacao-descricao").ids.input_title.text
    describe = self.sm.get_screen("anotacao-descricao").ids.input_describe.text
    date = self.sm.get_screen("anotacao-descricao").ids.input_data.text
    if(not (title and describe and date)):
      self.validateDialog.show_validate_dialog("Necessário preencher todos os campos corretamente!")      
      return
    self.sm.get_screen("main").ids.bottom_navigation.switch_tab("Screen Home")
    if(anotacao_id== '' or anotacao_id is None):      
      self.db.save_anotacao(date, describe, title)
    else:
      
      self.db.update_anotacao(anotacao_id, describe, title, date)
    self.sm.transition.direction = "right"
    self.sm.current = "main"    
        
  def save_lembrete(self):
    lembrete_id = self.sm.get_screen("lembrete-descricao").ids.input_lembrete_id.text
    
    instance = self.sm.get_screen("lembrete-descricao").ids.input_lembrete_instance.text
    title = self.sm.get_screen("lembrete-descricao").ids.input_lembrete_title.text
    number_repeat = self.sm.get_screen("lembrete-descricao").ids.input_lembrete_number_repeat.text
    describe = self.sm.get_screen("lembrete-descricao").ids.input_lembrete_describe.text
    if(not (instance and title and number_repeat and describe ) or int(number_repeat)>6):
      self.validateDialog.show_validate_dialog("Necessário preencher todos os campos corretamente!")
      self.sm.get_screen("lembrete-descricao").ids.input_lembrete_number_repeat.error = True      
      return
    self.sm.get_screen("main").ids.bottom_navigation.switch_tab("Screen Home")
    if(lembrete_id== '' or lembrete_id is None):      
      self.db.save_lembrete(instance, describe, title, number_repeat)
    else:
      self.db.update_lembrete(lembrete_id, describe, title, number_repeat)
    self.sm.transition.direction = "right"
    self.sm.current = "main"    
    
  def start_lembrete(self, element):
    if(element.icon == 'play'):
      if(self.last_lembrete_start is not None and self.last_lembrete_start != element):
        self.db.set_lembrete_on_start(self.last_lembrete_start.id, False)
        self.last_lembrete_start.icon = 'play'        
      lembrete = self.db.get_lembrete_by_id(element.id)
      self.start_clock(lembrete.lembrete_timestamp, lembrete.lembrete_count_repeat, element, lembrete.lembrete_title)
      self.db.set_lembrete_on_start(element.id, True)
      element.icon = 'stop'
      self.last_lembrete_start = element
    else:
      self.stop_clock()
      element.icon = 'play'
  def delete_lembrete(self,element):
    self.db.delete_lembrete(element.id)
    self.sm.get_screen("main").ids.bottom_navigation.switch_tab("Screen 4")
 
  def delete_anotacao(self,element):
    self.db.delete_anotacao(element.id)
    self.sm.get_screen("main").ids.bottom_navigation.switch_tab("Screen 5")
  
  
  def cancel_dialog(self, obj):
    if self.dialog:
      self.dialog.dismiss()
  
  def confirm_dialog(self,obj):
    if self.dialog:
      try:
        time = None
        minutes = int(self.dialog.content_cls.ids.input_minuto.text)
        hours = int(self.dialog.content_cls.ids.input_hora.text)      
        time = str(datetime.time(hour=hours,minute=minutes))
        self.dialog.content_cls.ids.instant_error.text = ""
        self.sm.get_screen("lembrete-descricao").ids.input_lembrete_instance.text = time
        self.dialog.dismiss()
      except:
        self.dialog.content_cls.ids.instant_error.text = "Digitar um tempo válido"
        self.dialog.content_cls.ids.input_minuto.text = ""
        self.dialog.content_cls.ids.input_hora.text = ""
        pass
      
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
        
  def on_save(self, instance, value, date_range):    
    self.sm.get_screen("anotacao-descricao").ids.input_data.text = str(value)
    

  def on_cancel(self, instance, value):
      '''Events called when the "CANCEL" dialog box button is clicked.'''

  def show_date_picker(self):
    date_dialog = MDDatePicker(
      title= "Selecione o Dia",
       min_year = datetime.date.today().year,                                 
    )
    date_dialog.bind(on_save=self.on_save, on_cancel=self.on_cancel)
    date_dialog.open()

MainApp().run()