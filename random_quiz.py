# import random

# capitals = {
# 'Alabama': 'Montgomery', 
# 'Alaska': 'Juneau', 
# 'Arizona': 'Phoenix', 
# 'Arkansas': 'Little Rock',
# 'California': 'Sacramento',
# 'Colorado': 'Denver', 
# 'Connecticut': 'Hartford',
#  'Delaware': 'Dover',
#   'Florida': 'Tallahassee', 
# 'Georgia': 'Atlanta',
#  'Hawaii': 'Honolulu',
#   'Idaho': 'Boise',
#    'Illinois':'Springfield',
#     'Indiana': 'Indianapolis', 
#     'Iowa': 'Des Moines', 
#     'Kansas': 'Topeka',
#     'Kentucky': 'Frankfort',
#      'Louisiana': 'Baton Rouge', 
#      'Maine': 'Augusta',
#     'Maryland': 'Annapolis',
#      'Massachusetts': 'Boston',
#       'Michigan': 'Lansing',
#        'Minnesota': 'Saint Paul',
#         'Mississippi': 'Jackson',
#          'Missouri': 'Jefferson City',
#           'Montana': 'Helena', 
#           'Nebraska': 'Lincoln',
#            'Nevada': 'Carson City', 
#            'New Hampshire': 'Concord',
#             'New Jersey': 'Trenton', 
#             'New Mexico': 'Santa Fe', 
#             'New York': 'Albany', 
#             'North Carolina': 'Raleigh', 
# 'North Dakota': 'Bismarck', 
# 'Ohio': 'Columbus',
#  'Oklahoma': 'Oklahoma City', 
# 'Oregon': 'Salem',
#  'Pennsylvania': 'Harrisburg', 
#  'Rhode Island': 'Providence', 
# 'South Carolina': 'Columbia',
#  'South Dakota': 'Pierre', 
#  'Tennessee': 'Nashville', 
#  'Texas': 'Austin', 
#  'Utah': 'Salt Lake City',
#   'Vermont': 'Montpelier',
#    'Virginia': 'Richmond',
#     'Washington': 'Olympia', 
#     'West Virginia': 'Charleston', 
#     'Wisconsin': 'Madison', 
#     'Wyoming': 'Cheyenne'}

# for quizNum in range(5):
#     increase = quizNum + 1
#     quizFile = open(f'question{increase}.txt', 'w')
#     answer_File = open(f'answer{increase}.txt', 'w')
#     quizFile.write('Date: \n\n' + 'period: \n\n')
#     quizFile.write((" " * 20) + f"State Capitals Quiz (Form  {increase} )")
#     quizFile.write('\n\n')
#     states = list(capitals.keys())
#     random.shuffle(states)
    
#     for question_Num in range(50):
#         inc = question_Num + 1
#         correct_answer = capitals[states[question_Num]]
#         wrong_answer = list(capitals.values())
#         wrong_answer = random.sample(wrong_answer, 3)
#         options = wrong_answer + [correct_answer]
#         random.shuffle(options)
#         quizFile.write(f'{inc}. What is the capital of {states[question_Num]}\n\n')
        
#         for i in range(4):
#             pos = 'ABCD'[i]
#             quizFile.write(f' {pos}. {options[i]}\n' )
#             quizFile.write("\n")

# print(capitals['Washington'])
print(django.get_version())
print('hello')