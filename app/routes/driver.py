from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def get_drivers():
    pass

@router.get("/{id}")
def get_driver(id : int):
    pass

@router.post("/")
def add_driver():
    pass

@router.put("/{id}")
def update_driver(id : int):
    pass

@router.delete("/{id}")
def delete_driver(id:int):
    pass

