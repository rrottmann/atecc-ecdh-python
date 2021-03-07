import base64
from cryptoauthlib import *

ATCA_SUCCESS = 0x00
load_cryptoauthlib()

cfg = eval('cfg_ateccx08a_i2c_default()')

cfg.cfg.atcai2c.bus = 1
cfg.cfg.atcai2c.slave_address = 0x6A

assert atcab_init(cfg) == ATCA_SUCCESS

with open("ec256-host.pub", "rb") as fd:
    ec256_host_pub = fd.read()

ec256_device_key = bytearray(32)
ec256_device_pub = bytearray(64)

atcab_ecdh_tempkey(ec256_host_pub, ec256_device_key)
assert atcab_genkey(0xFFFF, ec256_device_pub) == ATCA_SUCCESS

with open("ec256-device.pub", "wb") as fd:
    fd.write(ec256_device_pub)

assert atcab_ecdh_tempkey(ec256_host_pub, ec256_device_key) == ATCA_SUCCESS

ec256_device_key_b64 = base64.encodebytes(ec256_device_key).decode('utf8')

with open("ec256-device.key", "wb") as fd:
    fd.write(ec256_device_key)

print("Shared Secret: " + ec256_device_key_b64)