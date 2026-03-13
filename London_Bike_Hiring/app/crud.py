from sqlalchemy.orm import Session
from app.models import CycleJourney


def get_journeys(db: Session, limit: int = 100):

    return db.query(CycleJourney).limit(limit).all()


def get_journey(db: Session, journey_id: int):

    return db.query(CycleJourney).filter(
        CycleJourney.journey_id == journey_id
    ).first()


def get_top_routes(db: Session):

    result = db.execute("""
        SELECT start_station, end_station, COUNT(*) as trips
        FROM cycle_journeys
        GROUP BY start_station, end_station
        ORDER BY trips DESC
        LIMIT 20
    """)

    return result.fetchall()