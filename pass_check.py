import hashlib

#A function to check the password salt. It's returning false so it's not hashing correctly.

def check_password(input_password, stored_hash, stored_salt):
    input_password = input_password.encode("utf-8")
    stored_salt = stored_salt.encode("utf-8")
    input_hash = hashlib.pbkdf2_hmac("sha256", input_password, stored_salt, 100000)
    return input_hash.hex() == stored_hash

# Sample stored hash and salt
stored_hash = "17a39a210d7544dbc2da96c3c1452b164193abbe34d4eba024"
stored_salt = "04e60bdbb746ae55e7790db828a93578"

# Example usage
password_to_check = "default"
is_password_correct = check_password(password_to_check, stored_hash, stored_salt)
print(is_password_correct)
