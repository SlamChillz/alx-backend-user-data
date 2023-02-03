#!/usr/bin/env python3
"""
Hashing with bcrypt
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """
    hash password
    """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
