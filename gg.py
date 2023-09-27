import nmap

# Create an Nmap scanner object
nm = nmap.PortScanner()

# Define the target host or IP address
target = "101.188.67.134"

# Perform a basic scan of common ports
nm.scan(target, arguments="-F")

# Iterate through the scan results and print open ports
for host, scan_result in nm.all_hosts().items():
    print(f"Host: {host}")
    for port, port_info in scan_result["tcp"].items():
        if port_info["state"] == "open":
            print(f"Port: {port}, State: {port_info['state']}, Service: {port_info['name']}")

# Print the raw Nmap command used for the scan
print(f"Nmap command used: {nm.command_line()}")
