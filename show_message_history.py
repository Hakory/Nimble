import serial


def show_message_history(message):

    serial_port = serial.Serial('AT+CMGL=”{message}"r'.format(message))
    print(serial_port.name)  # Checando se a porta está em uso
    serial_port.write("AT\r\n")
    line = serial_port.readline(size=None, eol='\r\n')
    print(line)
    serial_port.close()
    return

"""message param pode assumir os seguintes valores:

# Recebidas
REC UNREAD
REC READ

#Enviadas
STO UNSENT
STO SENT

#Todas
ALL
"""