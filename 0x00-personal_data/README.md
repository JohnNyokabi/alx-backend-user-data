# 0x00.Personal data

## Requirements
   * ubuntu
   * emacs/vi/vim
   * python3
   * pycodestyle

## Tasks
   [ 0. Regex-ing ] - function `filter_datum` that returns a log message obfuscated
   [ 1. Log formatter ] - format method to filter values in incoming log records
   [ 2. Create logger ] - get_logger function that returns a `logging.logger` object
   [ 3. Connect to secure database ] - `get_db` function that returns a connector to the database
   [ 4. Read and filter data ] - function that obtains a database connection using `get_db` and retrieve all rows in the users table and display each row under a filtered format like this
   [ 5. Encrypt passwords ] - function `hash_password` that returns a byte string salted, hashed password
   [ 6. Check valid password ] - function `is_valid` that returns a boolean