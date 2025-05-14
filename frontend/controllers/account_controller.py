import requests
from datetime import datetime

API_URL = "http://localhost:8000"  # Đổi URL nếu cần

def login(username: str, password: str):
    try:
        response = requests.post(f"{API_URL}/api/user/login", json={
            "username": username,
            "password": password
        })
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError:
        return {"error": response.json().get("detail", "Login failed")}
    except Exception as e:
        return {"error": str(e)}

def signup(username: str, password: str, date_of_birth: str):
    try:
        # Ensure the date is in the correct format: 'yyyy-mm-dd'
        try:
            formatted_date = datetime.strptime(date_of_birth, "%Y-%m-%d").date()
        except ValueError:
            return {"error": "Invalid date format. Please use YYYY-MM-DD."}

        response = requests.post(f"{API_URL}/api/signup", json={
            "username": username,
            "password": password,
            "date_of_birth": formatted_date.strftime("%Y-%m-%d")  # Chuyển sang chuỗi
        })
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError:
        return {"error": response.json().get("detail", "Signup failed")}
    except Exception as e:
        return {"error": str(e)}

