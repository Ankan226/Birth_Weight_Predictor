# extensions.py

from flask_caching import Cache

cache = Cache(config={'CACHE_TYPE': 'SimpleCache'})
