from typing import Optional

from pydantic import BaseModel


class CityPydantic(BaseModel):
    id: int
    name: str
    timezone: str
    name = 'City'


class CityInPydantic(BaseModel):
    name: str
    timezone: str
    name = 'CityIn'


class CityOptPydantic(BaseModel):
    name: Optional[str]
    timezone: Optional[str]
    name = 'CityOpt'