# Flask REST API

A simple REST API built using **Python** and **Flask** to perform CRUD (Create, Read, Update, Delete) operations on user data.

## 📌 Objective

Develop a REST API that manages user information using Flask and demonstrates the basic HTTP methods:

- GET
- POST
- PUT
- DELETE

The user data is stored in an in-memory Python list.

---

## 🛠️ Technologies Used

- Python 3
- Flask
- REST API
- JSON

---

## 📂 Project Structure

```
Flask-REST-API/
│
├── app.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/flask-rest-api.git
```

Or download the project as a ZIP file.

### 2. Navigate to the project folder

```bash
cd Flask-REST-API
```

### 3. Install Flask

```bash
pip install flask
```

or

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Application

Run the following command:

```bash
python app.py
```

The server will start at:

```
http://127.0.0.1:5000/
```

---

## 📡 API Endpoints

### Home

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Welcome page |

---

### Get All Users

| Method | Endpoint |
|--------|----------|
| GET | `/users` |

Example Response

```json
[
  {
    "id": 1,
    "name": "Alice",
    "age": 20
  },
  {
    "id": 2,
    "name": "Bob",
    "age": 22
  }
]
```

---

### Get Single User

| Method | Endpoint |
|--------|----------|
| GET | `/users/<id>` |

Example

```
GET /users/1
```

---

### Add User

| Method | Endpoint |
|--------|----------|
| POST | `/users` |

Request Body

```json
{
    "name": "Charlie",
    "age": 25
}
```

---

### Update User

| Method | Endpoint |
|--------|----------|
| PUT | `/users/<id>` |

Request Body

```json
{
    "name": "Charles",
    "age": 26
}
```

---

### Delete User

| Method | Endpoint |
|--------|----------|
| DELETE | `/users/<id>` |

---

## 📁 Sample User Data

```python
users = [
    {"id": 1, "name": "Alice", "age": 20},
    {"id": 2, "name": "Bob", "age": 22}
]
```

---

## 📷 Testing

The API can be tested using:

- Postman
- cURL
- Web Browser (GET requests)

Example:

```bash
curl http://127.0.0.1:5000/users
```

---

## 📌 Features

- View all users
- View a single user
- Add a new user
- Update user information
- Delete a user
- JSON-based API responses
- Beginner-friendly implementation

---

## 📚 Learning Outcomes

- Understanding REST API architecture
- Working with Flask routes
- Handling HTTP methods
- Sending and receiving JSON data
- Building CRUD applications

---

## 👨‍💻 Author

**Ashley Fewin E**

B.Tech Artificial Intelligence and Data Science

---

## 📄 License

This project is created for educational purposes.

<img width="1457" height="910" alt="Screenshot 2026-07-03 194145" src="https://github.com/user-attachments/assets/cbd0bb63-fa5f-46f6-a407-285ed8b69c6e" />
<img width="1037" height="518" alt="Screenshot 2026-07-03 193905" src="https://github.com/user-attachments/assets/00877ec6-9a45-410c-b0f3-28510be81175" />
<img width="1021" height="582" alt="Screenshot 2026-07-03 193841" src="https://github.com/user-attachments/assets/45182667-4390-4c1f-8f4d-014d4483cc15" />


