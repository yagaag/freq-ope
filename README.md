# Freq-OPE

A novel order-preserving encryption scheme based on [this paper](https://drive.google.com/file/d/1so_jRS9AGCLSB59gEl16hqq7uEn4hW4p/view?usp=sharing)

## Installation

Freq-OPE is written and tested in Python 3.8. 

```bash
pip install freq-ope
```

## Usage

Order-Preserving Encryption schemes are used in a client-server setting. Although designed for use in outsourced databases where we have the client and server communicating via API, this library does not provide an implementation of network communication and is provided to the user as a framework to build an API upon. That is, both the client and server are in the same system and the user needs to write API wrappers as needed for practical use cases.

### Step #1: Server
Initialize the the frequency-hiding OPE server by specifying the ciphertext space as required. This is determined by the number of items the database would be expected to store.

```python
from freq_ope.server import OPEServer

server = OPEServer(1<<8) # Setting ciphertext space as 2^8
```

### Step #2: AES
The scheme uses an underlying AES algorithm to encrypt the ciphertexts while preserving order. Initialize an AES object with your preferred key. You can alternatively use the keygen algorithm in the package to generate a random key of needed length. This is done on the client node.

```python
from freq_ope.key import keygen # Optional
from freq_ope.aes import AESCipher 

aes = AESCipher(keygen(128)) # Passing key of length 128
```

### Step #3: Client
Initialize the client object by passing the AESCipher and OPEServer object. In a practical case, pass the API wrapper of the OPEServer object.

```python
from freq_ope.client import OPEClient

client = OPEClient(aes, server)
```

### Step #4: Add data
Add data to the server by passing the plaintexts to the client's function.

```python
plaintexts = [320, 12, 4139, 500, 320]
for pt in plaintexts:
    client.add_plaintext(pt)
```

### Step #5: Fetch data
As mentioned in [the paper](https://drive.google.com/file/d/1so_jRS9AGCLSB59gEl16hqq7uEn4hW4p/view?usp=sharing), the server stores a binary tree which is order-preserving and frequency-hiding with certain values. These values map to certain ciphertexts which is seperately kept in a dictionary. To view these, use the functions in OPEServer (Or the wrapper in an outsourced setting).

```python
# View ciphertext tree
print(client.ope.root.inorderTraversal())

# View encrypted dictionary
print(client.ope.dct)

```

All the aforementioned steps can be found along with some evaluations done on this library  [here](https://github.com/yagaag/freq-ope-eval).

### Author(s)
Yagaagowtham Palanikumar, Arizona State University