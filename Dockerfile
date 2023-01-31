FROM python:slim 

COPY ./requirements /requirements
RUN pip install -r /requirements/production.txt 

COPY bot bot 
COPY run.py ./

CMD ["python3", "run.py"]