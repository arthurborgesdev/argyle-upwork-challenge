FROM mcr.microsoft.com/playwright:focal

RUN mkdir -p /home/pwuser/webscanner

COPY . /home/pwuser/webscanner

WORKDIR /home/pwuser/webscanner

RUN pip install poetry

RUN poetry install

ENV PYTHONPATH /webscanner

RUN poetry run python ./scanner/spider.py

CMD ["cat", "./scan_data.json"]

