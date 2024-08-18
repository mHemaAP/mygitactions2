[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/I7A3K_cM)
[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-2e0aaae1b6195c2367325f4f02e2d04e9abb55f0b24a779b69b11b9e10269abc.svg)](https://classroom.github.com/online_ide?assignment_repo_id=15486797&assignment_repo_type=AssignmentRepo)

# Named Tuples
## Overview

This repository provides a set of Python utilities for generating and analyzing data using the '**namedtuple**' data structure from the '**collections**' module. The project primarily focuses on generating random profile data and stock market data using the '**Faker**' library, and then performing various analyses on this data. The key advantage of using '**namedtuple**' is its ability to offer immutable, lightweight objects with named fields, combining the readability of a class with the performance benefits of a tuple

## Features
### Profile Data Generation and Analysis
The core functionality of this project revolves around generating random profiles and analyzing them. The profiles include various attributes such as job title, company, social security number (SSN), residence, current location (latitude and longitude), blood group, website, username, name, sex, address, email, and birthdate. These attributes are stored in a '**namedtuple**' called '**Profile**', which allows for efficient storage and easy access to the data.

#### Profile Generation
The '**generate_profiles**' function generates a specified number of profiles. Each profile is created using the '**Faker**' library, which populates the fields with realistic but randomly generated data. The profiles are stored in a tuple, ensuring that they are immutable and can be processed quickly.

```
def generate_profiles(n=10000):
    """
    Generate n random profiles using the Faker library.

    Parameters:
    n (int): Number of profiles to generate.

    Returns:
    list: List of namedtuple containing profile information.
    """

```

#### Profile Analysis
The '**analyze_profiles**' function performs various analyses on the generated profiles:

- **Largest Blood Group:** Identifies the most common blood group among the profiles.
- **Mean Current Location:** Calculates the average latitude and longitude across all profiles.
- **Oldest Person's Age:** Determines the age of the oldest person based on their birthdate.
- **Average Age:** Computes the average age of all the profiles.

The analysis results are returned as a '**namedtuple**' called '**AnalysisResult**', which maintains the same performance benefits and ease of access as the '**Profile**' namedtuple.

```
def analyze_profiles(profiles):
    """
    Analyze a list of profiles to calculate the largest blood type group, 
    mean current location, oldest person's age, and average age.

    Parameters:
    profiles (list): List of namedtuple containing profile information.

    Returns:
    dict: Dictionary containing the largest blood group, mean current location,
    oldest age, and average age.
    """

```

### Dictionary-Based Implementation
For comparison purposes, the module also includes a dictionary-based implementation of the profile generation and analysis functions. This version stores profiles as dictionaries rather than '**namedtuple**' instances. While dictionaries offer more flexibility in terms of mutability and field names, they come with a performance cost due to the overhead of managing keys and values.

```
def generate_profiles_dict(n=10000)
    """
    Generate n random profiles using the Faker library and store them in a list of dictionaries.

    Parameters:
    n (int): Number of profiles to generate.

    Returns:
    list: List of dictionaries containing profile information.
    """

```

```
def analyze_profiles_dict(profiles):
    """
    Analyze a list of profiles to calculate the largest blood type group,
    mean current location, oldest person's age, and average age.

    Parameters:
    profiles (list): List of dictionaries containing profile information.

    Returns:
    dict: Dictionary containing the largest blood group, mean current location,
    oldest age, and average age.
    """

```

### Stock Market Data Simulation

In addition to profile data, the module includes functionality for simulating stock market data. The '**generate_stock_data**' function generates data for a number of imaginary companies, including attributes like the company name, stock symbol, opening price, highest price of the day, closing price, and a weight that represents the company's influence on the market.

### Stock Market Analysis
The '**calculate_market_values**' function uses the generated stock data to calculate the overall market values:

- '**Market Open Value:**' The weighted sum of the opening prices of all stocks.
- '**Market High Value:**' The weighted sum of the highest prices of all stocks.
- '**Market Close Value:**' The weighted sum of the closing prices of all stocks.
These calculations provide a snapshot of the simulated stock market's performance.

## Why Use Namedtuples?
### Performance
Namedtuples are essentially lightweight objects that behave like tuples but have named fields. This makes them both memory-efficient and faster than regular Python objects or dictionaries. The immutability of namedtuples also ensures that the data remains consistent throughout its lifecycle, making them ideal for large-scale data analysis.

### Readability
Despite their performance advantages, namedtuples retain the readability of classes. Each field in a namedtuple can be accessed by name, making the code easier to understand and maintain.

### Comparison with Dictionaries
While dictionaries offer flexibility, they introduce overhead in terms of memory usage and access time. The namedtuple implementation in this project demonstrates better performance in most cases, particularly when accessing fields and performing calculations. The project includes both namedtuple and dictionary implementations to allow for easy comparison.

## How to Use
### Dependencies
Ensure you have Python installed, along with the following libraries:

- '**Faker:**' Used for generating random, realistic data.
- '**collections:**' Provides the namedtuple class.
- '**statistics:**' Used for calculating mean values.
- '**datetime:**' Used for handling dates and calculating ages.
We can install '**Faker**' using pip:

```
pip install faker

```
## Running the Code

To generate and analyze profile data:

1. Use '**generate_profiles**' to create a dataset of profiles.
2. Pass the generated profiles to '**analyze_profiles**' for analysis.
3. Review the results stored in the '**AnalysisResult**' namedtuple.

For stock market simulation:

1. Generate stock data using '**generate_stock_data**'.
2. Analyze the market values using '**calculate_market_values**'.
3. Review the market summary.

### Example

Refer to the test_session8.py as well

```
profiles = generate_profiles(10000)
result = analyze_profiles(profiles)
print(result)

stocks = generate_stock_data(100)
market_values = calculate_market_values(stocks)
print(market_values)

```

## Conclusion
This assignment work highlights the power of '**namedtuples**' in Python for creating efficient, readable, and immutable data structures. Whether working with user profiles or simulating stock markets, namedtuples offer a compelling alternative to dictionaries and custom classes, combining performance with clarity.

---------------------------------------------------------------------------------------------------------------------------------------------------

**Submission by** - Hema Aparna M

**mail id** - mhema.aprai@gmail.com

---------------------------------------------------------------------------------------------------------------------------------------------------