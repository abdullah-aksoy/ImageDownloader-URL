import os
import requests
from pathlib import Path
import logging
from urllib.parse import urlparse

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

urls = [
    "https://example.com/image1.jpg",
    "https://example.com/image2.png"
]

# Create folder to download images
output_folder = Path("images")
output_folder.mkdir(parents=True, exist_ok=True)

def is_valid_url(url):
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except ValueError:
        return False

def download_image(url, output_folder, index):
    try:
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()  # catch errors

        # Get the file extension from the URL
        file_extension = Path(url).suffix

        # Set the filename with the correct extension
        filename = output_folder / f"image_{index + 1}{file_extension}"

        # Save the file
        with open(filename, "wb") as file:
            file.write(response.content)
        logging.info(f"Downloaded: {filename}")
    except requests.exceptions.RequestException as e:
        logging.error(f"Error: {url} not downloaded. Reason: {e}")

# Download images
for i, url in enumerate(urls):
    if is_valid_url(url):
        download_image(url, output_folder, i)
    else:
        logging.error(f"Invalid URL: {url}")
