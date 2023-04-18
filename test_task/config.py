db_config = {
        'USER': 'test_flask',
        'PASSWORD': 'test_flask',
        'DB': 'test_db',
}
class Config():
    SECRET_KEY = 'kjbn#x^d8ut2$hkgds@fgj0'
    SQLALCHEMY_DATABASE_URI =  f'postgresql://{db_config["USER"]}:{db_config["PASSWORD"]}@localhost:5432/{db_config["DB"]}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False,
    