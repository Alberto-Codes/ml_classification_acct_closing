# File: src/download_data.py

import os
import json
import subprocess

def download_kaggle_data(dataset_name, destination_folder):
    # Retrieve Kaggle credentials from environment variables
    kaggle_username = os.getenv("KAGGLE_USERNAME")
    kaggle_key = os.getenv("KAGGLE_KEY")

    if not kaggle_username or not kaggle_key:
        raise EnvironmentError("Kaggle API credentials not found in environment variables.")

    # Create kaggle.json file dynamically
    kaggle_json_path = os.path.expanduser("~/.kaggle")
    os.makedirs(kaggle_json_path, exist_ok=True)
    kaggle_json_content = {
        "username": kaggle_username,
        "key": kaggle_key
    }
    with open(os.path.join(kaggle_json_path, "kaggle.json"), "w") as f:
        json.dump(kaggle_json_content, f)

    # Make sure the destination folder exists
    os.makedirs(destination_folder, exist_ok=True)

    # Use subprocess to download the dataset using Kaggle API
    command = f"kaggle datasets download -d {dataset_name} -p {destination_folder} --unzip"
    try:
        subprocess.run(command, check=True, shell=True)
    except subprocess.CalledProcessError as e:
        print(f"Error downloading the dataset: {e}")

if __name__ == "__main__":
    dataset_name = "mlg-ulb/creditcardfraud"  # Update this with the desired Kaggle dataset
    destination_folder = "../data"  # Keeping data outside the main code folder
    download_kaggle_data(dataset_name, destination_folder)
