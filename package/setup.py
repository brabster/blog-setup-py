from setuptools import setup

print("Hello, I'm malicious in setup.py")

setup(
    name="demo-package",
    version="1.0.0",
    package_dir = {"": "src"}
)