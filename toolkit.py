import re
import socket
import uuid


def scan_open_ports(host: str, start_port: int = 1, end_port: int = 1024, timeout: float = 0.3) -> list[int]:
    if start_port < 1 or end_port > 65535 or start_port > end_port:
        raise ValueError("Invalid port range")

    open_ports: list[int] = []
    for port in range(start_port, end_port + 1):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(timeout)
            if sock.connect_ex((host, port)) == 0:
                open_ports.append(port)
    return open_ports


def get_network_info() -> dict[str, str]:
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    mac_raw = uuid.getnode()
    mac_address = ":".join(f"{(mac_raw >> ele) & 0xFF:02x}" for ele in range(40, -1, -8))
    return {"hostname": hostname, "ip_address": ip_address, "mac_address": mac_address}


def check_password_strength(password: str) -> dict[str, str | int]:
    score = 0
    if len(password) >= 8:
        score += 1
    if re.search(r"[A-Z]", password):
        score += 1
    if re.search(r"[a-z]", password):
        score += 1
    if re.search(r"\d", password):
        score += 1
    if re.search(r"[^\w\s]", password):
        score += 1

    if score <= 2:
        level = "Weak"
    elif score <= 4:
        level = "Moderate"
    else:
        level = "Strong"

    return {"score": score, "level": level}
