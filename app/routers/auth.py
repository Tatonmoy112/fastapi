from fastapi import APIRouter, Depends, HTTPException, status, Request
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from .. import database, schemas, models, utils
from .. import oauth2
from sqlalchemy.orm import Session


router = APIRouter (
    prefix="/auth",
    tags=["auth"],
    # responses={404: {"description": "Not found"}};
)

# Login route for user authentication
@router.post("/login", response_model=schemas.Token)
def login(user_credentials: OAuth2PasswordRequestForm = Depends(), 
          db: Session = Depends(database.get_db)
):
    # OAuth2PasswordRequestForm
    # {
    #     "username": str,
    #     "password": str,
    # }
    
    # Check if the user exists in the database based on the provided email
    user = db.query(models.User).filter(models.User.email == user_credentials.username).first()
    
    # If the user does not exist or the password is incorrect, raise an HTTPException with a 403 status code
    if not user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"Invalid Credentials")
    
    # Verify the provided password against the hashed password stored in the database
    if not utils.verify_password(user_credentials.password, user.password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"Invalid Credentials")
    
    #create a JWT token for the authenticated user (not implemented in this snippet)
    access_token = oauth2.create_access_token(data={"user_id": user.id})
    
    return {"message": "Successfully logged in!", "access_token": access_token, "token_type": "bearer"}   
