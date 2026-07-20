import glob
import re
import os

def analyze_logs():
    # Find all server*.log files in the current directory
    log_files = sorted(glob.glob('server*.log'))
    
    if not log_files:
        print("No server*.log files found in the current directory.")
        return

    # Regular expressions to match "CRC error" and "Link Down" (case-insensitive)
    crc_pattern = re.compile(r'crc\s+error', re.IGNORECASE)
    link_down_pattern = re.compile(r'link\s+down', re.IGNORECASE)
    
    results = {}
    
    for file_path in log_files:
        # Extract server name from the file name (e.g., 'server01' from 'server01.log')
        server_name = os.path.splitext(os.path.basename(file_path))[0]
        
        crc_count = 0
        link_down_count = 0
        
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            for line in f:
                # We only count lines with 'ERROR' severity to avoid counting
                # informational messages like 'CRC error recovered' or 'no CRC error found'
                if 'ERROR' in line:
                    if crc_pattern.search(line):
                        crc_count += 1
                    elif link_down_pattern.search(line):
                        link_down_count += 1
        
        results[server_name] = {
            'crc_error': crc_count,
            'link_down': link_down_count
        }
    
    # Print the results in a formatted table
    print(f"{'Server':<12} | {'CRC Error Count':<16} | {'Link Down Count':<16}")
    print("-" * 52)
    for server, counts in sorted(results.items()):
        print(f"{server:<12} | {counts['crc_error']:<16} | {counts['link_down']:<16}")

if __name__ == '__main__':
    analyze_logs()
