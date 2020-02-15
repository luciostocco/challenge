
## Python Technical challenge


## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. 

### Prerequisites

* Python 3.7.6

### Installing

1. Clone the repository

```sh
$ git clone https://github.com/luciostocco/challenge.git
```

2. Go to project folder

```sh
$ cd challenge
```

3. Install dependencies

```sh
$ pip install -r requirements.txt
```

4. See the Challenge results. If you want to test with different input data just update challenge_1_input.txt and challenge_2_input.txt

```sh
$ python app.py
```

5. Run Unit Tests

```sh
$ pytest test
```

### Additional information

* The requirements do not have clear information about the input. To facilitate the tests I decided to create a text files test_challenge_1.txt and test_challenge_2.txt, in which the input data was inserted exactly the same way as it is in the requirements.
* See the Challenge results. If you want to test with different input data just update challenge_1_input.txt and challenge_2_input.txt
* To make it more testable I decided not to print the result inside the ChallengeOne class. The challenge.analise_samples () method only returns a list of results. In the unit tests I printed the result, as requested.
* Also to facilitate mocking the input file in tests, ChallengeBase.get_input_data() class  returns an object
* The two Challenges inherit ChallengeBase class as both uses get_input_data () method.
* Only the number of test cases contained in the first line of the input will be tested. If there is more data in the file, it will be ignored.
* Unit tests are not covering 100% of the code. In a real situation it would be necessary to create specific unit tests for each method and for each constraints and validations.

