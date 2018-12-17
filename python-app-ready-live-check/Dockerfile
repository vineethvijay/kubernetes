FROM ubuntu

# Update
RUN apt-get update && apt-get install python  -y

# Bundle app source
COPY hostname.py /hostname.py

EXPOSE  8000
CMD ["python", "/hostname.py", "-p 8000"]