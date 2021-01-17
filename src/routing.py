import json

from src import controller

"""
    Define all the routes of API Gateway in the ROUTES variable
    Please change this variable to add or remove a route from app
"""
ROUTES = {
    "/health": {
        "action": "GET_HEALTH",
        "description": "Get health of service",
        "http_verbs": ["GET"],
        "api_function": controller.health,
    },
    "/registerUserData": {
        "action": "REGISTER_USER_DATA",
        "description": "Register user data",
        "http_verbs": ["POST"],
        "api_function": controller.register_user_data,
    }
}


def config_app_routing(flask_obj, routes, service=None):
    for route in routes:
        http_verbs = routes[route]["http_verbs"]
        api_function = routes[route]["api_function"]

        flask_obj.add_url_rule(route, view_func=api_function, methods=http_verbs)

    @flask_obj.before_request
    def before_request_api():
        # here are some logic before request processing
        pass

    @flask_obj.after_request
    def after_request_api(response):
        # here are some logic after request processing
        return response


class APIRouter:
    def __init__(self, routes={}):
        self.routes = routes

    def add_route(self, route, description, http_verbs, api_function):
        self.routes[route] = {
            "description": description,
            "http_verbs": http_verbs,
            "api_function": api_function,
        }

    def get_routes(self):
        return self.routes
