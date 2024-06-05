#!/usr/bin/env python
# -*- coding: utf_8 -*-
"""Settings for nodejsscan."""
from pathlib import Path

# GENERAL
VERSION = '4.8'
UPLOAD_FOLDER = Path('~/.nodejsscan/').expanduser().as_posix()
Path(UPLOAD_FOLDER).mkdir(parents=True, exist_ok=True)
UPLD_MIME = [
    'application/zip',
    'application/octet-stream',
    'application/x-zip-compressed',
    'binary/octet-stream',
]
IGNORE_PATHS = ('.git', '.DS_Store')
CHECK_MISSING_CONTROLS = True

# Postgres DB Connection URL
SQLALCHEMY_DATABASE_URI = 'postgresql://myuser:mypassword@0.0.0.0:5432/nodejsscan'

# Get Slack alerts
SLACK_WEBHOOK_URL = ''

# Get Email alerts
NJS_FROM_EMAIL = 'devopswlc@gmail.com'
NJS_TO_EMAIL = 'devopswlc@gmail.com'
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = None
SMTP_STARTTLS = False
SMTP_USER = 'devopswlc@gmail.com'
SMTP_PASS = 'uJ8C9wmLeLyfL6'
