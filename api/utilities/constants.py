"Module for storing constants"

INVALID_TOKEN_MSG = dict(
    message="Authorization failed due to an Invalid token."
)
EXPIRED_TOKEN_MSG = dict(
    message="Token expired. Please login to get a new token"
)
SIGNATURE_ERROR = dict(
    message="Cannot verify the signature of the token provided as \
    it was signed by a non matching private key"
)
SERVER_ERROR_MESSAGE = dict(
    message="Authorization failed. Please contact support."
)
NO_BEARER_MSG = dict(
    message="Bad request. The token should begin with the word 'Bearer'."
)
NO_TOKEN_MSG = dict(
    message="Bad request. Header does not contain an authorization token."
)

UTF_8 = 'utf-8'

jwt_errors = {
    'INVALID_TOKEN_MSG': INVALID_TOKEN_MSG,
    'EXPIRED_TOKEN_MSG': EXPIRED_TOKEN_MSG,
    'SIGNATURE_ERROR': SIGNATURE_ERROR,
    'SERVER_ERROR_MESSAGE': SERVER_ERROR_MESSAGE,
    'NO_BEARER_MSG': NO_BEARER_MSG,
    'NO_TOKEN_MSG': NO_TOKEN_MSG,
}