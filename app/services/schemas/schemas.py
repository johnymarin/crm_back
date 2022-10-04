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


class PersonSchema(BaseModel):
    person_id: int
    national_id_type: str
    national_id: str
    person_type: str

class PersonPostSchema(BaseModel):
    national_id_type: str
    national_id: str
    person_type: str

class PersonOptSchema(BaseModel):
    national_id_type: Optional[str]
    national_id: Optional[str]
    person_type: Optional[str]
