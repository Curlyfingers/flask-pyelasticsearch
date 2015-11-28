from pyelasticsearch import ElasticSearch as PyElasticSearch


class ElasticSearch(object):
    """
    A thin wrapper around pyelasticsearch.ElasticSearch()
    """
    def __init__(self, app=None):
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        self.app = app
        app.config.setdefault('ELASTICSEARCH_URL', 'http://localhost:9200/')
        if not hasattr(app, 'extensions'):
            app.extensions = {}
        app.extensions['elasticsearch'] = PyElasticSearch(app.config['ELASTICSEARCH_URL'])

    def __getattr__(self, item):
        if 'elasticsearch' not in self.app.extensions.keys():
            raise Exception('not initialised, did you forget to call init_app?')
        return getattr(self.app.extensions['elasticsearch'], item)
