# from fastapi import FastAPI,Depends,HTTPException
# from fastapi.security import OAuth2PasswordBearer,OAuth2PasswordRequestForm
# # from database import Base,engine
# # import models 
# from routes import router as login_router
# from otp import router as otp_router
# from forgotpassword import router as forgot_router
# # from routes import login_user


# # Base.metadata.create_all(bind=engine)


# app = FastAPI(title="Assignment API")

# app.include_router(login_router)
# app.include_router(forgot_router)
# app.include_router(otp_router)


from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
from routes import router as login_router
from otp import router as otp_router
from forgotpassword import router as forgot_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Assignment API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(login_router)
app.include_router(forgot_router)
app.include_router(otp_router)


def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Assignment API",
        version="1.0.0",
        routes=app.routes,
    )
    for path in openapi_schema["paths"].values():
        for method in path.values():
            method.get("responses", {}).pop("422", None)
            for response in method.get("responses", {}).values():
                response.pop("links", None)
                response.pop("content", None)

                if "content" in response:
                    for content in response["content"].values():
                        content.pop("schema",None)

    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = custom_openapi
