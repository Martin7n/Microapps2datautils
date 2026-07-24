from db_service.connection import engine

with engine.connect() as connection:
    print("Database connection successful")