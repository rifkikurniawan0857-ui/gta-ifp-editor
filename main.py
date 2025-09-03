"""
Main entry point for GTA SA IFP Editor APK
"""

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.metrics import dp

import os

class MainScreen(BoxLayout):
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = dp(20)
        self.spacing = dp(15)
        
        # Title
        title = Label(
            text='GTA SA IFP Editor', 
            size_hint_y=None, 
            height=dp(60),
            font_size=dp(24),
            bold=True
        )
        self.add_widget(title)
        
        # Description
        desc = Label(
            text='Create and edit GTA San Andreas animation files (.ifp)',
            size_hint_y=None,
            height=dp(80),
            text_size=(None, None)
        )
        self.add_widget(desc)
        
        # Buttons layout
        buttons_layout = BoxLayout(
            orientation='vertical',
            spacing=dp(10),
            size_hint_y=None,
            height=dp(300)
        )
        
        # Create New IFP button
        create_btn = Button(
            text='Create New IFP',
            size_hint_y=None,
            height=dp(60),
            font_size=dp(16)
        )
        create_btn.bind(on_press=self.create_new_ifp)
        buttons_layout.add_widget(create_btn)
        
        # Open IFP button
        open_btn = Button(
            text='Open IFP File',
            size_hint_y=None,
            height=dp(60),
            font_size=dp(16)
        )
        open_btn.bind(on_press=self.open_ifp)
        buttons_layout.add_widget(open_btn)
        
        # Save IFP button
        save_btn = Button(
            text='Save IFP File',
            size_hint_y=None,
            height=dp(60),
            font_size=dp(16)
        )
        save_btn.bind(on_press=self.save_ifp)
        buttons_layout.add_widget(save_btn)
        
        # Exit button
        exit_btn = Button(
            text='Exit',
            size_hint_y=None,
            height=dp(60),
            font_size=dp(16)
        )
        exit_btn.bind(on_press=self.exit_app)
        buttons_layout.add_widget(exit_btn)
        
        self.add_widget(buttons_layout)
        
        # Status label
        self.status_label = Label(
            text='Ready',
            size_hint_y=None,
            height=dp(40)
        )
        self.add_widget(self.status_label)
        
        # Info
        info = Label(
            text='GTA SA IFP Editor v0.1\\nSupports ANP3 and ANPK formats',
            size_hint_y=None,
            height=dp(60),
            text_size=(None, None)
        )
        self.add_widget(info)
    
    def show_popup(self, title, message):
        """Show a popup message"""
        popup_content = BoxLayout(orientation='vertical', padding=dp(10), spacing=dp(10))
        popup_content.add_widget(Label(text=message))
        
        close_btn = Button(text='Close', size_hint_y=None, height=dp(50))
        popup_content.add_widget(close_btn)
        
        popup = Popup(title=title, content=popup_content, size_hint=(0.8, 0.4))
        close_btn.bind(on_press=popup.dismiss)
        popup.open()
    
    def create_new_ifp(self, instance):
        """Create a new IFP file"""
        self.status_label.text = 'Creating new IFP...'
        self.show_popup('Info', 'In the full version, this would create a new IFP file.\\n\\nFor now, this is a demonstration interface.')
        self.status_label.text = 'Ready'
    
    def open_ifp(self, instance):
        """Open an existing IFP file"""
        self.status_label.text = 'Opening IFP...'
        self.show_popup('Info', 'In the full version, this would open an IFP file.\\n\\nFor now, this is a demonstration interface.')
        self.status_label.text = 'Ready'
    
    def save_ifp(self, instance):
        """Save the current IFP file"""
        self.status_label.text = 'Saving IFP...'
        self.show_popup('Info', 'In the full version, this would save the IFP file.\\n\\nFor now, this is a demonstration interface.')
        self.status_label.text = 'Ready'
    
    def exit_app(self, instance):
        """Exit the application"""
        App.get_running_app().stop()

class GTASAIFPEditorApp(App):
    def build(self):
        return MainScreen()

if __name__ == '__main__':
    GTASAIFPEditorApp().run()