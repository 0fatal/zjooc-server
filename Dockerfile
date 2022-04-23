FROM ubuntu:18.04

ENV PYTHONUNBUFFERED=1

RUN sed -i s@/archive.ubuntu.com/@/mirrors.aliyun.com/@g /etc/apt/sources.list
#更换apt下载源
RUN sed -i s@/security.ubuntu.com/@/mirrors.aliyun.com/@g /etc/apt/sources.list
#更换apt下载源

RUN apt-get update -y && \
    apt-get install -y python3-pip python3-dev nodejs

COPY ./requirements.txt /requirements.txt

WORKDIR /
RUN pip3 install --upgrade pip
RUN pip install -r requirements.txt

COPY . /
CMD ["gunicorn", "app:app", "-c", "./gunicorn.conf.py"]
