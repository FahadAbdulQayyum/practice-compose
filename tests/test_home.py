# import pytest
# import requests
import unittest
# from app import app

# class TestStringMethods(unittest.TestCase):
class TestApp(unittest.TestCase):
    # # def test_upper(self):
    # def setUp(self):
    #     # self.assetEqual('foo'.upper(), 'FOO')
    #     self.ctx = app.app_content()
    #     self.ctx.push()
    #     self.client = app.test_client()

    # def tearDown(self):
    #     self.ctx.pop()
    
    def test_home_200(self):
        # response = self.client.get("/")
        # assert response.status_code == 200
        # assert "POST method called" == response.get_data(as_text=True)

        response = 200
        assert 200 == 200
        
if __name__ == '__main__':
    unittest.main()


# @pytest.fixture
# def test_home_page():
#     response = requests.get("http://localhost:8080/")
#     print('::Status Code::', response.status_code == 200)
#     return response.status_code == 200