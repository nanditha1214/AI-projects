"""
DeepSeek AI Server for Raspberry Pi Pico W

Feel free to submit pull requests. I can't find or solve all bugs by myself
KNOWN BUGS:
  -server script hits an error after sending a long response, leading client to reach a timeout before the next prompt
    'ConnectionResetError: [WinError 10054] An existing connection was forcibly closed by the remote host'
-------------------------------------------
This script sets up a TCP server on a desktop that:
1. Listens for incoming queries from a client.
2. Sends queries to DeepSeek AI using the `ollama` library.
3. Streams the AI response to the console in real-time.
4. Sends the **complete response** (without `<think>` tags) back to the client.

Author: nanditha1214
GitHub: https://github.com/nanditha1214/AI-projects

import socket
import ollama
import re

# Server Configuration
HOST = ''  # Listen on all network interfaces
PORT = 8000  # Change this if needed, but update the client as well

def get_local_ip():
    """
    Returns the desktop's local IP address.
    This is useful for finding where the server is running. This will be needed for the client code
    """
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        try:
            s.connect(("8.8.8.8", 80))  # Google's public DNS
            return s.getsockname()[0]
        except Exception:
            return "127.0.0.1"  # Fallback to localhost

def clean_response(response):
    """
    Removes <think> tags from DeepSeek's response.
    This ensures only relevant text is sent to the Pico W.
    """
    return re.sub(r"</?think>", "", response).strip()

def query_deepseek(prompt):
    """
    Sends a user query to DeepSeek AI.
    
    - Streams the response in real-time to the console.
    - Returns the **full response** to send to Pico W.

    Notes:
    - The `ollama.chat()` function uses `stream=True` for real-time response streaming.
    - The collected response is cleaned before sending it back.
    - If you want to handle **conversation history**, modify the `messages` list.
    """
    full_response = ""

    completion = ollama.chat(
        model="deepseek-r1:1.5b",  # Change this if using another model
        messages=[{"role": "user", "content": prompt}],  
        stream=True
    )

    for chunk in completion:
        if 'message' in chunk and 'content' in chunk['message']:
            content = chunk['message']['content']
            print(content, end='', flush=True)  # Stream to console
            full_response += content

    print("\n")  # Newline for better readability
    return clean_response(full_response)  # Return clean text

def start_server():
    """
    Starts the TCP server to handle queries from the Pico W.

    - Prints the **desktop’s IP address** (so you know where the server is running).
    - Accepts **multiple client connections** (one at a time).
    - Sends DeepSeek’s response **only after it's fully received**.
    """
    print(f"Desktop IP Address: {get_local_ip()}")
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((HOST, PORT))
        s.listen()
        print(f"Server listening on port {PORT}...")

        while True:
            conn, addr = s.accept()
            with conn:
                print(f"Connected by {addr}")
                while True:
                    data = conn.recv(1024).decode().strip()
                    if not data:
                        break
                    
                    print(f"Received query: {data}")
                    response = query_deepseek(data)  # Stream to console, return full response
                    print("\nComplete Response Sent to Pico W\n")
                    
                    conn.sendall(response.encode())  # Send full response at once

# Start the server
if __name__ == "__main__":
    start_server()
