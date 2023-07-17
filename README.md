# Dentist Web Scraper

This project is a simple web scraping tool that fetches information about nearby dentists from Google search results and stores the information in a CSV file and a picture of the search.

## Features

- Fetches search results for "dentists near me" from Google.
- Retrieves the name of each dentist from the search results.
- Saves the dentist's names in a CSV file.
- Saves a screenshot of the browser at the end of the process.

## Requirements

The script requires the following Python libraries:

- `selenium`
- `csv`

## Usage

1. Install the required Python libraries using pip:

    ```bash
    pip install selenium
    ```

2. Download the appropriate ChromeDriver for your version of Chrome browser from the [ChromeDriver download page](https://sites.google.com/a/chromium.org/chromedriver/downloads) and place it in the `src/assets/` directory.

3. Run the script with Python:

    ```bash
    python main.py
    ```
    
The script will automatically fetch the dentist information and save it in a file named `dentists.csv` in the same directory as the script. The script will also save a screenshot named `screenshot.png`.

## Note

Please ensure that you use this script responsibly and respect Google's terms of service.
