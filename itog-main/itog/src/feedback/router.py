from fastapi import APIRouter, Depends, HTTPException, status
from feedback.schemas import FeedbackCreate, FeedbackRead
from sqlalchemy.orm import Session
from database import get_db
from feedback.models import Feedback

router = APIRouter(
    prefix = '/api/feedback',
    tags= ['feedback']
)



@router.post('/create' , response_model= FeedbackRead)
async def create_feedback(
    data : FeedbackCreate,
    db: Session = Depends(get_db)
):
    qu = Feedback(
            name = data.name,
            question = data.question
        )
    
    
    db.add(qu)
    db.commit()

    db.refresh(qu)#обнова состояния из db(добавление айди)

    return qu


