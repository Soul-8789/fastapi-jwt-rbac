import requests

BASE_URL = "http://127.0.0.1:8000"

# Sample user data
USER_ADMIN = {"username": "admin_user1", "password": "admin123", "role": "admin"}
USER_NORMAL = {"username": "normal_user1", "password": "user123", "role": "user"}

# Sample project data
PROJECT = {"name": "Test Project", "description": "This is a test project"}

# Store JWT tokens
tokens = {}

def register_user(user):
    """Register a user (admin/user)"""
    response = requests.post(f"{BASE_URL}/users/register", json=user)
    print(f"REGISTER {user['username']}:", response.json())

def login_user(username, password):
    """Login a user and get JWT token"""
    response = requests.post(f"{BASE_URL}/users/login", data={"username": username, "password": password})
    if response.status_code == 200:
        token = response.json()["access_token"]
        tokens[username] = token
        print(f"LOGIN {username}: Success")
    else:
        print(f"LOGIN {username}:", response.json())

def get_projects(username):
    """Fetch all projects (for any user)"""
    headers = {"Authorization": f"Bearer {tokens.get(username, '')}"}
    response = requests.get(f"{BASE_URL}/projects/", headers=headers)
    print(f"GET PROJECTS ({username}):", response.json())

def create_project(username, project_data):
    """Create a project (Admin only)"""
    headers = {"Authorization": f"Bearer {tokens.get(username, '')}"}
    response = requests.post(f"{BASE_URL}/projects/", json=project_data, headers=headers)
    print(f"CREATE PROJECT ({username}):", response.json())

if __name__ == "__main__":
    # 1️⃣ Register Users
    register_user(USER_ADMIN)
    register_user(USER_NORMAL)

    # 2️⃣ Login Users
    login_user(USER_ADMIN["username"], USER_ADMIN["password"])
    login_user(USER_NORMAL["username"], USER_NORMAL["password"])

    # 3️⃣ Get Projects (Both users)
    get_projects(USER_ADMIN["username"])
    get_projects(USER_NORMAL["username"])

    # 4️⃣ Create Project (Only Admin)
    create_project(USER_ADMIN["username"], PROJECT)
    create_project(USER_NORMAL["username"], PROJECT)  # This should fail due to role restriction
