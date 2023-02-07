#!/usr/bin/env python3
"""
A module: Defines an template class for all template
for all authentication system implemented in this application
"""
from flask import request

from typing import (
    List,
    TypeVar
)


class Auth:
    """
    API authentication class
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Requires authentication on every request
        """
        path = path + '/' if path is not None and path[-1] != '/' else path
        if (
            path is None
            or excluded_paths is None
            or len(excluded_paths) == 0
            or path not in excluded_paths
        ):
            return True
        return False

    def authorization_header(self, request=None) -> str:
        """
        Extract authorization header
        """
        auth = request.headers.get('Authorization', None)
        if request is None or auth is None:
            return None
        return auth

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Holds the current authenticated logged in user
        """
        return None
