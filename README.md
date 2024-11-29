# ZeroKno

ZeroKno is a simple, easy to use and lightweight zero-knowledge password storage method for Python.
The keys are stored in plain text, while the passwords are stored as base58-encoded SHA-256 hashes.

This makes it impossible for the application to know the password, while still being able to verify it. 
If you want to use this in a production environment, please make sure to use a secure storage method for the keys (e.g. a secure database).

Note that the passwords or values are not encrypted, but hashed. This means that the password cannot be retrieved from the hash, but the hash can be used to verify the password. Basically, you can't recover the password if you lose it.

## Installation

```bash
pip install zerokno
```

## Usage

```python
from zerokno import ZeroKno

# Create a new ZeroKno instance -- app_secret is a secret key for the application and storage is a directory to store the password hashes
zk = ZeroKno(app_secret, storage) 

# Add a new password -- please note that the password is stored as a hash, while the user id is stored as plain text
zk.store("password", "userid")

# Check password match
zk.validate("password", "userid")
# True
zk.validate("passwor1d", "userid")
# False
zk.validate("password", "userid1")
# Error: Userid not found

```

## Errors 

- `Key not found` - This error is raised when the user id is not found in the storage
- Any other error is raised when the storage file is not found or the storage file is corrupted or in any other way not accessible