FROM python:3.6
MAINTAINER Mubin Shaikh
COPY ./home/mubin/find_company_name_by_mac_address.py /opt/
COPY ./home/mubin/requirements.txt /opt
WORKDIR /opt
RUN pip3 --no-cache-dir install -r requirements.txt
EXPOSE 5000
CMD ["python", "find_company_name_by_mac_address.py", "44:38:39:ff:ef:57"]
