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