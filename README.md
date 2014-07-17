verse
=====

Django prototype of Verse, a publicly viewable system for distributing and delegating requests across social networks. Very preliminary.

Users can make requests of each other, as well as forward those requests or split them into subrequests to send to other participants. The chain of requests can be viewed by each participant, allowing for distant participants to directly contact each other. See [here](https://sites.google.com/site/requestverse/home/text) for more specific use cases.

Collaborators welcome!

## Developing verse

### Prerequisites
- python (Core development is on 2.7, but may work on older pythons.)
- pip
- virtualenv

### Setup
- Clone the repository
- Set up a virtual Python environment in the project's root directory:

```
cd path/to/verse/
virtualenv env
```
- Install the requirements

```
source env/bin/activate
pip install -r requirements.txt
```
- Set up the database

```
python manage.py syncdb
python manage.py migrate
```

### Running the test server
- If you haven't already activated your virtual environment in this session (you'll see a little "(env)" before your shell prompt), do that:

`env/bin/activate`
- Run the Django test server

`python manage.py runserver`
