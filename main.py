import kivy
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from screens import SplashScreen, MainScreen
from buying import Screen1
from screen2 import Screen2
from calculator import Screen3



kivy.require('2.3.0')

class MyApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.icon = 'airplane-ticket.png'


    def build(self):
        sm = ScreenManager()
        sm.add_widget(SplashScreen(name="Splash"))
        sm.add_widget(MainScreen(name="Main"))
        sm.current = "Splash"
        sm.add_widget(MainScreen(name='Main'))
        sm.add_widget(Screen1(name='Buying_a_ticket'))
        sm.add_widget(Screen2(name='Arrival_board'))
        sm.add_widget(Screen3(name='Calculator'))
        return sm

if __name__ =='__main__':
    MyApp().run()


