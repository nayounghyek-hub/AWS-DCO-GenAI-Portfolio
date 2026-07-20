import glob
import re
import os

def analyze_logs():
    # Find all server*.log files in the current directory
    log_files = sorted(glob.glob('server*.log'))
    
    if not log_files:
        print("No server*.log files found in the current directory.")
        return

    # Regular expressions (case-insensitive)
    # Matches 'serverXX ERROR' (or 'serverXX Error', etc.) to identify error level logs
    server_error_pattern = re.compile(r'server\d+\s+error', re.IGNORECASE)
    crc_pattern = re.compile(r'crc\s+error', re.IGNORECASE)
    link_down_pattern = re.compile(r'link\s+down', re.IGNORECASE)
    
    results = {}
    
    for file_path in log_files:
        server_name = os.path.splitext(os.path.basename(file_path))[0]
        
        crc_count = 0
        link_down_count = 0
        
        # Parse multi-line log entries
        entries = []
        current_entry = []
        
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            for line in f:
                stripped = line.strip()
                if not stripped:
                    continue
                
                # A line starting with spaces, tabs, or '->' is a continuation of the previous entry
                is_continuation = line.startswith(' ') or line.startswith('\t') or stripped.startswith('->')
                
                if is_continuation:
                    if current_entry:
                        current_entry.append(line)
                else:
                    if current_entry:
                        entries.append("".join(current_entry))
                    current_entry = [line]
            
            if current_entry:
                entries.append("".join(current_entry))
        
        # Analyze each parsed log entry
        for entry in entries:
            lines = entry.splitlines()
            if not lines:
                continue
            first_line = lines[0]
            
            # Check if the log level is 'ERROR' (case-insensitive check for 'serverXX error')
            if server_error_pattern.search(first_line):
                # Search for patterns within the entire multi-line entry
                if crc_pattern.search(entry):
                    crc_count += 1
                elif link_down_pattern.search(entry):
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
