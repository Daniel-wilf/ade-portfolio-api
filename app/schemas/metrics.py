from pydantic import BaseModel

class Metrics(BaseModel):
    uptime: str
    users: int
