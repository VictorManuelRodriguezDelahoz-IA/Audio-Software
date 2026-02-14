from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base_class import Base


class Match(Base):
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True, nullable=False)
    description = Column(String, nullable=True)
    date = Column(DateTime, nullable=False)
    location_name = Column(String, nullable=False)
    price_per_person = Column(Float, default=0.0)
    players_total = Column(Integer, default=10)
    players_current = Column(Integer, default=0)
    organizer_id = Column(Integer, ForeignKey("user.id"), nullable=False)

    organizer = relationship("User", back_populates="matches")
