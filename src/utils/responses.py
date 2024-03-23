from flask import make_response, jsonify

'''
CAVEATS: 
200 Ok: Standard rsponse to HTTP requests
201 Created: Request was fulfilled and a new resource has been created 
204 No Content: Successful request and no data has been returned
400 Bad Request: Server can't process the request due to a client error
403 Not Authorized: Valid request from a non-authorized client
404 Not Found: The requested resource doesn't exist on the server
422 Unprocessable Entity: Request can't be processed due to semantic error(s)
500 Internal Server Error: Generic error
'''

SUCCESS_200 = {
    'http_code': 200,
    'message': 'Successful operation.',
}

SUCCESS_201 = {
    'http_code': 201,
    'message': 'Successful operation, Entity Created.',
}

SUCCESS_204 = {
    'http_code': 204,
    'message': 'Successful Operation.',
}

BAD_REQUEST_400 = {
    'http_code': 400, 
    'code': 'badRequest',
    'message': 'Bad request.'
}

UNAUTHORIZED_403 = {
    'http code': 403,
    'code': 'notAuthorized',
    'message': 'Not authorized to execute this operation.'
}

SERVER_ERROR_404 = {
    'http code': 404,
    'code': 'serverError',
    'message': 'Server Error.'
}

INVALID_INPUT_422 = {
    'http_code': 422,
    'code': 'invalidInput',
    'message': 'Invalid input.'
}

MISSING_PARAMETERS_422 = {
    'http_code': 422,
    'code': 'missingParams',
    'message': 'Missing Parameters.'
}

INVALID_FIELD_NAME_SENT_422 = {
    'http_code': 422,
    'code': 'invalidField', 
    'message': 'Invalid field(s) found.'
}

SERVER_ERROR_500 = {
    'http code': 500,
    'code': 'serverError',
    'message': 'Internal Server Error: Generic Error.'
}

# Create a response fn 
def response_with(response, value=None, message=None, error=None, headers={}, pagination=None):
    result = {} 
    if value is not None:
        result.update(value)
    
    if response.get('message', None) is not None:
        result.update({'message': response['message']})

    result.update({'message': response['message']})
    
    if error is not None: 
        result.update({'errors': error})

    if pagination is not None:
        result.update({'pagination': pagination})
    
    headers.update({'Access-Control-Allow-Origin': '*'})
    headers.update({'server': 'user REST API'})
    
    return make_response(jsonify(result), response['http_code'], headers)
