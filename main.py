from fastapi import FastAPI

from app.routes.vehicle import router as vehicle_router
from app.routes.trip import router as trip_router
from app.routes.driver import router as driver_router

from app.database.database import engine


from app.models.driver import Driver


app = FastAPI(title="BhadaBook")
app.include_router(vehicle_router,prefix="/vehicle",tags=["Vehicle"])
app.include_router(trip_router,prefix="/trip",tags=["Trip"])
app.include_router(driver_router,prefix="/drivers",tags=["Driver"])

