import requests
import json
import time
import pandas as pd

#fetches movies data from the OMDB API
def fetch_movie_data(title, api_key):
    base_url = "http://www.omdbapi.com/"
    params = {
        "t": title,
        "type": "movie",  
        "apikey": api_key
    }
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code} for title {title}")
        return None
    
def main():
    api_key = "your-api-key"  
    df = pd.read_csv("query.csv")
    film_titles = df["filmLabel"][1000:].tolist()
    output_file = "film_responses.json"
    responses = []
    i = 0
    for title in film_titles:
        if ((i % 100)== 0):
            index = i / 100 
            print(f"Fetching data for {index} * 100th film")
        movie_data = fetch_movie_data(title, api_key)
        
        if movie_data and movie_data.get("Response") == "True" and movie_data.get("Type") == "movie":
            responses.append(movie_data)
        else:
            print(f"Skipping: {title} (not a movie or no data found)")
        
        # Avoid hitting the API rate limit by introducing a delay
        time.sleep(0.5)  # Adjust the delay as needed
        i = i+1

    # Save the collected data to a JSON file
    with open(output_file, "w") as f:
        json.dump(responses, f, indent=4)
    
    print(f"Data for {len(responses)} movies saved to {output_file}")

if __name__ == "__main__":
    main()