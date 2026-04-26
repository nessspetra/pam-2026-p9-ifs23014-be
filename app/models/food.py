from sqlalchemy import Column, Integer, Text, DateTime, ForeignKey
from datetime import datetime, timezone
from app.extensions import Base

class Food(Base):
    __tablename__ = "foods"

    id = Column(Integer, primary_key=True)
    description = Column(Text)  # Menggantikan text
    request_id = Column(Integer, ForeignKey("requests.id"))
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))