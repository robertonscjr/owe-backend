from flask import Flask
from flask_cors import CORS

import pymongo

from src.routing import APIRouter, config_app_routing


def create_app(app_name, secret_key, api_router):
    app = Flask(app_name)
    app.secret_key = secret_key
    cors = CORS(app)

    routes = api_router.get_routes()
    config_app_routing(app, routes)
    return app


def create_api_router(routes):
    api_router = APIRouter(routes)
    return api_router


def create_database(connstring):
    db = pymongo.MongoClient(connstring, serverSelectionTimeoutMS=2000)
    return db
