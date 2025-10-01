import os
import pathlib

from django_auth_ldap.backend import LDAPBackend


class CustomLDAPBackend(LDAPBackend):
    def authenticate_ldap_user(self, user, *args, **kwargs):
        env = os.environ.get("AUTH_LDAP_USER_LIST", "")
        try:
            user_list = pathlib.Path(env).read_text().splitlines()
        except Exception:
            user_list = env.split(",")
        user_list = list(map(str.strip, user_list))
        if user._username not in user_list:
            return None
        return super().authenticate_ldap_user(user, *args, **kwargs)
