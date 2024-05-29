# Clipboard Sync via Socket Programming

This project allows you to transfer copied text and images between two devices connected to the same network using socket programming. The client monitors the clipboard for changes and sends the copied data to the server. The server then updates its clipboard with the received data.

## Features

- Monitors clipboard for text and image changes.
- Converts images to hexadecimal format for easy transmission.
- Transfers clipboard data over a network using socket programming.
- Updates the clipboard on the receiving device with the received data.

## Requirements

- Python 3.x
- `Pillow` library for handling images
- `pyperclip` library for clipboard operations

## Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/jainikkhil/CTRL-C-V_ALL_DEVICES_HOTSPOT_-SOCKET-.git
    cd CTRL-C-V_ALL_DEVICES_HOTSPOT_-SOCKET-
    ```

2. Install the required Python libraries:

    ```sh
    pip install pillow pyperclip
    ```

## Usage

### Server

1. Open a terminal on the server device.
2. Run the server script:

    ```sh
    python server.py
    ```

### Client

1. Open a terminal on the client device.
2. Update the `SERVER_IP_ADDRESS` in the `client.py` script with the actual IP address of the server device.
3. Run the client script:

    ```sh
    python client.py
  
