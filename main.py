#!/usr/bin/env python3
"""
Cybersecurity Network Toolkit - Main Entry Point
A comprehensive toolkit for network security analysis and evaluation
"""

import sys
from modules.port_scanner import PortScanner
from modules.network_info import NetworkInfo
from modules.password_checker import PasswordChecker
from modules.intrusion_detection import IntrusionDetection
from modules.packet_sniffer import PacketSniffer
from gui.toolkit_gui import ToolkitGUI


def display_menu():
    """Display the main menu"""
    print("\n" + "="*60)
    print("   CYBERSECURITY NETWORK TOOLKIT")
    print("="*60)
    print("1. Port Scanner")
    print("2. Network Information Tool")
    print("3. Password Strength Checker")
    print("4. Intrusion Detection System")
    print("5. Packet Sniffer")
    print("6. Launch GUI Interface")
    print("7. Exit")
    print("="*60)


def run_port_scanner():
    """Run the port scanner module"""
    print("\n--- PORT SCANNER ---")
    target = input("Enter target IP/hostname: ").strip()
    port_range = input("Enter port range (e.g., 1-1000) or leave empty for common ports: ").strip()
    
    scanner = PortScanner()
    if port_range:
        start, end = map(int, port_range.split('-'))
        scanner.scan(target, start, end)
    else:
        scanner.scan_common_ports(target)


def run_network_info():
    """Run the network information tool"""
    print("\n--- NETWORK INFORMATION TOOL ---")
    net_info = NetworkInfo()
    net_info.display_system_info()
    net_info.display_network_interfaces()
    
    target = input("\nEnter target IP for detailed info (optional, press Enter to skip): ").strip()
    if target:
        net_info.get_target_info(target)


def run_password_checker():
    """Run the password strength checker"""
    print("\n--- PASSWORD STRENGTH CHECKER ---")
    checker = PasswordChecker()
    
    while True:
        password = input("Enter a password to check (or 'q' to quit): ").strip()
        if password.lower() == 'q':
            break
        
        strength = checker.check_strength(password)
        print(f"\nPassword Strength: {strength['level'].upper()}")
        print(f"Score: {strength['score']}/100")
        print("Feedback:")
        for feedback in strength['feedback']:
            print(f"  - {feedback}")
        print()


def run_intrusion_detection():
    """Run the intrusion detection system"""
    print("\n--- INTRUSION DETECTION SYSTEM ---")
    ids = IntrusionDetection()
    
    interface = input("Enter network interface (e.g., eth0, wlan0) or leave empty for default: ").strip()
    duration = input("Enter monitoring duration in seconds (default: 60): ").strip()
    
    try:
        duration = int(duration) if duration else 60
        ids.monitor_network(interface if interface else None, duration)
    except ValueError:
        print("Invalid duration. Using default of 60 seconds.")
        ids.monitor_network(interface if interface else None, 60)


def run_packet_sniffer():
    """Run the packet sniffer module"""
    print("\n--- PACKET SNIFFER ---")
    sniffer = PacketSniffer()
    
    interface = input("Enter network interface (e.g., eth0, wlan0) or leave empty for default: ").strip()
    packet_count = input("Enter number of packets to capture (default: 10): ").strip()
    
    try:
        packet_count = int(packet_count) if packet_count else 10
        sniffer.start_sniffing(interface if interface else None, packet_count)
    except ValueError:
        print("Invalid packet count. Using default of 10.")
        sniffer.start_sniffing(interface if interface else None, 10)


def main():
    """Main function - CLI entry point"""
    if len(sys.argv) > 1 and sys.argv[1] == '--gui':
        # Launch GUI directly
        try:
            gui = ToolkitGUI()
            gui.run()
        except ImportError:
            print("GUI dependencies not installed. Install with: pip install -r requirements-gui.txt")
            sys.exit(1)
        return
    
    # CLI Menu
    while True:
        display_menu()
        choice = input("Select an option (1-7): ").strip()
        
        try:
            if choice == '1':
                run_port_scanner()
            elif choice == '2':
                run_network_info()
            elif choice == '3':
                run_password_checker()
            elif choice == '4':
                run_intrusion_detection()
            elif choice == '5':
                run_packet_sniffer()
            elif choice == '6':
                try:
                    gui = ToolkitGUI()
                    gui.run()
                except ImportError:
                    print("GUI dependencies not installed. Install with: pip install -r requirements-gui.txt")
            elif choice == '7':
                print("\nExiting Cybersecurity Network Toolkit. Goodbye!")
                break
            else:
                print("Invalid option. Please try again.")
        except KeyboardInterrupt:
            print("\n\nOperation cancelled by user.")
        except Exception as e:
            print(f"Error: {str(e)}")
            print("Please try again.")


if __name__ == "__main__":
    main()
