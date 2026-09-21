from pydantic import BaseModel,ConfigDict

class VehicleCreate(BaseModel):
    vehicle_number : str

class VehicleResponse(BaseModel):
    id : int
    number : str

    model_config = ConfigDict(from_attributes = True)