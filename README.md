# atecc-ecdh-python - An ECDH Python Example for ATECC608A

This example shows the Elliptic Curve Diffie Hellman key exchange with ephemeral key created on ATECC608A.

## Prerequisites

* Debian 10 host
* Raspberry Pi device
    * e.g. Zero
    * Raspberry Pi OS
    * Attached ATECC608A I2C module
        * Personalized, locked and ready to use

## Setup

```bash
apt update
apt install -y python3 python3-venv build-essentials
python3 -m venv
source venv/bin/activate
pip3 install wheel
pip3 install -r requirements.txt 
```

## ECDH procedure

1. On device: Generate ephemeral key on ATECC608a via `python3 genkey_device.py`
2. Exchange `ec256-device.pub` with host
3. On host: Generate ephemeral key using python `python3 genkey_host.py`
4. Exchange `ec256-host.pub` with host
5. On device: Derive `ec256-device.key` via `python3 ecdh_device.py`
6. On host: Derive  `ec256-host.key` via `python3 ecdh_host.py`
7. On host: Calculate `md5 ec256-host.key`
8. On device: Calculate `md5 ec256-device.key`
9. Compare md5 hashes and see that they match