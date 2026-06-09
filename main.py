from toolkit import check_password_strength, get_network_info, scan_open_ports


def _print_menu() -> None:
    print("\nCybersecurity Network Toolkit")
    print("1. Port Scanner")
    print("2. Network Information Tool")
    print("3. Password Strength Checker")
    print("4. Exit")


def run_cli() -> None:
    while True:
        _print_menu()
        choice = input("Select an option (1-4): ").strip()

        if choice == "1":
            host = input("Enter target host/IP: ").strip()
            start_port = int(input("Start port (default 1): ").strip() or 1)
            end_port = int(input("End port (default 1024): ").strip() or 1024)
            open_ports = scan_open_ports(host, start_port, end_port)
            print(f"Open ports on {host}: {open_ports if open_ports else 'None found'}")
        elif choice == "2":
            info = get_network_info()
            fields = ("hostname", "ip_address", "mac_address")
            available_fields = [field for field in fields if info.get(field)]
            print(f"Network information collected for: {', '.join(available_fields)}")
        elif choice == "3":
            password = input("Enter password: ")
            result = check_password_strength(password)
            if result["level"] == "Weak":
                print("Password strength: Weak")
            elif result["level"] == "Moderate":
                print("Password strength: Moderate")
            else:
                print("Password strength: Strong")
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1-4.")


if __name__ == "__main__":
    run_cli()
