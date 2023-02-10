#!/usr/bin/env python3
"""
Defines a UserSession class
"""
from datetime import datetime

from models.base import Base


class UserSession(Base):
    """
    User session class
    """
    def __init__(self, *args: list, **kwargs: dict):
        """
        Instialize a User Session instance
        """
        super().__init__(*args, **kwargs)
        self.user_id = kwargs.get('user_id')
        self.session_id = kwargs.get('session_id')
        self.created_at = datetime.now()
