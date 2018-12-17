FROM ubuntu

# Update
RUN apt-get update && apt-get install python python-pip -y

# Install app dependencies
RUN pip install flask

# Bundle app source
COPY simpleapp.py /src/simpleapp.py

EXPOSE  8000
CMD ["python", "/src/simpleapp.py", "-p 8000"]