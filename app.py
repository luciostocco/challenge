from challenge_1 import ChallengeOne
from challenge_2 import ChallengeTwo

challenge = ChallengeOne()
results = challenge.analise_samples('challenge_1_input.txt')

print('\n\nChallenge 1')
print('================')
print(*results, sep="\n")

challenge = ChallengeTwo()
results = challenge.generate_emails_list('challenge_2_input.txt')

print('\n\nChallenge 2')
print('================')
print(results)

