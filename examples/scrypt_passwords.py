import os
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt
from cryptography.hazmat.backends import default_backend

# Returns N random bytes
salt = os.urandom(16)

kdf = Scrypt(salt=salt, 
            length=32, 
            n=2**14, 
            r=8, 
            p=1, 
            backend=default_backend()
            )

key = kdf.derive(b'mypass123')

kdf = Scrypt(salt=salt,
            length=32,
            n=2**14,
            r=8,
            p=1,
            backend=default_backend()
            )

kdf.verify(b'mypass123', key)