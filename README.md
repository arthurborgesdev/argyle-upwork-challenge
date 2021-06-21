# Upwork web scanner/scrapper for Argyle challenge

> The main objective of this project is to log into Upwork website using the credentials provided and extract data in JSON format.

Other objectives involve extracting more data and handling erros, making project maintainable and testable, etc.

## Built With

- Git
- GitFlow
- Github
- VSCode
- Python3
- Poetry
- Pyenv
- python-dotenv
- BeautifulSoup4
- Pytest
- Playwright
- Pydantic
- Flake8
- Mypy
- lxml
- Pytest-Playwright


To get a local copy up and running follow these simple example steps:

### Prerequisites

- Create a `.env` in the root of the project containing the following credentials:
  ```
  PORTAL_LINK=https://www.upwork.com/ab/account-security/login
  USERNAME=...
  PASSWORD=...
  SECRET=...
  ```
  (Change the ... with your own credentials)

- Select the correct python interpreter (with virtual environment):

  Press `Ctrl+Shift+P` on VSCode

  Select the desired python environment

  Now you can run the scripts

### Setup

- Go to a Terminal and clone the repository: `git clone git@github.com:arthurborgesdev/argyle-upwork-challenge.git`
- Make sure you are on the correct branch (`main`, by the time of the project submission, or `development` for the most stable recent one before project submission)


### Install

- Install `pyenv` using homebrew or other mecanism using [these](https://github.com/pyenv/pyenv) instructions
- Install `poetry`
- Run `poetry install` to install packages/libraries


### Usage

- Run `poetry run python ./scanner/spider.py`


### Run tests

Add the following libraries as dev dependencies:

- run `poetry add pytest --dev`
- run `poetry add pytest-playwright --dev`

Run tests with the command:

- `poetry run pytest`


### Run linters/type checkers

- Run `poetry run flake8`
- Run `poetry run mypy ./scanner`


### Docker image build

1 - Run `docker image build --tag scanner_spider:0.1.0 .`

2 - Run `docker container run --name scanner_spider scanner_spider:0.1.0`

3 - Run `docker container ls --all` to make sure the container has been created

The step 2 will already run and output the contents of the scanned data


### Deployment

TBD


### Performance improvements and considerations

- Need to change complete scanner architecture now? 

  - To puppeteer? No:
    https://blog.checklyhq.com/puppeteer-vs-selenium-vs-playwright-speed-comparison/

  - To a custom solution from scratch?
    Maybe (need more studies and a MVP from scratch using httpx, for example)

- Other optimizations involved changing html-parser to lxml in BeautifulSoup which improved performance.
- Attempted to use cChardet to improve performance of BeautifulSoup by 10x as stated [here](https://thehftguy.com/2020/07/28/making-beautifulsoup-parsing-10-times-faster/) but it does now works in Pyenv... maybe it's a good fit for a Docker image using only pip, though.

### Further documentation

Please consult the current [pull requests!](https://github.com/arthurborgesdev/argyle-upwork-challenge/pulls)


## Author

👤 **Arthur Borges**

- GitHub: [@arthurborgesdev](https://github.com/arthurborgesdev)
- Twitter: [@arthurmoises](https://twitter.com/arthurmoises)
- LinkedIn: [Arthur Borges](https://linkedin.com/in/arthurmoises)


## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

Feel free to check the [issues page](https://github.com/arthurborgesdev/argyle-upwork-challenge/issues)


## Show your support

Give a ⭐️ if you like this project!


## Acknowledgments

- Argyle for providing such a fun and 'challenging challenge'!
- All the libraries used by Argyle which inspired me into learning more about Web Scanning and Python
- Youtube videos and countless materials searched on Google to help me assemble a working Scraper/Scanner