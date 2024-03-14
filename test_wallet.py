from validate_wallet import is_valid_ethereum_address

def test_invalid_address():
    address1 = '0xbe549cd745c407f1046701d632081df9c9934cf3'
    address2 = '0x90f48bc9d2b4e1b54314b0f6ffe7b11f7a685524'
    assert not is_valid_ethereum_address(address1)
    assert not is_valid_ethereum_address(address2)
