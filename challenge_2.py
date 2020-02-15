import re
from challenge_1 import ChallengeBase


class ChallengeTwo(ChallengeBase):

    EMAIL_VALIDATION_REGEX = r'(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]{3}$)'

    def is_valid_email(self, email: str) -> bool:
        """
        Test if email is valid or not
        :param email: Email
        :return: Boolean
        """
        if re.search(self.EMAIL_VALIDATION_REGEX, email):
            return True
        else:
            return False

    def generate_emails_list(self, sample_filename: str) -> list:
        """
        Generate email list
        :param sample_filename: Sample file name
        :return: list of valid emails
        """
        input = self.get_input_data(sample_filename)

        number_test_cases = input.number_test_cases if len(input.data) > input.number_test_cases else len(input.data)

        results = []
        try:
            for item in range(0, number_test_cases):
                if self.is_valid_email(input.data[item]):
                    results.append(input.data[item])
        except IndexError:
            raise Exception('The number of samples (line 1) does not match '
                            'the amount of emails in the input file')
        results.sort()

        return results
