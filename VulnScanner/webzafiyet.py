import requests
from bs4 import BeautifulSoup

# hedef url
url = "http://ornek.com"

# potansiyel acıklar
vulns = [
    {"name": "SQL Injection", "url": "/search?q='"},
    {"name": "Cross-Site Scripting (XSS)", "url": "/search?q=<script>alert(1)</script>"},
]

def check_vulns(vuln):
    try:
        response = requests.get(url + vuln["url"])
        if response.status.code == 200:
            # belli açık tespiti icin icerik kontrolü
            if vuln["name"] == "SQL Injection" and "SQL syntax" in response.text:
                print(f"[VULNERABILITY FOUND] {vuln['name']} at {url + vuln['url']}")
            elif vuln["name"] == "Cross-Site Scripting (XSS)" and "<script>alert(1)</script>" in response.text:
                print(f"[VULNERABILITY FOUND] {vuln['name']} at {url + vuln['url']}")
        else:
            print(f"[INFO] {vuln['name']} check failed with status code: {response.status_code}")
    except Exception as e:
        print(f"[ERROR] {vuln['name']} check encountered an error: {e}")

def main():
    for vuln in vulns:
        check_vulns(vulns)

if __name__ == "__main__":
    main()
