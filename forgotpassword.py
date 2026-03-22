# from fastapi import APIRouter,Depends,HTTPException,status
# # from sqlalchemy.orm import Session
# # from database import get_db
# import schemas
# # from sqlalchemy import or_

# router = APIRouter(prefix='/users',tags=["Forgot-Password"])

# HARDCODED_OTP   = "123456"
# HARDCODED_PHONE = "9999999999"


# @router.post('/password/')
# # def reset_password(user:schemas.ForgotPassword,db: Session = Depends(get_db)):
# #     user = db.query(models.User).filter(or_(models.User.phone == HARDCODED_PHONE, models.User.email ==  user.email)).first()
# #     if not user:
# #         raise HTTPException(status_code=404,detail='User not found')
# #     return {'message': f"OTP sent to {user.phone}"}
# def reset_password(data:schemas.ForgotPassword):
#     if not data.phone:
#         return {"success": "false", "message": "Couldn't send an OTP, please try again."}

#     if data.mobile != HARDCODED_PHONE:
#         return {"success": "false", "message": "Account with this mobile number does not exist."}

#     return {"success": "true", "message": "OTP sent to your mobile."}


from fastapi import APIRouter
import schemas

router = APIRouter(prefix='/users', tags=["Forgot-Password"])

HARDCODED_PHONE = "9999999999"

@router.post('/password/')
def reset_password(data: schemas.ForgotPassword):
    # 1. Check karein ki schema mein field ka naam kya hai (phone ya mobile?)
    # Maan lete hain schema mein 'phone' hai:
    
    if not data.phone:
        return {
            "success": False, 
            "message": "Couldn't send an OTP, please try again."
        }

    if data.phone != HARDCODED_PHONE:
        return {
            "success": False, 
            "message": "Account with this mobile number does not exist."
        }

    return {
        "success": True, 
        "message": "OTP sent to your mobile."
    }
