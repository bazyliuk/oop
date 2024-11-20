from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen
from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.animation import Animation

class SplashScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Додаємо фон заставки
        self.background = Image(source="sky-dawn.jpg", allow_stretch=True, keep_ratio=False)
        self.add_widget(self.background)

        # Додаємо літак
        self.plane = Image(source="rb_20516.png", size_hint=(None, None), size=(500, 500))
        self.plane.pos = (-self.plane.width, Window.height // 2)
        self.add_widget(self.plane)

        # Запуск анімації літака
        self.start_animation()

    def start_animation(self):
        # Анімація літака з лівого до правого боку екрана
        animation = Animation(x=Window.width, duration=3)
        animation.bind(on_complete=self.on_animation_complete)
        animation.start(self.plane)


    def on_animation_complete(self, *args):
        # Перехід на головну сторінку
        self.manager.current = "Main"

class MainScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', spacing=20, padding=10)

        question = Label(text="Choose an action",
                         font_size = 48,
                         color = (1,1,1,1))
        layout.add_widget(question)


        button1 = Button(text ='Buy_a_ticket', size_hint=(1,0.3))
        button1.bind(on_press=self.goto_screen1)
        layout.add_widget(button1)

        button2 = Button(text='Arrival_board', size_hint=(1,0.3))
        button2.bind(on_press=self.goto_screen2)
        layout.add_widget(button2)

        button3 = Button(text='Calculator', size_hint=(1,0.3))
        button3.bind(on_press=self.goto_screen3)
        layout.add_widget(button3)

        self.add_widget(layout)

    def goto_screen1(self, instance):
        self.manager.current = 'Buying_a_ticket'
    def goto_screen2(self, instance):
        self.manager.current = 'Arrival_board'
    def goto_screen3(self, instance):
        self.manager.current = 'Calculator'



