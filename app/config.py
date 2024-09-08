class Config:
    @staticmethod
    def init_app():
        pass

class DevelopmentConfig(Config):
    # static attributes
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:iti@localhost:5432/flask_products" # postgresql

    # SQLALCHEMY_DATABASE_URI = "sqlite:///project.db"

class ProductionConfig(Config):
    DEBUG = True
    # mysql://username:password@server:port/db
    # postgresql://username:password@server:port/db
    SQLALCHEMY_DATABASE_URI = "postgresql://avnadmin:AVNS_wqK7YP-Nk4FaC8EW6iG@pg-29c39587-ahmedayman58134-67e2.e.aivencloud.com:20611/defaultdb" # postgresql


config_options = {
    "dev":DevelopmentConfig,
    'prd':ProductionConfig
}