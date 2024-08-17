# Disney Movies Scraping and Cleaning Project

## Table of Contents

- [Project Overview](#project-overview)
- [Technologies Used](#technologies-used)
- [Getting Started](#getting-started)
- [Scraping Process](#scraping-process)
- [Data Cleaning](#data-cleaning)
- [Final Output](#final-output)
- [Contributing](#contributing)
- [License](#license)

## Project Overview

This project aims to scrape data for all Disney movies from Wikipedia and perform data cleaning to prepare the dataset for analysis. The project involves extracting various attributes such as title, director, producer, release date, running time, and box office earnings. The cleaned data will be saved in JSON and CSV formats for easy access and further analysis.

## Technologies Used

- **Python**: The primary programming language used for scraping and data manipulation.
- **Beautiful Soup**: A library for parsing HTML and XML documents, used for web scraping.
- **Requests**: A library for making HTTP requests to fetch web pages.
- **Pandas**: A powerful data manipulation and analysis library used for handling data in DataFrames.
- **JSON**: A lightweight data interchange format used for storing the scraped data.
- **Pickle**: A Python module used for serializing and de-serializing Python objects, allowing for easy saving and loading of data.

## Getting Started

To get started with this project, you will need to have Python installed on your machine along with the required libraries. You can install the necessary libraries using pip:

```bash
pip install requests beautifulsoup4 pandas
```

## Scraping Process

1. **Scrape Movie List**: The project begins by scraping the list of all Disney movies from the [Wikipedia page](https://en.wikipedia.org/wiki/List_of_Walt_Disney_Pictures_films).
2. **Extract Movie Details**: For each movie, additional details such as the director, producer, release date, and box office earnings are scraped from the respective Wikipedia pages.
3. **Store Data**: The scraped data is initially stored in a structured format (e.g., a list of dictionaries) for further processing.

## Data Cleaning

The following cleaning steps are performed on the scraped data:

- **Remove References**: Strip out any references or citations from the text (e.g., [1], [2], etc.).
- **Convert Dates**: Convert release dates to a standardized datetime format.
- **Clean Running Time**: Convert the running time from string format (e.g., "64 minutes") to an integer representing the total minutes.
- **Standardize Monetary Values**: Convert budget and box office earnings from string format (e.g., "$950,000") to float values.
- **Repair Inconsistencies**: Split long strings in the "Starring" list into individual names and handle edge cases.

## Final Output

After cleaning the data, the final dataset is saved in multiple formats for easy access:

- **JSON**: The cleaned data is saved as `Disney_data_final.json`.
- **CSV**: The cleaned data is also saved as `Disney_data_final.csv`.
- **Pickle**: An intermediate cleaned dataset is saved as `Disney_data_cleaned.pickle`.

## Contributing

Contributions to this project are welcome! If you would like to contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature (`git checkout -b feature`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature`).
5. Open a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---
