# ip_blocklist_checker
Lightweight Python utility that cross-references a list of IP addresses against a blocklist and outputs approved IPs for network access control workflows.

How it works
Reads Input Files: Loads ip_addresses.txt and blocked_ip.txt.

Filters Blocked IPs: Compares each candidate IP against the blocklist 

Exports Approved IPs: Writes all valid, non-blocked IPs to approved_ip.txt, one per line.
