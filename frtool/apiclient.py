import requests


class ApiClient:
    def __init__(self, api_key="demokey", access_key="", base_url="https://7km5vhnbvd.execute-api.ca-central-1.amazonaws.com"):
        self.api_key = api_key
        self.base_url = base_url
        self.access_key = access_key

    def collect_questions(self):
        endpoint = f"{self.base_url}/questions"
        headers = {
            "Content-Type": "application/json"
        }
        data = {
            "api_key": self.api_key
        }
        try:
            response = requests.post(endpoint, json=data, headers=headers)
            response.raise_for_status()  # Raise an HTTPError for bad responses
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            return None

# Example usage
# api_key = "your_api_key_here"
# api_wrapper = ApiGatewayWrapper(api_key)
# questions = api_wrapper.collect_questions()
#
# if questions is not None:
#     print("Questions collected successfully:")
#     print(questions)
# else:
#     print("Failed to collect questions.")