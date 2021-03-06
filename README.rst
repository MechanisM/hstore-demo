==============
Schemaless SQL
==============

* Lightning talk given at DjangoCon.EU 2012
* http://bit.ly/django-hstore


Setup
=====

::

    git clone https://github.com/craigkerstiens/hstore-demo.git
    heroku create -s cedar
    git push heroku master
    heroku addons:remove shared-database
    heroku addons:add heroku-postgresql:dev
    heroku pg:promote HEROKU_POSTGRESQL_COLORGOESHEERE

Then connect to your database with 'heroku pg:psql' and create the hstore
extension

::
    
    create extension hstore;

Finally sync your database

::

    heroku run python manage.py syncdb


Example Uses
============

::

    from app.models import *
    django_pony = Product.objects.create(name='Django Pony', data={'rating': '5'})
    pink_pony = Product.objects.create(name='Pony', data={'color': 'pink', 'rating': '4'})
 
    colored_ponies = Product.objects.filter(data__contains='color')
    print colored_ponies[0]
    print colored_ponies[0].data
    print colored_ponies[0].data['color']

    favorite_ponies = Product.objects.filter(data__contains={'rating': '5'})
    print colored_ponies[0]

    all_ponies = Product.objects.all()
    for pony in all_ponies:
        print pony
        print pony.data