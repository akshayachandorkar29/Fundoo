"""
This is file for validating notes data coming from server
Author: Akshaya Revaskar
Date: 11/03/2020
"""

# importing necessary packages
import json
import jwt
import re
import os

from auth.validation import Validation
validation_object = Validation()


class Note:

    # CREATE NOTE API
    def create_note(self, that=None):
        response = {
            "success": False,
            "message": "something went wrong!!!",
            "data": []
        }

        try:
            # import pdb
            # pdb.set_trace()
            # reading the json data and converting it into python dictionary
            length = int(that.headers['Content-Length'])
            message = that.rfile.read(length)
            user_data = json.loads(message)

            # retriving token from headres to retrive id of the user who is logged in
            token = that.headers['token']
            if token:
                # decoding token to get the id
                payload = jwt.decode(token, 'secret', algorithms=['HS256'])
                user_id = payload.get('id')

                # adding user_id in json_data dictionary
                user_data["user_id"] = user_id

                # validating user entered data
                if "title" in user_data:
                    if len(user_data["title"]) == 0:
                        response["success"] = False
                        response['message'] = 'title can not be empty'
                        raise ValueError
                else:
                    response["message"] = "give title"
                    raise KeyError

                if "description" in user_data:
                    if len(user_data["description"]) == 0:
                        response["success"] = False
                        response['message'] = 'description can not be empty'
                        raise ValueError
                else:
                    response["message"] = "give description"
                    raise KeyError

                if "color" in user_data:
                    if len(user_data["color"]) == 0:
                        response["success"] = False
                        response['message'] = 'color can not be empty'
                        raise ValueError
                else:
                    response["message"] = "give color"
                    raise KeyError

                if len(user_data["title"]) > 0 and len(user_data["description"]) > 0 and len(user_data["color"]) > 0:
                    response["success"] = True
                    response['message'] = "valid data"
                    response["data"] = [user_data]

            else:
                response["success"] = False
                response["message"] = "You have to LOGIN first"

        except ValueError:
            response = response

        except KeyError:
            response = response

        except Exception as e:
            response = response

        return response

    # READ NOTE API
    def read_note(self, that=None):
        # import pdb
        # pdb.set_trace()

        response = {
            "success": False,
            "message": "something went wrong",
            "data": []
        }

        try:
            # getting token from headers
            token = that.headers['token']

            # validating token
            if token is None:
                response["success"] = False
                response["message"] = "You have to login first"

            else:
                payload = jwt.decode(token, 'secret', algorithms=['HS256'])
                user_id = payload.get('id')
                response["success"] = True
                response["message"] = "you got the token"
                response["data"] = user_id

        except Exception as e:
            response = response

        return response

    # UPDATE NOTE API
    def update_note(self, that=None):
        response = {
            "success": False,
            "message": "something went wrong",
            "data": []
        }
        try:
            # import pdb
            # pdb.set_trace()
            # reading the json data and converting it into python dictionary
            length = int(that.headers['Content-Length'])
            message = that.rfile.read(length)
            user_data = json.loads(message)

            # retriving token from headres to retrive id of the user who is logged in
            token = that.headers['token']
            if token:

                if "id" in user_data:
                    if user_data["id"] == 0:
                        response["success"] = False
                        response["message"] = "id can not be empty"
                        raise ValueError
                else:
                    response["message"] = "Give ID of the note which is to be updated"
                    raise KeyError

                if isinstance(user_data["id"], str):
                    response["success"] = False
                    response["message"] = "ID must be integer"
                    raise TypeError

                else:
                    response["success"] = True
                    response['message'] = "valid data"
                    response["data"] = [user_data]
            else:
                response["success"] = False
                response["message"] = "You have to LOGIN first"

        except ValueError:
            response = response

        except TypeError:
            response = response

        except KeyError:
            response = response

        except Exception:
            response = response

        return response

    # DELETE NOTE API
    def delete_note(self, that=None):
        response = {
            "success": False,
            "message": "something went wrong",
            "data": []
        }
        try:
            # reading the json data and converting it into python dictionary
            length = int(that.headers['Content-Length'])
            message = that.rfile.read(length)
            user_data = json.loads(message)

            # retriving token from headres to retrive id of the user who is logged in
            token = that.headers['token']
            if token:

                if "id" in user_data:
                    if user_data["id"] == 0:
                        response["success"] = False
                        response["message"] = "id can not be empty"
                        raise ValueError
                else:
                    response["message"] = "Give ID of the note which is to be deleted"
                    raise KeyError

                if isinstance(user_data["id"], str):
                    response["success"] = False
                    response["message"] = "ID must be integer"
                    raise TypeError

                else:
                    # if len(user_data["id"]) > 0:
                    response["success"] = True
                    response['message'] = "valid data"
                    response["data"] = [user_data]
            else:
                response["success"] = False
                response["message"] = "You have to LOGIN first"

        except ValueError:
            response = response

        except TypeError:
            response = response

        except KeyError:
            response = response

        except Exception as e:
            response = response

        return response

    # PIN NOTE API
    def pin_note(self, that=None):
        response = {
            "success": False,
            "message": "something went wrong",
            "data": []
        }

        try:
            # reading the json data and converting it into python dictionary
            length = int(that.headers['Content-Length'])
            message = that.rfile.read(length)
            user_data = json.loads(message)

            # retriving token from headres to retrive id of the user who is logged in
            token = that.headers['token']
            if token:
                # validating json data
                if "id" in user_data:
                    if user_data["id"] == 0:
                        response["success"] = False
                        response["message"] = "id can not be empty"
                        raise ValueError
                else:
                    response["message"] = "Give ID of the note which is to be pinned"
                    raise KeyError

                if "is_pinned" in user_data:
                    if type(user_data["is_pinned"]) == str:
                        response["success"] = False
                        response["message"] = "this field can not be string. Set boolean value"
                        raise ValueError
                else:
                    response["message"] = "Give is_pinned field"
                    raise KeyError

                if isinstance(user_data["id"], str):
                    response["success"] = False
                    response["message"] = "ID must be integer"
                    raise TypeError

                else:
                    response["success"] = True
                    response["message"] = "valid data"
                    response["data"] = [user_data]
            else:
                response["success"] = False
                response["message"] = "You have to login first"

        except ValueError:
            response = response

        except TypeError:
            response = response

        except KeyError:
            response = response

        except Exception as e:
            response = response

        return response

    # ARCHIVE NOTE API
    def archive_note(self, that=None):
        response = {
            "success": False,
            "message": "something went wrong",
            "data": []
        }

        try:

            # reading the json data and converting it into python dictionary
            length = int(that.headers['Content-Length'])
            message = that.rfile.read(length)
            user_data = json.loads(message)

            # retriving token from headres to retrive id of the user who is logged in
            token = that.headers['token']
            if token:
                # validating data coming from user
                if "id" in user_data:
                    if user_data["id"] == 0:
                        response["success"] = False
                        response["message"] = "id can not be empty"
                        raise ValueError
                else:
                    response["message"] = "Give ID of the note which is to be archived"
                    raise KeyError

                if "is_archived" in user_data:
                    if type(user_data["is_archived"]) == str:
                        response["success"] = False
                        response["message"] = "this field can not be string. Set boolean value"
                        raise ValueError
                else:
                    response["message"] = "Give is_archived field"
                    raise KeyError

                if isinstance(user_data["id"], str):
                    response["success"] = False
                    response["message"] = "ID must be integer"
                    raise TypeError
                else:
                    response["success"] = True
                    response["message"] = "valid data"
                    response["data"] = [user_data]
            else:
                response["success"] = False
                response["message"] = "You have to login first"

        except ValueError:
            response = response

        except TypeError:
            response = response

        except KeyError:
            response = response

        except Exception as e:
            response = response

        return response

    # TRASH NOTE API
    def trash_note(self, that=None):
        response = {
            "success": False,
            "message": "something went wrong",
            "data": []
        }

        try:
            # reading the json data and converting it into python dictionary
            length = int(that.headers['Content-Length'])
            message = that.rfile.read(length)
            user_data = json.loads(message)

            # retriving token from headres to retrive id of the user who is logged in
            token = that.headers['token']
            if token:
                # validating data coming from user
                if "id" in user_data:
                    if user_data["id"] == 0:
                        response["success"] = False
                        response["message"] = "id can not be empty"
                        raise ValueError
                else:
                    response["message"] = "Give ID of the note which is to be trashed"
                    raise KeyError

                if "is_trashed" in user_data:
                    if type(user_data["is_trashed"]) == str:
                        response["success"] = False
                        response["message"] = "this field can not be string. Set boolean value"
                        raise ValueError
                else:
                    response["message"] = "give field is_trashed"
                    raise KeyError

                if isinstance(user_data["id"], str):
                    response["success"] = False
                    response["message"] = "ID must be integer"
                    raise TypeError
                else:
                    response["success"] = True
                    response["message"] = "valid data"
                    response["data"] = [user_data]
            else:
                response["success"] = False
                response["message"] = "You have to login first"

        except ValueError:
            response = response

        except TypeError:
            response = response

        except KeyError:
            response = response

        except Exception as e:
            response = response

        return response


    # RESTORE NOTE API
    def restore_note(self, that=None):

        try:
            response = {

                "success": False,
                "message": "something went wrong",
                "data": []
            }
            # import pdb
            # pdb.set_trace()

            # reading the json data and converting it into python dictionary
            length = int(that.headers['Content-Length'])
            message = that.rfile.read(length)
            user_data = json.loads(message)

            # retriving token from headres to retrive id of the user who is logged in
            token = that.headers['token']
            if token:
                # validating data coming from user
                if "id" in user_data:
                    if user_data["id"] == 0:
                        response["success"] = False
                        response["message"] = "id can not be empty"
                        raise ValueError
                else:
                    response["message"] = "Give ID of the note which is to be restored"
                    raise KeyError

                if "is_restored" in user_data:
                    if type(user_data["is_restored"]) == str:
                        response["success"] = False
                        response["message"] = "this field can not be string. Set boolean value"
                        raise ValueError
                else:
                    response["message"] = "give field is_restored"
                    raise KeyError

                if isinstance(user_data["id"], str):
                    response["success"] = False
                    response["message"] = "ID must be integer"
                    raise TypeError

                else:
                    response["success"] = True
                    response["message"] = "valid data"
                    response["data"] = [user_data]

            else:
                response["success"] = False
                response["message"] = "You have to login first"

        except ValueError:
            response = response

        except TypeError:
            response = response

        except KeyError:
            response = response

        except Exception as e:
            response = response

        return response

    # LISTING PIN NOTE API
    def listing_pin(self, that=None):
        # import pdb
        # pdb.set_trace()

        response = {
            "success": False,
            "message": "something went wrong",
            "data": []
        }
        try:
            # getting token from headers
            token = that.headers['token']

            # validating token
            if token is None:
                response["success"] = False
                response["message"] = "You have to login first"
            else:
                payload = jwt.decode(token, 'secret', algorithms=['HS256'])
                user_id = payload.get('id')
                response["success"] = True
                response["message"] = "valid data"
                response["data"] = user_id

        except Exception as e:
            response = response

        return response

    # LISTING ARCHIVE NOTE API
    def listing_archive(self, that=None):
        try:
            response = {
                "success": False,
                "message": "something went wrong"
            }
            # import pdb
            # pdb.set_trace()

            # getting token from headers
            token = that.headers['token']

            # validating token
            if token is None:
                response["success"] = False
                response["message"] = "You have to login first"
            else:
                payload = jwt.decode(token, 'secret', algorithms=['HS256'])
                user_id = payload.get('id')
                response["success"] = True
                response["message"] = "valid data"
                response["data"] = user_id

        except Exception as e:
            response = response

        return response

    # LISTING TRASH NOTE API
    def listing_trash(self, that=None):
        response = {

            "success": False,
            "message": "something went wrong"
        }

        try:

            # getting token from headers
            token = that.headers['token']

            # validating token
            if token is None:
                response["success"] = False
                response["message"] = "You have to login first"
            else:
                payload = jwt.decode(token, 'secret', algorithms=['HS256'])
                user_id = payload.get('id')
                response["success"] = True
                response["message"] = "valid data"
                response["data"] = user_id

        except Exception as e:
            response = response

        return response

    # REMINDER API
    def set_reminder(self, that=None):
        response = {
            "success": False,
            "message": "something went wrong",
            "data": []
        }
        try:
            # reading the json data and converting it into python dictionary
            length = int(that.headers['Content-Length'])
            message = that.rfile.read(length)
            user_data = json.loads(message)

            # retriving token from headres to retrive id of the user who is logged in
            token = that.headers['token']
            if token:
                if "id" in user_data:
                    if user_data["id"] == 0:
                        response["success"] = False
                        response["message"] = "id can not be empty"
                        raise ValueError
                else:
                    response["message"] = "Give ID of the note which is to be remind"
                    raise KeyError

                if "reminder" in user_data:
                    if user_data["reminder"] == 0:
                        response['message'] = 'reminder can not be empty'
                        raise ValueError
                else:
                    response["message"] = "set date to remind"
                    raise KeyError

                if user_data["id"] is None:
                    response['message'] = 'give note id to set reminder'
                    raise ValueError

                if isinstance(user_data["id"], str):
                    response["success"] = False
                    response["message"] = "ID must be integer"
                    raise TypeError

                if len(user_data["reminder"]) > 0:
                    response["success"] = True
                    response["message"] = "valid data"
                    response["data"] = [user_data]
            else:
                response["success"] = False
                response["message"] = "You have to LOGIN first"

        except ValueError:
            response = response

        except KeyError:
            response = response

        except TypeError:
            response = response

        except Exception as e:
            response = response

        return response

    # LISTING REMINDER NOTE API
    def listing_reminder(self, that=None):
        response = {

            "success": False,
            "message": "something went wrong"
        }
        try:

            # getting token from headers
            token = that.headers['token']
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
            user_id = payload.get('id')

            # validating token
            if token is None:
                response["success"] = False
                response["message"] = "You have to LOGIN first"
            else:
                response["success"] = True
                response["message"] = "valid data"
                response["data"] = user_id

        except Exception as e:
            response = response

        return response

    # API for collaborating note
    def collaborator(self, that=None):
        response = {
            "success": False,
            "message": "Something went wrong",
            "data": []
        }
        try:

            # import pdb
            # pdb.set_trace()

            # getting token from headers
            token = that.headers['token']

            if token:
                payload = jwt.decode(token, 'secret', algorithms=['HS256'])
                user_id = payload.get('id')

                # reading the json data and converting it into python dictionary
                length = int(that.headers['Content-Length'])
                message = that.rfile.read(length)
                user_data = json.loads(message)

                # adding user id into user data dictionary
                user_data['user_id'] = user_id

                # validating user data
                res = validation_object.validating_user_data(**user_data)

                if res["success"]:
                    if user_data is not None:
                        response["success"] = True
                        response["data"] = [user_data]
            else:
                response["success"] = False
                response["message"] = "You have to LOGIN first"

        except Exception as e:
            response = response

        return response

