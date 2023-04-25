import pytest
import requests
from enums.url import APIUrls

character_id = 500


def test_get_character_with_id_500_check_name_equals_hosman_norcross():
    response = requests.get(f"{APIUrls.CHARACTERS.value}/{character_id}")
    response_body = response.json()
    assert response_body["name"] == "Hosman Norcross"


@pytest.mark.regression
def test_check_character_json_schema():
    response = requests.get(f"{APIUrls.CHARACTERS.value}/{character_id}")
    response_body = response.json()
    assert "url" in response_body
    assert "name" in response_body
    assert "gender" in response_body
    assert "culture" in response_body
    assert "born" in response_body
    assert "died" in response_body
    assert "titles" in response_body
    assert "aliases" in response_body
    assert "father" in response_body
    assert "mother" in response_body
    assert "spouse" in response_body
    assert "allegiances" in response_body
    assert "povBooks" in response_body
    assert "tvSeries" in response_body
    assert "playedBy" in response_body


@pytest.mark.regression
def test_check_content_type():
    response = requests.get(APIUrls.CHARACTERS.value)
    assert response.headers["Content-Type"] == "application/json; charset=utf-8"


def test_check_status_code():
    response = requests.get(APIUrls.CHARACTERS.value)
    assert response.status_code == 200
