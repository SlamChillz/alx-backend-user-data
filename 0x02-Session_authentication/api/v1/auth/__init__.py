import os


if os.getenv('AUTH_TYPE') == 'session_db_auth':
    from models.user_session import UserSession
    UserSession.load_from_file()
