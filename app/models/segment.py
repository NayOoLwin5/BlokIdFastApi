from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, Enum as SQLAlchemyEnum
from app.models.common import DateTimeModelMixin
from app.models.rwmodel import RWModel
from enum import Enum


class DeviceTypeEnum(Enum):
    mobile = "mobile"
    desktop = "desktop"

class Segment(DateTimeModelMixin, RWModel):
    __tablename__ = "segment"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False, default='')
    category = Column(String(255), index=True, nullable=False)
    country = Column(String(255), nullable=False)
    start_date = Column(DateTime, default=datetime.utcnow)
    end_date = Column(DateTime, default=datetime.utcnow)
    language = Column(String(255), nullable=True)
    device_type = Column(SQLAlchemyEnum(DeviceTypeEnum), nullable=True)
    site_identifier = Column(String, nullable=True)