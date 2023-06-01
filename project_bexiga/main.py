from kivymd.app import MDApp
from kivymd.uix.screenmanager import MDScreenManager
from screens.ScreenMain.screen_main import ScreenMainView
from screens.ScreenAlerta.screen_alerta import ScreenAlertaView

class MainApp(MDApp):
  def __init__(self, **kwargs):
    super().__init__(**kwargs)
    self.sm = MDScreenManager()  
    self.load_all_kv_files(self.directory)    

  def build(self):
    self.sm.add_widget(ScreenMainView())
    self.sm.add_widget(ScreenAlertaView())
    
    return self.sm
  
  def manage_title(self):
    print("TESTE")
  
  
MainApp().run()