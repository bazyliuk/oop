from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen
from kivy.uix.scrollview import ScrollView
from models import Tickets, session
from models import create_default_tickets
import random


create_default_tickets()




class Screen2(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical', spacing=10, padding=10)

        self.refresh_button = Button(text="Refresh Board")
        self.refresh_button.bind(on_press=self.display_random_tickets)
        self.layout.add_widget(self.refresh_button)

        # Додаємо прокручуваний борд
        self.board = BoxLayout(orientation='vertical', spacing=5, size_hint=(1, None), height=300)
        self.board.bind(minimum_height=self.board.setter('height'))
        scroll = ScrollView(size_hint=(1, 1))
        scroll.add_widget(self.board)
        self.layout.add_widget(scroll)

        back_button = Button(text="Back to Main")
        back_button.bind(on_press=self.go_to_main)
        self.layout.add_widget(back_button)

        self.add_widget(self.layout)
        self.display_random_tickets()

    def display_random_tickets(self, instance=None):
        self.board.clear_widgets()
        tickets = session.query(Tickets).all()

        if not tickets:
            self.board.add_widget(Label(text="No tickets available", size_hint_y=None, height=30))
            return

        random_tickets = random.sample(tickets, min(5, len(tickets)))

        for ticket in random_tickets:
            ticket_label = Label(
                text=f"{ticket.route} | {ticket.price} {ticket.currency} | Buyer: {ticket.buyer}",
                size_hint_y=None,
                height=30
            )
            self.board.add_widget(ticket_label)

    def go_to_main(self, instance):
        self.manager.current = 'Main'
