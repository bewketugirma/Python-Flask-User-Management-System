# config.py

import os

class Config:
    SECRET_KEY = 'your-secret-key'  # for flash messages
    SQLALCHEMY_DATABASE_URI = 'mysql://root:@localhost/flask'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
