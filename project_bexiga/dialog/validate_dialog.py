from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivymd.theming import ThemeManager
from kivymd.uix.label import MDLabel
class ValidateDialog():
  dialog = None
  
  def confirm_dialog(self,obj):    
    self.dialog.dismiss()
      
  
  def show_validate_dialog(self, message):
    if not self.dialog:
        self.dialog = MDDialog(
            title="Atenção!",
            radius=[20, 7, 20, 7],
            type="custom",
            content_cls=MDLabel(text= message),
            buttons=[                
                MDFlatButton(                    
                    text="OK",
                    theme_text_color="Custom",
                    text_color=ThemeManager().primary_color,
                    on_release = self.confirm_dialog
                ),
            ],
        )
    self.dialog.open()
    
    
    
  