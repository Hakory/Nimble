import subprocess
import os

"""
Disparo padrão de ping, apenas para checar se o rasp está conectado a internet
"""

def ping():
    DEVNULL = open(os.devnull, 'wb')
    try:
        result = subprocess.check_call(["ping", "-c", "8", "www.elitedev.com.br"], stdout=DEVNULL, stderr=DEVNULL)
    except subprocess.CalledProcessError as excep:  # error code <> 0
        result = excep.returncode
    DEVNULL.close()
    return result


if __name__ == "__main__":
    status = ping()
    print(status)