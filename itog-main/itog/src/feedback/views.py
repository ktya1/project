from pathlib import Path

from fastapi import APIRouter, Depends, Form, HTTPException, Request, status
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from database import get_db
from feedback.models import Feedback


BASE_DIR = Path( __file__).resolve().parents[2] #корень приложения 
TEMPLATES_DIR = BASE_DIR / 'templates'

templates = Jinja2Templates(directory=str(TEMPLATES_DIR))



router = APIRouter(
    prefix= '/feedback' ,
    tags= ['feedback_pages'] #для группировки обработчиков
)


@router.get('/create')
async def get_create_post(
    request: Request
):
    return templates.TemplateResponse(
        request=request,
        name='feedback/create.html'
    )

@router.post('/create')
async def create_post(
    name: str = Form(...),
    question: str = Form(...),
    db: Session = Depends(get_db)
):
    qu = Feedback(
        name=name,
        question=question, 
    )
        
    db.add(qu)
    db.commit()
    db.refresh(qu)

    return RedirectResponse(
        url='answer_feedback',
        status_code=status.HTTP_303_SEE_OTHER
    )


@router.get('/answer_feedback')
async def answer_get_feedback(
    request: Request
    ):
        return templates.TemplateResponse(
            request=request,
            name='feedback/answer_feedback.html'
        )