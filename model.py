from sqlalchemy.orm import declarative_base
from sqlalchemy import (
    Column,
    Integer,
    String,
    CHAR,
    MetaData,
    VARCHAR,
    ForeignKey,
    UniqueConstraint,
)
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
    total_amount = Column(NUMERIC(10, 2), nullable=False)

    def __repr__(self):
        return "<Bookings(book_ref='%s', book_date='%s', total_amount='%s')>" % (
            self.book_ref,
            self.book_date,
            self.total_amount,
        )


class Flights(Base):
    __tablename__ = "flights"

    flight_id = Column(Integer, nullable=False, primary_key=True)
    flight_no = Column(
        CHAR(6),
        ForeignKey("aircrafts.aircraft_code"),
        nullable=False,
    )
    scheduled_departure = Column(TIMESTAMP(timezone=True), nullable=False)
    scheduled_arrival = Column(TIMESTAMP(timezone=True), nullable=False)
    departure_airport = Column(
        CHAR(3), ForeignKey("airports.airport_code"), nullable=False
    )
    arrival_airport = Column(
        CHAR(3), ForeignKey("airports.airport_code"), nullable=False
    )
    status = Column(VARCHAR(20), nullable=False)
    aircraft_code = Column(CHAR(3), nullable=False)
    actual_departure = Column(TIMESTAMP(timezone=True), nullable=True)
    actual_arrival = Column(TIMESTAMP(timezone=True), nullable=True)

    __table_args__ = tuple(UniqueConstraint("flight_no", "scheduled_departure"))

    def __repr__(self):
        return (
            "<Flights(flight_id='%s', flight_no='%s', scheduled_departure='%s', scheduled_arrival='%s', departure_airport='%s', arrival_airport='%s', \
                status='%s', aircraft_code='%s', actual_departure='%s', actual_arrival='%s')>"
            % (
                self.flight_id,
                self.flight_no,
                self.scheduled_departure,
                self.scheduled_arrival,
                self.departure_airport,
                self.arrival_airport,
                self.status,
                self.aircraft_code,
                self.actual_departure,
                self.actual_arrival,
            )
        )


class Seats(Base):
    __tablename__ = "seats"

    aircraft_code = Column(CHAR(3), primary_key=True, nullable=False)
    seat_no = Column(VARCHAR(4), nullable=False)
    fare_conditions = Column(VARCHAR(10), nullable=False)

    def __repr__(self):
        return "<Flights(aircraft_code='%s', seat_no='%s', fare_conditions='%s')>" % (
            self.aircraft_code,
            self.fare_conditions,
            self.seat_no,
        )
