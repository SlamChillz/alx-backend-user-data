#!/usr/bin/env python3
"""
Defines Session Auth class that uses a file storage DB
"""
from typing import Union

from models.user_session import UserSession
from api.v1.auth.session_exp_auth import SessionExpAuth


class SessionDBAuth(SessionExpAuth):
    """
    Database Session Authentication implementation
    """
    def create_session(self, user_id=None) -> Union[str, None]:
        """
        Create session id from random string
        """
        session_id =  super().create_session(user_id)
        if session_id:
            kwargs = {'user_id': user_id, 'session_id': session_id}
            new_user_session = UserSession(**kwargs)
            new_user_session.save()
        return session_id

    def user_id_for_session_id(self, session_id=None) -> Union[str, None]:
        """
        Get user id based on session id from DB
        """
        usersession = UserSession.get(session_id)
        if usersession:
            if not self._has_expired(usersession.created_at):
                return usersession.user_id
        return None

    def destroy_session(self, request=None) -> bool:
        """
        Deletes the user session from DB / logout user
        """
        if request is None:
            return False
        session_id = self.session_cookie(request)
        if session_id is None:
            return False
        usersession = UserSession.get(session_id)
        if not usersession:
            return False
        usersession.remove()
        return True
