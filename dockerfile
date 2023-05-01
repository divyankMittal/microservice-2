FROM python
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r /code/requirements.txt
COPY . /code/
EXPOSE 80
ENTRYPOINT ["python", "app2.py"]
