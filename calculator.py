from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import Screen


class Screen3(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical', spacing=10, padding=10)

        self.solution = TextInput(readonly=True, halign='right', font_size=55)
        self.layout.add_widget(self.solution)

        buttons = [
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "+"],
            [".", "0", "C", "-"],
        ]

        for row in buttons:
            row_layout = BoxLayout()
            for label in row:
                button = Button(text=label)
                button.bind(on_press=self.on_button_press)
                row_layout.add_widget(button)
            self.layout.add_widget(row_layout)

        equal_button = Button(text="=")
        equal_button.bind(on_press=self.on_solution)
        self.layout.add_widget(equal_button)

        back_button = Button(text="Back to Main")
        back_button.bind(on_press=self.go_to_main)
        self.layout.add_widget(back_button)

        self.add_widget(self.layout)

    def on_button_press(self, instance):
        text = instance.text
        if text == "C":
            self.solution.text = ""
        else:
            self.solution.text += text

    def on_solution(self, instance):
        try:
            self.solution.text = str(eval(self.solution.text))
        except Exception:
            self.solution.text = "Error"

    def go_to_main(self, instance):
        self.manager.current = 'Main'
