FROM python

WORKDIR /app/python_app

COPY . .

RUN pip install flask

EXPOSE 5000

CMD ["python","app.py"]

# After cloning the repository 
# Add the above code in Dockerfile inside that repository and run below command
# Now execute the below commands
# docker build . -t py_web_app (To create the docker image)
# docker run -it -d -p 3010:5000 py_web_app (To create the container)
# go to localhost:3010


# OR create a Dockerfile in your local machine and add the following command without clonning the application

FROM python

RUN apt update && apt install -y git

RUN git clone https://github.com/Anubhav-04/python-flask-application /app

WORKDIR /app

RUN pip install --no-cache-dir || pip install flask

RUN ls -l

EXPOSE 5000

CMD ["python","app.py"]

# Now execute the below commands

# docker build . -t application 

# docker run -it -p 3015:5000 -d application

# go to localhost:3015