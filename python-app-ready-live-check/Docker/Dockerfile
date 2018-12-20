FROM ubuntu

# Update
RUN apt-get update && apt-get install python  -y

# Bundle app source
COPY hello_from_hostname.py /python.py

EXPOSE  8000
CMD ["python", "/python.py", "-p 8000"]
