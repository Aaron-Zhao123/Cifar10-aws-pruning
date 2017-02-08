from tensorflow/tensorflow:latest
MAINTAINER Aaron Zhao (yaz21@cam.ac.uk)

WORKDIR /root
COPY cache.py /root/cache.py
COPY cifar10.py /root/cifar10.py
COPY dataset.py /root/dataset.py
COPY download.py /root/download.py
COPY train.py /root/train.py
COPY run.py /root/run.py
COPY 20170206.pkl /root/20170206.pkl
COPY mask.pkl /root/mask.pkl



CMD ["python", "/root/run.py"]
