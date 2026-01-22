import sys
import time
import requests


def check_health(url: str, timeout: int = 5) -> None:
    start = time.time()
    try:
        resp = requests.get(url, timeout=timeout)
        latency = round(time.time() - start, 3)

        print(f"Status: {resp.status_code}")
        print(f"Latency: {latency}s")

        if resp.status_code >= 400:
            print("Warning: non-success response returned")

    except requests.exceptions.RequestException as exc:
        print(f"ERROR contacting {url}: {exc}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python api_health_check.py <url>")
        sys.exit(1)

    check_health(sys.argv[1])
