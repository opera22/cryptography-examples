import string

def create_shift_substitutions(n: int) -> tuple[dict, dict]:
    encoding = {}
    decoding = {}
    # string.ascii_uppercase is a set: ABCDEFGHIJKLMNOPQRSTUVWXYZ
    alphabet_size = len(string.ascii_uppercase)
    for i in range(alphabet_size):
        letter = string.ascii_uppercase[i]
        subst_letter = string.ascii_uppercase[(i + n) % alphabet_size]

        encoding[letter] = subst_letter
        decoding[subst_letter] = letter
    return encoding, decoding

def encode(message: str, subst: dict) -> str:
    cipher = ''
    for letter in message:
        if letter in subst:
            cipher += subst[letter]
        else:
            cipher += letter
    return cipher

# Alternative definition
# def encode (message, subst):
#     return "".join(subst.get(x, x) for x in message)

# Note it is the same logic
def decode(message: str, subst: dict) -> str:
    return encode(message, subst)

print(encode('HELLO WORLD', create_shift_substitutions(1)[0]))
print(decode('IFMMP XPSME', create_shift_substitutions(1)[1]))


# Cracking the shift cipher
encrypted_message = 'FANQADZAFFANQFTMFUEFTQCGQEFUAZ'

# Try all 25 possible shifts
for i in range(1,26):
    print(f'{i} ', decode(encrypted_message, create_shift_substitutions(i)[1]))
# i of 12 seems to crack it
