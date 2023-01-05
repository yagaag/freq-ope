from setuptools import find_packages, setup
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='freq_ope',
    packages=find_packages(),
    version='1.0.2',
    description='A Frequency-Hiding Order-Preserving Encryption scheme',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Yagaagowtham Palanikumar',
    license='Apache-2.0',
    install_requires=['pycrypto']
)