from fastapi import APIRouter,Depends,HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import Select
from app.database.session import get_db
from app.models.trip import Trip

from app.schemas.trip import TripCreate

router = APIRouter()

"""
Get all the trips of all vehicles
"""
@router.get("/")
def get_trips(db : Session = Depends(get_db)):
    trips = db.execute(Select(Trip)).scalars().all()
    return trips

"Get recently added trips of all vehicle"
@router.get("/recent")
def recent_trips(page : int = 1, limit : int = 10,db : Session = Depends(get_db)):
    trips = db.execute(Select(Trip).limit(10)).scalars().all()


"Get recently added trips of a specific vehicle"
@router.get("/recent/{vehile_id}")
def recent_trip(db : Session = Depends(get_db)):
    pass

"Add a trip of a vehicle"
@router.post("/")
def add_trip(trip : TripCreate,db : Session = Depends(get_db)):
    print(f"Trip deetials we got is : {trip} ")
    trip = Trip(**trip.model_dump())
    db.add(trip)
    db.commit()
    db.refresh(trip)
    return {"success" : trip}

"Delete a trip"
@router.delete("/")
def delete_trip(db : Session = Depends(get_db)):
    pass

"Update a trip"
@router.put("/{trip_id}")
def update_trip(db : Session = Depends(get_db)):
    pass

