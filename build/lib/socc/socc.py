import socket
import telnetlib

class socc:
    """A small wrapper class for socket to provide cleaner code."""
    def __init__(self, host, port):
        """Create a socket connection to given host and port."""
        self._host = host
        self._port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((host, port))

    def send(self, message):
        """Send a string over the socket."""
        if message[-1:] != "\n":
            message += "\n"
        self.socket.send(message.encode())

    def send_bytes(self, message):
        """Send a bytes object over the socket."""
        if message[-1:] != b"\n":
            message += b"\n"
        self.socket.send(message)

    def recv(self, amount=1024):
        """Recieve a string over the socket."""
        return self.socket.recv(amount).decode()

    def recv_bytes(self, amount=1024):
        """Recieve a bytes object over the socket."""
        return self.socket.recv(amount)

    def ignore(self, number_of_lines=1, amount=1024):
        """Recieve and ignore the specified amount of lines from the socket."""
        for i in range(0, number_of_lines):
            self.socket.recv(amount)

    def duplicate(self):
        """Returns a new socc object of the same host and port."""
        return socc.socc(self._host, self._port)

    def interact(self):
        """Allows the user to interact with the socket."""
        t = telnetlib.Telnet()
        t.sock = self.socket
        t.interact()

    def close(self):
        """Closes the socket."""
        self.socket.close()
