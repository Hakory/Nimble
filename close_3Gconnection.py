import os
import sys
import signal

"""
Fecha a conexão matando o processo pelo PID
Obs -> Esse PID é retornado pela funcão open_3Gconnection

"""

def close_3Gconnection(arguments):
    pid = int(arguments[1])
    print(pid)
    os.kill(pid, signal.SIGTERM)


if __name__ == "__main__":
    close_3Gconnection(sys.argv)
