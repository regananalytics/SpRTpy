FROM python:3.9-slim

COPY requirements.txt /
RUN pip install -r requirements.txt

RUN mkdir /src
RUN mkdir /dev/uinput

COPY . /src
WORKDIR /src
RUN pip install ./vsdbg

CMD python keyboard_notepad.py