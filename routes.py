from fastapi import APIRouter,Depends,HTTPException,status
# from sqlalchemy.orm import Session
# # from database import get_db
import schemas


router = APIRouter(prefix='/users',tags=["Users"])


HARDCODED_EMAIL    = "johndoe@mail.com"
HARDCODED_PASSWORD = "12345678"
HARDCODED_ROLE     = "farmer"
HARDCODED_TYPE     = "email/facebook/google/apple"
HARDCODED_SOCIAL_ID = "0imfnc8mVLWwsAawjYr4Rx-Af50DDqtlx"
HARDCODED_TOKEN    = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c"

# @router.post('/register/',response_model=schemas.UserResponseModel)
# def register_user(user: schemas.UserLogin,db: Session = Depends(get_db)):
#     existing = db.query(models.User).filter(models.User.email == user.email).first()
#     if existing:
#         raise HTTPException(status_code= status.HTTP_409_CONFLICT,detail="User Already Exist!")
#     new_user = models.User(**user.model_dump())
#     db.add(new_user)
#     db.commit()
#     db.refresh(new_user)
#     return new_user







HARDCODED_EMAIL    = "johndoe@mail.com"
HARDCODED_TOKEN    = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c"


@router.post(
    "/register",
    responses={
        200: {
            "content": {
                "application/json": {
                    "examples": {
                        "All fields required": {
                            "value": {"success": "false", "message": "All fields are required."}
                        },
                        "Server error": {
                            "value": {"success": "false", "message": "Server error while registering."}
                        },
                        "Email exists": {
                            "value": {"success": "false", "message": "Email already exists."}
                        },
                        "Registration failed": {
                            "value": {"success": "false", "message": "Registration failed."}
                        },
                        "Invalid token": {
                            "value": {"success": "false", "message": "Invalid token."}
                        },
                        "Social id required": {
                            "value": {"success": "false", "message": "Social id required."}
                        },
                        "Registered": {
                            "value": {"success": "true", "message": "Registered.", "token": HARDCODED_TOKEN}
                        },
                    }
                }
            }
        },
        401: {
            "content": {
                "application/json": {
                    "examples": {
                        "Unauthorized": {
                            "value": {"success": "false", "message": "Access denied! unauthorized user."}
                        }
                    }
                }
            }
        },
    }
)
def register(data: schemas.UserRegister):

    if not data.full_name or not data.email or not data.password:
        return {"success": "false", "message": "All fields are required."}

    if not data.social_id:
        return {"success": "false", "message": "Social id required."}

    if data.email != HARDCODED_EMAIL:
        return {"success": "false", "message": "Email already exists."}

    return {
        "success": "true",
        "message": "Registered.",
        "token"  : HARDCODED_TOKEN
    }

## Response Flow







@router.post('/login/')
# def login_user(user: schemas.UserLogin,db: Session = Depends(get_db)):
#     existing = db.query(models.User).filter(models.User.email == user.email).first()
#     if not existing:
#         raise HTTPException(status_code=status.Http404,detail='User not found')
#     if existing.password != user.password:
#         raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail='Wrong password')
#     return {"message":"Login successful!","user_id": existing.id}

def login_user(user: schemas.UserLogin):
    if not user.email:
        return {"success": "false", "message": "Email cannot be empty."}

    # Password empty check
    if not user.password:
        return {"success": "false", "message": "Password cannot be empty."}

    # Social id empty check
    if not user.social_id:
        return {"success": "false", "message": "Social id cannot be empty."}

    # Account does not exist
    if user.email != HARDCODED_EMAIL:
        return {"success": "false", "message": "Account does not exist."}

    # Invalid password
    if user.password != HARDCODED_PASSWORD:
        return {"success": "false", "message": "Invalid password."}

    # Role not matched
    if user.role != HARDCODED_ROLE:
        return {"success": "false", "message": "Role not matched."}

    # Type not matched
    if user.type != HARDCODED_TYPE:
        return {"success": "false", "message": "Type not matched."}

    # Social id not matched
    if user.social_id != HARDCODED_SOCIAL_ID:
        return {"success": "false", "message": "Social id not matched."}

    # Success
    return {
        "success": "true",
        "message": "Login successfull.",
        "token"  : HARDCODED_TOKEN
    }

