# Simple URL Shortener

Simple URL Shortener based on bijective numeration to convert positive integer to short strings

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

First of all you have to install vagrant and virtual box. Download you copies here:

[Vagrant](https://www.vagrantup.com/downloads.html)
[VirtualBox](https://www.virtualbox.org/wiki/Downloads)

After that, clone this repo:

```
git clone git@github.com:archix/Simple-URL-Shortener.git
```

### Installing

Once you've installed vagrant and cloned repo cd to project and run next command:

```
vagrant up
```

This should automatically setup whole project (download and run Ubuntu 16.04 on vm, and install all needed packages for running project)

To connect to vm just type

```
vagrant ssh
```

Once you're in, to run API type next commands:

enter dir

```
cd /home/ubuntu/app
```

activate virtual environment

```
source .env/bin/activate
```

actually run API

```
python app.py
```

You can check if app's running by visiting next link (since port 5000 is forwarded it's easy to access via localhost):

[http://localhost:5000/](http://localhost:5000/)

Open second terminal and try to create short url via cURL:

```
curl -X POST \
  http://localhost:5000/shorten/ \
  -H 'cache-control: no-cache' \
  -H 'content-type: application/json' \
  -d '{
        "url": "http://www.google.com"
        }'
```

You should get short link in response that looks like http://localhost/3

*To solve ultra short first urls, since the logic is to convert IDs, we could set primary key to go from some larger number*

To test if it works try next command in the terminalL

```
curl http://localhost:5000/3 -v
```

## Docs

TBD

## Running the tests

There're just basic unittests which can be run by (from project root with virtual env activated):
```
python shortener/tests.py
```

### Break down into end to end tests

TBD

### And coding style tests

TBD

## Deployment

TBD

## Built With

* [Vagrant](https://www.vagrantup.com/)
* [PostgreSQL](https://www.postgresql.org/)
* [Flask](http://flask.pocoo.org/)
* [SqlAlchemy](https://www.sqlalchemy.org/)

## Contributing

TBD

## Versioning

TBD

## Authors

* **Igor Dakić**  - [Archix](https://github.com/archix)


## License

This project is licensed under the GPL v3.0 License - see the [LICENSE.md](LICENSE.md) file for details