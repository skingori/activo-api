""" Module holding all error messages, facilitates DRY principle"""

# Group errors by field type, generic messages go under field_{}
serialization_errors = {
    'email_syntax': '{0} is not a valid email address',
    'email_exists': '{0} is already registered',
    'email_length': 'Email must be at least 6 characters',
    'field_required': 'This field is required',
    'field_length': 'Field must be at least {0} characters',
    'json_invalid': 'Invalid JSON input provided',
    'string_characters': 'Field must start and end with a letter, only contain letters, non-consecutive fullstops, hyphens, spaces and apostrophes', #noqa
    'string_length': 'Field must be {0} characters or less'
}
jwt_errors = {
    'INVALID_TOKEN_MSG': "Authorization failed due to an Invalid token.",
    'EXPIRED_TOKEN_MSG': "Token expired. Please login to get a new token",
    'SIGNATURE_ERROR': "Cannot verify the signature of the token provided as \
    it was signed by a non matching private key",
    'SERVER_ERROR_MESSAGE': "Authorization failed. Please contact support.",
    'NO_BEARER_MSG': "Bad request. The token should begin with the word 'Bearer'.", 
    'NO_TOKEN_MSG': "Bad request. Header does not contain an authorization token.",
}
database_errors = {
    'model_delete_children': 'Delete failed. The instance has relationship(s) with {0} not deleted.' #noqa
}
