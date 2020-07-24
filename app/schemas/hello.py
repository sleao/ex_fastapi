from pydantic import BaseModel

class Hello(BaseModel):
    msg: str

    class Config:
        schema_extra = {
            'example': {
                'msg': 'Hello World'
            }
        }