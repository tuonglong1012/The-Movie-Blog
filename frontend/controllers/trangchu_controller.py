import requests

API_URL = "http://localhost:8000"  # Thay đổi nếu cần

def get_all_movies():
    try:
        response = requests.get(f"{API_URL}/api/movies")
        response.raise_for_status()
        return response.json()  # Trả về danh sách phim
    except requests.exceptions.HTTPError:
        return {"error": response.json().get("detail", "Failed to fetch movies")}
    except Exception as e:
        return {"error": str(e)}
