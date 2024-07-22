from pydantic import BaseModel
from datetime import datetime
from enum import Enum
from app.schemas.message import ApiResponse


class DeviceTypeEnum(Enum):
    mobile = "mobile"
    desktop = "desktop"

class SegmentBase(BaseModel):
    title: str
    content: str

class segmentCreate(BaseModel):
    name : str
    category : str
    country : str
    start_date : datetime
    end_date : datetime
    language : str
    device_type : DeviceTypeEnum
    site_identifier : str

class segmentUpdate(BaseModel):
    name : str
    category : str
    country : str
    start_date : datetime
    end_date : datetime
    language : str
    device_type : DeviceTypeEnum
    site_identifier : str


class SegmentResponse(ApiResponse):
    message: str = "User API Response"
    data: str =  "Success"