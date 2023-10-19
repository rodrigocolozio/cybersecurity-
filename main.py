import re
import argparse
from collections import Counter

# Define a regular expression pattern for Apache access log
log_pattern = r'(\S+) (\S+) (\S+) \[([\w:/]+\s[+\-]\d{4})\] "(\S+) (\S+)\s*(\S*)" (\d{3}) (\d+) "(\S+)" "([^"]+)"'

# Define a function to parse log entries
def parse_log_entry(line):
    match = re.match(log_pattern, line)
    if match:
        return {
            "ip": match.group(1),
            "identd": match.group(2),
            "user": match.group(3),
            "timestamp": match.group(4),
            "method": match.group(5),
            "path": match.group(6),
            "protocol": match.group(7),
            "status": match.group(8),
            "size": match.group(9),
            "referer": match.group(10),
            "user_agent": match.group(11)
        }
    else:
        return None

# Define a function to analyze log entries
def analyze_log(log_file):
    with open(log_file, 'r') as file:
        log_entries = [parse_log_entry(line) for line in file]

    # Analyze log entries here
    total_requests = len(log_entries)
    status_codes = [entry["status"] for entry in log_entries]
    status_count = Counter(status_codes)

    print(f"Total Requests: {total_requests}")
    for status, count in status_count.items():
        print(f"Status {status}: {count} times")

    # Future analysis goes here ++++

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Log File Analysis")
    parser.add_argument("log_file", help="Path to the log file to analyze")
    args = parser.parse_args()
    analyze_log(args.log_file)
