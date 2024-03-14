import re
import binascii
import hashlib

def is_valid_ethereum_address(address):
    if not re.match(r'^(0x)?[0-9a-fA-F]{40}$', address):
        return False
    
    # Checksum validation
    address = address.replace('0x', '')
    address_hash = address.lower()
    address_hash = binascii.unhexlify(address_hash)
    address_hash = hashlib.sha3_256(address_hash).hexdigest()
    for i, c in enumerate(address):
        if c.isdigit():
            if int(address_hash[i], 16) > 7:
                return False
        elif c.isalpha():
            if c.islower() and int(address_hash[i], 16) > 7:
                return False
            elif c.isupper() and int(address_hash[i], 16) <= 7:
                return False
    return True
