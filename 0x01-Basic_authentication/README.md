# 0x01. Basic authentication

## Requirements
	* Ubuntu
	* python3
	* Pycodestyle
	* Flask
	* emacs/vi/vim

## Tasks
   | Task | Details |
   | ---- | ------- |
   | [ 0. Simple-basic-API ] | serialization/deserialization in files |
   | [ 1. Error handler: Unauthorized ] | executes error handler for 401 by calling `abort(401)` |
   | [ 2. Error handler: Forbidden ] | executes error handler for 403 by calling `abort(403)` |
   | [ 3. Auth class ] | class `Auth` to manage the API authentication |
   | [ 4. Define which routes don't need authentication ] | returns True if the path is not in the list of strings excluded_paths |
   | [ 5. Request validation! ] | filters of each request using Flask `before_request` |
   | [ 6. Basic auth ] | class `BasicAuth` that inherits from `Auth` |
   | [ 7. Basic - Base64 part ] | returns the Base64 part of the `Authorization` header for a Basic Authentication |
   | [ 8. Basic - Base64 decode ] | returns the decoded value of a Base64 string `base64_authorization_header` |
   | [ 9. Basic - User credentials ] | returns the user email and password from the Base64 decoded value |
   | [ 10. Basic - User object ] | returns the User instance based on his email and password |
   | [ 11. Basic - Overload current_user - and BOOM! ] | overloads Auth and retrieves the User instance for a request |
   | [ 12. Basic - Allow password with ":" ] | method def extract_user_credentials(self, decoded_base64_authorization_header) to allow password with : |