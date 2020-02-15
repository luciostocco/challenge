
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

4. See the Challenge results. Run the tests (It is important to use the -s option so that you can see the prints of the results)

```sh
$ pytest test -s
```

### Additional information

* The requirement do not have clear information on how the input would be made. To facilitate the tests I decided to create a text files test_challenge_1.txt and test_challenge_2.txt, in which the input data was inserted exactly the same way as it is in the requirements.

* To see the script result, just run the unit tests. To do this, enter in the script directory and execute the command line: pytest test -s

* To make it more testable I decided not to print the result inside the ChallengeOne class. The challenge.analise_samples () method only returns a list of results. In the unit tests I print the result, as requested.

* Only the number of test cases contained in the first line of the input will be tested. If there is more data in the file, it will be ignored.



