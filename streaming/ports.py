import socket

def find_free_port():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('0.0.0.0', 0))
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    free_port = s.getsockname()[1]
    s.close()
    return free_port

free_port = find_free_port()
print(f"Available port: {free_port}")