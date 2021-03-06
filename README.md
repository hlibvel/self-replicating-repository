self-replicating-repository
===========================

Self replicating GitHub repository

Installation
------------

Clone the repository:

```bash
git clone https://github.com/hlibvel/self-replicating-repository.git
cd self-replicating-repository
```

Create a virtual environment:

```bash
mkvirtualenv srr --python=`which python3`
```

From this moment each time you work with the application switch to that environment:

```bash
workon ssr
```

Install requirements:

```bash
pip install -r requirements.txt
```

Running the application
---------------------
To start the app in dev mode:

```bash
python app.py
```

To run inside the gunicorn:

```bash
gunicorn app:app -b 0.0.0.0:8000
```

Deploy
-------

Add the remote heroku repository

```bash
heroku git:remote -a self-replicating-repository
```

Push code to the Heroku:

```bash
git push heroku master
```

If you are deploying to the fresh Heroku application enable the web worker:

```bash
heroku ps:scale web=1 -a self-replicating-repository
```
