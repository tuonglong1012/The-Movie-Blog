from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import get_db
from ..models import Movie
import json
import os

router = APIRouter()
@router.post("/import-json")

def import_movies(db: Session=Depends(get_db)):
    json_path = os.path.join("data","test1.json")
    try:
        with open(json_path,"r",encoding="UTF-8") as f:
            movies_data = json.load(f)
        if not isinstance(movies_data, list):
            raise HTTPException(status_code=400, detail="File JSON phải là danh sách các đối tượng.")
        for movie in movies_data:
            newMovie = Movie(
                title = movie.get("title"),
                rank = movie.get("rank"),
                episodes= movie.get("episodes"),
                score= movie.get("score"),
                external_id = movie.get("id"),
                type = movie.get("test",{}).get("Type"),
                aired = movie.get("test",{}).get("Aired"),
                members = movie.get("test",{}).get("Members"),
            )
            db.add(newMovie)

        db.commit()
        return {"message": f"Đã thêm {len(movies_data)} phim vào cơ sở dữ liệu."}


    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="Không tìm thấy file JSON.")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))








