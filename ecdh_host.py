import base64
from cryptography.hazmat.primitives.serialization import load_pem_private_key
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.backends import default_backend
from cryptography.utils import int_from_bytes

with open("ec256-host.pem", "rb") as fd:
    ec256_host_pem = fd.read()

ec256_host_key = load_pem_private_key(ec256_host_pem,
                                      password=None,
                                      backend=default_backend()
                                     )

with open("ec256-device.pub", "rb") as fd:
    ec256_device_pub = fd.read()

ec256_device_pub = ec.EllipticCurvePublicNumbers(
    curve=ec.SECP256R1(),
    x=int_from_bytes(ec256_device_pub[0:32], byteorder='big'),
    y=int_from_bytes(ec256_device_pub[32:64], byteorder='big'),
).public_key(default_backend())

ec256_host_key = ec256_host_key.exchange(ec.ECDH(), ec256_device_pub)

ec256_host_key_b64 = base64.encodebytes(ec256_host_key).decode("utf8")

with open("ec256-host.key", "wb") as fd:
    fd.write(ec256_host_key)

print(ec256_host_key_b64)