from http import HTTPStatus
from typing import List, Any

from fastapi import APIRouter

from app.data.models.models import CityTortoise
from app.services.schemas.schemas import CityPydantic, CityInPydantic, CityOptPydantic

api_router = APIRouter()


@api_router.get('/cities', response_model=List[CityPydantic])
async def get_cities() -> List:
    query = await CityTortoise.all()
    return query


@api_router.post('/cities', response_model=CityPydantic, status_code=HTTPStatus.CREATED)
async def create_city(city: CityInPydantic) -> Any:

    city_obj = await CityTortoise.create(
        name=city.name,
        timezone=city.timezone,
    )
    return city_obj


@api_router.get('/cities/{city_id}', response_model=CityPydantic)
async def read_city(city_id: int) -> Any:
    city_obj = await CityTortoise.filter(id=city_id).get()
    return city_obj


@api_router.put('/cities/{city_id}', response_model=CityPydantic)
async def update_city(city_id: int, city: CityOptPydantic) -> Any:
    city_obj = await CityTortoise.filter(id=city_id).update(**city.dict(exclude_unset=True))
    # update does not return a queryset istead it update on db itself so again
    city_obj_to = await CityTortoise.filter(id=city_id).get()
    return city_obj_to


@api_router.delete('/cities/{city_id}', response_model=None, status_code=HTTPStatus.NO_CONTENT)
async def delete_city(city_id: int):
    await CityTortoise.filter(id=city_id).delete()
    return None


@api_router.get("/")
async def root():
    return {"message": "Hello World"}


@api_router.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}