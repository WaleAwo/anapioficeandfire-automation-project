import pytest
import requests
from enums.url import APIUrls

pagination = "?page=1&pageSize=15"


@pytest.mark.regression
def test_get_all_books_equals_12():
    response = requests.get(f"{APIUrls.BOOKS.value}{pagination}")
    response_body = response.json()
    assert len(response_body) == 12


@pytest.mark.regression
def test_check_book_json_schema():
    response = requests.get(f"{APIUrls.BOOKS.value}/12")
    response_body = response.json()
    assert "url" in response_body
    assert "name" in response_body
    assert "isbn" in response_body
    assert "authors" in response_body
    assert "numberOfPages" in response_body
    assert "publisher" in response_body
    assert "country" in response_body
    assert "mediaType" in response_body
    assert "released" in response_body
    assert "characters" in response_body
    assert "povCharacters" in response_body


@pytest.mark.regression
def test_check_content_type():
    response = requests.get(APIUrls.BOOKS.value)
    assert response.headers["Content-Type"] == "application/json; charset=utf-8"


def test_check_status_code():
    response = requests.get(APIUrls.BOOKS.value)
    assert response.status_code == 200
