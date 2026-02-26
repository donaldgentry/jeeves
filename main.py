import os
import requests

DNDTOOLS_URL = os.getenv("DNDTOOLS_URL", "http://localhost:8000")


def roll(die: str, count: int) -> dict:
    response = requests.get(f"{DNDTOOLS_URL}/roll/{die}/{count}")
    response.raise_for_status()
    return response.json()


def main():
    result = roll("d6", 5)
    print(result["result"])
    result = roll("d10", 5)
    print(result["result"])


if __name__ == "__main__":
    main()

