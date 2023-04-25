import requests
from enums.url import APIUrls

pagination = "?page=1&pageSize=15"


def test_get_the_total_number_pages():
    # Send a GET API request and store the response
    response = requests.get(f"{APIUrls.BOOKS.value}{pagination}")

    # Check if the response was successful
    if response.status_code == 200:

        # Parse JSON response into a python dictionary
        response_body = response.json()

        # Set a count for the total number of pages
        total_pages = 0

        # Loop through the response and store the value of the "numberOfPages" key
        # for each book in the 'total_pages' variable
        for book in response_body:
            pages_per_book = book["numberOfPages"]
            total_pages += pages_per_book

        # Print the total number of pages of all the books
        print("Total number of pages:", total_pages)
    else:
        print("Error:", response.status_code)
