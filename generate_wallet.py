import ecdsa
import binascii
from Crypto.Hash import keccak

def generate_ethereum_keypair():
    private_key = ecdsa.SigningKey.generate(curve=ecdsa.SECP256k1)
    public_key = private_key.get_verifying_key()
    private_key_hex = binascii.hexlify(private_key.to_string()).decode()
    public_key_hex = binascii.hexlify(public_key.to_string()).decode()
    return private_key_hex, public_key_hex

def derive_ethereum_address(public_key_hex):
    public_key_bytes = binascii.unhexlify(public_key_hex)
    keccak_hash = keccak.new(digest_bits=256)
    keccak_hash.update(public_key_bytes)
    hash_result = keccak_hash.digest()
    ethereum_address = '0x' + binascii.hexlify(hash_result[-20:]).decode()
    return ethereum_address

private_key_hex, public_key_hex = generate_ethereum_keypair()
print(f"Chave Privada Ethereum: {private_key_hex}")


ethereum_address = derive_ethereum_address(public_key_hex)
print(f"Endereço Ethereum: {ethereum_address}")
