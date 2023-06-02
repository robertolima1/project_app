from kivymd.app import MDApp
from kivymd.uix.screenmanager import MDScreenManager
from screens.ScreenMain.screen_main import ScreenMainView
from screens.ScreenAlerta.screen_alerta import ScreenAlertaView
from screens.ScreenAlertaDescricao.screen_alerta_descricao import ScreenAlertaDescricao
from kivymd.uix.list import TwoLineListItem


class MainApp(MDApp):
  def __init__(self, **kwargs):
    super().__init__(**kwargs)
    self.sm = MDScreenManager()  
    self.load_all_kv_files(self.directory)    

  def build(self):
    self.sm.add_widget(ScreenMainView())
    self.sm.add_widget(ScreenAlertaView())
    self.sm.add_widget(ScreenAlertaDescricao())
    
    return self.sm
  
  def on_start(self):
    for i in range (20):
       self.sm.get_screen("alerta").ids.list_alert.add_widget(TwoLineListItem(text=f'Alerta {i}', secondary_text = "Lorem ipsum dolor sit amet, consectetur adipisci elit, sed eiusmod tempor incidunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur.", on_release= self.setAlertDescribe))
  
  def setAlertDescribe(self, onelinelistitem):
    self.sm.transition.direction = "left"
    self.sm.current = "alerta-descricao"
  
MainApp().run()