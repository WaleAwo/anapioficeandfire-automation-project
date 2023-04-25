import pytest
import requests
from enums.url import APIUrls

house_id = 70


def test_get_house_with_id_70_check_name_equals_house_chester_of_greenshield():
    response = requests.get(f"{APIUrls.HOUSES.value}/{house_id}")
    response_body = response.json()
    assert response_body["name"] == "House Chester of Greenshield"


@pytest.mark.regression
def test_check_house_json_schema():
    response = requests.get(f"{APIUrls.HOUSES.value}/1")
    response_body = response.json()
    assert "url" in response_body
    assert "name" in response_body
    assert "region" in response_body
    assert "coatOfArms" in response_body
    assert "words" in response_body
    assert "titles" in response_body
    assert "seats" in response_body
    assert "currentLord" in response_body
    assert "heir" in response_body
    assert "overlord" in response_body
    assert "founded" in response_body
    assert "founder" in response_body
    assert "diedOut" in response_body
    assert "ancestralWeapons" in response_body
    assert "cadetBranches" in response_body
    assert "swornMembers" in response_body


@pytest.mark.regression
def test_check_content_type():
    response = requests.get(APIUrls.HOUSES.value)
    assert response.headers["Content-Type"] == "application/json; charset=utf-8"


def test_check_status_code():
    response = requests.get(APIUrls.HOUSES.value)
    assert response.status_code == 200
