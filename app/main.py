from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.data.db.config_tortoise import register_db
from app.services.endpoints.endpoints import api_router

app = FastAPI(
    title="Migracion CRM by Johny Marin Gutierrez",
    openapi_url=f"/crm/openapi.json",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],

)

app.include_router(api_router, prefix="/api")

register_db(app)
