from sqlalchemy import Column,Integer,String,DateTime,func
from app.database.session import Base

class Vehicle(Base):
    __tablename__ = "vehicle"
    id = Column(Integer,primary_key=True)
    number = Column(String,nullable=False)
    created_at = Column(DateTime(timezone=True),server_default=func.now(),nullable=False)
    updated_at = Column(DateTime(timezone=True),server_default=func.now(),onupdate=func.now(),nullable=False)


