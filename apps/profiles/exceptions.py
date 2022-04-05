from rest_framework.exceptions import ApiException


class ProfileNotFound(ApiException):
    status_code = 404
    default_detail = "The requested profile does not exist"

class NotYourProfile(ApiException):
    status_code = 403
    default_detail = "You cannot edit a profile that doesn't belog to you"