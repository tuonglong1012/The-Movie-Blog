from fastapi import FastAPI
from .database import engine, Base
from .routes import movie_routes,account_routes,review_routes


# Tạo bảng nếu chưa có
Base.metadata.create_all(bind=engine)

app = FastAPI()


# Đăng ký router
app.include_router(movie_routes.router, prefix="/api", tags=["Movies"])
app.include_router(account_routes.router, prefix="/api", tags=["Account"])
app.include_router(review_routes.router, prefix="/api", tags=["Review"])


@app.get("/")
def read_root():
    return {"message": "API phim đang hoạt động!"}