# Suppliers in Novosibirsk

The project contains of two scripts to help in generating static sites. The first one -  "static_site_generator.py" automaticly generates from jinja2 templates a site. And the second - "site_auto_reloader.py" runs the server and reloads the page in the browser on changes. Project contains an example of the generated site in "src" and initial templates in "templates".


## Example of the generated site:

### [romabiker.github.io](http://romabiker.github.io)


## Quickstart

Example of script launch on Linux, Python 3.5:

```
$ pip install -r requirements.txt # alternatively try pip3
$ python3 static_site_generator.py -s static favicon.ico
$ python3 site_auto_reloader.py -sd src


```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
