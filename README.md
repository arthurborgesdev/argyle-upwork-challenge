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
- Flake8
- Mypy


To get a local copy up and running follow these simple example steps.

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
TBD
### Install

- Install `pyenv` using homebrew or other mecanism using [these](https://github.com/pyenv/pyenv) instructions.
- Install `poetry`.
- Run `poetry install` to install packages/libraries


### Usage

- Run `poetry run python ./spider/spider.py`

### Run tests
TBD

### Run linters/type checkers

- Run `poetry run flake8`
- Run `poetry run mypy ./spider/spider.py`

### Deployment
TBD


## Author

👤 **Arthur Borges**

- GitHub: [@arthurborgesdev](https://github.com/arthurborgesdev)
- Twitter: [@arthurmoises](https://twitter.com/arthurmoises)
- LinkedIn: [Arthur Borges](https://linkedin.com/in/arthurmoises)

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

Feel free to check the [issues page](https://github.com/arthurborgesdev/argyle-upwork-challenge/issues).

## Show your support

Give a ⭐️ if you like this project!

## Acknowledgments

- Argyle for providing such a fun and 'challenging challenge'!
- All the libraries used by Argyle which inspired me into learning more about Web Scanning and Python
- Youtube videos and countless materials searched on Google to help me assemble a working Scraper/Scanner