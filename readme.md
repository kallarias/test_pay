# Django examples with stripe

A Django project with example accept a payment.

The current list of apps include:

1. app_pay
An app to demonstrate using a custom user model in Django.

2. products
An app to receive user payments through Stripe.

## Running this project

* start by installing the requirements:

```
pip install --upgrade pip
pip install -r requirements.txt
```

* the following environment variables need to be exported prior to use:

```
export SECRET_KEY='your django secret key'
export STRIPE_PUBLIC_KEY_TEST='pk_test_12345...'
export STRIPE_SECRET_KEY_TEST='sk_test_12345...'
```


* after that you can run the following:

```
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

* you can create a new product through the admin panel