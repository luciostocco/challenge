from email.utils import parsedate_tz, mktime_tz


class InputData:
    # Class that represent Input Data

    def __init__(self, data: list, number_test_cases: int):
        self.data = data
        self.number_test_cases = number_test_cases

    def __repr__(self):
        return self.__class__.__name__


class ChallengeBase:

    def get_input_data(self, sample_filename: str) -> InputData:
        """
        Return sample input input_data from file
        :param sample_filename: Sample filename path
        :return: <number_test_cases>, <input_data_list>
        """
        try:
            with open(sample_filename) as data_file:
                input_data = [line.rstrip() for line in data_file]
        except IOError:
                raise Exception('Could not read the file')

        try:
            number_test_cases = int(input_data[0])
        except ValueError:
            raise Exception('Number of test-cases invalid')

        # delete first line from the input input_data
        del input_data[0]

        return InputData(
            input_data,
            number_test_cases,
        )


class ChallengeOne(ChallengeBase):

    YEAR_LIMIT = 3000

    def timestamp_absolute_difference(self, timestamp_1: str, timestamp_2: str) -> int:
        """
        Absolute difference (in seconds) between teh two timestamps.
        :param timestamp_1: Timestamp 1
        :param timestamp_2: Timestamp 2
        :return: seconds
        """
        try:
            parsedate_1 = parsedate_tz(timestamp_1)
            parsedate_2 = parsedate_tz(timestamp_2)

            if parsedate_1[0] >= self.YEAR_LIMIT or parsedate_2[0] >= self.YEAR_LIMIT:
                raise

            return mktime_tz(parsedate_1) - mktime_tz(parsedate_2)
        except Exception as e:
            raise Exception('Invalid timestamp')

    def analise_samples(self, sample_filename: str) -> list:
        """
        Analyze input file and print the result
        :param sample_filename: Sample filename path
        :return: List of results
        """
        input = self.get_input_data(sample_filename)

        # Iterate through the input input lines, getting pars of lines
        # for <number_test_cases> times and calculate the timestamp_absolute_difference
        results = []
        try:
            for item in range(0, (input.number_test_cases * 2) - 1, 2):
                results.append(
                    self.timestamp_absolute_difference(
                        timestamp_1=input.data[item],
                        timestamp_2=input.data[item + 1]
                    )
                )
        except IndexError:
            raise Exception('The number of samples (line 1) does not match '
                            'the amount of timestamp in the input file')

        return results

