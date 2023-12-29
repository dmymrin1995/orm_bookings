from model import Aircrafts, Airports, BoardingPasses, Bookings, Flights
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine("")

Session = sessionmaker()
Session.configure(bind=engine)

session = Session()

aircrafts = session.query(Flights).all()

for a in aircrafts:
    print(a)
