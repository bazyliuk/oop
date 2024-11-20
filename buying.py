from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import Screen
from models import Tickets, session


class Screen1(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical', spacing=10, padding=10)

        self.route_input = TextInput(hint_text="Route", multiline=False)
        self.layout.add_widget(self.route_input)

        self.price_input = TextInput(hint_text="Price", multiline=False, input_filter='float')
        self.layout.add_widget(self.price_input)

        self.currency_input = TextInput(hint_text="Currency (e.g., USD)", multiline=False)
        self.layout.add_widget(self.currency_input)

        self.buyer_input = TextInput(hint_text="Buyer Name", multiline=False)
        self.layout.add_widget(self.buyer_input)

        self.plane_input = TextInput(hint_text="Plane Number", multiline=False, input_filter='int')
        self.layout.add_widget(self.plane_input)

        self.additional_input = TextInput(hint_text="Additional Info (e.g., luggage=extra)", multiline=False)
        self.layout.add_widget(self.additional_input)

        save_button = Button(text="Buy Ticket")
        save_button.bind(on_press=self.save_ticket)
        self.layout.add_widget(save_button)

        back_button = Button(text="Back to Main")
        back_button.bind(on_press=self.go_to_main)
        self.layout.add_widget(back_button)

        self.add_widget(self.layout)

    def save_ticket(self, instance):
        try:
            new_ticket = Tickets(
                price=float(self.price_input.text),
                currency=self.currency_input.text,
                route=self.route_input.text,
                buyer=self.buyer_input.text,
                plane=int(self.plane_input.text),
                additionaly=self.additional_input.text or None
            )
            session.add(new_ticket)
            session.commit()
            self.route_input.text = ""
            self.price_input.text = ""
            self.currency_input.text = ""
            self.buyer_input.text = ""
            self.plane_input.text = ""
            self.additional_input.text = ""
            print("Ticket bought successfully!")
        except Exception as e:
            print(f"Error saving ticket: {e}")

    def go_to_main(self, instance):
        self.manager.current = 'Main'
