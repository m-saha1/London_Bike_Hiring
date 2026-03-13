from pydantic import BaseModel, ConfigDict
from datetime import datetime


class JourneyBase(BaseModel):

    start_date: datetime
    start_station: str
    end_station: str
    bike_number: int
    total_duration: int


class JourneyOut(JourneyBase):

    model_config = ConfigDict(from_attributes=True)

    journey_id: int