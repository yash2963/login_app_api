from pydantic import BaseModel,validator
from typing import Optional,List

class UserLogin(BaseModel):
    email: str = "johndoe@mail.com"
    password: str = "12345678"
    role: str = "farmer"
    device_token: str = "0imfnc8mVLWwsAawjYr4Rx-Af50DDqtlx"
    type: str = "email/facebook/google/apple"
    social_id: str = "0imfnc8mVLWwsAawjYr4Rx-Af50DDqtlx"
# class UserResponseModel(BaseModel):
#     id : int
#     name : str
#     email : str
#     is_active : bool

    # class Config:
    #     from_attributes = True

class ForgotPassword(BaseModel):
    phone: str = "+1984512598"
    # email: Optional[str] = None

class VerifyOTP(BaseModel):
    otp: str = "895642"

class ResetPassword(BaseModel):
    token: str = "895642"
    password: str = "examplepassword"
    cpassword: str = "examplepassword"

    # @validator('new_password')
    # def password_length(cls,new_password):
    #     if len(new_password) < 8:
    #         raise ValueError('Password must be at least 8 character')
    #     return new_password

    # @validator('confirm_password')
    # def password_match(cls,confirm_password,values):
    #     if 'new_password' in values and confirm_password != values['new_password']:
    #         raise ValueError('Password do not match')
    #     return confirm_password
    

class BusinessHours(BaseModel):
    mon: List[str] = ["8:00am - 10:00am", "10:00am - 1:00pm"]
    tue: List[str] = ["8:00am - 10:00am", "10:00am - 1:00pm"]
    wed: List[str] = ["8:00am - 10:00am", "10:00am - 1:00pm", "1:00pm - 4:00pm"]
    thu: List[str] = ["8:00am - 10:00am", "10:00am - 1:00pm", "1:00pm - 4:00pm"]
    fri: List[str] = ["8:00am - 10:00am", "10:00am - 1:00pm"]
    sat: List[str] = ["8:00am - 10:00am", "10:00am - 1:00pm"]
    sun: List[str] = ["8:00am - 10:00am"]


class UserRegister(BaseModel):
    full_name: str = "john doe"
    email: str = "johndoe@mail.com"
    phone: str = "+19876543210"
    password: str = "12345678"
    role: str = "farmer"
    business_name: str = "Dairy Farm"
    informal_name: str = "London Dairy"
    address: str = "3663 Marshville Road"
    city: str = "Poughkeepsie"
    state: str = "New York"
    zip_code: int = 12601
    registration_proof: str = "my_proof.pdf"
    business_hours: BusinessHours = BusinessHours()
    device_token: str = "0imfnc8mVLWwsAawjYr4Rx-Af50DDqtlx"
    type: str = "email/facebook/google/apple"
    social_id: str = "0imfnc8mVLWwsAawjYr4Rx-Af50DDqtlx"