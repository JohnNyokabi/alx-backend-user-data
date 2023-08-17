# 0x03. User authentication service

## Requirements
	* Ubuntu
	* Python3
	* Pycodestyle
	* bcrypt
	* SQLAlchemy
	* vi/vim/emacs

## Tasks
   | Task | Details |
   | ---- | ------- |
   | [ 0. User model ] | SQLAlchemy model named User for a database table named users |
   | [ 1. create user ] | method that saves the user to the database |
   | [ 2. Find user ] | method that takes in arbitrary keyword arguments and returns the first row found in the users table as filtered by the method’s input arguments |
   | [ 3. update user ] | method that use find_user_by to locate the user to update, then will update the user’s attributes as passed in the method’s arguments then commit changes to the database |
   | [ 4. Hash password ] | method that returns bytes from password string argument |
   | [ 5. Register user ] | takes in mandatory email and password string arguments and return a User object |
   | [ 6. Basic Flask app ] | returns JSON payload |
   | [ 7. Register user ] | method for registering new user |
   | [ 8. Credentials validation ] | Tries locating the user's existence by email. Checks the password with `bcrypt.checkpw` and returns True if it exists otherwise returns False |
   | [ 9. Generate UUIDs ] | function that returns a string representation of a new UUID |
   | [ 10. Get session ID ] | method that finds the user corresponding to an email, generates a new UUID and store it in the database as the user’s session_id, then returns the session ID |
   | [ 11. Log in ] | method that implements a login function to respond to the `POST /sessions` route |
   | [ 12. Find user by session ID ] | method that takes in a single session_id string argument and returns the corresponding User or None |
   | [ 13. Destroy session ] | method updates the corresponding user’s session ID to None |
   | [ 14. Log out ] | method that implements logout function |
   | [ 15. User profile ] | method that finds the user profile |
   | [ 16. Generate reset password token ] | Finds the user corresponding to the email and generates a UUID and update the user’s reset_token database field |
   | [ 17. Get reset password token ] | method that generates a token and respond with a 200 HTTP status and a JSON payload |
   | [ 18. Update password ] | updates the user’s hashed_password field with the new hashed password and the reset_token field to None |
   | [ 19. Update password end-point ] | method for updating password end-point |
   | [ 20. End-to-end integration test ] | functions that Use the requests module to query the web server for the corresponding end-point |