Flask-PyElasticSearch
=====================

Integrates ElasticSearch with Flask using the [pyelasticsearch][]
python package.

[pyelasticsearch]: https://pyelasticsearch.readthedocs.org/

Installation
------------

Flask-PyElasticSearch is not yet pip installable. You will be able to do this in future:

    pip install Flask-PyElasticSearch

You can install for now like this:

    pip install https://github.com/jace/flask-pyelasticsearch/archive/master.zip#egg=Flask-PyElasticSearch-dev

Configure
---------

The only configuration is `ELASTICSEARCH_URL`, defaults to `http://localhost:9200/`.
