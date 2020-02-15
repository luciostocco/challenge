from unittest import TestCase
from unittest.mock import patch
from challenge_1 import ChallengeOne, ChallengeBase, InputData
from challenge_2 import ChallengeTwo


class TestChallenges(TestCase):

    challenge_1_mock_data_input = ['Sun 10 May 2015 13:54:36 -0700',
                                   'Sun 10 May 2015 13:54:36 -0000',
                                   'Sat 02 May 2015 19:54:36 +0530',
                                   'Fri 01 May 2015 13:54:36 -0000']

    challenge_2_mock_data_input = ['lucio@example.com',
                                   'john-doe23@example.com',
                                   'jane_35@example.com',
                                   'joe%bloggs@example.com']

    @patch.object(ChallengeBase, 'get_input_data', return_value=InputData(challenge_1_mock_data_input, 2))
    def test_challenge_1(self, mock1):
        """
        Test Python challenge 1
        """

        challenge = ChallengeOne()
        results = challenge.analise_samples('challenge_1_input.txt')

        self.assertEqual(results, [25200, 88200])

    @patch.object(ChallengeBase, 'get_input_data', return_value=InputData(challenge_2_mock_data_input, 4))
    def test_challenge_2(self, mock1):
        """
        Test Python challenge 2
        """

        challenge = ChallengeTwo()
        results = challenge.generate_emails_list('challenge_2_input.txt')

        self.assertEqual(results,  ['jane_35@example.com', 'john-doe23@example.com', 'lucio@example.com'])

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


