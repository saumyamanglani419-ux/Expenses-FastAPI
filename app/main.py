from fastapi import FastAPI
from .core.db import Base , engine
from .models import user
from .models import expense
from app.routers.expense import expense_router

app = FastAPI()
app.include_router(expense_router)

Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {"message": "server running"}
