# Health Data Trend Analyzer

#### Video Demo
https://drive.google.com/file/d/1g_nbpHGdqSaisubhiVe3iBt8H38sW6YR/view?usp=sharing

#### Description
Health Data Trend Analyzer is a Python project developed for CS50's Introduction to Programming with Python final project. It analyzes historical cancer death-rate data for Pakistan, calculates summary statistics, identifies changes over time, and provides a simple overview of the observed trend.

The project demonstrates how Python can be used to load data from a CSV file, organize numerical information, perform calculations, and communicate results in a readable format. It is designed to be beginner-friendly while demonstrating practical programming and data analysis skills.

#### Project Files

- `project.py`: Contains the main program, loads the CSV dataset, calculates summary statistics, identifies the highest and lowest death rates, calculates percentage change, and summarizes the overall trend.
- `test_project.py`: Contains automated tests written with `pytest` to check that the analysis functions return the expected results.
- `data/death-rate-from-cancer.csv`: Contains the historical cancer death-rate data used by the program.

#### Design Choices

I separated the program into functions so that each function has a clear responsibility. The `load_data()` function reads the CSV file and extracts the years and death rates for Pakistan. The `calculate_average()` function calculates the average rate, while `find_highest_rate()` and `find_lowest_rate()` identify the maximum and minimum values. The `calculate_percentage_change()` function calculates the percentage change between two rates.

I also implemented a simple one-year forecast using the average annual change between the first and last recorded death rates. The program adds this change to the last recorded rate to estimate the rate for the following year. Separating this calculation into the `calculate_forecast()` function makes it easier to test independently.

The `main()` function coordinates these operations and displays the results. Keeping the calculations in separate functions makes the code easier to read, test, and maintain.

I also created automated tests to verify the behavior of the analysis functions using sample values. This helps detect calculation errors without needing to run the entire analysis manually.

#### How to Run the Project

1. Make sure Python 3 is installed.
2. Open a terminal in the project directory.
3. Run the program using:

   ```bash
   python project.py
   ```

The program reads the historical cancer death-rate data from the CSV file, calculates summary statistics, and displays the results in the terminal.

#### Running the Tests

To run the automated tests, install `pytest` if it is not already installed:

```bash
pip install pytest
```

Then execute:

```bash
pytest test_project.py
```

The tests check whether the analysis functions produce the expected results for sample inputs.

#### Data Source and Interpretation

The dataset used in this project is `death-rate-from-cancer.csv`, obtained from Our World in Data. The underlying data comes from the World Health Organization's Global Health Estimates.

The dataset contains estimated cancer death rates for both sexes combined, expressed as deaths per 100,000 people. This project analyzes Pakistan's data from 2000 to 2021.

The results are descriptive statistics based on the available estimates. They show how the recorded estimates changed over time, but they do not explain why those changes occurred. The estimates should be interpreted cautiously because WHO notes limitations in the quality of cause-of-death registration data for Pakistan.


#### Example Results

When the program analyzes Pakistan's cancer death-rate data from 2000 to 2021, it produces the following results:

- **Average death rate:** 52.86 deaths per 100,000 people.
- **Highest death rate:** 54.95 in 2019.
- **Lowest death rate:** 49.61 in 2021.
- **Overall change:** The death rate decreased by 2.12 between 2000 and 2021, representing a decrease of approximately 4.1%.
- **One-year forecast:** The estimated rate for 2022 is 49.51 deaths per 100,000 people.

These results summarize the historical data and demonstrate how Python can be used to analyze trends and make a simple projection. The forecast is an estimate based on the historical average annual change, not an official prediction.

#### Limitations

This project analyzes historical data only through 2021, so its results should not be interpreted as current cancer statistics. Changes in estimated death rates do not, by themselves, establish the causes of those changes. The one-year forecast is a simple linear projection based on the average annual change between the first and last observations. It is not an official forecast and may not reflect future outcomes.
