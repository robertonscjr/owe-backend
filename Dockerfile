FROM python3.7
COPY src /src
COPY requirements.txt /
RUN pip3 install -r /requirements.txt
ENTRYPOINT []
