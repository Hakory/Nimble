import subprocess
import os
import sys

"""
Abre conexão e retorna o pid do processo
"""

def open_3Gconnection():
    DEVNULL = open(os.devnull, 'wb')
    try:
        wvdial = subprocess.Popen(["wvdial", "3gconnect"], stdout=DEVNULL, stderr=DEVNULL)
    except subprocess.CalledProcessError as ex:  # error code <> 0
        print(ex.returncode)
        sys.exit(-1)

    DEVNULL.close()
    return wvdial.pid


if __name__ == "__main__":
    wvdial_PID = open_3Gconnection()
    print(wvdial_PID)