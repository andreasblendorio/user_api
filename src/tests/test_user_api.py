import requests

ENDPOINT = "http://localhost:5000"

def test_can_call_endpoint():
    response = requests.get(ENDPOINT)
    assert response.status_code == 200

# Create test
def test_can_create_user():
    payload = new_user_payload()
    create_user_response = create_user(payload)
    assert create_user_response.status_code == 200

    data = create_user_response.json()
    print(data)

    user_id = data['user']['user_id']
    get_user_response = get_user(user_id)

    assert get_user_response.status_code == 200
    get_user_data = get_user_response.json()
    assert get_user_data['user_id'] == payload['user_id']

    # Update test: create + update + get changes
    def test_can_update_user():
        payload = new_user_payload
        create_user_response = create_user(payload)
        user_id = create_user_response.json()['user']['user_id']

        new_payload = new_user_payload()

    def create_user(payload):
        return requests.post(ENDPOINT + '/user', json=payload)
    
    def get_user(user_id):
        return requests.get(ENDPOINT + f"/user/{user_id}")
    
    def new_user_payload():
        return {
            "user_id": 1,
            "first_name": "test_name",
            "last_name": "tes_lastname",
            "username": "test_username",
            "user_password": "Ttest_password",
            "email": "test_email@email.com",
            "telephone": "1234567890",
            "insertion_date": "2024-03-21T12:00:00", 
            "update_date": "2024-03-21T12:00:00", 
            "user_status": "true" 
        }
        