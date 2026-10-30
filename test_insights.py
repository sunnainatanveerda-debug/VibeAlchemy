
import os
import requests
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("QLOO_API_KEY")

if not api_key:
    print("ERROR: Qloo API key is missing.")
else:
    url = "https://hackathon.api.qloo.com/v2/insights"

    headers = {
        "X-Api-Key": api_key,
        "Accept": "application/json",
    }

    params = {
        "filter.type": "urn:entity:artist",
        "signal.interests.entities": (
            "3C9EEC3A-F4FE-48A4-B89F-97375F292448"
        ),
        "take": 5,
    }

    try:
        response = requests.get(
            url,
            headers=headers,
            params=params,
            timeout=30,
        )

        print("HTTP status:", response.status_code)

        if response.ok:
            data = response.json()
            results = data.get("results", {})
            entities = results.get("entities", [])

            print("SUCCESS: Insights API responded!")
            print("Number of recommendations:", len(entities))

            for item in entities:
                print("-", item.get("name", "Unnamed entity"))
        else:
            print("Request failed.")
            print("Response:", response.text[:1000])

    except requests.RequestException as error:
        print("Connection error:", error)
