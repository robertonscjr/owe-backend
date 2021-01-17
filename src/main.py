from src import config, factory, routing


database = factory.create_database(config.MONGODB_CONNSTRING)
api_router = factory.create_api_router(routing.ROUTES)
app = factory.create_app(config.SERVICE_NAME, config.SECRET_KEY, api_router)
