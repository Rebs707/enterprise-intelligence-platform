from fastapi import APIRouter

router = APIRouter()

@router.get("/insights")
def insights():
    return {"message": "Enterprise insights"}
