from util.json import list_to_json, model_to_json
from models.bookmark import Bookmark
from fastapi import APIRouter, status
from services.bookmark_service import BookmarkService

router = APIRouter(prefix='/bookmarks')
service = BookmarkService()

@router.get('/', status_code=status.HTTP_200_OK)
def find_all():
    results = service.find_all()
    return list_to_json(results)

@router.get('/{id}', status_code=status.HTTP_200_OK)
def find_by_id(id: str):
    result = service.find_by_id(id)
    return model_to_json(result)

@router.get('/title/{title}', status_code=status.HTTP_200_OK)
def find_by_title(title: str):  
    results = service.find_by_title(title)
    return list_to_json(results)

@router.get('/group_id/{group_id}', status_code=status.HTTP_200_OK)
def find_by_group_id(group_id: str):  
    results = service.find_by_group_id(group_id)
    return list_to_json(results)

@router.get('/tag/{tag}', status_code=status.HTTP_200_OK)
def find_by_tag(tag: str):  
    results = service.find_by_tag(tag)
    return list_to_json(results)

@router.post('/', status_code=status.HTTP_201_CREATED)
def create(bookmark: Bookmark):
    result = service.create(bookmark)
    return model_to_json(result)

@router.put('/{id}', status_code=status.HTTP_200_OK)
def update(id: str, bookmark: Bookmark):
    result = service.update(id, bookmark)
    return model_to_json(result)

@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete(id: str):
    service.delete(id)
    
@router.put('/{id}/group/{group_id}', status_code=status.HTTP_200_OK)
def add_bookmark_to_group(id: str, group_id: str):
    result = service.add_bookmark_to_group(id, group_id)
    return model_to_json(result)
