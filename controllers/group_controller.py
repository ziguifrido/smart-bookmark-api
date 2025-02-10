from models.group import Group
from util.error import not_found
from util.json import list_to_json
from fastapi import APIRouter, status
from services.group_service import GroupService

router = APIRouter(prefix="/groups")
service = GroupService()

@router.get("/", status_code=status.HTTP_200_OK)
def find_all():
    results = service.find_all()
    return list_to_json(results)

@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=Group)
def find_by_id(id: str):
    result = service.find_by_id(id)
    if not result:
        not_found("Group not found")
    return result

@router.get("/title/{title}", status_code=status.HTTP_200_OK)
def find_by_title(title: str):  
    results = service.find_by_title(title)
    if not results:
        not_found("No Group found")        
    return list_to_json(results)

@router.post('/', status_code=status.HTTP_201_CREATED, response_model=Group)
def create(group: Group):
    result = service.create(group)
    return result

@router.put('/{id}', status_code=status.HTTP_200_OK, response_model=Group)
def update(id: str, group: Group):
    result = service.update(id, group)
    return result

@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete(id: str):
    service.delete(id)
