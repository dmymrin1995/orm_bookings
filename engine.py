from model import Aircrafts, Airports, BoardingPasses
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine("<>")

Session = sessionmaker()
Session.configure(bind=engine)

session = Session()

aircrafts = session.query(BoardingPasses).where(BoardingPasses.seat_no == "23B")

for a in aircrafts:
    print(a)
