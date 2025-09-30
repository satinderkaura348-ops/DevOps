# Base OS
FROM python:3.12-slim

#working directory
WORKDIR /app

#copy source code
COPY . .

#no need to expose port, as not mentioned

#run the libraries command
RUN pip install psutil && pip install py-notifier

#cmd to continuosly running
CMD [ "python", "battery.py" ]
