from unittest import TestCase
from challenge_1 import ChallengeOne
from challenge_2 import ChallengeTwo


class TestChallenges(TestCase):

    def test_challenge_1(self):
        """
        Test Python challenge 1
        """

        challenge = ChallengeOne()
        results = challenge.analise_samples('challenge_1_input.txt')

        self.assertEqual(results, [25200, 88200])

        # Print the result
        print('\n\nChallenge 1')
        print('================')
        print(*results, sep="\n")

    def test_challenge_2(self):
        """
        Test Python challenge 2
        """

        challenge = ChallengeTwo()
        results = challenge.generate_emails_list('challenge_2_input.txt')

        # Print the result
        print('\n\nChallenge 2')
        print('================')
        print(results)

        self.assertEqual(results,  ['clara@example.com', 'jane_35@example.com', 'john-doe23@example.com'])

    def test_is_valid_email(self):
        """
        Test is_valid_email
        """

        challenge = ChallengeTwo()
        self.assertEqual(True, challenge.is_valid_email('clara@example.com'))
        self.assertEqual(True, challenge.is_valid_email('john-doe23@example.com'))
        self.assertEqual(True, challenge.is_valid_email('jane_35@example.com'))
        self.assertEqual(True, challenge.is_valid_email('joe@example22.com'))

        self.assertEqual(False, challenge.is_valid_email('joe@example'))
        self.assertEqual(False, challenge.is_valid_email('joe***loggs@example.com'))
        self.assertEqual(False, challenge.is_valid_email('joe@example_x.com'))
        self.assertEqual(False, challenge.is_valid_email('joe@example.xxxx'))


