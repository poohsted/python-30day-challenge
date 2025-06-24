import requests

def get_random_quote():
    url = "https://api.quotable.io/random"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        print(f"🧠 Quote: {data['content']}")
        print(f"— {data['author']}")
    else:
        print("❌ Failed to retrieve quote.")

if __name__ == "__main__":
    get_random_quote()
