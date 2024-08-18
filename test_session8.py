import session8
from session8 import *
from datetime import datetime
import pytest
from io import StringIO 
import sys
import time
import inspect
import os
import re

README_CONTENT_CHECK_FOR = [
"namedtuple",
"Faker",
"dictionary",
"comparison",
"generate",
"stock market",
"profile data"
]

def test_readme_exists():
    assert os.path.isfile("README.md"), "README.md file missing!"

def test_readme_contents():
    readme = open("README.md", "r")
    readme_words = readme.read().split()
    readme.close()
    assert len(readme_words) >= 500, "Make your README.md file interesting! Add atleast 500 words"

def test_readme_proper_description():
    READMELOOKSGOOD = True
    f = open("README.md", "r", encoding="utf-8")
    content = f.read()
    f.close()
    for c in README_CONTENT_CHECK_FOR:
        if c not in content:
            READMELOOKSGOOD = False
            pass
    assert READMELOOKSGOOD == True, "You have not described all the functions/class well in your README.md file"

def test_readme_file_for_formatting():
    f = open("README.md", "r", encoding="utf-8")
    content = f.read()
    f.close()
    assert content.count("#") >= 10

def test_indentations():
    ''' Returns pass if used four spaces for each level of syntactically \
    significant indenting.'''
    lines = inspect.getsource(session8)
    spaces = re.findall('\n +.', lines)
    for space in spaces:
        assert len(space) % 4 == 2, "Your script contains misplaced indentations"
        assert len(re.sub(r'[^ ]', '', space)) % 4 == 0, "Your code indentation does not follow PEP8 guidelines"

def test_function_name_had_cap_letter():
    functions = inspect.getmembers(session8, inspect.isfunction)
    for function in functions:
        assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"


# def test_analyze_profiles():
#     """
#     Test the analyze_profiles function with different datasets.
#     """
#     # Test case 1: Check if the largest blood group is returned correctly
#     profiles = generate_profiles(10000)
#     result = analyze_profiles(profiles)
#     assert result.largest_blood_group in ['A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-'], "Test case 1 failed"

#     # Test case 2: Check if mean current location is a tuple with two elements
#     assert isinstance(result.mean_current_location, tuple) and len(result.mean_current_location) == 2, "Test case 2 failed"

#     # Test case 3: Check if the oldest age is a non-negative integer
#     assert isinstance(result.oldest_age, int) and result.oldest_age >= 0, "Test case 3 failed"

#     # Test case 4: Check if the average age is a non-negative float
#     assert isinstance(result.average_age, float) and result.average_age >= 0, "Test case 4 failed"

#     # Test case 5: Check if analyze_profiles returns all expected fields
#     expected_fields = {"largest_blood_group", "mean_current_location", "oldest_age", "average_age"}
#     assert expected_fields.issubset(result._fields), "Test case 5 failed"

#     print("All test cases passed!")

def test_tuple_empty_profile_list():
    """
    Test case 1: Check behavior with an empty profile list
    """

    profiles = []
    result = analyze_profiles(profiles)
    assert result.largest_blood_group is None, "Test case 1 failed: Expected None for largest_blood_group with tuple"
    assert result.mean_current_location == (None, None), "Test case 1 failed: Expected (None, None) for mean_current_location with tuple"
    assert result.oldest_age is None, "Test case 1 failed: Expected None for oldest_age with tuple"
    assert result.average_age is None, "Test case 1 failed: Expected None for average_age with tuple"

    print("Test case 1: Tuple empty profile list passed!")

def test_tuple_single_profile():
    """
    Test case 2: Check behavior with a single profile with tuples
    """
    profiles = generate_profiles(1)
    result = analyze_profiles(profiles)
    assert result.largest_blood_group in ['A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-'], "Tuple Test: Unknown blood type"
    assert isinstance(result.mean_current_location, tuple) and len(result.mean_current_location) == 2, "Tuple Test: Mean current location length is not equal to 2"
    assert isinstance(result.oldest_age, int) and result.oldest_age >= 0, "Tuple Test: Old Age should be greater than 0"
    assert isinstance(result.average_age, int) and result.average_age >= 0, "Tuple Test: Average age should be greater than 0"

    print("Test case 2: Tuple single profile passed!")

