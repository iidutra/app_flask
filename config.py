import os

class Config():
    CSRF_ENABLE = True
    SECRET = "140795"
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    TEMPLATE_FOLDER = os.path.join(ROOT_DIR, 'templates')
    APP = None

class DevelopmentConfig(Config):
    DEBUG = True
    IP_HOST = 'localhost'
    PORT_HOST = 8000
    URL_MAIN = 'http://%s:%s' % (IP_HOST, PORT_HOST)
    SQLALCHEMY_DATABASE_URI = 'mysql+mysql.connector://tiago.silva:de_m7jBG^WZ=@localhost:3306/dashboard_aula'

class TestingConfig(Config):
   pass

app_config = {
    'development': DevelopmentConfig(),
    'testing': TestingConfig()
}
app_active = os.getenv('FLASK_ENV')
if app_active is None:
    app_active = 'development'