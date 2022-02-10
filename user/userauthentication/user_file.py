import logging
from user import *
from user.userauthentication.user_exceptions import UserNotFoundException


class UserFile:
    def __init__(self, src_file):
        self.src_file = src_file

    def get_user_details(self, username):
        with open(self.src_file) as user_list:
            for line in user_list:
                if username == line.split(',')[0]:
                    return line
        raise UserNotFoundException

    def get_user_object(self, username):
        try:
            user = self.get_user_details(username)
        except UserNotFoundException:
            logging.error("User not found")
        else:
            if user.split(',')[1] == "Free\n":
                return FreeUser(user.split(',')[0])
            else:
                return PremiumUser(user.split(',')[0])
