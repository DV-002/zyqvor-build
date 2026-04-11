from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label

class ZyqvorgramApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=10)
        
        # Поле для вывода сообщений
        self.chat_logs = Label(text="Welcome to Zyqvorgram!\n", halign="left", valign="top")
        layout.add_widget(self.chat_logs)
        
        # Поле для ввода текста
        self.message_input = TextInput(hint_text="Type a message...", multiline=False)
        layout.add_widget(self.message_input)
        
        # Кнопка отправки
        send_btn = Button(text="Send", size_hint_y=None, height=50)
        send_btn.bind(on_press=self.send_message)
        layout.add_widget(send_btn)
        
        return layout

    def send_message(self, instance):
        msg = self.message_input.text
        if msg:
            self.chat_logs.text += f"You: {msg}\n"
            self.message_input.text = ""

if __name__ == "__main__":
    ZyqvorgramApp().run()
