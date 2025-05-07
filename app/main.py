from fastapi import FastAPI
from .database import engine, Base
from .routes import movie_routes, account_routes, review_routes
import os
import subprocess

# Tạo bảng nếu chưa có
Base.metadata.create_all(bind=engine)


async def lifespan(app: FastAPI):
    run_scrapyd_and_deploy()
    yield


app = FastAPI(lifespan=lifespan)


# Đăng ký router
app.include_router(movie_routes.router, prefix="/api", tags=["Movies"])
app.include_router(account_routes.router, prefix="/api", tags=["Account"])
app.include_router(review_routes.router, prefix="/api", tags=["Review"])


@app.get("/")
def read_root():
    return {"message": "API phim đang hoạt động!"}

# run scrapyd and scrapyd-deploy

# filepath: /home/TP/The-Movie-Blog/app/main.py


def run_scrapyd_and_deploy():
    try:
        # Set the working directory to the Scrapy project folder
        scrapy_project_path = os.path.join(
            os.path.dirname(__file__), "../myanimelist")
        os.chdir(scrapy_project_path)

        # Start scrapyd
        subprocess.Popen(["scrapyd"], stdout=subprocess.DEVNULL,
                         stderr=subprocess.DEVNULL)

        # Deploy the scrapy project
        subprocess.run(["scrapyd-deploy", "default"], check=True)
    except Exception as e:
        print(f"Error starting scrapyd or deploying: {e}")
