#!/usr/bin/env python3
"""
Defines SessionExpAuth class that implements session expiration
"""
import os
from datetime import datetime
from typing import Union

from api.v1.auth.session_auth import SessionAuth


class SessionExpAuth(SessionAuth):
    """
    Session Authentication class with expiration
    """
    def __init__(self):
        """
        Instialize a SessionExpAuth instance
        """
        try:
            duration = int(os.environ.get('SESSION_DURATION', 0))
        except Exception:
            duration = 0
        self.session_duration = duration

    def create_session(self, user_id=None) -> Union[str, None]:
        """
        Create session id from random string
        """
        session_id = super().create_session(user_id)
        if session_id == None:
            return None
        self.user_id_by_session_id[session_id] = {
            'user_id': user_id, 'created_at': datetime.now()}
        return session_id

    def user_id_for_session_id(self, session_id=None) -> Union[str, None]:
        """
        Get user id from given session id
        """
        if session_id == None:
            return None
        if session_id not in self.user_id_by_session_id:
            return None
        if self.session_duration <= 0:
            return self.user_id_by_session_id[session_id]['user_id']
        if 'created_at' not in self.user_id_by_session_id[session_id]:
            return None
        created_at = self.user_id_by_session_id[session_id]['created_at']
        if self._has_expired(created_at):
            return None
        return self.user_id_by_session_id[session_id]['user_id']
    
    def _has_expired(self, created_at) -> bool:
        """
        Checks if session has expired
        """
        time_diff = created_at - datetime.now()
        time_diff = divmod(time_diff.days * 24 * 60 * 60 + \
                           time_diff.seconds + self.session_duration, 60)
        print(time_diff)
        return time_diff < (0, 0)
