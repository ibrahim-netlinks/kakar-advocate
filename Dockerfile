FROM odoo:10
MAINTAINER NETLINKS (http://netlinks.af)

USER root

WORKDIR /var/lib/odoo
ADD requirements.txt ./requirements.txt

RUN pip install -r ./requirements.txt

USER odoo

RUN echo 'MOFA HR dependencies installed.'