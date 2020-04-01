"""
This is file for validating user data which is coming from server
Author: Akshaya Revaskar
Date: 11/03/2020
"""

# importing necessary packages
import json
from auth.validation import Validation

validation_object = Validation()


class User:

    # function for user registration
    def register(self, that=None):

        try:
            response = {
                "success": False,
                "message": "Something Went Wrong!!!",
                "data": []
            }

            # reading the json data and converting it into python dictionary
            length = int(that.headers['Content-Length'])
            message = that.rfile.read(length)
            user_data = json.loads(message)

            response = validation_object.validating_user_data(**user_data)

            if response["success"]:
                if user_data['username'] is not None and user_data['password'] is not None and user_data['email'] is not None:
                    response["success"] = True
                    response["message"] = "Valid Data..."
                    response["data"] = [user_data]

        except Exception as e:
            response = response

        return response

    # function for user login
    def login(self, that=None):

        try:
            response = {
                "success": False,
                "message": "Something Went Wrong",
                "data": []
            }

            # reading the json data and converting it into a python dictionary
            length = int(that.headers['Content-Length'])
            message = that.rfile.read(length)
            user_data = json.loads(message)

            response = validation_object.validating_user_data(**user_data)

            if response["success"]:
                if user_data['email'] is not None and user_data['password'] is not None:
                    response["success"] = True
                    response["message"] = "Valid Data..."
                    response["data"] = [user_data]

        except Exception as e:
            response = response

        return response

    # function for logout
    # def logout(self):
    #
    #     response = {
    #         "success": True
    #     }
    #     return response

    # function for forgot password
    def forgot(self, that=None):

        try:
            response = {
                "success": False,
                "message": "Something Went wrong...",
                "data": []
            }

            # read the message and convert it into a python dictionary
            length = int(that.headers['Content-Length'])
            message = that.rfile.read(length)
            user_data = json.loads(message)

            response = validation_object.validating_user_data(**user_data)

            if response["success"]:
                if user_data['email'] is not None:
                    response["success"] = True
                    response["message"] = "Valid Data..."
                    response["data"] = [user_data]

        except Exception as e:
            response = response

        return response

    # function for reset password
    def reset(self, that=None):

        try:
            response = {
                "success": False,
                "message": "Something Went Wrong",
                "data": []
            }

            # reading the json data and converting it into a python dictionary
            length = int(that.headers['Content-Length'])
            message = that.rfile.read(length)
            user_data = json.loads(message)

            res = validation_object.validating_user_data(**user_data)

            if res["success"]:
                if user_data['password'] is not None:
                    response["success"] = True
                    response["message"] = "Valid Data..."
                    response["data"] = [user_data]

        except Exception as e:
            response = response

        return response
