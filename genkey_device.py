from cryptoauthlib import *

ATCA_SUCCESS = 0x00
load_cryptoauthlib()

cfg = eval('cfg_ateccx08a_i2c_default()')

cfg.cfg.atcai2c.bus = 1
cfg.cfg.atcai2c.slave_address = 0x6A

assert atcab_init(cfg) == ATCA_SUCCESS

ec256_device_pub = bytearray(64)

# Using tempkey slot 0xFFFF/65535 and deriving ecdh_secret
assert atcab_genkey(0xFFFF, ec256_device_pub) == ATCA_SUCCESS

with open("ec256-device.pub", "wb") as fd:
    fd.write(ec256_device_pub)

