
import os
import requests
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("QLOO_API_KEY")

if not api_key:
    print("ERROR: Qloo API key is missing from .env")
else:
    try:
        response = requests.get(
            "https://hackathon.api.qloo.com/search",
            headers={"X-Api-Key": api_key},
            params={"query": "Taylor Swift", "take": 3},
            timeout=30,
        )

        print("HTTP status:", response.status_code)

        if response.ok:
            print("SUCCESS: Qloo API connection works!")
            data = response.json()
            results = data.get("results", [])

            print("Results type:", type(results).__name__)
            print("Number of results:", len(results))

            if isinstance(results, list) and results:
                print("First result:")
                print(results[0])
            else:
                print("No results returned. Check the query.")
        elif response.status_code == 401:
            print("Authentication failed. Check your API key.")
        else:
            print("Request unsuccessful.")
            print("Response:", response.text[:500])

    except requests.RequestException as error:
        print("Connection error:", type(error).__name__)
