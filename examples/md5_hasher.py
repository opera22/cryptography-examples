import hashlib
import string

# Returns a hash object
md5hasher = hashlib.md5(b'a'*100000)
# Returns bytes
print(md5hasher.digest())
# Returns hex string
print(md5hasher.hexdigest())

# Even-or-odd is also a "hash" function, although not a "cryptographic" one
# This is because the "domain" (all positive ints) is larger than the "range" (even or odd)
num = 13
print('EVEN' if num % 2 == 0 else 'ODD')

md5hash_seed = hashlib.md5(b'M').hexdigest()

for letter in string.ascii_uppercase:
    print(f"Testing letter: {letter}")
    md5hash_test = hashlib.md5(str.encode(letter)).hexdigest()
    if md5hash_test == md5hash_seed:
        print("Found match:")
        print(md5hash_seed)
        print(md5hash_test)
        break


