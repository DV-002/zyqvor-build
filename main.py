from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.core.window import Window

class ZyqvorgramApp(App):
    def build(self):
        # Делаем черный фон, как в терминале
        Window.clearcolor = (0, 0, 0, 1)
        
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        # Область, где будут сообщения
        self.chat_logs = Label(
            text="[System] Добро пожаловать в Zyqvorgram!\n",
            color=(0, 1, 0, 1), # Зеленый текст
            valign='top',
            halign='left',
            text_size=(Window.width - 20, None)
        )
        layout.add_widget(self.chat_logs)

        # ПОЛЕ ВВОДА (оно вызовет клавиатуру!)
        self.input_data = TextInput(
            multiline=False,
            size_hint_y=None,
            height=50,
            background_color=(0.1, 0.1, 0.1, 1),
            foreground_color=(1, 1, 1, 1),
            hint_text="Напиши что-нибудь..."
        )
        self.input_data.bind(on_text_validate=self.send_message)
        layout.add_widget(self.input_data)
        
        return layout

    def send_message(self, instance):
        if self.input_data.text:
            new_text = f"Вы: {self.input_data.text}\n"
            self.chat_logs.text += new_text
            self.input_data.text = "" # Очистить после отправки

if __name__ == "__main__":
    ZyqvorgramApp().run()
