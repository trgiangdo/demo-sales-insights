from taipy.auth import hash_taipy_password, AnyOf, Credentials
from taipy.gui import State, navigate, notify
import taipy.enterprise.gui as tp_enterprise
import os 
from taipy.config import Config


os.environ["TAIPY_AUTH_HASH"] = "taipy"

username = "Login"
credentials = Credentials(user_name=username, roles=[])

passwords = {
  "florian": hash_taipy_password("florian"),
  "alexandre": hash_taipy_password("alexandre")
}

roles = {
  "florian": ["admin", "TAIPY_ADMIN"],
  "alexandre": ["TAIPY_READER"],
}

Config.configure_authentication("taipy", passwords=passwords, roles=roles)


def on_login(state: State, id, login_args):
    state.username, password = login_args["args"][:2]
    if state.username is None or password is None: # The user canceled the login request
        notify(state, "error", "Login canceled!")
        state.username = 'Login'
        navigate(state, "", force=True)
        return 

    try:
        state.credentials = tp_enterprise.login(state, state.username, password)        
        navigate(state, state.current_page, force=True)
    except:
        notify(state, "error", "Login failed!")
        state.username = 'Login'
        navigate(state, "login", force=True)


login_page = "<|Login|login|>"

admin_page = AnyOf("admin", "Admin", "login")
is_admin = AnyOf("admin", True, False)
