import os
import requests


urls = [
    "https://example.com/image1.jpg",
    "https://example.com/image2.png"
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

        # get the file extension from the URL
        file_extension = url.split('.')[-1]  # Get the part after the last '.'

        # set the filename with the correct extension
        filename = os.path.join(output_folder, f"image_{i + 1}.{file_extension}")

        # save the file
        with open(filename, "wb") as file:
            file.write(response.content)
        print(f"Downloaded: {filename}")
    except Exception as e:
        print(f"Error: {url} not downloaded. Reason: {e}")
