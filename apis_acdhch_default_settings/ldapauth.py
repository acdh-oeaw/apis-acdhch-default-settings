import os
import pathlib
import logging

from django_auth_ldap.backend import LDAPBackend

logger = logging.getLogger(__name__)


class CustomLDAPBackend(LDAPBackend):
    def authenticate_ldap_user(self, user, *args, **kwargs):
        env = os.environ.get("AUTH_LDAP_USER_LIST", "")
        user_list = env.split(",")
        if env.startswith("file://"):
            try:
                user_list = pathlib.Path.from_uri(env).read_text().splitlines()
            except Exception as e:
                logger.debug("Error reading user list from file: %s", e)
        user_list = list(map(str.strip, user_list))
        if user._username not in user_list:
            logger.debug(
                "User %s not in AUTH_LDAP_USER_LIST, passing on", user._username
            )
            return None
        return super().authenticate_ldap_user(user, *args, **kwargs)
