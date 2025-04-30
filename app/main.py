from fastapi import FastAPI
from .database import engine, Base
from .routes import movie_routes


# Tạo bảng nếu chưa có
Base.metadata.create_all(bind=engine)

app = FastAPI()


# Đăng ký router
app.include_router(movie_routes.router, prefix="/api", tags=["Movies"])
@app.get("/")
def read_root():
    return {"message": "API phim đang hoạt động!"}