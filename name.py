from fastapi import APIRouter, Path
from model import Name

name_router = APIRouter()

name_list = []

@name_router.post("/name")
async def add_name(name: Name) -> dict:
    name.id = len(name_list) + 1
    name_list.append(name)
    return {
        "msg": "posted name successfully"
    }

@name_router.get("/name")
async def retrieve_names() -> dict:
    return {
        "names": name_list
    }

@name_router.get("/name/{name_id}")
async def get_single_name(name_id: int = Path(..., title="The Id to retrieve")) -> dict:
    for name in name_list:
        if name.id == name_id:
            return {"name": name}
    return {"msg": "name with supplied ID doesn't exist"}

@name_router.delete("/name/{name_id}")
async def delete_name(name_id: int) -> dict:
    for name in name_list:
        if name.id == name_id:
            name_list.remove(name)
            return {"msg": "name deleted successfully"}
    return {"msg": "name with supplied ID doesn't exist"}
