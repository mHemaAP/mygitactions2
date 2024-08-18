from collections import namedtuple, Counter
from faker import Faker
from statistics import mean
from datetime import datetime
import time
import random

# # Initialize Faker and namedtuple
faker = Faker()
Profile = namedtuple('Profile', 'job company ssn residence current_location blood_group website username name sex address mail birthdate')
AnalysisResult = namedtuple('AnalysisResult', 'largest_blood_group mean_current_location oldest_age average_age')

def generate_profiles(n=10000):
    """
    Generate n random profiles using the Faker library.

    Parameters:
    n (int): Number of profiles to generate.

    Returns:
    list: List of namedtuple containing profile information.
    """
    profiles = tuple(Profile(**faker.profile()) for _ in range(n))
    return profiles

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
    # Early return if profiles list is empty
    if not profiles:
        return AnalysisResult(None, (None, None), None, None)

    blood_groups = (profile.blood_group for profile in profiles)
    current_locations = [profile.current_location for profile in profiles]
    birthdates = [profile.birthdate for profile in profiles]

    # Calculate blood group frequencies
    largest_blood_group = Counter(blood_groups).most_common(1)[0][0]

    # Calculate mean of current locations (latitude, longitude)
    mean_latitude = mean(location[0] for location in current_locations)
    mean_longitude = mean(location[1] for location in current_locations)

    # Calculate ages
    today = datetime.today().date()
    ages = [(today - birthdate.date() if isinstance(birthdate, datetime) else today - birthdate).days // 365 for birthdate in birthdates]
    oldest_age = max(ages)
    average_age = mean(ages)

    # Return results as a namedtuple
    return AnalysisResult(
        largest_blood_group=largest_blood_group,
        mean_current_location=(mean_latitude, mean_longitude),
        oldest_age=oldest_age,
        average_age=average_age
    )

# Dictionary-based implementation for comparison
def generate_profiles_dict(n=10000):
    """
    Generate n random profiles using the Faker library and store them in a list of dictionaries.

    Parameters:
    n (int): Number of profiles to generate.

    Returns:
    list: List of dictionaries containing profile information.
    """
    profiles = [faker.profile() for _ in range(n)]
    return profiles

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
    if not profiles:
        return {
            "largest_blood_group": None,
            "mean_current_location": (None, None),
            "oldest_age": None,
            "average_age": None
        }

    # Precompute fields to avoid repeated dictionary access
    blood_groups = [profile['blood_group'] for profile in profiles]
    current_locations = [profile['current_location'] for profile in profiles]
    birthdates = [profile['birthdate'] for profile in profiles]

    # Calculate blood group frequencies
    largest_blood_group = Counter(blood_groups).most_common(1)[0][0]

    # Calculate mean of current locations (latitude, longitude)
    mean_latitude = mean(location[0] for location in current_locations)
    mean_longitude = mean(location[1] for location in current_locations)

    # Calculate ages
    today = datetime.today().date()
    ages = [(today - birthdate.date() if isinstance(birthdate, datetime) else today - birthdate).days // 365 for birthdate in birthdates]
    oldest_age = max(ages)
    average_age = mean(ages)

    return {
        "largest_blood_group": largest_blood_group,
        "mean_current_location": (mean_latitude, mean_longitude),
        "oldest_age": oldest_age,
        "average_age": average_age
    }

# Define the Stock namedtuple
Stock = namedtuple('Stock', ['name', 'symbol', 'open', 'high', 'close', 'weight'])

def generate_stock_data(num_companies=100):
    """
    Generate stock data for an imaginary stock exchange.

    Parameters:
    num_companies (int): Number of companies to generate data for.

    Returns:
    list: List of namedtuple containing stock information.
    """
    stocks = []

    for _ in range(num_companies):
        name = faker.company()
        symbol = ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ', k=3))

        open_price = round(random.uniform(100, 500), 2)
        high_price = round(random.uniform(open_price, open_price + random.uniform(0.1, 50)), 2)
        close_price = round(random.uniform(open_price, high_price), 2)

        weight = random.uniform(0.01, 1)

        stocks.append(Stock(name=name, symbol=symbol, open=open_price, high=high_price, close=close_price, weight=weight))

    return stocks

def calculate_market_values(stocks):
    """
    Calculate the stock market values based on stock data.

    Parameters:
    stocks (list): List of namedtuple containing stock information.

    Returns:
    dict: Dictionary containing the market's open value, high value, and close value.
    """
    total_weight = sum(stock.weight for stock in stocks)

    def weighted_value(stock_price):
        return sum((stock_price(stock) * stock.weight) / total_weight for stock in stocks)

    market_open_value = weighted_value(lambda stock: stock.open)
    market_high_value = weighted_value(lambda stock: stock.high)
    market_close_value = weighted_value(lambda stock: stock.close)

    return {
        "market_open_value": market_open_value,
        "market_high_value": market_high_value,
        "market_close_value": market_close_value
    }