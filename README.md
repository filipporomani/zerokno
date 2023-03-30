# ZeroKno

ZeroKno is a simple, easy to use and lightweight zero-knowledge password storage method for Python.

## Installation

```bash
pip install zerokno
```

## Usage

```python
from zerokno import ZeroKno

# Create a new ZeroKno instance
zk = ZeroKno()

# Add a new password
zk.store("password", "userid")

# Check password match
zk.validate("password", "userid")
# True
zk.validate("passwor1d", "userid")
# False
zk.validate("password", "userid1")
# Error: Userid not found

```
