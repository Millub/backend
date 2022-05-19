from fastapi import HTTPException, status

def exception_test(e):
    return HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail=str(e),
        headers={"WWW-Authenticate": "Bearer"},
    )

exception_40101 = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="40101_Could not validate credentials",
    headers={"WWW-Authenticate": "Bearer"},
)

exception_40102 = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="40102_Incorrect username or password",
    headers={"WWW-Authenticate": "Bearer"},
)

exception_40201 = HTTPException(
    status_code=status.HTTP_402_PAYMENT_REQUIRED,
    detail="40201_Not Enough Point",
    headers={"WWW-Authenticate": "Bearer"},
)

exception_40301 = HTTPException(
    status_code=status.HTTP_403_FORBIDDEN,
    detail="40301_Please Retry",
    headers={"WWW-Authenticate": "Bearer"},
)

exception_40302 = HTTPException(
    status_code=status.HTTP_403_FORBIDDEN,
    detail="40302_Not Order Alert",
    headers={"WWW-Authenticate": "Bearer"},
)

exception_40601 = HTTPException(
    status_code=status.HTTP_406_NOT_ACCEPTABLE,
    detail="40601_Invalid Data Content",
    headers={"WWW-Authenticate": "Bearer"},
)

exception_40602 = HTTPException(
    status_code=status.HTTP_406_NOT_ACCEPTABLE,
    detail="40602_Already Data Existed",
    headers={"WWW-Authenticate": "Bearer"},
)

exception_40603 = HTTPException(
    status_code=status.HTTP_406_NOT_ACCEPTABLE,
    detail="40603_Included Special Char",
    headers={"WWW-Authenticate": "Bearer"},
)