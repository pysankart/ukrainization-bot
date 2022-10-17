FROM python:slim 

COPY requirements.txt ./
RUN pip install -r requirements.txt 

COPY bot bot 
COPY run.py boot.sh ./

CMD ./boot.sh