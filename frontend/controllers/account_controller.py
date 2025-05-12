import requests

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

def signup(username: str, password: str, age: int):
    try:
        response = requests.post(f"{API_URL}/api/signup", json={
            "username": username,
            "password": password,
            "age": age
        })
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError:
        return {"error": response.json().get("detail", "Signup failed")}
    except Exception as e:
        return {"error": str(e)}
