#Stockholm
Stockholm es un script en python que encripta y desencripta los ficheros que haya en el directorio /infection de la carpeta del usuario usando encriptación **AES256** y una clave de encriptación.
##Instalación en Ubuntu:
1. Instalación de python -> apt install python3.8
2. Instalación de pip -> apt install python3-pip
3. Instalación de librería de encriptación AES -> pip install pyAesCrypt  
##Funcionamiento
Al ejecutar el script, este pide una clave de encriptación de al menos 16 caracteres (la clave no es visible al teclearla) y encripta los ficheros que haya en el directorio /infection (y sus subdirectorios) de la carpeta del usuario actual. Afecta a los mismos ficheros que afectaría el Ramsonware WanaCry y los renombra con el mismo nombre y extensión + ".ft". Para desencriptar los ficheros usaremos la opción -r --reverse que nos solicitará la clave de encriptación (la clave no es visible al teclearla). En caso de que la clave sea erronea nos la volverá a pedir.
## Opciones:
- **-v --version Versión.** Muestra la versión actual del programa
- **-h --help Ayuda.** Muestra la ayuda.
- **-r --reverse Revertir encriptación.** Desencripta los ficheros .ft que haya en el directorio del usuario /infection/ tras pedir la clave de encriptación.
- **-o --output Directorio de salida.** Al desencriptar los ficheros podemos elegir en que directorio desencriptarlos. En caso de no existir creará si es posible el directorio seleccionado.
- **-S --silent Modo silencioso.** En este modo el script solo mostrará mensajes al pedir la clave de encriptación y mensajes de error. No mostrará el resto de mensajes informativos. 
