# Function to update the allow list by removing unauthorized IPs
def update_allow_list(import_file, remove_list):
    # 1. Open the file and read the current allowed IPs
    with open(import_file, "r") as file:
        ip_addresses = file.read()

    # 2. Convert the string of IPs into a list for easy manipulation
    ip_addresses = ip_addresses.split()

    # 3. Iterate through the remove_list to find and remove unauthorized IPs
    for element in remove_list:
        if element in ip_addresses:
            ip_addresses.remove(element)

    # 4. Convert the list back into a string format to save to the file
    ip_addresses = " ".join(ip_addresses)

    # 5. Overwrite the original file with the updated security list
    with open(import_file, "w") as file:
        file.write(ip_addresses)
    
    print("Security Update Complete: Unauthorized IPs have been revoked.")

# Example usage:
# List of IPs that have lost their security clearance
unauthorized_ips = ["192.168.1.105", "10.0.0.45", "172.16.5.12"]

# Running the update on the server's allow list
update_allow_list("allow_list.txt", unauthorized_ips)
