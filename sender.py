import socket
import pyperclip
import time
from PIL import ImageGrab,Image
import io
import binascii
def send_data(data):
    host = 'server_ip(reciever)'  # IP address of the server device
    port = 65432

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    client_socket.sendall(data)
    print("sent data")
    client_socket.close()

def get_clipboard_image():
    try:
        clipboard_data = ImageGrab.grabclipboard()
        if isinstance(clipboard_data, Image.Image):
            # Single image
            with io.BytesIO() as output:
                clipboard_data.save(output, format="PNG")
                hex_data = binascii.hexlify(output.getvalue()).decode()

                return hex_data
        elif isinstance(clipboard_data, list) and all(isinstance(item, Image.Image) for item in clipboard_data):
            # List of images
            with io.BytesIO() as output:
                clipboard_data[0].save(output, format="PNG")  # Process the first image in the list
                hex_data = binascii.hexlify(output.getvalue()).decode()
                return hex_data
    except Exception as e:
        print("Error capturing image:", e)
    

def monitor_clipboard():
    recent_text = ""
    recent_image = None
    while True:
        # Check for text changes
        tmp_text = pyperclip.paste()
        if tmp_text != recent_text:
            recent_text = tmp_text
            print("Clipboard changed (text):", recent_text)
            send_data(recent_text.encode())  # Convert to bytes before sending
        
        # Check for image changes
        image_data = get_clipboard_image()
        if image_data != recent_image:
            recent_image = image_data
            print("Clipboard changed (image)")
            send_data(image_data.encode())  # Send image data

        time.sleep(1)

monitor_clipboard()
