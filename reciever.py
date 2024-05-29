import socket
import binascii
import pyperclip
from PIL import Image
import io

def handle_received_data(data):
    try:
        # Try to decode as text
        received_text = data.decode()
        pyperclip.copy(received_text)
        print("Clipboard updated with received text:", received_text)
    except UnicodeDecodeError:
        # If decoding as text fails, assume it's image data
        try:
            image_bytes = binascii.unhexlify(data)
            image = Image.open(io.BytesIO(image_bytes))
            image.show()  
            print("Clipboard updated with received image")
        except Exception as e:
            print("Error handling received data:", e)

def start_server():
    host = '0.0.0.0'  # Listen on all available interfaces
    port = 65432      # Arbitrary non-privileged port

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)

    print('Server listening on port', port)
    
    conn, addr = server_socket.accept()
    print('Connected by', addr)
    
    while True:
        data = conn.recv(1024)
        if not data:
            break
        handle_received_data(data)
    
    conn.close()

start_server()