FROM docker.io/tensorflow/tensorflow
LABEL   description="Using tensorflow base image build a Xray model that predict wether the person iS COVID Positive or Negative \
        Python Packages= flask and pillow"
WORKDIR /root/ws/ml
RUN apt autoremove && pip3 install flask pillow && mkdir uploads
#inside src/ kept app.py,covidModel.h5,static and template
COPY src/ . 
EXPOSE 80
ENTRYPOINT ["python3"]
CMD ["-m","flask","run","--host=0.0.0.0","--port=80"]

