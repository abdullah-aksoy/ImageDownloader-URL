import os
import requests

# URL listesi
urls = [
    "https://url.com",
    "https://url.com"
]


# create folder to download images
output_folder = "images"
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# download images
for i, url in enumerate(urls):
    try:
        response = requests.get(url)
        response.raise_for_status()  # catch errors

        # set the filename
        filename = os.path.join(output_folder, f"image_{i + 1}.jpg")

        # save the file
        with open(filename, "wb") as file:
            file.write(response.content)
        print(f"Downloaded: {filename}")
    except Exception as e:
        print(f"Error: {url} not downloaded. Reason: {e}")
