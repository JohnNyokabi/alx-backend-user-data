# 0x02. Session authentication

## Requirements
	* Ubuntu
	* python3
	* Pycodestyle
	* Flask
	* emacs/vi/vim

## Tasks
   | Task | Details |
   | ---- | ------- |
   | [ 0. Et moi et moi et moi! ] | endpoint `GET /users/me` that retrieves the authenticated User object |
   | [ 1. Empty session ] | class `SessionAuth` that inherits from Auth |
   | [ 2. Create a session ] | retrieves an User id based on a Session ID |
   | [ 3. User ID for Session ID ] | instance method `def user_id_for_session_id(self, session_id: str = None) -> str:` that returns a `User` ID based on a Session ID |
   | [ 4. Session cookie ] |  method `def session_cookie(self, request=None):` that returns a cookie value from a request |
   | [ 5. Before request ] | URL path `/api/v1/auth_session/login/` in the list of excluded paths of the method `require_auth` - this route should be accessible outside authentication |
   | [ 6. Use Session ID for identifying a User ] | instance method `def current_user(self, request=None):` (overload) that returns a User instance based on a cookie value |
   | [ 7. New view for Session Authentication ] | new Flask view that handles all routes for the Session authentication |
   | [ 8. Logout ] | Updated the class SessionAuth by adding a new method `def destroy_session(self, request=None):` that deletes the user session / logout |
   | [ 9. Expiration? ] | Updated `api/v1/app.py` to instantiate auth with `SessionExpAuth` if the environment variable `AUTH_TYPE` is equal to `session_exp_auth` |
   | [ 10. Sessions in database ] | Updated `api/v1/app.py` to instantiate auth with `SessionDBAuth` if the environment variable `AUTH_TYPE` is equal to `session_db_auth` |