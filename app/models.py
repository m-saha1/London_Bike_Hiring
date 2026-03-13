from sqlalchemy import Column, Integer, String, BigInteger, DateTime
from app.database import Base


class CycleJourney(Base):

    __tablename__ = "cycle_journeys"

    journey_id = Column(BigInteger, primary_key=True)
    start_date = Column(DateTime)
    start_station_id = Column(Integer)
    start_station = Column(String)
    end_date = Column(DateTime)
    end_station_id = Column(Integer)
    end_station = Column(String)
    bike_number = Column(Integer)
    bike_model = Column(String)
    total_duration = Column(String)
    total_duration_ms = Column(BigInteger)