FROM mcr.microsoft.com/playwright:focal

WORKDIR /home/pwuser/webscanner

COPY . /home/pwuser/webscanner/

RUN pip install poetry

RUN poetry install

ENV PYTHONPATH /home/pwuser/webscanner

RUN poetry run python ./scanner/spider.py

CMD ["cat", "./scan_data.json"]

