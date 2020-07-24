from fastapi import APIRouter

from app.schemas import echo, hello

router = APIRouter()

@router.get('/hello', response_model=hello.Hello)
def hello_world():
    return {'msg': 'Hello World'}

@router.post('/echo', response_model=echo.Echo)
def echo(msg_in: echo.Echo):
    return {'msg': echo}