#!/usr/bin/env python3
"""
Defines a BasicAuth class that inherits from Auth class
"""
import base64

from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """
    Basic Authentication class implementation
    """
    def extract_base64_authorization_header(
        self, authorization_header: str
    ) -> str:
        """
        Extract Authorization header value
        """
        if (
            authorization_header is None
            or type(authorization_header) != str
            or not authorization_header.startswith('Basic ')
        ):
            return None
        return ''.join(authorization_header.split('Basic ')[1:])

    def decode_base64_authorization_header(
        self, base64_authorization_header: str
    ) -> str:
        """
        Base64 encode authorization_header
        """
        if (
            base64_authorization_header is None
            or type(base64_authorization_header) != str
        ):
            return None
        try:
            encoded = base64.b64decode(base64_authorization_header)
        except Exception:
            return None
        return encoded.decode('utf-8')
