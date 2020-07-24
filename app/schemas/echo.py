from pydantic import BaseModel

class Echo(BaseModel):
    body: str

    class Config:
        schema_extra = {
            'example': {
                'body': 'Text to echo'
            }
        }