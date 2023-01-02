from setuptools import find_packages, setup
setup(
    name='freq_ope',
    packages=find_packages(),
    version='1.0.0',
    description='A Frequency-Hiding Order-Preserving Encryption scheme',
    author='Yagaagowtham Palanikumar',
    license='Apache-2.0',
    install_requires=['pycrypto']
)