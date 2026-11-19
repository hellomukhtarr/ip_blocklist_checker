### Import the file containing the list of IP addresses
import_file = "ip_addresses.txt"
with open(import_file, "r") as file:
    # Assign a variable to the imported file
    list_ip = file.read().splitlines()[1:]  # Skip the first line (header) and read the rest of the lines
#Import the file containing the blocked IPs
import_file = "blocked_ip.txt"
with open(import_file, "r") as file:
    # Assign a variable to the imported file
    blocked_ip = file.read().splitlines()[1:]  # Skip the first line (header) and read the rest of the lines
#run the ip addresses against the list of blocked IPs and save to new file "approved_ip.txt"
with open("approved_ip.txt", "w") as file:
    for ip in list_ip:
        if ip not in blocked_ip:
            file.write(ip + "\n")