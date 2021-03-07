from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives.serialization import Encoding, PublicFormat, PrivateFormat, NoEncryption


def convert_ec_pub_to_pem(raw_pub_key):
    public_key_der = bytearray.fromhex('3059301306072A8648CE3D020106082A8648CE3D03010703420004') + raw_pub_key
    public_key_b64 = base64.b64encode(public_key_der).decode('ascii')
    public_key_pem = (
            '-----BEGIN PUBLIC KEY-----\n'
            + '\n'.join(public_key_b64[i:i + 64] for i in range(0, len(public_key_b64), 64)) + '\n'
            + '-----END PUBLIC KEY-----'
    )
    return public_key_pem


ec256_host_key = ec.generate_private_key(ec.SECP256R1(), default_backend())
ec256_host_pub = ec256_host_key.public_key().public_bytes(encoding=Encoding.X962,
                                                          format=PublicFormat.UncompressedPoint)[1:]
with open("ec256-host.pem", 'wb') as fd:
    ec256_host_key_pem = ec256_host_key.private_bytes(
        encoding=Encoding.PEM,
        format=PrivateFormat.PKCS8,
        encryption_algorithm=NoEncryption()
    )
    fd.write(ec256_host_key_pem)
with open("ec256-host.pub", 'wb') as fd:
    fd.write(ec256_host_pub)
