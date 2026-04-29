from fastapi import APIRouter, Depends
from app.core.dependencies import get_current_user, require_role

router = APIRouter()


@router.get("/me")
def get_me(current_user=Depends(get_current_user)):
    return {
        "id": current_user.id,
        "email": current_user.email,
        "role": current_user.role
    }

@router.get("/admin-only")
def admin_route(current_user = Depends(require_role(["admin"]))):
    return {"message": "Welcome Admin"}


@router.get("/manager-only")
def manager_route(current_user = Depends(require_role(["admin", "manager"]))):
    return {"message": "Welcome Manager/Admin"}