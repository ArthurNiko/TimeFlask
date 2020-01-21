FROM python
WORKDIR /app
RUN pip install flask
RUN pip install requests
COPY . .
ENTRYPOINT [ "python" ]
CMD [ "TimeFlask.py" ]