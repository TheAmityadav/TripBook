from fastapi import APIRouter,Depends,HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import select
from app.schemas.vehicle import VehicleCreate,VehicleResponse
from app.models.vehicle import Vehicle

from app.database.session import get_db

router = APIRouter()

@router.get("/",response_model=list[VehicleResponse])
def get_vehciles(db : Session = Depends(get_db)):
    return db.execute(select(Vehicle)).scalars().all()

    

@router.get("/{id}",response_model=VehicleResponse)
def get_vehicle(id:int, db : Session = Depends(get_db)):
    vehicle = db.execute(select(Vehicle).where(Vehicle.id == id)).scalar_one_or_none()
    if not vehicle:
        raise HTTPException(status_code=404,detail=f"vehicle not found")
    return vehicle

@router.post("/")
def add_vehicle(vehicle : VehicleCreate, db : Session = Depends(get_db)):
    print(f"Vehcile info we got is : {vehicle}")
    vehcile_info = Vehicle(number= vehicle.vehicle_number)
    db.add(vehcile_info)
    db.commit()
    db.refresh(vehcile_info)
    print(f"Vehicle model object : {vehicle}")
    return vehcile_info



@router.delete("/{id}")
def delete_vehcile(id : int, db : Session = Depends(get_db)):
    result = db.execute(select(Vehicle).where(Vehicle.id == id))
    vehicle = result.scalar_one_or_none()
    if not vehicle:
        raise HTTPException(status_code=404,detail=f"vehicle with id {id} not exists")
    db.delete(vehicle)
    db.commit()
    return {"success" : vehicle}


@router.put("/{id}")
def update_vehcile(id: int , vehicle_info : VehicleCreate, db : Session = Depends(get_db)):
    vehicle = db.execute(select(Vehicle).where(Vehicle.id == id)).scalar_one_or_none()
    if not vehicle:
        raise HTTPException(status_code=404,detail="vehicle not exists")
    vehicle.number = vehicle_info.vehicle_number
    db.commit()
    db.refresh(vehicle)
    return vehicle

