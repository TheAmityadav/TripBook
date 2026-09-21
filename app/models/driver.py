from sqlalchemy import Column,String,Integer,DateTime,func
from app.database.session import Base

class Driver(Base):
    __tablename__ = "driver"
    id = Column(Integer,primary_key=True)
    name = Column(String,nullable=False)
    phone = Column(String,nullable=True)
    created_at = Column(DateTime(timezone=True),server_default=func.now(),nullable=False)
    updated_at = Column(DateTime(timezone=True),server_default=func.now(),onupdate=func.now(),nullable=False)
