from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, CHAR, MetaData, VARCHAR
from sqlalchemy.dialects.postgresql import TIMESTAMP, NUMERIC


Base = declarative_base(metadata=MetaData(schema="bookings"))


class Aircrafts(Base):
    __tablename__ = "aircrafts"

    aircraft_code = Column(CHAR(3), nullable=False, primary_key=True)
    model = Column(String, nullable=False)
    range = Column(Integer, nullable=False)

    def __repr__(self):
        return "<Aircrafts(aircraft_code='%s', model='%s', range='%s')>" % (
            self.aircraft_code,
            self.model,
            self.range,
        )


class Airports(Base):
    __tablename__ = "airports"

    airport_code = Column(CHAR(3), nullable=False, primary_key=True)
    airport_name = Column(String, nullable=False)
    city = Column(String, nullable=False)
    coordinates = Column(String, nullable=False)
    timezone = Column(String, nullable=False)

    def __repr__(self):
        return (
            "<Airports(airport_code='%s', airport_name='%s', city='%s', coordinates='%s', timezone='%s')>"
            % (
                self.airport_code,
                self.airport_name,
                self.city,
                self.coordinates,
                self.timezone,
            )
        )


class BoardingPasses(Base):
    __tablename__ = "boarding_passes"

    ticket_no = Column(CHAR(13), primary_key=True, nullable=False)
    flight_id = Column(Integer, nullable=False)
    boarding_no = Column(Integer, nullable=False)
    seat_no = Column(VARCHAR(4), nullable=False)

    def __repr__(self):
        return (
            "<BoardingPasses(ticket_no='%s', flight_id='%s', boarding_no='%s', seat_no='%s')>"
            % (
                self.ticket_no,
                self.flight_id,
                self.boarding_no,
                self.seat_no,
            )
        )


class Bookings(Base):
    __tablename__ = "bookings"

    book_ref = Column(CHAR(6), primary_key=True, nullable=False)
    book_date = Column(TIMESTAMP(timezone=True), nullable=False)
    total_amount = Column(NUMERIC(10, 2), nullable=True)

    def __repr__(self):
        return "<Bookings(book_ref='%s', book_date='%s', total_amount='%s')>" % (
            self.book_ref,
            self.book_date,
            self.total_amount,
        )
