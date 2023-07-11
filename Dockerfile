FROM continuumio/anaconda3:2023.03-1
COPY . /code
WORKDIR /code

CMD ["python", "./main.py"]