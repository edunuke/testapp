import os

# *****************************
# Environment specific settings
# *****************************

# DO NOT use "DEBUG = True" in production environments
DEBUG = False
TESTING = False
# DO NOT use Unsecure Secrets in production environments
# Generate a safe one with:
#     python -c "import os; print repr(os.urandom(24));"
SECRET_KEY = 'asdkjflkasdjfñlaksjdñflkajsñdlfkjñalsdklfj'

# SQLAlchemy settings:
SQLALCHEMY_DATABASE_URI ="postgresql://postgres:test@psqldb/postgres"
SQLALCHEMY_TRACK_MODIFICATIONS = False    # Avoids a SQLAlchemy Warning

# Flask-Mail settings

MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 587
MAIL_USE_SSL = True
MAIL_USE_TLS = False
MAIL_USERNAME = 'eduardo.denadai@gmail.com'
MAIL_PASSWORD = '@tomP0werS2485'
MAIL_DEFAULT_SENDER = 'eduardo.denadai@gmail.com'

# Sendgrid settings
SENDGRID_API_KEY='place-your-sendgrid-api-key-here'

# Flask-User settings
USER_APP_NAME = "Exchange"
USER_EMAIL_SENDER_NAME = 'Exchange'
USER_EMAIL_SENDER_EMAIL = 'eduardo.denadai@gmail.com'

ADMINS = [
    '"Admin One" <eduardo.denadai@gmail.com>',
    ]
