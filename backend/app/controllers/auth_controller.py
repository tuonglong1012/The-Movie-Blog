# auth_controller.py
import requests

API_URL = "http://localhost:8000"  # Thay đổi nếu cần

def login(username: str, password: str):
    try:
        response = requests.post(f"{API_URL}/user/login", json={
            "username": username,
            "password": password
        })
        response.raise_for_status()
        return response.json()  # Trả về dữ liệu user nếu thành công
    except requests.exceptions.HTTPError as e:
        return {"error": response.json().get("detail", "Login failed")}
    except Exception as e:
        return {"error": str(e)}

def signup(username: str, email: str, password: str, birthday: str):
    try:
        response = requests.post(f"{API_URL}/signup", json={
            "username": username,
            "password": password,
            "email": email,
            "birthday": birthday
        })
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as e:
        return {"error": response.json().get("detail", "Signup failed")}
    except Exception as e:
        return {"error": str(e)}
