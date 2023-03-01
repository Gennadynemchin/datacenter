# datacenter

The first Django project which show the simplest MVC model.

### How to install

```
git clone git@github.com:Gennadynemchin/datacenter.git
```

```
pip install -r requirements.txt
```

Use example.env as a draft and fill all of the requested
setiings to connect database:

```
ENGINE=<Database engine>
HOST=<Addres of database>
PORT=<Requested port>
NAME=<DB name>
USER=<Username>
PASSWORD=<DB password>
SECRET_KEY=<SECRET_KEY>
DEBUG_STATUS=False
```
Then save and rename to .env

### How to start

Run in a terminal:

```
python manage.py runserver
```

The code is written for educational purposes https://dvmn.org