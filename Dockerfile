FROM python:3-alpine

ENV STRESS_MINS=1
ENV CORE_ALLOC=-1


WORKDIR /opt/app

COPY . .

CMD [ "python3", "stress.py" ]