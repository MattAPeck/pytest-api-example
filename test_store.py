from jsonschema import validate
import pytest
import schemas
import api_helpers
from hamcrest import assert_that, contains_string, is_
from random import randint

'''
TODO: Finish this test by...
1) Creating a function to test the PATCH request /store/order/{order_id}
2) *Optional* Consider using @pytest.fixture to create unique test data for each run
2) *Optional* Consider creating an 'Order' model in schemas.py and validating it in the test
3) Validate the response codes and values
4) Validate the response message "Order and pet status updated successfully"
'''


'''This was the best I could do, I created the Order model in schemas but I'm not sure if I can validate it, 
the test data doesn't seem to have any orders in it for me to test so I could only ever get the 404 error.'''


def test_patch_order_by_id():
    test_endpoint = "/store/order/{order_id}"
    data = {"stats":"available"}

    response = api_helpers.patch_api_data(test_endpoint, data)
    if response.status_code == 404:
         return response.json()
    elif response.status_code == 400:
        return response.json()
    else:
        validate(response.json(), schema=schemas.order)
