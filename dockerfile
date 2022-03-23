FROM nginx
RUN apt update && apt install python3
WORKDIR /
COPY . .
RUN python3 -m unittest test_sitecreator.py
RUN python3 sitecreator.py
MV index.html /usr/share/nginx/html
