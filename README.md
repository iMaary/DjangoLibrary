## Desafio Biblioteca Literária

### Installation

```bash
git clone https://github.com/iMaary/DjangoLibrary.git
cd DjangoLibrary
```

### Environment Prepare

```bash
python -m venv venv
source venv/bin/activate  # MacOS/Linux
venv\Scripts\activate     # Windows
```

##### Install Requirements

```bash
pip install -r requirements.txt
```

### Configure & Populate Database

```bash
python manage.py migrate
```

### Running Server

```bash
python manage.py runserver
```
Access: http://127.0.0.1:8000/

### Testing

##### Run tests

```bash
coverage run manage.py test portal/tests
```

##### Coverage Report

```bash
coverage report -m
```
