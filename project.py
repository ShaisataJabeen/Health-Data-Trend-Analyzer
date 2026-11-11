import csv  # Import Python's CSV-reading tool

# Load Pakistan's cancer death-rate data
def load_data():
    # Create empty lists to store Pakistan's data
    years = []
    death_rates = []

    # Open the cancer statistics CSV file
    with open("data/death-rate-from-cancer.csv", "r") as file:
        # Read the CSV file row by row
        reader = csv.reader(file)

        # Skip the column headings
        next(reader)

        # Examine each row in the dataset
        for row in reader:
            # Keep only records for Pakistan
            if row[0] == "Pakistan":
                # Convert the year to an integer
                year = int(row[2])

                # Convert the death rate to a decimal
                rate = float(row[3])

                # Store each value in its corresponding list
                years.append(year)
                death_rates.append(rate)

    return years, death_rates

# Display the collected data
# print(years)
# print(death_rates)

# Define a function to calculate the average death rate
def calculate_average(death_rates):

    # Add all the death rates together
    total = sum(death_rates)

    # Count the number of death rates
    count = len(death_rates)

    # Return the average to the caller
    return total / count

# Define a function to find the highest death rate
def find_highest_rate(death_rates):

    # Return the largest value in the list
    return max(death_rates)

# Define a function to find the lowest death rate
def find_lowest_rate(death_rates):

    #Return the smallest value in the list
    return min(death_rates)


# Define a function to calculate percentage change
def calculate_percentage_change(first_rate, last_rate):

    # Calculate the difference between the final and initial rates
    change = last_rate - first_rate

    # Calculate the percentage change
    percentage_change = (change / first_rate) * 100

    # Return the calculated result
    return percentage_change

def calculate_forecast(last_rate, average_annual_change):
    # Add the average annual change to the last recorded rate
    forecast_rate = last_rate + average_annual_change

    # Return the forecast rate
    return forecast_rate

def main():
     # Load the years and death rates from the CSV file
    years, death_rates = load_data()

    # Get the first and last years in the dataset
    first_year = years[0]
    last_year = years[-1]

    # Calculate the number of years between the first and last year
    number_of_years = last_year - first_year

    # Get the death rates from the first and last years
    first_rate = death_rates[0]
    last_rate = death_rates[-1]

    # Calculate the average annual change in the death rate
    average_annual_change = (last_rate - first_rate) / number_of_years

    # Estimate the death rate for the year after the last observation
    forecast_year = last_year + 1

    # Use our forecast function to estimate the next year's rate
    forecast_rate = calculate_forecast(last_rate, average_annual_change)

    # Calculate the average cancer death rate
    average = calculate_average(death_rates)
    print("Average cancer death rate:", round(average, 2))

    # Find the highest and lowest death rates
    highest_rate = find_highest_rate(death_rates)
    lowest_rate = find_lowest_rate(death_rates)

    # Find the years with the highest and lowest rates
    highest_index = death_rates.index(highest_rate)
    highest_year = years[highest_index]

    lowest_index = death_rates.index(lowest_rate)
    lowest_year = years[lowest_index]

    # Get the death rates from the first and last years
    first_rate = death_rates[0]
    last_rate = death_rates[-1]

    # Calculate the absolute change between the first and last years
    change = last_rate - first_rate

    # Describe the overall change in the death rate
    if change > 0:
        print("The death rate increased")
    elif change < 0:
        print("The death rate decreased")
    else:
        print("The death rate stayed the same")

    print("Absolute change:", round(change, 2))

    # Calculate the percentage change
    percentage_change = calculate_percentage_change(first_rate, last_rate)

    # Display the results
    print("Highest death rate:", round(highest_rate, 2))
    print("Lowest death rate:", round(lowest_rate, 2))
    print("Year with highest death rate:", highest_year)
    print("Year with lowest death rate:", lowest_year)
    print("Percentage change:", round(percentage_change, 2))

    # Display the estimated rate for the next year
    print("Forecast year:", forecast_year)
    print("Estimated cancer death rate:", round(forecast_rate, 2))

# Run main() only when this file is executed directly
if __name__ == "__main__":
    main()
