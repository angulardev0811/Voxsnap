FROM robd003/python3-node12:latest
LABEL Description="VoxSnap Django & Node" Maintainer="Robert Palmer <rob@voxsnap.com>"

ENV PYTHONUNBUFFERED 1

WORKDIR /opt/voxsnap-v2

# copy project relevant files into container
COPY Pipfile /opt/voxsnap-v2

# install project specific requirements
RUN pip install -U pipenv setuptools virtualenv virtualenv-clone certifi
RUN pipenv install --three

COPY . /opt/voxsnap-v2
RUN cd frontend && npm --unsafe-perm install

CMD ./wait-for-it.sh -t 60 -h crate -p 5432 -- pipenv run python manage.py runserver 0.0.0.0:8000
