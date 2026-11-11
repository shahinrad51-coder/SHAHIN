from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class SHAHINApp(App):
    def build(self):
        self.title = "SHAHIN C2 Monitor"
        
        layout = BoxLayout(orientation='vertical', padding=20, spacing=15)
        
        self.header = Label(
            text="[b]SHAHIN CYBER SYSTEM[/b]", 
            markup=True, 
            font_size='22sp', 
            size_hint_y=None, 
            height=50
        )
        layout.add_widget(self.header)
        
        self.status_input = TextInput(
            text="System Initialized. Engineer SHAHIN node online...", 
            readonly=True, 
            size_hint_y=0.6
        )
        layout.add_widget(self.status_input)
        
        self.btn = Button(
            text="Initialize Secure Scan", 
            size_hint_y=None, 
            height=60,
            background_color=(0.1, 0.6, 0.2, 1)
        )
        self.btn.bind(on_press=self.on_scan_click)
        layout.add_widget(self.btn)
        
        return layout

    def on_scan_click(self, instance):
        self.status_input.text += "\n[+] Executing telemetry & secure socket protocol..."

if __name__ == '__main__':
    SHAHINApp().run()
