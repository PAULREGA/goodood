"""Code constants"""

import os
import random
import string


class _Const():
    """String constants"""
    @property
    def default_constants(self):
        """default_constants"""
        return "default_constants"

    @property
    def secret_key(self):
        """secret_key"""
        secret = ''.join(  # generating random secret-key
            random.choice(
                string.ascii_letters
            ) for i in range(32)
        )
        return secret

    @property
    def email_template(self):
        """Template for email data object"""
        url = os.getenv('APP_URL')
        port = os.getenv('APP_PORT')
        return {
            'sender': "no-reply@app.com",
            'app_name': os.getenv('APP_NAME'),
            'title': None,
            'email': None,
            'body': None,
            'message': None,
            'url': f"{url}:{port}/api",
            'url_token': None,
            'greeting': None,
            'button': None,
        }
