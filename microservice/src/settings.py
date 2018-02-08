from os import environ

eget = environ.get


settings = {
    # SERVER
    'PORT': int(eget('PORT')),
    'ENV': eget('ENV'),
    'DB_DSN': eget('DB_DSN')
}
