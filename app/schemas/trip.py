from pydantic import BaseModel
from datetime import date,time

class TripCreate(BaseModel):
    bhada_no : int
    from_location : str
    to_location : str
    loading_date : date
    loading_time : time
    unloading_date : date
    unloading_time : time
    weight : float
    real_weight : float
    size : Dimension
    real_size : Dimension
    rate : int
    final_rate : int
    party_advance : int
    party_balance : int
    driver_advance : int
    khali_bhatta : int
    load_bhatta : int
    toll : int
    disel_liter : int
    disel_amount : int
    driver_bachat : int
    commission : int
    empty_toll : int
    empty_disel : int
    parking : int
    broker_name : str

class Dimension(BaseModel):
    height : float
    width : float
    length : float