def test_tuple_same_blood_group_profiles():
    """
    Test case 3: Check behavior when all tuple profiles have the same blood group
    """
    profiles = generate_profiles(100)
    profiles = tuple(profile._replace(blood_group='AB+') for profile in profiles)
    result = analyze_profiles(profiles)
    assert result.largest_blood_group == 'AB+', "Test case 3 failed: Expected AB+ for tuple largest_blood_group"

    print("Test case 3: All profiles of the same blood group with tuples passed!")

def test_tuple_same_birthdate_profiles():
    """
    Test case 4: Check behavior when all profiles have the same birthdate
    """
    birthdate = datetime(1990, 1, 1).date()
    profiles = generate_profiles(100)
    profiles = tuple(profile._replace(birthdate=birthdate) for profile in profiles)
    result = analyze_profiles(profiles)
    expected_age = (datetime.today().date() - birthdate).days // 365
    assert result.oldest_age == expected_age, "Test case 4 failed: Oldest age is incorrect with tuple"
    assert result.average_age == expected_age, "Test case 4 failed: Average age is incorrect with tuple"

    print("Test case 4: Profiles with the same birthdate with tuples passed!")

def test_tuple_accuracy_data():
    """
    Test case 5: Check for accuracy with known data
    """
    profiles = [
        Profile(job="Engineer", company="Company A", ssn="123-45-6789", residence="Place A",
                current_location=(10.0, 20.0), blood_group="A+", website="http://example.com",
                username="user1", name="John Doe", sex="M", address="123 Street A",
                mail="john@example.com", birthdate=datetime(1980, 1, 1).date()),
        Profile(job="Doctor", company="Company B", ssn="987-65-4321", residence="Place B",
                current_location=(30.0, 40.0), blood_group="O-", website="http://example.org",
                username="user2", name="Jane Smith", sex="F", address="456 Street B",
                mail="jane@example.com", birthdate=datetime(1990, 1, 1).date())
    ]
    result = analyze_profiles(profiles)
    assert result.largest_blood_group in ['A+', 'O-'], "Test case 5 failed: Incorrect largest blood group with tuple"
    assert result.mean_current_location == (20.0, 30.0), "Test case 5 failed: Incorrect mean current location with tuple"
    assert result.oldest_age == 44, "Test case 5 failed: Incorrect oldest age with tuple"
    assert abs(result.average_age - 39.5) <= 0.5, "Test case 5 failed: Incorrect average age with tuple"

    print("Test case 5: Check for accuracy with known data with tuples passed!")

def test_dict_empty_profile_list():
    """
    Test case 1: Check behavior with an empty profile list with dictionary.
    """
    profiles = []
    result = analyze_profiles_dict(profiles)
    assert result["largest_blood_group"] is None, "Test case 1 failed: Expected None for largest_blood_group with dict"
    assert result["mean_current_location"] == (None, None), "Test case 1 failed: Expected (None, None) for mean_current_location with dict"
    assert result["oldest_age"] is None, "Test case 1 failed: Expected None for oldest_age with dict"
    assert result["average_age"] is None, "Test case 1 failed: Expected None for average_age with dict"

    print("Test case 1: Dict empty profile list passed!")

def test_dict_single_profile():
    """
    Test case 2: Check behavior with a single profile with dict
    """
    profiles = generate_profiles_dict(1)
    result = analyze_profiles_dict(profiles)
    assert result["largest_blood_group"] in ['A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-'], "Dict Test: Unknown Blood group"
    assert isinstance(result["mean_current_location"], tuple) and len(result["mean_current_location"]) == 2, "Dict Test: Mean current location not equal to 2"
    assert isinstance(result["oldest_age"], int) and result["oldest_age"] >= 0, "Dict Test: Oldest Age should be greater than 0"
    assert isinstance(result["average_age"], int) and result["average_age"] >= 0, "Dict Test: Average age should be greater than 0"

    print("Test case 2: Dict single profile passed!")

def test_dict_same_blood_group_profiles():
    """
    Test case 3: Check behavior when all dictionary profiles have the same blood group
    """
    profiles = generate_profiles_dict(100)
    for i in range(100):
        profiles[i]['blood_group'] = 'AB+'
    result = analyze_profiles_dict(profiles)
    assert result["largest_blood_group"] == 'AB+', "Test case 3 failed: Expected AB+ for largest_blood_group with dict"

    print("Test case 3: All profiles of the same blood group with dict passed!")

