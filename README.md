FROM python

WORKDIR /app/python_app

COPY . .

RUN pip install flask

EXPOSE 5000

CMD ["python","app.py"]

<!-- After cloning the repository 
Add the above code in Dockerfile inside that repository and run below command  -->

#  docker build . -t py_web_app (To create the docker image)
#  docker run -it -d -p 3010:5000 py_web_app (To create the container)
# go to localhost:3010