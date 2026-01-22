import sys
from collections import Counter


def most_common_errors(path: str, top_n: int = 5) -> None:
    counter = Counter()

    with open(path, "r", errors="ignore") as f:
        for line in f:
            if "ERROR" in line:
                counter[line.strip()] += 1

    print(f"Top {top_n} ERROR messages:")
    for msg, count in counter.most_common(top_n):
        print(f"{count}x - {msg}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python log_errors.py <logfile>")
        sys.exit(1)

    most_common_errors(sys.argv[1])