def test_dict_same_birthdate_profiles():
    """
    Test case 4: Check behavior when all dictionary profiles have the same birthdate
    """
    birthdate = datetime(1990, 1, 1)
    profiles = generate_profiles_dict(100)
    for i in range(100):
        profiles[i]['birthdate'] = birthdate
    result = analyze_profiles_dict(profiles)
    expected_age = (datetime.today() - birthdate).days // 365
    assert result["oldest_age"] == expected_age, "Test case 4 failed: Oldest age is incorrect with dict"
    assert result["average_age"] == expected_age, "Test case 4 failed: Average age is incorrect with dict"

    print("Test case 4: Profiles with the same birthdate with dict passed!")


def test_dict_accuracy_data():
    """
    Test case 5: Check for accuracy with known data with dictionary
    """
    profiles = [
        {'job': "Engineer", 'company': "Company A", 'ssn': "123-45-6789", 'residence': "Place A",
         'current_location': (10.0, 20.0), 'blood_group': "A+", 'website': "http://example.com",
         'username': "user1", 'name': "John Doe", 'sex': "M", 'address': "123 Street A",
         'mail': "john@example.com", 'birthdate': datetime(1980, 1, 1)},
        {'job': "Doctor", 'company': "Company B", 'ssn': "987-65-4321", 'residence': "Place B",
         'current_location': (30.0, 40.0), 'blood_group': "O-", 'website': "http://example.org",
         'username': "user2", 'name': "Jane Smith", 'sex': "F", 'address': "456 Street B",
         'mail': "jane@example.com", 'birthdate': datetime(1990, 1, 1)}
    ]
    result = analyze_profiles_dict(profiles)
    assert result["largest_blood_group"] in ['A+', 'O-'], "Test case 5 failed: Incorrect largest blood group with dict"
    assert result["mean_current_location"] == (20.0, 30.0), "Test case 5 failed: Incorrect mean current location with dict"
    assert result["oldest_age"] == 44, "Test case 5 failed: Incorrect oldest age with dict"
    assert abs(result["average_age"] - 39.5) <= 0.5, "Test case 5 failed: Incorrect average age with dict"

    print("Test case 5: Check for accuracy with known data with dictionary passed!")

# Performance Comparison
def test_compare_performance():
    """
    Compare the performance between namedtuple-based and dictionary-based implementations.
    """
    print("Executing test_compare_performance...")
    num_profiles = 100000
    
    # namedtuple-based implementation
    start_time = time.time()
    profiles_namedtuple = generate_profiles(num_profiles)
    analyze_profiles(profiles_namedtuple)
    namedtuple_duration = time.time() - start_time
    
    # dictionary-based implementation
    start_time = time.time()
    profiles_dict = generate_profiles_dict(num_profiles)
    analyze_profiles_dict(profiles_dict)
    dict_duration = time.time() - start_time
    
    print(f"namedtuple-based implementation took {namedtuple_duration:.4f} seconds.")
    print(f"dictionary-based implementation took {dict_duration:.4f} seconds.")
    print(f"namedtuple is faster by {dict_duration - namedtuple_duration:.4f} seconds.")

    assert namedtuple_duration < dict_duration, "Test case time failed: Dict Profile is faster"

# def test_unique_stock_symbol():
#     """
#     Test case 1: Ensure all stock symbols are unique
#     """
#     stocks = generate_stock_data(100)
#     symbols = [stock.symbol for stock in stocks]
#     assert len(symbols) == len(set(symbols)), "Stock Market Sim: Stock symbols are not unique"

# def test_weight_distribution():
#     """
#     Test case 1: Validate stock weight distribution
#     """
#     stocks = generate_stock_data(100)
#     total_weight = sum(stock.weight for stock in stocks)

#     # The total weight should be equal to the number of stocks if each weight was uniformly distributed.
#     assert round(total_weight, 2) == len(stocks), f"Test case 1 failed: Total weight ({total_weight}) does not equal the number of stocks ({len(stocks)})"

def test_unique_stock_symbol():
    # Test case 1: Ensure all company names are unique
    stocks = generate_stock_data(100)
    company_names = [stock.name for stock in stocks]
    assert len(company_names) == len(set(company_names)), "Test case 1 failed: Company names are not unique"

