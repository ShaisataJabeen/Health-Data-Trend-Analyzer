# Health Data Trend Analyzer

## Overview

Health Data Trend Analyzer is a Python-based data analysis project that explores historical cancer death-rate estimates in Pakistan from 2000 to 2021.

The project processes a CSV dataset, calculates descriptive statistics, identifies changes in cancer death rates over time, and provides a simple estimate for the following year based on historical trends.

It demonstrates the use of Python for data processing, numerical calculations, trend analysis, automated testing, and presenting analytical results in a structured and understandable way.

Originally developed as a final project for CS50's Introduction to Programming with Python, this project provided an opportunity to apply programming concepts to a real-world health dataset.

## Key Features

- **Data Processing:** Loads and extracts historical cancer death-rate data for Pakistan from a CSV file.
- **Statistical Analysis:** Calculates the average death rate and identifies the highest and lowest recorded values.
- **Trend Analysis:** Measures the overall percentage change in death rates between the first and last recorded years.
- **Simple Forecasting:** Estimates the following year's death rate using the average annual change across the available period.
- **Automated Testing:** Uses pytest to test individual analysis functions and verify their expected results.

## Technologies Used

- Python 3
- CSV data processing
- pytest for automated testing

## Project Structure

```text
Health-Data-Trend-Analyzer/
│
├── data/
│   └── death-rate-from-cancer.csv
│
├── project.py
├── test_project.py
└── README.md
```

## Getting Started

### Prerequisites

- Python 3 installed on your system.
- pytest for running automated tests.

### Running the Project

1. Clone the repository:

   ```bash
   git clone https://github.com/ShaisataJabeen/Health-Data-Trend-Analyzer.git
   ```

2. Navigate to the project directory:

   ```bash
   cd Health-Data-Trend-Analyzer
   ```

3. Run the program:

   ```bash
   python project.py
   ```

The program loads the dataset, performs the analysis, and displays the calculated results in the terminal.

### Running the Tests

Install pytest if it is not already installed:

```bash
pip install pytest
```

Run the automated tests:

```bash
pytest test_project.py
```

## Example Results

The analysis of Pakistan's cancer death-rate estimates from 2000 to 2021 produces the following results:

| Metric | Result |
|---|---:|
| Average death rate | 52.86 per 100,000 people |
| Highest death rate | 54.95 (2019) |
| Lowest death rate | 49.61 (2021) |
| Overall change | -2.12 |
| Percentage change | -4.1% |
| Estimated rate for 2022 | 49.51 per 100,000 people |

The results indicate an overall decrease in the estimated cancer death rate over the analyzed period.

The 2022 estimate is a simple projection based on the average annual change between the first and last observations. It should not be interpreted as an official forecast.

## Data Source

The dataset, `death-rate-from-cancer.csv`, was obtained from **Our World in Data**, with underlying estimates from the **World Health Organization (WHO) Global Health Estimates**.

The data represents estimated cancer death rates for both sexes combined, expressed as deaths per 100,000 people.

This project focuses on Pakistan's estimates from 2000 to 2021.

## Methodology and Design Decisions

The program is organised into separate functions, each responsible for a specific part of the analysis.

- `load_data()`: Reads the CSV dataset and extracts the relevant years and death rates for Pakistan.
- `calculate_average()`: Calculates the average death rate.
- `find_highest_rate()`: Identifies the highest recorded death rate and its corresponding year.
- `find_lowest_rate()`: Identifies the lowest recorded death rate and its corresponding year.
- `calculate_percentage_change()`: Calculates the percentage change between two recorded rates.
- `calculate_forecast()`: Estimates the following year's rate using the average annual change between the first and last observations.
- `main()`: Coordinates the analysis functions and displays the results.

Separating the calculations into individual functions makes the program easier to understand, maintain, and test. Automated tests are included to check the behaviour of the analysis functions using sample values.

## Limitations

This project is based on historical estimates available through 2021 and does not represent current cancer statistics.

The observed changes do not establish the causes behind variations in cancer death rates. Additionally, the dataset contains estimated values, and the quality of cause-of-death registration data can affect their reliability.

The forecasting method uses a simple linear projection based on the average annual change between the first and last observations. It does not account for other factors that may influence future cancer death rates and should not be treated as a reliable medical or public health prediction.

## Learning Outcomes

Through this project, I applied Python programming concepts to a real-world dataset and gained practical experience in:

- Reading and processing structured CSV data.
- Organising code using functions and modular programming.
- Performing statistical calculations and analysing historical trends.
- Implementing a basic forecasting method.
- Writing automated tests with pytest.
- Interpreting numerical results while considering data limitations.
