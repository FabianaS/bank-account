#!/usr/bin/python
# -*- coding: utf-8 -*-
import logging
from logging.handlers import RotatingFileHandler
from flask import Flask
from flask_mongoengine import MongoEngine
from flask_jwt import JWT

# ------------------------------------------------------------------------------
# SETUP GENERAL APPLICATION
# ------------------------------------------------------------------------------

__version__ = '1.0'
app = Flask('bank_account_gen')
app.config.from_object('config')
app.debug = True

# ------------------------------------------------------------------------------
# SETUP LOGGING
# ------------------------------------------------------------------------------

handler = RotatingFileHandler('bank_account_gen.log', maxBytes=10000, backupCount=1)
handler.setLevel(logging.INFO)
app.logger.addHandler(handler)

# ------------------------------------------------------------------------------
# SETUP MONGO DB 
# ------------------------------------------------------------------------------

db = MongoEngine(app)

# ------------------------------------------------------------------------------
# SETUP JWT AUTHENTICATION
# ------------------------------------------------------------------------------

# Import all bank_account_gen controller files
from bank_account_gen.controllers import *
from bank_account_gen.security import idam

jwt = JWT(app, idam.authenticate, idam.identity)
