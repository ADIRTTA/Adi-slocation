import requests
from colorama import Fore, Style, init
import socket
import os

# Initialize colorama
init(autoreset=True)

def clear():
    os.system('clear')  # Clears the terminal

def ascii_banner():
    banner = """
             ___    ____  ________  _______________
            /   |  / __ \/  _/ __ \/_  __/_  __/   |
           / /| | / / / // // /_/ / / /   / / / /| |      code by adirtta 💀
          / ___ |/ /_/ // // _, _/ / /   / / / ___ |       THANK YOU FOR USE MY TOOL❤️
         /_/  |_/_____/___/_/ |_| /_/   /_/ /_/  |_|        don't copy my tool🤗

                    IP Location Finder Tool
    """
    print(Fore.BLUE + banner)

def get_location_from_ip(ip):
    try:
        response = requests.get(f"http://ip-api.com/json/{ip}").json()
        if response['status'] == 'success':
            details = {
                "IP": ip,
                "Status": response['status'],
                "Country": response['country'],
                "Country Code": response['countryCode'],
                "Region": response['region'],
                "Region Name": response['regionName'],
                "City": response['city'],
                "ZIP": response['zip'],
                "Lat": response['lat'],
                "Lon": response['lon'],
                "Timezone": response['timezone'],
                "ISP": response['isp'],
                "Org": response['org'],
                "AS": response['as'],
                "Google Maps": f"https://www.google.com/maps/place/{response['lat']}+{response['lon']}",
                "Website": get_website_from_ip(ip)  # New feature: website name
            }
            return details
        else:
            return {"Status": "Location not found"}
    except requests.RequestException:
        return {"Status": "Error fetching location"}

def get_website_from_ip(ip):
    try:
        # Perform reverse DNS lookup to get the website/domain associated with the IP
        domain = socket.gethostbyaddr(ip)[0]
        return domain
    except (socket.herror, socket.gaierror):
        return "No associated website found"

def track_own_ip():
    try:
        # Using an external service to get the user's own public IP address
        ip_response = requests.get("https://api64.ipify.org?format=json").json()
        ip = ip_response['ip']
        print(Fore.GREEN + f"Your IP: {ip}")
        return ip
    except requests.RequestException:
        print(Fore.RED + "Error fetching your IP.")
        return None

def main():
    clear()  # Clear the screen before showing the banner
    ascii_banner()
    print(Fore.YELLOW + Style.BRIGHT + "IP Location Finder with Detailed Information")
    print(Fore.BLUE + "1. Track Your Own IP")
    print(Fore.BLUE + "2. Track Victim's IP")

    choice = input(Fore.RED + "Choose mode (1/2): ")

    if choice == '1':
        # Track your own IP
        ip = track_own_ip()
        if ip:
            location_info = get_location_from_ip(ip)
        else:
            print(Fore.RED + "Unable to get your IP address.")
            return
    elif choice == '2':
        # Track a victim's IP
        ip = input(Fore.GREEN + "Enter Victim's IP address: ")
        location_info = get_location_from_ip(ip)
    else:
        print(Fore.RED + "Invalid choice! Exiting.")
        return

    if "Status" in location_info and location_info["Status"] == 'success':
        # Print detailed information
        print(Fore.CYAN + f"| IP: {location_info['IP']}")
        print(Fore.CYAN + f"| Status: {location_info['Status']}")
        print(Fore.CYAN + f"| Country: {location_info['Country']}")
        print(Fore.CYAN + f"| Country Code: {location_info['Country Code']}")
        print(Fore.CYAN + f"| Region: {location_info['Region']}")
        print(Fore.CYAN + f"| Region Name: {location_info['Region Name']}")
        print(Fore.CYAN + f"| City: {location_info['City']}")
        print(Fore.CYAN + f"| ZIP: {location_info['ZIP']}")
        print(Fore.CYAN + f"| Lat: {location_info['Lat']}")
        print(Fore.CYAN + f"| Lon: {location_info['Lon']}")
        print(Fore.CYAN + f"| Timezone: {location_info['Timezone']}")
        print(Fore.CYAN + f"| ISP: {location_info['ISP']}")
        print(Fore.CYAN + f"| Org: {location_info['Org']}")
        print(Fore.CYAN + f"| AS: {location_info['AS']}")
        print(Fore.CYAN + f"| Map: {location_info['Google Maps']}")
        print(Fore.CYAN + f"| Website: {location_info['Website']}")
    else:
        print(Fore.RED + location_info["Status"])

if __name__ == "__main__":
    main()
