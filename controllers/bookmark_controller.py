from util.error import not_found
from util.json import list_to_json
from models.bookmark import Bookmark
from fastapi import APIRouter, status
from services.bookmark_service import BookmarkService

router = APIRouter(prefix="/bookmarks")
service = BookmarkService()

@router.get("/", status_code=status.HTTP_200_OK)
def find_all():
    results = service.find_all()
    return list_to_json(results)

@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=Bookmark)
def find_by_id(id: str):
    result = service.find_by_id(id)
    if not result:
        not_found("Bookmark not found")
    return result

@router.get("/title/{title}", status_code=status.HTTP_200_OK)
def find_by_title(title: str):  
    results = service.find_by_title(title)
    if not results:
        not_found("No Bookmark found")        
    return list_to_json(results)

@router.get("/group/{group}", status_code=status.HTTP_200_OK)
def find_by_group(group: str):  
    results = service.find_by_group(group)
    if not results:
        not_found("No Bookmark found")        
    return list_to_json(results)

@router.get("/tag/{tag}", status_code=status.HTTP_200_OK)
def find_by_tag(tag: str):  
    results = service.find_by_tag(tag)
    if not results:
        not_found("No Bookmark found")        
    return list_to_json(results)

@router.post('/', status_code=status.HTTP_201_CREATED, response_model=Bookmark)
def create(bookmark: Bookmark):
    result = service.create(bookmark)
    return result

@router.put('/{id}', status_code=status.HTTP_200_OK, response_model=Bookmark)
def update(id: str, bookmark: Bookmark):
    result = service.update(id, bookmark)
    return result

@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete(id: str):
    service.delete(id)
