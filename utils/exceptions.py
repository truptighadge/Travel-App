from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework import status

def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)
    # If the default exception handler didn't return a response
    if response is None:
        return response
    # Mapping of status codes to error messages
    error_messages = {
        400: "Invalid data provided.",
        401: "Unauthorized access.",
        404: "Not found.",
        500: "Internal Server error."
    }
    error_message = error_messages.get(response.status_code, "An unexpected error occurred.")
    response.data={"error": error_message}
    response.data["status_code"] = response.status_code   
    return response

