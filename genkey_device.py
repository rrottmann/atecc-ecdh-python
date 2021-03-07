from cryptoauthlib import *

ec256_device_pub = bytearray(64)

# Using tempkey slot 0xFFFF/65535 and deriving ecdh_secret
assert atcab_genkey(0xFFFF, ec256_device_pub) == ATCA_SUCCESS

with open("ec256-device.pub", "wb") as fd:
    fd.write(ec256_device_pub)

