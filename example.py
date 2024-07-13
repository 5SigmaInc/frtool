from frtool.apiclient import ApiClient

apiclient = ApiClient(api_key="demokey")
questions = apiclient.collect_questions()
