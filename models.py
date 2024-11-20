from sqlalchemy import create_engine, Column, Integer, String, PickleType, Numeric
from sqlalchemy.orm import sessionmaker,declarative_base

Base = declarative_base()

class Tickets(Base):
    __tablename__ = 'tickets'
    id = Column(Integer, primary_key=True)
    price = Column(Numeric(10,2), nullable=False)
    currency = Column(String(3), default='USD', nullable=False)
    route = Column(String(100), nullable=False)
    buyer = Column(String(100), nullable=False)
    plane = Column(Integer, nullable=False)
    additionaly = Column(PickleType, nullable=True)




engine = create_engine('sqlite:///local_data.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

#Function for creating basic categories

def create_default_tickets():
    existing_tickets = session.query(Tickets).count()  # Перевіряємо, чи вже є квитки
    if existing_tickets > 0:
        print("Default tickets already exist.")
        return

    data = [
        {"price": 2000, "currency": "EUR", "route": "Zhytomyr-Milan", "buyer": "Ivanenko", "plane": 2435, "additionally": None},
        {"price": 1500, "route": "Kyiv-Lviv", "buyer": "Petrenko", "plane": 1234, "additionally": {"luggage": "extra"}},
        {"price": 3000, "route": "Odesa-Paris", "buyer": "Shevchenko", "plane": 6789, "additionally": {"meals": "vegan"}},
        {"price": 2500, "route": "Dnipro-Berlin", "buyer": "Kovalenko", "plane": 5678, "additionally": {"seat": "window"}},
        {"price": 1800, "route": "Kharkiv-Prague", "buyer": "Boyko", "plane": 3456, "additionally": None},
    ]

    for cat in data:
        new_ticket = Tickets(
            price=cat["price"],
            currency=cat.get("currency", "USD"),
            route=cat["route"],
            buyer=cat["buyer"],
            plane=cat["plane"],
            additionaly=cat["additionally"]
        )
        session.add(new_ticket)

    session.commit()
    print("The main tickets have been created.")
