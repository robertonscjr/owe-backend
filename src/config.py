import os

# Service configuration
SERVICE_NAME = "owe-monolithic"
SERVICE_URI = "http://0.0.0.0:5000"
SERVICE_LIST = []

# MongoDB credential
MONGODB_CONNSTRING = os.environ.get("MONGODB_CONNSTRING", "mongodb://0.0.0.0:27017")

# JWT setup
SECRET_KEY = os.environ.get("SECRET_KEY", b"devkey")
JWT_ALGO = "HS256"
