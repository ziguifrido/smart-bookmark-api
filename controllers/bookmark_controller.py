from fastapi import APIRouter, HTTPException, status
from services.bookmark_service import BookmarkService
from util.json import list_to_json

router = APIRouter(prefix="/bookmarks")
service = BookmarkService()

@router.get("/title/{title}", status_code=status.HTTP_200_OK)
def find_by_title(title: str):  
    results = service.find_by_title(title)
    if not results:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Bookmark not found"
        )
        
    return list_to_json(results)

@router.get("/tag/{tag}", status_code=status.HTTP_200_OK)
def find_by_tag(tag: str):  
    results = service.find_by_tag(tag)
    if not results:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Bookmark not found"
        )
        
    return list_to_json(results)
