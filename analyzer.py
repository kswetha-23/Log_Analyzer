import re
from collections import Counter

def analyze_log(file_path):
    ip_list = []
    status_list = []
    url_list = []

    pattern = r'(\d+\.\d+\.\d+\.\d+).*?"(GET|POST) (.*?) HTTP.*?" (\d+)'

    with open(file_path, 'r', errors='ignore') as file:
        for line in file:
            match = re.search(pattern, line)
            if match:
                ip, method, url, status = match.groups()
                ip_list.append(ip)
                status_list.append(status)
                url_list.append(url)

    total_requests = len(ip_list)
    top_ips = Counter(ip_list).most_common(5)
    top_urls = Counter(url_list).most_common(5)
    error_counts = Counter(status_list)

    suspicious_ips = [ip for ip, count in Counter(ip_list).items() if count > 50]

    return {
        "total_requests": total_requests,
        "top_ips": top_ips,
        "top_urls": top_urls,
        "error_counts": error_counts,
        "suspicious_ips": suspicious_ips
    }
