from frtool.apiclient import ApiClient

apiclient = ApiClient(api_key="demokey")
questions = apiclient.collect_questions()
answers = apiclient.generate_mock_answers(questions)
scores = apiclient.calculate_score(answers)
if scores['index_score_result']>0:
  print(f'Your score is {scores['index_score']} it is {scores['index_score_result']}% higher than average score {scores['index_score_value_to_compare']}')
else:
  print(
    f'Your score is {scores['index_score']} it is {abs(scores['index_score_result'])}% lower than average score {scores['index_score_value_to_compare']}')