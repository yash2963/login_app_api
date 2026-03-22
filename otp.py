from fastapi import APIRouter,Depends,HTTPException,status
from sqlalchemy.orm import Session
# from database import get_db
import schemas
from sqlalchemy import or_

router = APIRouter(prefix='/users',tags=["Verify OTP"])

HARDCODED_OTP   = "123456"
HARDCODED_PHONE = "9999999999"
HARDCODED_TOKEN  = "895642"

# @router.post('/verify-opt/', responses={
#      200: {
#         "content": {
#             "application/json": {
#                 "examples": {
#                     "OTP cannot be empty": {
#                         "value": {"success": "false", "message": "OTP cannot be empty."}
#                     },
#                     "Unable to verify OTP": {
#                         "value": {"success": "false", "message": "Unable to verify OTP, please try again."}
#                     },
#                     "OTP verified": {
#                         "value": {"success": "true", "message": "OTP verified successful.", "token": "895642"}
#                     },
#                 }
#             }
#         }
#     },
#     401: {
#         "description": "Invalid OTP.",  
#         "content": {
#             "application/json": {
#                 "example": {"success": "false", "message": "Invalid OTP."}  
#             }
#         }
#     },
# }
# )
# # def otp(data:schemas.Otp,db: Session = Depends(get_db)):
# #     if data.otp != HARDCODED_OTP:
# #         raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="Invalid OTP")
# #     return {"Message":"OTP verified successfully"}
# def opt(data:schemas.VerifyOTP):
#     if not data.otp:
#         return {"success": "false", "message": "OTP cannot be empty."}

#     if data.otp != HARDCODED_OTP:
#         return {"success": "false", "message": "Invalid OTP."}

#     return {
#         "success": "true",
#         "message": "OTP verified successful.",
#         "token"  : HARDCODED_TOKEN
#     }


# @router.post('/reset', responses={
#         200: {
#             "content": {
#                 "application/json": {
#                     "examples": {
#                         "Request failed": {
#                             "value": {"success": "false", "message": "Your password reset request failed, please try again."}
#                         },
#                         "OTP expired": {
#                             "value": {"success": "false", "message": "Your password reset OTP was expired."}
#                         },
#                         "Invalid token": {
#                             "value": {"success": "false", "message": "Invalid token."}
#                         },
#                         "Password not matched": {
#                             "value": {"success": "false", "message": "Password and confirm password not matched."}
#                         },
#                         "Password changed": {
#                             "value": {"success": "true", "message": "Your password has been successfully changed.", "is_verified": "true"}
#                         },
#                     }
#                 }
#             }
#         }
#     }
# )
# # def reset(data:schemas.Reset_password,db: Session = Depends(get_db)):
# #     user = db.query(models.User).filter(models.User.phone == HARDCODED_PHONE).first()

# #     if not user:
# #         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='User not found')
# #     user.password = data.new_password
# #     db.commit()
# #     raise {'message':'Password reset successfully'}
# def reset(data:schemas.ResetPassword):
#     if not data.token:
#         return {"success": "false", "message": "Your password reset request failed, please try again."}

#     if data.token != HARDCODED_TOKEN:
#         return {"success": "false", "message": "Invalid token."}

#     if data.password != data.cpassword:
#         return {"success": "false", "message": "Password and confirm password not matched."}

#     return {
#         "success"    : "true",
#         "message"    : "Your password has been successfully changed.",
#         "is_verified": "true"
#     }

@router.post('/verify-opt/', responses={
    200: {
        "description": "OTP cannot be empty.",
        "content": {"application/json": {"example": {
            "success": "false", "message": "OTP cannot be empty."
        }}}
    },
    401: {
        "description": "Invalid OTP.",
        "content": {"application/json": {"example": {
            "success": "false", "message": "Invalid OTP."
        }}}
    },
    202: {
        "description": "Unable to verify OTP, please try again.",
        "content": {"application/json": {"example": {
            "success": "false", "message": "Unable to verify OTP, please try again."
        }}}
    },
    203: {
        "description": "OTP verified successful.",
        "content": {"application/json": {"example": {
            "success": "true", "message": "OTP verified successful.", "token": "895642"
        }}}
    },
})
def opt(data: schemas.VerifyOTP):
    if not data.otp:
        return {"success": "false", "message": "OTP cannot be empty."}
    if data.otp != HARDCODED_OTP:
        return {"success": "false", "message": "Invalid OTP."}
    return {"success": "true", "message": "OTP verified successful.", "token": HARDCODED_TOKEN}


@router.post('/reset', responses={
    200: {
        "description": "Your password reset request failed, please try again.",
        "content": {"application/json": {"example": {
            "success": "false", "message": "Your password reset request failed, please try again."
        }}}
    },
    202: {
        "description": "Your password reset OTP was expired.",
        "content": {"application/json": {"example": {
            "success": "false", "message": "Your password reset OTP was expired."
        }}}
    },
    203: {
        "description": "Invalid token.",
        "content": {"application/json": {"example": {
            "success": "false", "message": "Invalid token."
        }}}
    },
    204: {
        "description": "Password and confirm password not matched.",
        "content": {"application/json": {"example": {
            "success": "false", "message": "Password and confirm password not matched."
        }}}
    },
    205: {
        "description": "Your password has been successfully changed.",
        "content": {"application/json": {"example": {
            "success": "true", "message": "Your password has been successfully changed.", "is_verified": "true"
        }}}
    },
})
def reset(data: schemas.ResetPassword):
    if not data.token:
        return {"success": "false", "message": "Your password reset request failed, please try again."}
    if data.token != HARDCODED_TOKEN:
        return {"success": "false", "message": "Invalid token."}
    if data.password != data.cpassword:
        return {"success": "false", "message": "Password and confirm password not matched."}
    return {"success": "true", "message": "Your password has been successfully changed.", "is_verified": "true"}