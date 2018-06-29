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


Start the application:
```bash
python app.py
```