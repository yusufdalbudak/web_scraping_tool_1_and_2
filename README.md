#  Web Scraping Tool


This Python script is a web scraping tool designed to fetch data from Exploit-DB without relying on HTML structure. It utilizes the `requests` library to make HTTP requests and extract relevant information from the website.

## Features

- **Customizable:** The script comes with customizable parameters such as headers, cookies, and query parameters to adapt to any changes in the Exploit-DB website.

- **Data Extraction:** Extracts information such as exploit ID, title, type, platform, author, and download link from the Exploit-DB API.

## Usage

1. Install the required libraries:
    ```bash
    pip install requests
    ```

2. Update the `cookies` and `headers` with your own values if necessary.

3. Run the script:
    ```bash
    python web_scrap_file2.py
    ```

4. Explore the extracted data from Exploit-DB.

## Dependencies

- [requests](https://docs.python-requests.org/en/latest/)
  
## Example Output

- Exploit ID: 12345
- Title: Sample Exploit Title
- Type: Remote
- Platform: Windows
- Author: John Doe
- Download Link: [Exploit Download](https://www.exploit-db.com/download/12345)





