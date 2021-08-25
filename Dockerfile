FROM docker.io/tensorflow/tensorflow
WORKDIR /root/ws/ml
RUN apt autoremove && pip3 install flask pillow && mkdir uploads
#inside src/ kept app.py,covidModel.h5,static and template
COPY src/ . 
EXPOSE 80
ENTRYPOINT ["python3","app.py"]


