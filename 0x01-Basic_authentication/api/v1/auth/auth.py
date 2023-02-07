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
        return False

    def authorization_header(self, request=None) -> str:
        """
        Extract authorization header
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Holds the current authenticated logged in user
        """
        return None
