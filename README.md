# Cybersecurity Network Toolkit

A comprehensive Python-based toolkit for network security analysis, featuring port scanning, network reconnaissance, password evaluation, intrusion detection, and packet analysis with both CLI and GUI interfaces.

![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Status](https://img.shields.io/badge/Status-Active-brightgreen.svg)

## 📋 Features

### Core Tools

#### 1. **Port Scanner** 🔍
- Detect open ports on target systems
- Multi-threaded scanning for performance
- Common ports database with service identification
- Custom port range scanning
- Real-time progress reporting

#### 2. **Network Information Tool** 🌐
- Display system information (OS, hostname, architecture)
- Show network interfaces and IP configuration
- Hostname resolution and DNS lookups
- System network details
- Target network reconnaissance

#### 3. **Password Strength Checker** 🔐
- Comprehensive password evaluation
- Security level assessment (Very Weak to Excellent)
- Detailed improvement feedback
- Detects weak password patterns
- Estimates password crack time

#### 4. **Intrusion Detection System** 🛡️
- Network traffic monitoring
- Suspicious connection detection
- Port scanning identification
- Security alert logging
- Threat analysis and reporting

#### 5. **Packet Sniffer** 📦
- Network packet capture and analysis
- Protocol distribution analysis
- IP traffic statistics
- Packet content inspection
- Network behavior analysis

#### 6. **GUI Interface** 🖥️
- User-friendly tkinter interface
- Tabbed design for easy navigation
- Real-time output display
- Cross-platform compatibility
- Non-blocking operations with threading

## 🚀 Quick Start

### Installation

```bash
# Clone the repository
git clone https://github.com/Hydra038/Cybersecurity-Network-Toolkit-Python-.git
cd Cybersecurity-Network-Toolkit-Python-

# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Running the Toolkit

**CLI Mode:**
```bash
python3 main.py
```

**GUI Mode:**
```bash
python3 main.py --gui
```

**With elevated privileges (for IDS/Sniffer):**
```bash
sudo python3 main.py
sudo python3 main.py --gui
```

## 📖 Usage Examples

### Port Scanner
```bash
# Run from menu
Select option: 1
Enter target IP/hostname: 192.168.1.1
Enter port range (e.g., 1-1000) or leave empty for common ports: 
```

### Password Strength Checker
```bash
# Run from menu
Select option: 3
Enter a password to check: MySecure!Pass123
# Output: Excellent (Score: 85/100)
```

### Network Information
```bash
# Run from menu
Select option: 2
# Displays system info, network interfaces, and DNS information
```

### Intrusion Detection
```bash
# Requires elevated privileges
sudo python3 main.py
Select option: 4
Enter monitoring duration: 60
# Monitors for suspicious network activity
```

### Packet Sniffer
```bash
# Requires elevated privileges
sudo python3 main.py
Select option: 5
Enter number of packets: 100
# Captures and analyzes network packets
```

## 📁 Project Structure

```
Cybersecurity-Network-Toolkit-Python-/
├── main.py                 # Main entry point with CLI menu
├── requirements.txt        # Python dependencies
├── requirements-gui.txt    # GUI specific dependencies
├── README.md              # This file
├── INSTALLATION.md        # Installation guide
├── USAGE.md              # Detailed usage guide
├── modules/              # Core modules
│   ├── __init__.py
│   ├── port_scanner.py   # Port scanning functionality
│   ├── network_info.py   # Network information gathering
│   ├── password_checker.py # Password strength evaluation
│   ├── intrusion_detection.py # IDS functionality
│   └── packet_sniffer.py # Packet capture and analysis
└── gui/                  # GUI components
    ├── __init__.py
    └── toolkit_gui.py    # tkinter GUI implementation
```

## 🔧 Technologies Used

- **Python 3.7+** - Core language
- **Socket Programming** - Network communication
- **Threading** - Multi-threaded scanning
- **Tkinter** - GUI interface
- **OS/Subprocess** - System commands
- **Struct** - Binary data handling

## 🎯 Features in Detail

### Port Scanner
- Supports both IPv4 addresses and hostnames
- 30+ pre-configured common ports
- Customizable port ranges
- Service identification for known ports
- Multi-threaded for speed and efficiency
- Timeout handling for unresponsive hosts

### Network Information
- System details (OS, Python version, architecture)
- Local IP and MAC address detection
- Full Qualified Domain Name (FQDN)
- Hostname resolution with all associated IPs
- Target reachability testing (ping)
- DNS record lookups

### Password Strength Checker
- Length analysis (8 char minimum, 12+ good, 16+ excellent)
- Character type verification (upper, lower, numbers, symbols)
- Pattern detection (consecutive, repeated, sequential)
- Common password dictionary check
- Scoring system (0-100)
- Crack time estimation

### Intrusion Detection System
- Real-time connection monitoring
- Suspicious port detection (backdoor ports)
- Port scanning pattern identification
- Alert logging and reporting
- Network interface monitoring
- Windows and Unix/Linux support

### Packet Sniffer
- Live packet capture
- Protocol analysis (TCP, UDP, ICMP)
- Source and destination IP tracking
- Packet size analysis
- Traffic statistics and summary
- IP traffic distribution reporting

### GUI Interface
- Dark theme for reduced eye strain
- Tabbed interface for organization
- Real-time output scrolling
- Threading for responsive UI
- Input validation
- Error handling with dialog boxes

## ⚙️ Requirements

### Minimum Requirements
- Python 3.7+
- pip package manager
- 50MB disk space

### System Requirements
- **Port Scanner**: Network connectivity
- **Network Info**: Network interface access
- **Password Checker**: No special requirements
- **IDS/Packet Sniffer**: Administrator/root privileges, network interface access

### Optional Requirements
- **GUI**: tkinter (usually included with Python)
  - Ubuntu/Debian: `sudo apt-get install python3-tk`
  - Fedora/RHEL: `sudo dnf install python3-tkinter`

## 📚 Documentation

- [INSTALLATION.md](INSTALLATION.md) - Detailed installation instructions
- [USAGE.md](USAGE.md) - Comprehensive usage guide
- Code comments in individual modules

## ⚖️ Legal and Ethical Notice

**IMPORTANT**: This toolkit is designed for educational purposes and authorized security testing only.

**Responsible Use:**
- Only scan systems you own or have explicit permission to scan
- Obtain proper authorization before network monitoring
- Use for legitimate security research and testing
- Respect privacy and applicable laws
- Do not use for unauthorized network access or attacks

**Disclaimer:**
Users are solely responsible for their use of this software. The authors assume no liability for misuse or damage caused by this tool.

## 🤝 Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📝 Future Improvements

- [ ] Add intrusion detection features enhancement
- [ ] Implement advanced packet analysis
- [ ] Add GeoIP location tracking
- [ ] Enhanced GUI with graphs and charts
- [ ] Configuration file support
- [ ] Multi-threaded GUI operations
- [ ] Network topology mapping
- [ ] Vulnerability scanning integration
- [ ] Export reports (PDF, CSV)
- [ ] SSH/SSL certificate analysis

## 🐛 Troubleshooting

### Permission Denied
```bash
# Linux/macOS - use sudo
sudo python3 main.py

# Windows - Run as Administrator
# Right-click Command Prompt → Run as administrator
```

### Module Not Found
```bash
pip install -r requirements.txt
pip install -r requirements-gui.txt
```

### GUI Won't Start
```bash
# Test tkinter installation
python3 -m tkinter
```

For more help, see [INSTALLATION.md](INSTALLATION.md)

## 📊 Version History

- **v1.0** (Current) - Initial release with all core features
  - Port Scanner with multi-threading
  - Network Information Tool
  - Password Strength Checker
  - Intrusion Detection System
  - Packet Sniffer
  - Complete GUI Interface

## 📞 Support

For issues, questions, or suggestions:
1. Check existing documentation (README.md, USAGE.md, INSTALLATION.md)
2. Review code comments for specific features
3. Open an issue on GitHub

## 📄 License

This project is licensed under the MIT License - see LICENSE file for details.

## 👤 Author

**Hydra038**

## 🙏 Acknowledgments

- Python community for excellent standard library
- Security community for best practices
- Contributors and testers

## 🔗 Links

- [Python Documentation](https://docs.python.org/)
- [Socket Programming Guide](https://docs.python.org/3/library/socket.html)
- [Cybersecurity Resources](https://www.cybersecurityinstitute.org/)

---

**Last Updated**: 2024
**Status**: Active Development
**Python Version**: 3.7+
