import serial
import sys
from curses import ascii

def sendsms(phoneNumber, message):
    serial_port = serial.Serial('/dev/ttyUSB1')
    print(serial_port.name)  # Checando se a porta está em uso

    serial_port.write("AT\r\n")
    line = serial_port.readline(size=None, eol='\r\n')
    print(line)

    serial_port.write("AT+CMGF=1\r\n")
    line = serial_port.readline(size=None, eol='\r\n')
    print(line)

    serial_port.write('AT+CMGS="{phoneNumber}"\r\n'.format(phoneNumber))
    serial_port.write(message)
    serial_port.write(ascii.ctrl('z'))
    print(serial_port.readline())
    serial_port.close()
    return


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Wrong number of arguments\nUsage: send_sms.py <phone number> <message text>")
        sys.exit(-1)

    phoneNumber = sys.argv[1]
    smsText = sys.argv[2]
    sendsms(phoneNumber, smsText)
