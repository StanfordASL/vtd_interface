import cstruct
import socket

SCP_DEFAULT_PORT = 48179
SCP_NAME_LENGTH  = 64
SCP_MAGIC_NO     = 40108
SCP_VERSION      = 0x0001
TCP_IP           = '127.0.0.1'

scp_conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
scp_conn.connect((TCP_IP, SCP_DEFAULT_PORT))

class SCP_MSG_HDR_t(cstruct.CStruct):
    __byte_order__ = cstruct.LITTLE_ENDIAN
    __struct__ = """
        unsigned short magicNo;
        unsigned short version;
        char sender[64];
        char receiver[64];
        unsigned int dataSize;
    """

    def get_msg(self, text, sender="SCP", receiver="TaskControl"):
        self.magicNo = SCP_MAGIC_NO
        self.version = SCP_VERSION
        self.sender = bytes(sender)
        self.receiver = bytes(receiver)
        payload = bytes(text) + b"\x00"
        self.dataSize = len(payload)
        return self.pack() + payload

def send_message(content):
    msg_class = SCP_MSG_HDR_t()
    msg = msg_class.get_msg(content)
    try:
        scp_conn.send(msg)
    except:
        print("Connection lost ... reconnecting")
        # scp_conn.shutdown()
        scp_conn.close()
        scp_conn.connect((TCP_IP, SCP_DEFAULT_PORT))
        scp_conn.send(msg)