def test_non_negative_price():
    """
    Test case 2: Ensure open, high, and close prices are not negative
    """
    stocks = generate_stock_data(100)
    for stock in stocks:
        assert stock.open >= 0, "Stock Market Sim: Open price is negative"
        assert stock.high >= 0, "Stock Market Sim: High price is negative"
        assert stock.close >= 0, "Stock Market Sim: Close price is negative"

def test_high_price_gte_open_close_price():
    """
    Test case 3: Ensure high price is greater than or equal to open and close prices
    """
    stocks = generate_stock_data(100)
    for stock in stocks:
        assert stock.high >= stock.open, "Stock Market Sim: High price is less than open price"
        assert stock.high >= stock.close, "Stock Market Sim: High price is less than close price"

def test_correct_market_open_price():
    """
    Test case 4: Ensure market open value is calculated correctly
    """
    stocks = generate_stock_data(100)
    market_values = calculate_market_values(stocks)
    assert market_values["market_open_value"] > 0, "Stock Market Sim: Market open value is not positive"

def test_market_high_gte_open_close_price():
    """
    Test case 5: Ensure market high value is greater than or equal to market open and close values
    """
    stocks = generate_stock_data(100)
    market_values = calculate_market_values(stocks)
    assert market_values["market_high_value"] >= market_values["market_open_value"], "Stock Market Sim: Market high value is less than market open value"
    assert market_values["market_high_value"] >= market_values["market_close_value"], "Stock Market Sim: Market high value is less than market close value"

def test_correct_market_close_price():
    """
    Test case 6: Ensure market close value is calculated correctly
    """
    stocks = generate_stock_data(100)
    market_values = calculate_market_values(stocks)
    assert market_values["market_close_value"] > 0, "Stock Market Sim: Market close value is not positive"

def test_single_stock_behaviour():
    """
    Test case 7: Test behavior with a single stock
    """
    sstock = generate_stock_data(1)
    single_stock = list(sstock)
    single_stock_market_values = calculate_market_values(single_stock)
    assert round(single_stock_market_values["market_open_value"], 2) == single_stock[0].open, "Stock Market Sim: Market open value is incorrect for single stock"
    assert single_stock_market_values["market_high_value"] == single_stock[0].high, "Stock Market Sim: Market high value is incorrect for single stock"
    assert round(single_stock_market_values["market_close_value"], 2) == single_stock[0].close, "Stock Market Sim: Market close value is incorrect for single stock"

def test_non_zero_weight():
    """
    Test case 8: Ensure total weight is non-zero
    """
    stocks = generate_stock_data(100)
    total_weight = sum(stock.weight for stock in stocks)
    assert total_weight > 0, "Stock Market Sim: Total weight is zero"

def test_non_zero_weight():
    """
    Test case 9: Ensure stock market values are consistent with weights
    """
    stocks = generate_stock_data(100)
    market_values = calculate_market_values(stocks)
    total_weight = sum(stock.weight for stock in stocks)
    assert total_weight > 0, "Stock Market Sim: Total weight is zero in test_non_zero_weight"
    weighted_open_value = sum((stock.open * stock.weight) for stock in stocks) / total_weight
    assert abs(market_values["market_open_value"] - weighted_open_value) < 0.01, "Stock Market Sim: Weighted open value is inconsistent"


def test_correct_companies_count():
    """
    Test case 10: Ensure generating stock data returns correct number of companies
    """
    stocks_50 = generate_stock_data(50)
    assert len(stocks_50) == 50, "Stock Market Sim: Incorrect number of companies generated"

def test_validate_stock_weights_distribution():
    """
    Test case 11: Validate the distribution of stock weights
    """
    stocks = generate_stock_data(100)
    total_weight = sum(stock.weight for stock in stocks)

    # Check that the total weight is within a reasonable range
    expected_total_weight = len(stocks) * 0.5  # assuming the average weight should be around 0.5
    tolerance = len(stocks) * 0.1  # allow a 10% deviation
    assert abs(total_weight - expected_total_weight) <= tolerance, f"Test case 11 failed: Total weight ({total_weight}) deviates too much from the expected value ({expected_total_weight})"


