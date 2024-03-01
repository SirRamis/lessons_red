import pytest
import requests

base_url = "https://restful-booker.herokuapp.com/booking"
# def sum_it(x, y):
#     return x + y
#
#
# def test_equal():
#     assert sum_it(5, 3) == 8
#
#
# def test_not_equal():
#     assert sum_it(4, 8) == 11
# def test_get_code():
#     result = requests.get(base_url)
#     print(result)
#     assert result.status_code == 200

def test_get_booking_by_id():
    response = requests.get(f'{base_url}/1')
    response_data = response.json()
    print(response_data)
    assert response.status_code == 200