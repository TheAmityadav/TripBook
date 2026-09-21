from pydantic import BaseModel

class DriverCreate(BaseModel):
    name : str
    phone : str | None

class DriverResponse(BaseModel):
    name : str
    phone : str