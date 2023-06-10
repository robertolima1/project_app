from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivymd.theming import ThemeManager

class DialogConfirmation():
  dialog = None
  
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
    
    
    
  