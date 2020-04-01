import re


class Validation:

    def validating_user_data(self, **user_data):
        try:
            # import pdb
            # pdb.set_trace()
            response = {
                "success": False,
                "message": "Valid Data...",
                "data": []
            }

            regex_email = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
            regex_username = r"(^[a-zA-Z][a-zA-Z0-9_-]{3,16}$)"
            regex_password = r"([A-Za-z0-9@#$%^&+=]{8,})"

            if 'email' in user_data:
                email = user_data["email"]
                if re.match(regex_email, email):
                    response["success"] = True
                else:
                    response["success"] = False
                    response["message"] = "Incorrect Email..."
                    raise ValueError

            if 'username' in user_data:
                username = user_data["username"]
                if re.match(regex_username, username):
                    response["success"] = True
                else:
                    response["success"] = False
                    response["message"] = "Incorrect Username..."
                    raise ValueError

            if 'password' in user_data:
                password = user_data["password"]
                if re.match(regex_password, password):
                    response["success"] = True
                else:
                    response["success"] = False
                    response["message"] = "Incorrect Password... Length must be 8 or more!!!"
                    raise ValueError

        except ValueError:
            response = response

        except Exception as e:
            response = response

        return response