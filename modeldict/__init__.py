__all__ = ('VERSION', 'ModelDict')

try:
    VERSION = __import__('pkg_resources') \
        .get_distribution('django-modeldict').version
except Exception as e:
    VERSION = 'unknown'

from modeldict.models import ModelDict
